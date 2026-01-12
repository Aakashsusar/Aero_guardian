import time
import os
import base64
from io import BytesIO

from flask import Flask, render_template, request, jsonify
from ultralytics import YOLO
from PIL import Image, ImageDraw

# ---------------- FLASK APP ----------------
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# ---------------- MODEL LOAD (SAFE FOR RENDER) ----------------
print("Loading YOLO model...")

model = YOLO("best.pt")
model.to("cpu")                 # 🔴 FORCE CPU
model.overrides["fuse"] = False # 🔴 DISABLE FUSION (CRITICAL)

CONF = 0.3

print("Model loaded successfully!")

# ---------------- DETECTION LOGIC ----------------
def detect_people(image):
    start = time.time()

    if image is None:
        return None, [], 0, "LOW", 0, []

    # Convert & resize (HARD memory cap)
    img = image.convert("RGB")
    img = img.resize((640, 640))

    # YOLO prediction (CPU-safe)
    results = model.predict(
        img,
        conf=CONF,
        device="cpu",
        half=False,
        verbose=False
    )

    draw = ImageDraw.Draw(img)
    logs = []
    detections = []
    count = 0

    for r in results:
        if r.boxes is None:
            continue

        for box in r.boxes:
            cls = int(box.cls[0])
            label = model.names[cls].lower()
            conf = float(box.conf[0])

            if label not in ["person", "human"]:
                continue

            count += 1
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            # Draw bounding box
            draw.rectangle([x1, y1, x2, y2], outline="#00fff7", width=3)
            draw.text((x1, max(y1 - 15, 0)), f"HUMAN {conf:.2f}", fill="#00fff7")

            logs.append(f"TARGET LOCKED | CONF={conf:.2f}")
            detections.append({
                "bbox": [x1, y1, x2, y2],
                "confidence": round(conf, 2),
                "label": "HUMAN"
            })

    if count == 0:
        logs.append("AREA CLEAR")

    fps = round(1 / max(time.time() - start, 0.001), 2)

    # Threat level logic
    if count >= 3:
        threat = "HIGH"
    elif count > 0:
        threat = "MEDIUM"
    else:
        threat = "LOW"

    return img, logs, count, threat, fps, detections

# ---------------- ROUTES ----------------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        if "image" not in request.files:
            return jsonify({
                "status": "error",
                "message": "No image file provided"
            }), 400

        file = request.files["image"]

        try:
            image = Image.open(file.stream)
        except Exception:
            return jsonify({
                "status": "error",
                "message": "Invalid image format"
            }), 400

        annotated_img, logs, count, threat, fps, detections = detect_people(image)

        # Encode image → base64
        buffer = BytesIO()
        annotated_img.save(buffer, format="PNG")
        img_base64 = base64.b64encode(buffer.getvalue()).decode()

        return jsonify({
            "status": "success",
            "people_count": count,
            "threat_level": threat,
            "fps": fps,
            "logs": logs,
            "detections": detections,
            "annotated_image": f"data:image/png;base64,{img_base64}"
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

# ---------------- ENTRY POINT ----------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
