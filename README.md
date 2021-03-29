# Counting-Vehicle

A vehicle count model that takes an input of the path of the video and two coordinates (these coordinates are used to create a line you have to count the vehicles crossing this line) using YOLO.


# How to use it ?

* Install [python 3.7+](https://www.python.org/downloads/release/python-378/)
* Open a terminal and type in the below command to install **virtualenv** module
~~~
pip install virtualenv
~~~

* Create a new folder and clone this repository *(Assuming you already have **git** installed)*
~~~
git clone https://github.com/HOTSONHONET/eazyBeat.git
~~~

* Use `Shift + rightclick` to open up a terminal in the folder
* Create a virtual environment and install all the dependecies from **requirements.txt**
~~~
virtualenv <name-of-env>
./<name-of-env>/Scripts/activate
pip install -r requirements.txt
~~~
* Now, once all of the packages are installed, go to the cloned folder and run this command to start the application *(Assuming you are on windows like me 😉, for linux and mac users, replace **py** with **python3**)*
~~~
cd ./main
py wsgi.py
~~~

* You will see a **http** url in the terminal, copy that link and open it in your browser
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






