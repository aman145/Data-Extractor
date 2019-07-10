# Data-Extractor
Data Extraction from images


# Problem
It is difficult to assemble or organise the health deatils files(for eg. lab test report ).Doctor also took time to examine the reports.

# Solution 
Combining both the senarios and coming with automate and digital solution.
User just to upload the lab reports (images ) in the application .All the data will be extract and will give the digital reports.
Benifits:

1: Get rid of oraganising the bundle of reports.

2: Secure Digital data analysing.

3: Patient can also track his or her health care by distinct parameters.

4: Doctor will also get a simple methodology to examine the reports of perticular patient. 

# About Project

 Initial Handlings and Packages

 Programing Language: Python
 Methods: Image Processing , Tesseract-OCR , Flask(For UI Interface)

# Inititial installations:
Python :3.7
Softwares: Anaconda,Atom,Spyder,PyCharm (Any One)

# Packages
Flask : for UI Interface

Install Commands:

pip install flask

Other packages inside flask:

pip install flask-wtf : Direct forms interface with flask

pip install flask-sqlalchemy : Database connectivity with flask

For Image Processing:

Opencv : pip install opencv

NumPy : as usually installed

Imutils : pip install imutils

Argparse : pip install argparse

Skimage : pip install scikit-image

PIL : pip install pillow

# Data Extractiong from Iamges and PDFs
Pytesseract: pip install pytesseract


# Procedure

Phase 1:

Phase 1- Developed Scanner using OpenCv

Building a scanner with OpenCV can be accomplished in just three simple steps:

Step 1: Detect edges.

Step 2: Use the edges in the image to find the contour (outline) representing the piece of paper being scanned.

Step 3: Apply a perspective transform to obtain the top-down view of the document.

Step 1: Detect edges

![original Image](https://user-images.githubusercontent.com/37553965/60964604-5b2e5980-a331-11e9-9d9a-2ccb2ba856c4.PNG)



