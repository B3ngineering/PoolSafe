# PoolSafe
#### The Raspberry Pi lifeguarding assistant

This project leverages OpenCV and Python, as well as a drowning detection model to monitor a space and determine whether or not there is someone drowning.
By connecting a camera to a Raspberry Pi, we can identify possible drowning accidents as they happen and send an email to the pool owner to alert them.

It is also possible to set up a buzzer system for the Raspberry Pi or send a text message, but I opted for email due to simplicity.

Run with: python3 drowning_detection.py --modeldir=coc_ssd

Demo: https://youtu.be/V16wfmXP7nk


### Installation and Setup
Physical Resources: Raspberry Pi 4, camera (usb or other will do), power supply
Software Commands (outside of normal pi setup):
- pip install -U numpy
- python3 -m pip install tflite-runtime
- sudo apt -y install libjpeg-dev libtiff5-dev libjasper-dev  libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev
- sudo apt -y install libatlas-base-dev libhdf5-103
- python -m pip install opencv--python==4.5.3.56


### Resources
Some guides/tutorials that I used to get started:
- https://pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/
- https://www.instructables.com/Human-Position-Recognition-With-Camera-and-Raspber/
- https://www.digikey.ca/en/maker/projects/how-to-perform-object-detection-with-tensorflow-lite-on-raspberry-pi/b929e1519c7c43d5b2c6f89984883588
- https://universe.roboflow.com/yashwanee-tetar-jm88u/drowning-detection-and-prevention-in-swimming-pools (Model API)
