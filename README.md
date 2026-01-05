# 🔐 Privacy-Guard

<div align="center">

![Privacy Guard](https://img.shields.io/badge/Privacy-Guard-blue?style=for-the-badge&logo=security)
![Python 3.7+](https://img.shields.io/badge/Python-3.7+-green?style=for-the-badge&logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-red?style=for-the-badge&logo=opencv)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Hand%20Detection-blue?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

**A real-time privacy protection application that automatically detects multiple faces and secures your screen**

[Features](#-features) • [Quick Start](#-quick-start) • [Installation](#-installation) • [Usage](#-usage) • [Documentation](#-documentation) • [Contributing](#-contributing)

</div>

---

## 📋 Overview

**Privacy-Guard** is an intelligent desktop application designed to protect your privacy by automatically detecting when multiple faces are present in your webcam feed. The moment a second face is detected, the application immediately minimizes your active window, preventing unauthorized viewing of your screen content.

Perfect for:
- 🏢 Corporate environments
- 🏠 Home office setups
- 🎓 Educational institutions
- 🏥 Healthcare facilities
- 📱 Developers and content creators

---

## ✨ Features

| Feature | Description | Status |
|---------|-------------|--------|
| 🎥 **Real-time Face Detection** | Continuous monitoring using webcam | ✅ |
| 🔔 **Instant Alerts** | Automatic response on face detection | ✅ |
| ⚡ **Lightweight & Fast** | Minimal CPU/RAM consumption | ✅ |
| 📊 **Visual Feedback** | Real-time face count display | ✅ |
| 🔧 **Cross-Platform** | Windows, macOS, and Linux support | ✅ |
| 🎯 **Smart Detection** | Reduces false positives with 2-sec validation | ✅ |
| 🚀 **Easy Setup** | Simple one-command installation | ✅ |
| 🛡️ **Open Source** | MIT Licensed, fully customizable | ✅ |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- Webcam
- pip (Python package manager)

### Installation (60 seconds)

```bash
# Clone the repository
git clone https://github.com/askaks19/Privacy-Guard.git
cd Privacy-Guard

# Install dependencies
pip install -r requirements.txt

# Run the application
python privacy_guard.py
```

### That's it! 🎉
Your privacy guard is now active and monitoring.

---

## 📦 Installation

### Option 1: Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Option 2: Direct Installation

```bash
pip install opencv-python mediapipe pyautogui
```

---

## 🎮 Usage

### Basic Usage

```bash
python privacy_guard.py
```

### How It Works

1. **Launch** → Application starts monitoring your webcam
2. **Normal Operation** → Green text shows "Faces Detected: 1"
3. **Detection** → When 2+ faces detected, window automatically minimizes
4. **Exit** → Press 'q' to quit

### Control Keys

| Key | Action |
|-----|--------|
| `q` | Quit application |
| `s` | Save current frame |
| `r` | Reset detection timer |
| `d` | Toggle debug mode |

---

## 🏗️ Architecture

```
┌─────────────────┐
│   Webcam Feed   │
└────────┬────────┘
         │
         ▼
┌──────────────────────────┐
│  MediaPipe Face Detection │
│  (Real-time Processing)   │
└────────┬─────────────────┘
         │
         ▼
┌──────────────────────────┐
│  Face Count Analysis     │
│  (Smart Validation)      │
└────────┬─────────────────┘
         │
    ┌────┴────────────┐
    │ 1 Face?         │ 2+ Faces?
    │ Continue Normal │ Minimize Window
    └─────────────────┘
```

---

## 📊 Technical Details

### Dependencies

```
opencv-python==4.8.0.76      # Computer vision processing
mediapipe==0.10.0              # Face landmark detection
pyautogui==0.9.53              # Window control
```

### System Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| RAM | 2 GB | 4 GB |
| CPU | Dual-core | Quad-core+ |
| Webcam | 720p | 1080p+ |
| OS | Windows 7+ | Windows 10+, macOS 10.13+, Ubuntu 18.04+ |

---

## 📖 Documentation

For detailed setup and troubleshooting, see [SETUP.md](SETUP.md)

### Key Documentation

- **[SETUP.md](SETUP.md)** - Detailed installation guide and troubleshooting
- **[LICENSE](LICENSE)** - MIT License terms
- **[requirements.txt](requirements.txt)** - Python dependencies

---

## 🔍 How Detection Works

1. **Frame Capture** → Continuous webcam frame capture at 30 FPS
2. **Face Recognition** → MediaPipe detects all faces in the frame
3. **Face Counting** → Algorithm counts detected faces
4. **Smart Validation** → Requires 2-second sustained detection to prevent false positives
5. **Action Trigger** → Upon confirmation, minimizes active window
6. **Cool-down Period** → 3-second cooldown prevents spam minimization

---

## ⚙️ Customization

### Adjust Detection Sensitivity

Edit `privacy_guard.py` line 7:
```python
min_detection_confidence=0.6  # Lower = More sensitive, Higher = Less sensitive
```

### Modify Cooldown Period

Edit line 18:
```python
MINIMIZE_COOLDOWN = 3  # Cooldown in seconds
```

---

## 🐛 Troubleshooting

### Camera Not Found
```bash
# Try different camera index
# In privacy_guard.py, change:
cap = cv2.VideoCapture(0)  # Try 1, 2, 3...
```

### Slow Performance
- Reduce background processes
- Lower detection confidence value
- Close unnecessary applications

### Window Not Minimizing (Linux/macOS)
- **Linux**: Ensure X11 display is available
- **macOS**: Grant accessibility permissions to terminal

For more help, see [SETUP.md](SETUP.md)

---

## 🤝 Contributing

Contributions are welcome! Please feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 askaks19

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

---

## 🙏 Acknowledgments

- [MediaPipe](https://mediapipe.dev/) - Face detection framework
- [OpenCV](https://opencv.org/) - Computer vision library
- [PyAutoGUI](https://pyautogui.readthedocs.io/) - GUI automation

---

## 📞 Support

Need help? 

- 📚 Check [SETUP.md](SETUP.md) for detailed troubleshooting
- 🐛 [Open an issue](https://github.com/askaks19/Privacy-Guard/issues) with:
  - Your OS and Python version
  - Error message (if any)
  - Steps to reproduce

---

## 🎯 Roadmap

- [ ] Multi-monitor support
- [ ] Scheduled monitoring (e.g., office hours only)
- [ ] Custom alert sounds
- [ ] GUI dashboard
- [ ] Mobile app integration
- [ ] Cloud sync for settings

---

<div align="center">

**[⬆ Back to Top](#-privacy-guard)**

Made with ❤️ by [askaks19](https://github.com/askaks19)

⭐ If you find this project helpful, please consider giving it a star!

</div>
