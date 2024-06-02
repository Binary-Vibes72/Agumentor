
# Agumentor (Virtual Painting)

## Objective:
To develop a virtual painting application that allows users to draw and paint on a digital canvas using hand gestures, leveraging computer vision techniques provided by the OpenCV library.

## Project Description:
The Virtual Painting application enables users to interact with a digital canvas without traditional input devices like a mouse or stylus. Instead, it uses a webcam to capture hand gestures, which are then processed to control the painting actions. This project demonstrates the integration of real-time video processing and gesture recognition to create an intuitive and interactive drawing experience

## Technologies Used:
- __Programming Language__ : Python
- __Libraries__: OpenCV for computer vision tasks, NumPy for numerical operations
- __Tools__: Webcam for real-time video capture

## Implementation Steps:
- __Set Up Environment__ : Install Python, OpenCV, and other necessary libraries using the 'requirements.txt'.
```bash
pip install -r requirements.txt
```
and run project by,

```bash
python VirtualPainting.py
```

- __Hand Detection__ : Use OpenCV to process video frames from the webcam and detect the hand's position.
- __Gesture Recognition__ : Implement contour detection and convex hull techniques to identify specific hand gestures.

- __Drawing Mechanism__ : Map the detected hand movements to corresponding drawing actions on the canvas.
- __User Interface__ : Design a simple UI to display the canvas and controls for color and brush size selection.
- __Testing and Debugging__ : Thoroughly test the application to ensure smooth and accurate gesture recognition and drawing.

### note:
if you found and bug or error then, you can contribute to this project by raising the bug request to this repository. 