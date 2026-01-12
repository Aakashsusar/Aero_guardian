# Quick Start Guide

## Running the Application

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Start the Flask Server
```bash
python app.py
```

### 3. Access the Web Interface
Open your browser and go to:
```
http://localhost:7860
```

## Using the Interface

1. **Upload an Image**
   - Click the upload area or drag & drop an image
   - Supported formats: JPG, PNG, etc.

2. **Initiate Scan**
   - Click the "🚨 INITIATE SCAN" button
   - Wait for the analysis to complete

3. **View Results**
   - Detection count displayed in the center circle
   - Threat level indicator shows risk assessment
   - Annotated image shows detected people with bounding boxes
   - Detection logs show detailed information
   - Right panel lists all detected persons with confidence scores

## API Usage Example

### Using cURL
```bash
curl -X POST http://localhost:7860/predict \
  -F "image=@path/to/your/image.jpg"
```

### Using Python
```python
import requests

url = "http://localhost:7860/predict"
files = {"image": open("path/to/image.jpg", "rb")}
response = requests.post(url, files=files)
print(response.json())
```

### Using JavaScript (Fetch API)
```javascript
const formData = new FormData();
formData.append('image', fileInput.files[0]);

fetch('http://localhost:7860/predict', {
    method: 'POST',
    body: formData
})
.then(response => response.json())
.then(data => console.log(data));
```

## Expected Response Format

```json
{
    "status": "success",
    "people_count": 7,
    "threat_level": "HIGH",
    "fps": 12.5,
    "logs": [
        "TARGET LOCKED | CONF=0.95",
        "TARGET LOCKED | CONF=0.87",
        "..."
    ],
    "detections": [
        {
            "bbox": [100, 150, 200, 350],
            "confidence": 0.95,
            "label": "HUMAN"
        }
    ],
    "annotated_image": "data:image/png;base64,iVBORw0KG..."
}
```

## Troubleshooting

### Port Already in Use
If port 7860 is already in use, modify `app.py`:
```python
app.run(host='0.0.0.0', port=8080, debug=True)
```

### Model Not Found
Ensure `best.pt` is in the same directory as `app.py`.

### Memory Issues
For large images, the server might need more memory. Consider resizing images before upload.

## Next Steps

- Integrate with your custom frontend
- Add authentication if needed
- Deploy to production server
- Enable CORS for cross-origin requests
- Add rate limiting for API protection
