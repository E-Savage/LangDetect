# 🕵️ Language Detective 🥸

** NOTE: It should be noted that this application is the final Project for the CIS 542: Digital Forensics Course and was created as a requirement for the project submission of this course.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation
Prereqs: 
1. You will need to do the pip install for python curses for your system using "*__pip install curses__*", if you are on a windows machine you will need to use "*__pip install windows-curses__*"
2. you will need to install the scikit learn packages using "*__pip install scikit-learn__*"
3. you need to install joblib using "*__pip install joblib__*"

*__If you are using anaconda then you will should not have to install prerequisite 2 or 3, but it should be noted you should stil check if anaconda installed the library properly__*

To download the application:

Download zipped file from github and extract where you would like to and it will be runnable from there.

## Usage
The intended use of this application is to be used alongside digital evidence in which the investigator made need to check the language of the text they are looking at.

To run the app user the terminal to navigate to the directory the app is in and then execute thr program by using "python main.py"

**The main window of the application can be navigated using the arrow keys and enter to to select the option**  

Features within the app:
1. Language Detection - this feature allows the user to input text and have it discern the language, the app stores the previous detection to keep it for the next detection. To exit the language detection mode one can enter a single q or enter in a blank space, after that you may move through the application as usual.
2. The help page gives a short description of each feature of the app. It has a description for Language detection, help page, about page, and then the exit button.
3. The about page shares a short description about the project itself and its purpose. it also shares about how it was made.
4. The exit button signals to the system to shut down the program.

## Contributing
