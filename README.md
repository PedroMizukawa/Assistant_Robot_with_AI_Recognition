# Assistant Robot with AI Recognition 🤖

This project integrates hardware and software to create an interactive robot that recognizes human facial expressions in real-time and reacts to them with physical movements and contextual music. 

The system uses an ESP32 camera for local video streaming, Python-based image processing for emotion detection, Bluetooth Low Energy (BLE) integration with Lego Boost motors, and the Spotify API for media control.

## Technologies and Architecture

*   **Computer Vision:** Real-time video processing on the PC using OpenCV and the MTCNN-based `fer` (Facial Expression Recognition) library.
*   **IoT & Hardware:** ESP32-S3 CAM OV5640 acting as a local Wi-Fi video streaming server.
*   **Robotics:** Motor control of the Lego Boost Hub via Bluetooth Low Energy (BLE) using the `pylgbst` library.
*   **Media Integration:** Spotify API (`spotipy` with OAuth) to play specific playlists based on the detected emotion.

## 🛠️ Hardware Requirements

*   ESP32-S3 CAM (OV5640) module.
*   Lego Boost "MoveHub" and one external encoded motor.
*   Local computer to run the Python processing scripts.

## ⚙️ Setup and Installation

### 1. Camera Setup (ESP32)
1. Open the `EspCode.ino` file in the Arduino IDE.
2. Insert your local Wi-Fi network credentials into the `ssid` and `password` variables.
3. Upload the code to the ESP32.
4. Open the Serial Monitor to find the assigned IP address and update the `STREAM_URL` variable in either `MainCode.py` or `TesteFERESP.py`.

### 2. Python Environment Setup
Create a virtual environment and install the required dependencies:
```bash
pip install opencv-python
pip install fer
pip install spotipy
pip install pylgbst
pip install bleak
