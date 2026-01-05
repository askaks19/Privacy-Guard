# 📋 Privacy Guard Setup Guide

## Prerequisites

- **Python 3.7+** installed
- **pip** (Python package manager)
- A working **webcam**
- **Windows, macOS, or Linux** OS

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/askaks19/Privacy-Guard.git
cd Privacy-Guard
```

### 2. Create a Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

```bash
python privacy_guard.py
```

## How It Works

1. **Single Face**: Display shows green text "Faces Detected: 1" - Normal operation ✔
2. **Multiple Faces**: Detects 2+ faces and automatically minimizes the active window ⚠
3. **Exit**: Press 'q' to quit the application

## Features

✅ Real-time face detection using MediaPipe  
✅ OpenCV video stream processing  
✅ Automatic window minimization on detection  
✅ Visual feedback with face count display  
✅ Lightweight and efficient  

## Troubleshooting

### Camera Not Found
- Check if webcam is connected
- Ensure no other app is using the camera
- Try using a different camera index (modify `cv2.VideoCapture(0)` to `cv2.VideoCapture(1)`)

### Slow Performance
- Reduce frame size in the code
- Lower the `min_detection_confidence` value (currently 0.6)

### Window Not Minimizing
- On Linux: PyAutoGUI may need X11 display
- On macOS: May require accessibility permissions

## System Requirements

- **RAM**: Minimum 2GB
- **CPU**: Dual-core processor or better
- **Webcam**: 720p or higher recommended

## License

MIT License - See LICENSE file for details

## Support

For issues, please open a GitHub issue with:
- OS and Python version
- Error message
- Steps to reproduce
