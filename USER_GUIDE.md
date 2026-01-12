# User Guide - AERO GUARDIAN

## Getting Started

### Step 1: Start the Server
```bash
python app.py
```

You should see:
```
Loading YOLO model...
Model loaded successfully!
 * Running on http://0.0.0.0:7860
```

### Step 2: Open the Interface
Open your web browser and navigate to:
```
http://localhost:7860
```

## Interface Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                    🚁 DRONE ICON (Animated)                     │
│                                                                 │
│           SURVIVOR/PEOPLE DETECTION USING DRONE                 │
│              ● SYSTEM ONLINE    POWERED BY AI                   │
└─────────────────────────────────────────────────────────────────┘

┌──────────────────┬──────────────────┬──────────────────────────┐
│  LEFT PANEL      │  CENTER PANEL    │  RIGHT PANEL             │
│                  │                  │                          │
│  LIVE FEED/      │  DETECTION       │  DETECTION RESULTS       │
│  UPLOAD          │  RESULTS         │                          │
│                  │                  │                          │
│  ┌────────────┐  │     ┌───┐       │  › SYSTEM READY          │
│  │  DROP OR   │  │     │ 0 │       │  › AWAITING INPUT...     │
│  │  CLICK TO  │  │     └───┘       │                          │
│  │  UPLOAD    │  │                  │                          │
│  └────────────┘  │  PERSON COUNT: 0 │                          │
│                  │                  │                          │
│  🚨 INITIATE     │  THREAT LEVEL    │                          │
│     SCAN         │     LOW          │                          │
│                  │  [▓▓▓░░░░░░░]    │                          │
│                  │                  │                          │
│                  │  FPS: 0.0        │                          │
└──────────────────┴──────────────────┴──────────────────────────┘
```

## Using the Interface

### 1. Upload an Image

**Method A: Click to Upload**
1. Make sure "📤 UPLOAD IMAGE" mode is selected
2. Click on the upload area in the left panel
3. Select an image file from your computer
4. Supported formats: JPG, PNG, BMP, etc.

**Method B: Drag & Drop**
1. Make sure "📤 UPLOAD IMAGE" mode is selected
2. Drag an image file from your computer
3. Drop it onto the upload area
4. The preview will appear automatically

### 2. Use Live Camera

**Camera Mode:**
1. Click "📹 LIVE CAMERA" button at the top
2. Click "📹 START CAMERA" to activate your webcam
3. Allow camera permissions when prompted
4. Your live camera feed will appear
5. Click "🚨 INITIATE SCAN" to capture and analyze the current frame
6. Click "⏹️ STOP CAMERA" when done

**Note:** Camera mode captures a single frame for analysis. For continuous detection, click scan multiple times.

### 2. Preview Your Image

After uploading:
- The image preview appears in the left panel
- The "🚨 INITIATE SCAN" button becomes active
- You can remove the image by clicking the ✕ button

**Or use Camera:**
- Switch to "📹 LIVE CAMERA" mode
- Start your webcam
- The scan button activates when camera is ready

### 3. Run Detection

1. Click the "🚨 INITIATE SCAN" button
2. Wait for the analysis (usually 1-3 seconds)
3. A loading spinner appears during processing

### 4. View Results

After scanning, you'll see:

**Center Panel:**
- Large detection count in the animated circle
- Person count display
- Threat level indicator (LOW/MEDIUM/HIGH)
- FPS (frames per second) measurement

**Left Panel:**
- Annotated image with bounding boxes
- Cyan boxes around detected people
- Confidence scores on each detection

**Right Panel:**
- Real-time command logs
- List of detected persons
- Confidence percentage for each detection

## Understanding the Results

### Detection Circle
```
     ┌─────┐
     │  7  │  ← Number of people detected
     └─────┘
