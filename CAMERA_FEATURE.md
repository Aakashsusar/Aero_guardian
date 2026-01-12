# 📹 Live Camera Feature

## Overview

The Flask app now includes live camera functionality, allowing you to detect people in real-time using your webcam!

## How to Use

### Step 1: Switch to Camera Mode
Click the **"📹 LIVE CAMERA"** button at the top of the left panel.

### Step 2: Start Camera
Click **"📹 START CAMERA"** to activate your webcam.

**Browser will ask for permission:**
- Click "Allow" to grant camera access
- Your live video feed will appear

### Step 3: Capture & Analyze
Click **"🚨 INITIATE SCAN"** to:
- Capture the current frame
- Run people detection
- Display results

### Step 4: Stop Camera
Click **"⏹️ STOP CAMERA"** when finished.

## Features

### Two Modes Available

**📤 Upload Mode (Default)**
- Upload images from your computer
- Drag & drop support
- Preview before scanning

**📹 Camera Mode (New!)**
- Live webcam feed
- Real-time frame capture
- Instant detection

### Camera Capabilities

- **Resolution**: Up to 1280x720 (HD)
- **Format**: JPEG capture
- **Quality**: 95% compression
- **Speed**: Same as image upload (~1-3 seconds)

## Browser Compatibility

### Supported Browsers
✅ Chrome/Edge (Recommended)
✅ Firefox
✅ Safari (macOS/iOS)
✅ Opera

### Requirements
- Modern browser with WebRTC support
- Camera permissions granted
- Working webcam/camera device

## Permissions

### First Time Use
Browser will prompt:
```
[Your Site] wants to use your camera
[Block] [Allow]
```

Click **Allow** to enable camera access.

### If Blocked
1. Click the camera icon in address bar
2. Change permission to "Allow"
3. Refresh the page

### Chrome/Edge
```
Settings → Privacy and security → Site settings → Camera
```

### Firefox
```
Settings → Privacy & Security → Permissions → Camera
```

## Technical Details

### How It Works

1. **Camera Access**: Uses `navigator.mediaDevices.getUserMedia()`
2. **Video Stream**: Displays live feed in `<video>` element
3. **Frame Capture**: Draws current frame to `<canvas>`
4. **Image Conversion**: Converts canvas to JPEG blob
5. **Upload**: Sends blob to `/predict` endpoint
6. **Detection**: Same ML logic as image upload
7. **Results**: Displays annotated frame and data

### Code Flow

```javascript
// Start camera
navigator.mediaDevices.getUserMedia({ video: true })
  ↓
// Display in video element
video.srcObject = stream
  ↓
// On scan button click
canvas.drawImage(video, 0, 0)
  ↓
// Convert to blob
canvas.toBlob(blob => ...)
  ↓
// Send to API
fetch('/predict', { body: formData })
  ↓
// Display results
```

## Use Cases

### Security Monitoring
- Monitor entrance/exit points
- Count people in real-time
- Alert on crowd detection

### Attendance Tracking
- Capture and count attendees
- Real-time headcount
- Event monitoring

### Retail Analytics
- Customer counting
- Traffic analysis
- Queue monitoring

### Smart Home
- Presence detection
- Visitor monitoring
- Security alerts

## Tips for Best Results

### Lighting
- Ensure good lighting
- Avoid backlighting
- Use natural or bright light

### Camera Position
- Position camera at eye level
- Ensure people are in frame
- Avoid extreme angles

### Distance
- Keep subjects 2-10 feet away
- Avoid too close or too far
- Ensure faces are visible

### Performance
- Close other camera apps
- Use good quality webcam
- Ensure stable internet (if remote)

## Troubleshooting

### Camera Not Starting

**Error: "Camera access denied"**
- Check browser permissions
- Allow camera access
- Refresh the page

**Error: "Camera not found"**
- Ensure webcam is connected
- Check device manager
- Try different browser

### Poor Detection

**Issue: People not detected**
- Improve lighting
- Adjust camera angle
- Move closer to camera
- Ensure people are fully visible

**Issue: Slow performance**
- Close other applications
- Use smaller video resolution
- Check CPU usage

### Video Not Displaying

**Black screen:**
- Check camera is not in use by another app
- Restart browser
- Check camera drivers

**Frozen video:**
- Refresh the page
- Stop and restart camera
- Clear browser cache

## Privacy & Security

### Data Handling
- ✅ All processing is local (on your server)
- ✅ No frames sent to external services
- ✅ Camera stops when you close/leave page
- ✅ No video recording (only frame capture)

### Best Practices
- Only use in authorized areas
- Inform people of monitoring
- Comply with local privacy laws
- Secure your server/network

## Comparison: Upload vs Camera

| Feature | Upload Mode | Camera Mode |
|---------|-------------|-------------|
| **Input** | Image files | Live webcam |
| **Speed** | Fast | Fast |
| **Quality** | Original | HD (720p) |
| **Use Case** | Batch processing | Real-time |
| **Offline** | Yes | Yes (local) |
| **Storage** | Temporary | No storage |

## Advanced Usage

### Continuous Monitoring

For continuous detection, you can:
1. Click scan repeatedly
2. Or implement auto-scan (custom code)

**Example auto-scan:**
```javascript
// Add to app.js
let autoScan = false;
setInterval(() => {
    if (autoScan && cameraStream) {
        performScan();
    }
}, 3000); // Scan every 3 seconds
```

### Multiple Cameras

To support multiple cameras:
```javascript
// Get available cameras
navigator.mediaDevices.enumerateDevices()
    .then(devices => {
        const cameras = devices.filter(d => d.kind === 'videoinput');
        // Show camera selection UI
    });
```

## API Compatibility

Camera mode uses the same `/predict` endpoint:
- Same request format (multipart/form-data)
- Same response format (JSON)
- Same ML detection logic
- Same performance

## Future Enhancements

Possible additions:
- [ ] Auto-scan mode (continuous detection)
- [ ] Camera selection (front/back)
- [ ] Video recording
- [ ] Snapshot gallery
- [ ] Detection history
- [ ] Alert notifications
- [ ] Multiple camera support

## Summary

✅ **Easy to use**: Two-click camera activation
✅ **Fast**: Same speed as image upload
✅ **Secure**: All processing local
✅ **Compatible**: Works in all modern browsers
✅ **Flexible**: Switch between upload and camera modes

---

**Enjoy real-time people detection with your webcam! 📹**
