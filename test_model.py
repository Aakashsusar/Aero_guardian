"""
Test if the YOLO model loads correctly
"""
print("Testing YOLO model loading...")
print("=" * 50)

try:
    from ultralytics import YOLO
    print("✅ Ultralytics imported")
    
    print("\nLoading model from best.pt...")
    model = YOLO("best.pt")
    print("✅ Model loaded successfully!")
    
    print(f"\nModel type: {type(model)}")
    print(f"Model names: {model.names}")
    
    print("\n" + "=" * 50)
    print("✅ Model is ready to use!")
    print("\nYou can now run: python app.py")
    
except FileNotFoundError:
    print("❌ Error: best.pt file not found")
    print("Make sure best.pt is in the same directory as this script")
except Exception as e:
    print(f"❌ Error loading model: {e}")
    import traceback
    traceback.print_exc()
