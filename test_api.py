"""
Simple test script to verify the Flask API is working correctly.
Run this after starting the Flask server (python app.py)
"""

import requests
import sys
import os

def test_api(image_path):
    """Test the /predict endpoint with an image"""
    
    if not os.path.exists(image_path):
        print(f"❌ Error: Image file not found: {image_path}")
        return False
    
    print(f"📤 Testing API with image: {image_path}")
    print("=" * 50)
    
    try:
        # Prepare the request
        url = "http://localhost:7860/predict"
        files = {"image": open(image_path, "rb")}
        
        # Send request
        print("⏳ Sending request to /predict endpoint...")
        response = requests.post(url, files=files, timeout=30)
        
        # Check response
        if response.status_code == 200:
            data = response.json()
            
            print("✅ API Response Successful!")
            print("=" * 50)
            print(f"Status: {data.get('status')}")
            print(f"People Count: {data.get('people_count')}")
            print(f"Threat Level: {data.get('threat_level')}")
            print(f"FPS: {data.get('fps')}")
            print(f"\nLogs:")
            for log in data.get('logs', []):
                print(f"  › {log}")
            print(f"\nDetections: {len(data.get('detections', []))}")
            for i, det in enumerate(data.get('detections', []), 1):
                print(f"  Person {i}: Confidence {det['confidence']}")
            
            return True
        else:
            print(f"❌ Error: HTTP {response.status_code}")
            print(response.text)
            return False
            
    except requests.exceptions.ConnectionError:
        print("❌ Error: Could not connect to server.")
        print("Make sure the Flask server is running (python app.py)")
        return False
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

def test_home():
    """Test the home endpoint"""
    try:
        print("\n📤 Testing home endpoint...")
        response = requests.get("http://localhost:7860/", timeout=5)
        if response.status_code == 200:
            print("✅ Home page accessible")
            return True
        else:
            print(f"❌ Error: HTTP {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

if __name__ == "__main__":
    print("🚀 AERO GUARDIAN API Test")
    print("=" * 50)
    
    # Test home endpoint
    home_ok = test_home()
    
    # Test predict endpoint if image provided
    if len(sys.argv) > 1:
        image_path = sys.argv[1]
        predict_ok = test_api(image_path)
    else:
        print("\n⚠️  No image provided for /predict test")
        print("Usage: python test_api.py <path_to_image>")
        predict_ok = None
    
    print("\n" + "=" * 50)
    print("Test Summary:")
    print(f"  Home endpoint: {'✅ PASS' if home_ok else '❌ FAIL'}")
    if predict_ok is not None:
        print(f"  Predict endpoint: {'✅ PASS' if predict_ok else '❌ FAIL'}")
