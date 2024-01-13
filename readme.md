# PyBlink: Real-time Blink Detection using Python and OpenCV

PyBlink is a Python script that leverages the dlib library and OpenCV to perform real-time blink detection in a live video stream. It counts the number of blinks and records the count in a JSON file.

## Prerequisites

- **Python 3.x**
- **OpenCV:** Install using `pip install opencv-python`
- **dlib:** Install using `pip install dlib`

## Setup

1. Clone the repository or download the `pyblick.py` script.
2. Install the required libraries:

    ```bash
    pip install opencv-python dlib
    ```
   
3. Download the `shape_predictor_68_face_landmarks.dat` file from [dlib.net](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2) and place it in the same directory as `pyblick.py`.

## Usage

Run the script using the following command:

```bash
python pyblick.py


Press 'q' to exit the video stream.

The script displays the live video stream with rectangles around detected eyes and the blink count. The blink count is saved to a file named blink_count.json.


#Acknowledgments

This script uses the `shape_predictor_68_face_landmarks.dat` model from the dlib library.

#License

This project is licensed under the MIT License - see the LICENSE file for details.

#Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.
