# Counting-Vehicle

A vehicle count model that takes an input of the path of the video and two coordinates (these coordinates are used to create a line you have to count the vehicles crossing this line) using YOLO.


# How to install dependecies ?

* Install [python 3.7+](https://www.python.org/downloads/release/python-378/)
* Open a terminal and type in the below command to install **virtualenv** module
~~~
pip install virtualenv
~~~

* Create a new folder and clone this repository *(Assuming you already have **git** installed)*
~~~
git clone https://github.com/HOTSONHONET/Counting-Vehicle.git
~~~

* Use `Shift + rightclick` to open up a terminal in the folder
* Create a virtual environment and install all the dependecies from **requirements.txt**
~~~
virtualenv <name-of-env>
./<name-of-env>/Scripts/activate
pip install -r requirements.txt
~~~

* Download the yolo weights file from [here...](https://drive.google.com/file/d/1hY8edW6v2czNGr0lO4g6urzH6dlKYiT-/view?usp=sharing)


# Folder Structure
* After downloading the weight file, make sure you have the same folder structure
* It may happen that you may not have the *__pyache__* folder, it's completely fine 👌
~~~
│   .gitignore
│   log.txt
│   main.py
│   requirements.txt
│
├───.vscode
│       settings.json
│
├───blobs
│   │   blob.py
│   │   __init__.py
│   │
│   └───__pycache__
│           blob.cpython-37.pyc
│           __init__.cpython-37.pyc
│
├───detector
│   │   detector.py
│   │   labels.txt
│   │   yolov3.cfg
│   │   yolov3.weights
│   │   __init__.py
│   │
│   └───__pycache__
│           detector.cpython-37.pyc
│           __init__.cpython-37.pyc
~~~


# How to run the application ?
* Open command prompt inside the clone folder using `Shift + rightclick`
* Type the below command, this will ask you for the video path and the cross line height in terms of precentage
~~~
py main.py
~~~
* Watch this video 😉

[![Working Video](https://user-images.githubusercontent.com/56304060/112906740-4b106c00-910a-11eb-820a-0d8cc1acb9ac.png)](https://user-images.githubusercontent.com/56304060/112905094-7b0a4000-9107-11eb-9e5c-96b7d6a4fabe.mp4)
