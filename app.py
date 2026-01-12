import time
import os
import base64
from io import BytesIO

from flask import Flask, render_template, request, jsonify
from ultralytics import YOLO
from PIL import Image, ImageDraw

# ---------------- FLASK APP ----------------
app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024

os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

# ---------------- MODEL LOAD ----------------
print("Loading YOLO model...")

model = YOLO("best.pt")
model.to("cpu")
model.model.eval()  # inference mode only

CONF = 0.3

print("Model loaded successfully!")

# ---------------- DETECTION LOGIC ----------------
def detect_people(image):
    start = time.time()

    img = image.convert("RGB").resize((640, 640))

    results = model.predict(
        img,
        conf=CONF,
        device="cpu",
        verbose=False
    )

    draw = ImageDraw.Draw(img)
    logs, detections = [], []
    count = 0

    for r in results:
        if not r.boxes:
            continue

        for box in r.boxes:
            cls = int(box.cls[0])
            label = model.names[cls].lower()

            if label != "person":
                continue

            confidence = float(box.conf[0])
            count += 1
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            draw.rectangle([x1, y1, x2, y2], outline="#00fff7", width=3)
            draw.text((x1, max(y1 - 15, 0)), f"HUMAN {confidence:.2f}", fill="#00fff7")

            logs.append(f"TARGET LOCKED | CONF={confidence:.2f}")
            detections.append({
                "bbox": [x1, y1, x2, y2],
                "confidence": round(confidence, 2),
                "label": "HUMAN"
            })

    if count == 0:
        logs.append("AREA CLEAR")

    fps = round(1 / max(time.time() - start, 0.001), 2)

    threat = "LOW"
    if count >= 3:
        threat = "HIGH"
    elif count > 0:
        threat = "MEDIUM"

    return img, logs, count, threat, fps, detections

# ---------------- ROUTES ----------------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        if "image" not in request.files:
            return jsonify({"status": "error", "message": "No image"}), 400

        image = Image.open(request.files["image"].stream)

        annotated, logs, count, threat, fps, detections = detect_people(image)

        buf = BytesIO()
        annotated.save(buf, format="PNG")
        img_b64 = base64.b64encode(buf.getvalue()).decode()

        return jsonify({
            "status": "success",
            "people_count": count,
            "threat_level": threat,
            "fps": fps,
            "logs": logs,
            "detections": detections,
            "annotated_image": f"data:image/png;base64,{img_b64}"
        })

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
