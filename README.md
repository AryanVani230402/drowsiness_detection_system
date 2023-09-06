# Drowsiness Detection System
## Introduction
This is a Python-based Drowsiness Detection System that uses computer vision to detect if a person's eyes are closed, which can be indicative of drowsiness or fatigue. When drowsiness is detected, the system can trigger an alert, such as a sound, to alert the person.

## Prerequisites
Before you begin, ensure you have met the following requirements:
Python 3.x installed
Required Python packages installed (see 'Installation' section)

## Installation
To install the necessary packages, you can use "pip install requirements"

## Usage
Clone this repository to your local machine:
"git clone https://github.com/yourusername/drowsiness-detection-system.git"

Navigate to the project directory:
"cd drowsiness-detection-system"

Run the program:
"python main.py"

The program will open your computer's camera and start monitoring for drowsiness. When drowsiness is detected, the alert sound will play.

To exit the program, press 'q' in the terminal.

## Configuration
You can configure the following parameters in the main.py file to customize the behavior of the system:

ear_threshold: Adjust this threshold to control when the system considers eyes to be closed.
sound_file: Set this to the path of the WAV sound file you want to play when drowsiness is detected.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
This project uses the Dlib library for face detection and facial landmark prediction.
Sound alerts are played using the pygame library.

## Contributing
Contributions are welcome! If you would like to contribute to this project, please open an issue or create a pull request.

## Contact
If you have any questions or suggestions, feel free to contact me at [aryanvani2304@gmail.com].

## Troubleshooting
If you encounter any issues while setting up or running the system, check the following:

Ensure that you have installed all the required packages (see 'Prerequisites' and 'Installation' sections).
Verify that the shape predictor file is in the project directory.
Make sure your sound file is in WAV format and is located in the project directory.

## References
Dlib
pygame


## Thank you for using the Drowsiness Detection System! We hope it helps improve safety and alertness in various applications. If you encounter any issues or have suggestions for improvements, please don't hesitate to reach out.
