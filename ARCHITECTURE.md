# System Architecture

## High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         USER BROWSER                            │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │              FRONTEND (HTML/CSS/JS)                       │ │
│  │                                                           │ │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────────┐  │ │
│  │  │   Upload    │  │  Detection  │  │   Detection     │  │ │
│  │  │   Area      │  │   Circle    │  │   Results       │  │ │
│  │  └─────────────┘  └─────────────┘  └─────────────────┘  │ │
│  │                                                           │ │
│  │  ┌─────────────────────────────────────────────────────┐ │ │
│  │  │           JavaScript (app.js)                       │ │ │
│  │  │  - File upload handling                             │ │ │
│  │  │  - API communication                                │ │ │
│  │  │  - Result display                                   │ │ │
│  │  │  - Animations                                       │ │ │
│  │  └─────────────────────────────────────────────────────┘ │ │
│  └───────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
                              ↕ HTTP/AJAX
┌─────────────────────────────────────────────────────────────────┐
│                      FLASK WEB SERVER                           │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │                    ROUTES                                 │ │
│  │                                                           │ │
│  │  GET  /          →  Serve index.html                     │ │
│  │  POST /predict   →  Process image & return JSON          │ │
│  └───────────────────────────────────────────────────────────┘ │
│                              ↓                                  │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │              DETECTION LOGIC (Preserved)                  │ │
│  │                                                           │ │
│  │  def detect_people(image):                               │ │
│  │      1. Preprocess image                                 │ │
│  │      2. Run YOLO inference                               │ │
│  │      3. Filter person/human detections                   │ │
│  │      4. Draw bounding boxes                              │ │
│  │      5. Calculate threat level                           │ │
│  │      6. Generate logs                                    │ │
│  │      7. Return results                                   │ │
│  └───────────────────────────────────────────────────────────┘ │
│                              ↓                                  │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │                  YOLO MODEL                               │ │
│  │                                                           │ │
│  │  model = YOLO("best.pt")                                 │ │
│  │  - Loaded once at startup                                │ │
│  │  - Confidence threshold: 0.3                             │ │
│  │  - Detects: person, human                                │ │
│  └───────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

## Request Flow

### 1. Page Load (GET /)

```
User Browser                Flask Server
     │                           │
     │──── GET / ───────────────>│
     │                           │
     │                      Load index.html
     │                      from templates/
     │                           │
     │<──── HTML + CSS + JS ─────│
     │                           │
   Render UI
```

### 2. Image Upload & Detection (POST /predict)

```
User Browser                Flask Server                YOLO Model
     │                           │                           │
  Upload                         │                           │
   Image                         │                           │
     │                           │                           │
     │── POST /predict ─────────>│                           │
     │   (multipart/form-data)   │                           │
     │                           │                           │
     │                      Receive image                    │
     │                      Validate file                    │
     │                           │                           │
     │                      Open with PIL                    │
     │                           │                           │
     │                           │── model.predict() ───────>│
     │                           │                           │
     │                           │                      Run inference
     │                           │                      Detect people
     │                           │                           │
     │                           │<──── Results ─────────────│
     │                           │                           │
     │                      Process results:                 │
     │                      - Draw bounding boxes            │
     │                      - Count people                   │
     │                      - Calculate threat               │
     │                      - Generate logs                  │
     │                      - Encode image                   │
     │                           │                           │
     │<──── JSON Response ───────│                           │
     │                           │                           │
  Display                        │                           │
  Results                        │                           │
```

## Data Flow

### Input Processing

```
User Image (File)
      ↓
File Upload (multipart/form-data)
      ↓
Flask Request Handler
      ↓
PIL Image Object
      ↓
RGB Conversion
      ↓
YOLO Model Input
```

### Output Processing

```
YOLO Predictions
      ↓
Filter (person/human only)
      ↓
Bounding Box Drawing
      ↓
Annotated PIL Image
      ↓
Base64 Encoding
      ↓
JSON Response
      ↓
Frontend Display
```

## Component Architecture

### Backend Components

```
app.py
├── Flask App Configuration
│   ├── Upload folder setup
│   ├── File size limits
│   └── Static/template paths
│
├── Model Loading (Startup)
│   ├── Load YOLO model
│   ├── Set confidence threshold
│   └── Cache in memory
│
├── Detection Logic
│   ├── detect_people()
│   │   ├── Image preprocessing
│   │   ├── Model inference
│   │   ├── Result filtering
│   │   ├── Bounding box drawing
│   │   ├── Threat calculation
│   │   └── Log generation
│   │
│   └── Helper functions
│
└── Route Handlers
    ├── index() - Serve UI
    └── predict() - Process images
```

### Frontend Components