```
- **Green glow**: Normal operation
- **Red glow + flashing**: People detected (alert mode)
- **Rotating line**: Radar sweep animation

### Threat Level Indicator

**LOW** (Green)
- 0 people detected
- Area clear
- No immediate concern

**MEDIUM** (Orange)
- 1-2 people detected
- Moderate activity
- Monitor situation

**HIGH** (Red)
- 3+ people detected
- High activity level
- Alert status

### Detection Logs

Example logs:
```
› SYSTEM READY
› AWAITING INPUT...
› IMAGE LOADED: photo.jpg
› INITIATING SCAN...
› TARGET LOCKED | CONF=0.95
› TARGET LOCKED | CONF=0.87
› TARGET LOCKED | CONF=0.92
› SCAN COMPLETE | 3 PERSON(S) DETECTED
```

### Detection List

Each detected person shows:
```
┌─────────────────────────┐
│ PERSON 1                │
│ CONFIDENCE: 95.2%       │
└─────────────────────────┘
```

## Visual Indicators

### Status LED
- **Green pulsing dot**: System online and ready
- Located in the header next to "SYSTEM ONLINE"

### Animated Background
- **Grid pattern**: Moving grid lines
- **Stars**: Twinkling stars effect
- **Dark theme**: Space/surveillance aesthetic

### Drone Icon
- **Animated**: Floating up and down
- **Spinning propellers**: Rotating circles
- Located at the top center

## Alert System

When people are detected:
1. **Visual Alert**: Detection circle turns red and flashes
2. **Sound Alert**: Alarm tone plays automatically
3. **Threat Level**: Updates to MEDIUM or HIGH
4. **Logs**: Show "TARGET LOCKED" messages

## Tips for Best Results

### Image Quality
- Use clear, well-lit images
- Avoid blurry or low-resolution photos
- Ensure people are visible in the frame

### File Size
- Maximum file size: 16MB
- Larger images take longer to process
- Consider resizing very large images

### Detection Accuracy
- Confidence threshold: 30%
- Higher confidence = more reliable detection
- Partial occlusion may reduce accuracy

## Keyboard Shortcuts

- **Click upload area**: Open file picker
- **Drag & drop**: Quick upload
- **✕ button**: Remove current image

## Troubleshooting

### "No image file provided"
- Make sure you've selected an image
- Check that the file is a valid image format

### "Empty filename"
- The file upload was cancelled
- Try uploading again

### Slow Processing
- Large images take longer to process
- Wait for the loading spinner to complete
- Check your internet connection

### No Detections
- Image may not contain people
- People may be too small or obscured
- Try a different image

### Alert Sound Not Playing
- Check browser audio permissions
- Ensure volume is not muted
- Some browsers block autoplay audio

## Advanced Usage

### Multiple Scans
1. Upload and scan first image
2. Click ✕ to remove
3. Upload and scan next image
4. Results update for each scan

### Comparing Results
- Take note of detection counts
- Compare threat levels
- Review confidence scores

### Saving Results
- Right-click annotated image → Save As
- Screenshot the entire interface
- Copy detection logs for records

## Mobile Usage

The interface is responsive and works on mobile devices:
- Touch to upload images
- Tap to initiate scan
- Swipe to scroll logs
- Pinch to zoom on results

## API Usage (Advanced)

For developers integrating with the API:

```bash
curl -X POST http://localhost:7860/predict \
  -F "image=@path/to/image.jpg"
```

See `test_api.py` for more examples.

## Support

For issues or questions:
1. Check the logs in the right panel
2. Review the QUICKSTART.md guide
3. See DEPLOYMENT.md for production setup
4. Check BEFORE_AFTER.md for architecture details

## Safety and Privacy

- Images are processed locally on your server
- No data is sent to external services
- Uploaded images are stored temporarily in `uploads/`
- Consider clearing the uploads folder periodically

## Performance Notes

- First scan may be slower (model initialization)
- Subsequent scans are faster (model cached)
- FPS indicates processing speed
- Higher FPS = faster processing

## Enjoy Using AERO GUARDIAN! 🚁

Your AI-powered drone surveillance system is ready for operation.
