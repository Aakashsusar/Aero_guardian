import sys

# 🔴 REMOVE all Gunicorn CLI args before Ultralytics loads
sys.argv = [""]

from app import app  # noqa: E402

# Gunicorn will look for `app`