```
templates/index.html
├── Structure
│   ├── Header (title, status)
│   ├── Left Panel (upload)
│   ├── Center Panel (results)
│   └── Right Panel (logs)
│
static/css/style.css
├── Layout
│   ├── Grid system
│   ├── Responsive design
│   └── Panel styling
│
├── Theme
│   ├── Colors (cyan #00fff7)
│   ├── Fonts (Orbitron)
│   └── Background effects
│
└── Animations
    ├── Grid movement
    ├── Star twinkling
    ├── Drone floating
    ├── Radar sweep
    ├── Alert flash
    └── Element transitions
│
static/js/app.js
├── Event Handlers
│   ├── Upload click
│   ├── Drag & drop
│   ├── Remove image
│   └── Scan button
│
├── API Communication
│   ├── FormData creation
│   ├── Fetch request
│   └── Response handling
│
└── UI Updates
    ├── Display results
    ├── Update counters
    ├── Show logs
    └── Trigger alerts
```

## File System Structure

```
aero-guardian/
│
├── app.py                    # Flask backend
│   ├── Flask app setup
│   ├── Model loading
│   ├── Detection logic
│   └── Route handlers
│
├── best.pt                   # YOLO model (5.5 MB)
│   └── Pre-trained weights
│
├── uploads/                  # Temporary storage
│   └── (uploaded images)
│
├── templates/
│   └── index.html           # Main UI template
│       ├── HTML structure
│       ├── SVG graphics
│       └── Template variables
│
├── static/
│   ├── css/
│   │   └── style.css        # Styling & animations
│   │       ├── Layout rules
│   │       ├── Theme colors
│   │       └── Keyframe animations
│   │
│   └── js/
│       └── app.js           # Frontend logic
│           ├── DOM manipulation
│           ├── Event handling
│           └── API calls
│
└── Documentation/
    ├── README.md
    ├── QUICKSTART.md
    ├── DEPLOYMENT.md
    ├── USER_GUIDE.md
    ├── BEFORE_AFTER.md
    ├── CONVERSION_SUMMARY.md
    ├── ARCHITECTURE.md
    └── CHECKLIST.md
```

## Technology Stack

### Backend
```
Python 3.10
├── Flask 3.0.0          (Web framework)
├── Ultralytics 8.1.0    (YOLO)
├── PyTorch 2.1.2        (Deep learning)
├── Pillow               (Image processing)
└── NumPy                (Numerical operations)
```

### Frontend
```
HTML5
├── Semantic structure
├── SVG graphics
└── Template syntax

CSS3
├── Grid layout
├── Flexbox
├── Animations
└── Media queries

JavaScript (ES6+)
├── Fetch API
├── FormData
├── DOM manipulation
└── Event handling
```

## Security Architecture

```
┌─────────────────────────────────────┐
│         Security Layers             │
├─────────────────────────────────────┤
│ 1. File Size Limit (16MB)          │
│ 2. File Type Validation             │
│ 3. Upload Folder Isolation          │
│ 4. Error Handling                   │
│ 5. Input Sanitization               │
└─────────────────────────────────────┘
```

## Scalability Architecture

```
┌─────────────────────────────────────┐
│      Load Balancer (Nginx)          │
└──────────┬──────────────────────────┘
           │
    ┌──────┴──────┐
    │             │
┌───▼───┐    ┌───▼───┐
│ Flask │    │ Flask │
│ App 1 │    │ App 2 │
└───┬───┘    └───┬───┘
    │             │
    └──────┬──────┘
           │
    ┌──────▼──────┐
    │ Shared      │
    │ Model Cache │
    └─────────────┘
```

## Deployment Architecture

### Development
```
localhost:7860
     │
     └── Flask Development Server
         └── Single Process
```

### Production
```
Domain (HTTPS)
     │
     └── Nginx (Reverse Proxy)
         │
         └── Gunicorn (WSGI Server)
             │
             ├── Worker 1
             ├── Worker 2
             ├── Worker 3
             └── Worker 4
```

## Performance Optimization

```
┌─────────────────────────────────────┐
│     Optimization Strategies         │
├─────────────────────────────────────┤
│ 1. Model loaded once at startup     │
│ 2. Efficient image processing       │
│ 3. Base64 encoding for responses    │
│ 4. Minimal frontend dependencies    │
│ 5. CSS/JS minification (optional)   │
│ 6. Static file caching              │
│ 7. Multi-worker support             │
└─────────────────────────────────────┘
```

## Monitoring Architecture

```
Application
     │
     ├── Logs → File System
     │
     ├── Metrics → Prometheus
     │
     ├── Errors → Sentry
     │
     └── Uptime → Pingdom
```

## Summary

This architecture provides:
- ✅ Clean separation of concerns
- ✅ Scalable backend design
- ✅ Modern frontend implementation
- ✅ Preserved ML functionality
- ✅ Production-ready structure
- ✅ Easy maintenance and extension
