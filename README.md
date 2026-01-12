# AERO GUARDIAN - Drone Survivor Detection System

Flask-based web service for people detection using YOLO model with a modern, futuristic UI.

## Project Structure

```
.
├── app.py                  # Flask backend server
├── best.pt                 # YOLO model file (DO NOT MODIFY)
├── requirements.txt        # Python dependencies
├── runtime.txt            # Python version
├── uploads/               # Temporary uploaded images
├── templates/
│   └── index.html         # Main UI template
└── static/
    ├── css/
    │   └── style.css      # Drone surveillance theme styles
    └── js/
        └── app.js         # Frontend logic
```

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the Flask server:
```bash
python app.py
```

3. Open your browser and navigate to:
```
http://localhost:7860
```

## API Endpoints

### GET `/`
Serves the main web interface with drone surveillance UI.

### POST `/predict`
Performs people detection on uploaded images.

**Request:**
- Method: POST
- Content-Type: multipart/form-data
- Body: `image` (file upload)

**Response:**
```json
{
    "status": "success",
    "people_count": 7,
    "threat_level": "HIGH",
    "fps": 12.5,
    "logs": [
        "TARGET LOCKED | CONF=0.95",
        "TARGET LOCKED | CONF=0.87"
    ],
    "detections": [
        {
            "bbox": [100, 150, 200, 350],
            "confidence": 0.95,
            "label": "HUMAN"
        }
    ],
    "annotated_image": "data:image/png;base64,..."
}
```

## Features

- **Flask Backend**: Clean REST API for ML inference
- **Model Loading**: YOLO model loaded once at startup for efficiency
- **Modern UI**: Futuristic drone surveillance theme with animations
- **Real-time Detection**: Upload images and get instant results
- **Visual Feedback**: Annotated images with bounding boxes
- **Threat Assessment**: Automatic threat level calculation
- **Detection Logs**: Real-time command log display
- **Responsive Design**: Works on desktop and mobile devices

## ML Logic

The existing YOLO-based people detection logic has been **preserved intact**:
- Model: `best.pt` (unchanged)
- Confidence threshold: 0.3
- Detection classes: "person", "human"
- Bounding box visualization with cyan color (#00fff7)
- FPS calculation
- Threat level assessment (LOW/MEDIUM/HIGH)

## UI Theme

The interface features a drone surveillance aesthetic:
- Animated grid background
- Twinkling stars effect
- Animated drone icon
- Radar sweep animation
- Glowing cyan accents (#00fff7)
- Alert animations for detections
- Sound alerts when people are detected

## Custom UI Integration

This Flask backend is ready for custom UI integration:
- Clean JSON API responses
- CORS can be enabled if needed
- Stateless design for easy scaling
- Base64 encoded images in responses

## Notes

- Maximum upload size: 16MB
- Supported formats: All image formats (PNG, JPG, etc.)
- Model inference runs on CPU by default
- For GPU acceleration, ensure CUDA-compatible PyTorch is installed

## Credits

Original ML implementation by: Nirmiti | Sumit | Onkar
Flask conversion: Maintains all original detection logic
