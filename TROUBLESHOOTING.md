# Troubleshooting Guide

## Common Issues and Solutions

### ✅ RESOLVED: NumPy Warning

**Issue:**
```
UserWarning: Failed to initialize NumPy: _ARRAY_API not found
```

**Solution:**
This has been fixed! The requirements.txt now specifies compatible versions:
- numpy==1.26.4
- opencv-python-headless==4.8.1.78

**To apply the fix:**
```bash
pip install -r requirements.txt --force-reinstall
```

---

## Other Common Issues

### 1. Port Already in Use

**Error:**
```
OSError: [Errno 98] Address already in use
```

**Solution:**
Change the port in `app.py`:
```python
# At the bottom of app.py, change:
app.run(host='0.0.0.0', port=7860, debug=True)
# To:
app.run(host='0.0.0.0', port=8080, debug=True)
```

Or kill the process using port 7860:
```bash
# Windows
netstat -ano | findstr :7860
taskkill /PID <PID> /F

# Linux/Mac
lsof -ti:7860 | xargs kill -9
```

---

### 2. Model File Not Found

**Error:**
```
FileNotFoundError: [Errno 2] No such file or directory: 'best.pt'
```

**Solution:**
Ensure `best.pt` is in the same directory as `app.py`:
```bash
# Check if file exists
dir best.pt    # Windows
ls best.pt     # Linux/Mac
```

---

### 3. Import Errors

**Error:**
```
ModuleNotFoundError: No module named 'flask'
```

**Solution:**
Install all dependencies:
```bash
pip install -r requirements.txt
```

**Verify imports:**
```bash
python test_imports.py
```

---

### 4. CUDA/GPU Issues

**Warning:**
```
CUDA not available, using CPU
```

**Solution:**
This is normal if you don't have a GPU. The app works fine on CPU.

For GPU support, install CUDA-enabled PyTorch:
```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
```

---

### 5. Slow First Prediction

**Issue:**
First prediction takes 10-20 seconds

**Solution:**
This is normal! The model needs to initialize. Subsequent predictions are much faster (1-3 seconds).

---

### 6. Upload Fails

**Error:**
```
413 Request Entity Too Large
```

**Solution:**
Image is too large (>16MB). Resize it or increase limit in `app.py`:
```python
app.config['MAX_CONTENT_LENGTH'] = 32 * 1024 * 1024  # 32MB
```

---

### 7. Browser Can't Connect

**Error:**
```
This site can't be reached
```

**Solution:**
1. Check if server is running:
   ```bash
   python app.py
   ```

2. Look for this message:
   ```
   * Running on http://0.0.0.0:7860
   ```

3. Try different URLs:
   - http://localhost:7860
   - http://127.0.0.1:7860
   - http://0.0.0.0:7860

---

### 8. Static Files Not Loading

**Issue:**
CSS/JS not loading, page looks broken

**Solution:**
1. Check folder structure:
   ```
   static/
   ├── css/
   │   └── style.css
   └── js/
       └── app.js
   ```

2. Clear browser cache (Ctrl+F5)

3. Check Flask is serving static files:
   ```python
   # In app.py, ensure:
   app = Flask(__name__)  # No custom static_folder
   ```

---

### 9. Template Not Found

**Error:**
```
TemplateNotFound: index.html
```

**Solution:**
Check folder structure:
```
templates/
└── index.html
```

Ensure `templates` folder is in the same directory as `app.py`.

---

### 10. Permission Denied (uploads folder)

**Error:**
```
PermissionError: [Errno 13] Permission denied: 'uploads'
```

**Solution:**
Create uploads folder manually:
```bash
mkdir uploads    # Windows/Linux/Mac
```

Or run as administrator/sudo.

---

## Dependency Conflicts

### Check Installed Versions

```bash
pip list | grep -E "flask|torch|ultralytics|numpy|opencv"
```

### Expected Versions

```
flask==3.0.0
torch==2.1.2
ultralytics==8.1.0
numpy==1.26.4
opencv-python-headless==4.8.1.78
```

### Clean Install

If you have conflicts:
```bash
# Uninstall all
pip uninstall flask torch torchvision ultralytics numpy opencv-python-headless -y

# Reinstall from requirements
pip install -r requirements.txt
```

---

## Testing

### Test Imports
```bash
python test_imports.py
```

### Test API
```bash
python test_api.py path/to/image.jpg
```

### Test Server
```bash
# Start server
python app.py

# In another terminal
curl http://localhost:7860
```

---

## Performance Issues

### Slow Predictions

**Causes:**
1. Large images (resize to 640x640)
2. CPU-only inference (use GPU)
3. First run (model loading)

**Solutions:**
```python
# Resize images before upload
# Or modify detection function to resize:
img = img.resize((640, 640))
```

### High Memory Usage

**Solution:**
Reduce image size or use smaller model.

---

## Browser-Specific Issues

### Chrome
- Clear cache: Ctrl+Shift+Delete
- Disable extensions
- Try incognito mode

### Firefox
- Clear cache: Ctrl+Shift+Delete
- Check console (F12) for errors

### Safari
- Enable developer tools
- Check console for errors

---

## Production Issues

### Gunicorn Not Working

**Error:**
```
gunicorn: command not found
```

**Solution:**
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:7860 app:app
```

### Workers Crashing

**Solution:**
Reduce worker count:
```bash
gunicorn -w 2 -b 0.0.0.0:7860 app:app
```

---

## Debugging

### Enable Debug Mode

In `app.py`:
```python
app.run(host='0.0.0.0', port=7860, debug=True)
```

### Check Logs

Look for error messages in terminal output.

### Test Individual Components

```python
# Test model loading
from ultralytics import YOLO
model = YOLO("best.pt")
print("Model loaded!")

# Test Flask
from flask import Flask
app = Flask(__name__)
print("Flask initialized!")
```

---

## Getting Help

### Check Documentation
1. README.md - Overview
2. QUICKSTART.md - Setup
3. USER_GUIDE.md - Usage
4. DEPLOYMENT.md - Production

### Verify Installation
```bash
python test_imports.py
```

### Check System
```bash
python --version    # Should be 3.10 or 3.11
pip --version       # Should be recent
```

---

## Quick Fixes Checklist

- [ ] Run `pip install -r requirements.txt`
- [ ] Run `python test_imports.py`
- [ ] Check `best.pt` exists
- [ ] Check folder structure (templates/, static/, uploads/)
- [ ] Try different port
- [ ] Clear browser cache
- [ ] Restart server
- [ ] Check firewall settings

---

## Still Having Issues?

1. Check all files are in correct locations
2. Verify Python version (3.10 or 3.11)
3. Try clean install of dependencies
4. Check system resources (RAM, disk space)
5. Review error messages carefully
6. Test with `test_imports.py` and `test_api.py`

---

**Most issues are resolved by:**
```bash
pip install -r requirements.txt --force-reinstall
python test_imports.py
python app.py
```
