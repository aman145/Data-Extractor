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

![original Image](https://user-images.githubusercontent.com/37553965/60964604-5b2e5980-a331-11e9-9d9a-2ccb2ba856c4.PNG) ![Edge detection](https://user-images.githubusercontent.com/37553965/60964751-c710c200-a331-11e9-9292-fdc249d15e9b.PNG)


Step 2: Use the edges in the image to find the contour (outline) representing the piece of paper being scanned.

![Edge 2](https://user-images.githubusercontent.com/37553965/60965015-5f0eab80-a332-11e9-942a-7a15226b920c.PNG)

Step 3: Apply a perspective transform to obtain the top-down view of the document.
![original Image](https://user-images.githubusercontent.com/37553965/60965091-9b420c00-a332-11e9-8a54-dea75b8ca7e0.PNG)![Output Image2](https://user-images.githubusercontent.com/37553965/60965096-9ed59300-a332-11e9-8a3c-b3446440026d.PNG)

Phase 2- Convert scanned image into text file
 Using Tessereact, all the data is extracted from processed image and stored in text file for data mining and analysis.![Screenshot (2)](https://user-images.githubusercontent.com/37553965/61353955-a3e49600-a88e-11e9-9758-f9a4b6968423.png)

Phase 3- Desiging the User Interface for better Intersection and Visualization
![Screenshot (3)](https://user-images.githubusercontent.com/37553965/61354107-063d9680-a88f-11e9-87af-22715668335d.png)
![Screenshot (4)](https://user-images.githubusercontent.com/37553965/61354132-1a819380-a88f-11e9-9d38-72c40814515e.png)
![Screenshot (5)](https://user-images.githubusercontent.com/37553965/61354139-1fdede00-a88f-11e9-8c5d-2ca227dd1c1e.png)
![Screenshot (6)](https://user-images.githubusercontent.com/37553965/61354151-253c2880-a88f-11e9-880b-e2b28340585e.png)
![Screenshot (7)](https://user-images.githubusercontent.com/37553965/61354165-2bcaa000-a88f-11e9-8d54-e41e9f33497f.png)

 
