<p align="center">
  <img src="preview.png" width="500" alt="Gesture Volume Control Preview"/>
</p>

<h1 align="center">🎛️ Gesture Volume Control</h1>
<p align="center">
  Control your PC volume in real-time using hand gestures with <b>OpenCV</b>, <b>MediaPipe</b>, and <b>PyCaw</b>.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?logo=python"/>
  <img src="https://img.shields.io/badge/OpenCV-4.0+-red?logo=opencv"/>
  <img src="https://img.shields.io/badge/License-MIT-green"/>
  <img src="https://img.shields.io/badge/Platform-Windows-lightgrey"/>
</p>

---

## 📖 Overview
A smart and interactive system that lets you **control your PC’s volume using hand gestures** via webcam.  
Built with `OpenCV`, `MediaPipe`, `PyCaw`, and enhanced with **voice feedback** using `pyttsx3`.

---

## 📽️ Demo
> 🎥 _Coming soon: GIF demo of finger distance controlling volume and pinky gesture for mute/unmute._

---

## 🚀 Features
- 🖐️ Real-time hand detection using webcam  
- 📏 Adjusts system volume based on **thumb–index finger distance**  
- 🔇 Mute/Unmute with a **thumb + pinky** gesture  
- 🔊 Voice feedback using **pyttsx3**  
- 🎯 Displays volume percentage and FPS for smooth interaction  
- ✅ Error handling (e.g., missing modules, camera not available)  

---

## ⚙️ Tech Stack
| Category        | Tools / Libraries |
|-----------------|-------------------|
| **Language**    | Python 3.10       |
| **Computer Vision** | OpenCV        |
| **Hand Tracking**   | MediaPipe     |
| **System Volume**   | PyCaw         |
| **Audio Feedback**  | pyttsx3       |
| **Others**          | NumPy, math   |

---
## 🗂️ Project Structure
```
GestureVolumeControl/
├── HandTrackingModule.py   # Hand detection using MediaPipe
├── VolumeHandControl.py    # Main gesture-to-volume logic
├── requirements.txt        # All dependencies
├── README.md               # Project documentation
└── venv310/                # Virtual environment (optional)
```
---

## 🤝 Contributing
Contributions are welcome!  
- Fork the repository  
- Create your feature branch (`git checkout -b feature-name`)  
- Commit your changes (`git commit -m "Added feature"`)  
- Push to the branch (`git push origin feature-name`)  
- Open a Pull Request 

For major changes, please open an **issue** first to discuss what you’d like to change.  

---

## 🧑‍💻 Author
**Devanshu Dasgupta**  
Made with ❤️ and a passion for open source.  

🌐 [LinkedIn](https://www.linkedin.com/in/devanshu-dasgupta)  
✉️ [Email](mailto:devanshu.das.gupta14@gmail.com)  

---

## 🧾 License
This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE.md) file for more details.
