"""
Quick test to verify all imports work correctly
"""
import sys

print("Testing imports...")
print("=" * 50)

try:
    print("1. Testing Flask...")
    from flask import Flask
    print("   ✅ Flask imported successfully")
except Exception as e:
    print(f"   ❌ Flask import failed: {e}")
    sys.exit(1)

try:
    print("2. Testing PIL...")
    from PIL import Image
    print("   ✅ PIL imported successfully")
except Exception as e:
    print(f"   ❌ PIL import failed: {e}")
    sys.exit(1)

try:
    print("3. Testing NumPy...")
    import numpy as np
    print(f"   ✅ NumPy {np.__version__} imported successfully")
except Exception as e:
    print(f"   ❌ NumPy import failed: {e}")
    sys.exit(1)

try:
    print("4. Testing OpenCV...")
    import cv2
    print(f"   ✅ OpenCV {cv2.__version__} imported successfully")
except Exception as e:
    print(f"   ❌ OpenCV import failed: {e}")
    sys.exit(1)

try:
    print("5. Testing PyTorch...")
    import torch
    print(f"   ✅ PyTorch {torch.__version__} imported successfully")
except Exception as e:
    print(f"   ❌ PyTorch import failed: {e}")
    sys.exit(1)

try:
    print("6. Testing Ultralytics YOLO...")
    from ultralytics import YOLO
    print("   ✅ Ultralytics YOLO imported successfully")
except Exception as e:
    print(f"   ❌ YOLO import failed: {e}")
    sys.exit(1)

print("=" * 50)
print("✅ All imports successful!")
print("\nYour Flask app should run without issues.")
print("Run: python app.py")
