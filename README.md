# Gesture-Controlled Screen Brightness

An interactive Computer Vision application built in Python that uses real-time hand gesture tracking to control system monitor brightness. By measuring the distance between the user's thumb and index finger, the application dynamically updates hardware brightness levels seamlessly.

## 🚀 Key Features
* **Real-Time Hand Tracking:** Leverages Google's `MediaPipe` Hands framework to map 21 distinct 3D hand coordinates at high frame rates.
* **Hardware Integration:** Employs the `screen_brightness_control` library to directly manipulate the operating system's native monitor brightness settings.
* **Smart Linear Interpolation:** Uses NumPy's mathematical mapping (`interp`) to safely convert custom pixel-distance ranges into standard hardware brightness values (0% to 100%).
* **Immersive Visual Feedback:** Includes an interactive full-screen OpenCV window overlay that draws tracking vectors and displays live percentage statuses.

## 🛠️ Tech Stack
* **Language:** Python
* **Computer Vision:** OpenCV (cv2)
* **Machine Learning Tracking:** MediaPipe
* **Data Processing & Math:** NumPy

## 📦 Installation & Setup
1. Clone the repository.
2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
3. Execute the script with a connected webcam:

    '''bash
    python main.py