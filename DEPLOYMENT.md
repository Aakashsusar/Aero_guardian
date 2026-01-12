# Deployment Guide

## Production Deployment Options

### Option 1: Using Gunicorn (Recommended for Production)

1. Install Gunicorn:
```bash
pip install gunicorn
```

2. Run with Gunicorn:
```bash
gunicorn -w 4 -b 0.0.0.0:7860 app:app
```

Parameters:
- `-w 4`: 4 worker processes
- `-b 0.0.0.0:7860`: Bind to all interfaces on port 7860
- `app:app`: Module name and Flask app instance

### Option 2: Using Docker

1. Create `Dockerfile`:
```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 7860

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:7860", "app:app"]
```

2. Build and run:
```bash
docker build -t aero-guardian .
docker run -p 7860:7860 aero-guardian
```

### Option 3: Cloud Deployment

#### Heroku
1. Create `Procfile`:
```
web: gunicorn app:app
```

2. Deploy:
```bash
heroku create aero-guardian
git push heroku main
```

#### AWS EC2
1. Launch EC2 instance (Ubuntu)
2. Install dependencies:
```bash
sudo apt update
sudo apt install python3-pip nginx
pip3 install -r requirements.txt
```

3. Configure Nginx as reverse proxy
4. Use systemd to manage the service

#### Google Cloud Run
1. Build container:
```bash
gcloud builds submit --tag gcr.io/PROJECT_ID/aero-guardian
```

2. Deploy:
```bash
gcloud run deploy --image gcr.io/PROJECT_ID/aero-guardian --platform managed
```

## Production Considerations

### 1. Security

**Enable CORS (if needed):**
```python
from flask_cors import CORS
CORS(app, origins=["https://yourdomain.com"])
```

**Add rate limiting:**
```python
from flask_limiter import Limiter
limiter = Limiter(app, default_limits=["100 per hour"])
```

**Add authentication:**
```python
from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

@app.route('/predict', methods=['POST'])
@auth.login_required
def predict():
    # ... existing code
```

### 2. Performance

**Use Redis for caching:**
```python
from flask_caching import Cache
cache = Cache(app, config={'CACHE_TYPE': 'redis'})
```

**Optimize model loading:**
- Load model once at startup (already implemented)
- Use GPU if available
- Consider model quantization for faster inference

**Image optimization:**
- Resize large images before processing
- Compress uploaded images
- Set maximum file size limits (already implemented)

### 3. Monitoring

**Add logging:**
```python
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
```

**Health check endpoint:**
```python
@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200
```

**Metrics collection:**
- Track request count
- Monitor inference time
- Log error rates

### 4. Scaling

**Horizontal scaling:**
- Deploy multiple instances behind a load balancer
- Use container orchestration (Kubernetes)
- Implement request queuing for high load

**Vertical scaling:**
- Use GPU instances for faster inference
- Increase worker processes
- Optimize memory usage

### 5. Environment Variables

Create `.env` file:
```
FLASK_ENV=production
MODEL_PATH=best.pt
UPLOAD_FOLDER=uploads
MAX_FILE_SIZE=16777216
CONFIDENCE_THRESHOLD=0.3
```

Load in app:
```python
from dotenv import load_dotenv
load_dotenv()

app.config['MODEL_PATH'] = os.getenv('MODEL_PATH', 'best.pt')
```

## Nginx Configuration Example

```nginx
server {
    listen 80;
    server_name yourdomain.com;

    location / {
        proxy_pass http://127.0.0.1:7860;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        
        # Increase timeout for ML inference
        proxy_read_timeout 300;
        proxy_connect_timeout 300;
        proxy_send_timeout 300;
    }

    # Increase max upload size
    client_max_body_size 20M;
}
```

## SSL/HTTPS Setup

Using Let's Encrypt:
```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d yourdomain.com
```

## Backup and Recovery

1. **Model file backup:**
   - Keep `best.pt` in version control or cloud storage
   - Regular backups of model files

2. **Database backup (if added):**
   - Automated daily backups
   - Store in separate location

3. **Logs:**
   - Rotate logs regularly
   - Archive old logs to cloud storage

## Monitoring Tools

- **Application Performance:** New Relic, DataDog
- **Server Monitoring:** Prometheus, Grafana
- **Error Tracking:** Sentry
- **Uptime Monitoring:** Pingdom, UptimeRobot

## Cost Optimization

1. Use spot instances for non-critical workloads
2. Implement auto-scaling based on demand
3. Cache frequently requested results
4. Optimize model size and inference time
5. Use CDN for static assets

## Maintenance

1. Regular security updates
2. Monitor disk space (uploads folder)
3. Clean up old uploaded files
4. Update dependencies regularly
5. Performance testing and optimization
