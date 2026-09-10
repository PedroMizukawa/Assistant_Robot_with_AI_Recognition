# Assistant Robot with AI Recognition 🤖

Following the pandemic period experienced in Brazil in 2020, there was an increase in cases of loneliness and anxiety due to social distancing and the loss of family members that occurred during that time. Therefore, it became necessary to develop accessible and personalized mechanisms that could help reduce social isolation.

The project aims to combine robotics and artificial intelligence (AI) by creating a digital assistant that interacts with individuals through music. The songs are pre-selected by the user, providing a sense of personal comfort based on their musical preferences.

The robot captures an image of the user using an ESP32-CAM S3 camera and sends it to a computer, where an AI model performs facial recognition and identifies the user's emotional state. Based on the user's emotion (happy, sad, etc.), the system selects and plays a song, while the robot performs pre-programmed movements.

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
