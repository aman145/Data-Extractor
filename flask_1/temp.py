import csv
import imutils
import cv2
import random
import numpy as np
import argparse
from skimage.filters import threshold_local

def order_points(pts):
    rect=np.zeros((4,2),dtype="float32")
    s=pts.sum(axis=1)
    rect[0]=pts[np.argmin(s)]
    rect[2]=pts[np.argmax(s)]
    diff=np.diff(pts,axis=1)
    rect[1]=pts[np.argmin(diff)]
    rect[3]=pts[np.argmax(diff)]
    return rect

def four_point_transform(image,pts):
    rect=order_points(pts)
    (tl,tr,br,bl)=rect
    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))
    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))
    dst = np.array(
        [[0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype = "float32")
    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
    return warped
def text_extract(picture):
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image",help = "Path to the image to be scanned")
    image = cv2.imread(picture,0)
    ratio = image.shape[0] / 500.0
    orig = image.copy()
    image = imutils.resize(image, height = 500)
    gray = cv2.GaussianBlur(image, (5, 5), 0)
    edged = cv2.Canny(gray, 75, 200)
    cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sorted(cnts, key = cv2.contourArea, reverse=True)[:5]
    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        if len(approx) == 4:
            screenCnt = approx
            break
    warped = four_point_transform(orig, screenCnt.reshape(4, 2) * ratio)
    T = threshold_local(warped, 11, offset = 10, method = "gaussian")
    warped = (warped > T).astype("uint8") * 255
    imS = cv2.resize(warped, (1350, 1150))
    from PIL import Image
    import PIL.Image
    
    from pytesseract import image_to_string
    import pytesseract
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'
    TESSDATA_PREFIX = 'C:/Program Files (x86)/Tesseract-OCR'
    output = pytesseract.image_to_string(imS, lang='eng')
    counter=str(random.randint(1,10000000000))
    myfile=open(r"C:\Users\admin\Desktop\Project_1\flask_1\static\text_files\demo"+counter+".txt",'w')
    myfile.write(output)
    myfile.close()
    with open(r"C:\Users\admin\Desktop\Project_1\flask_1\static\text_files\demo"+counter+".txt", 'r') as infile, open(r"C:\Users\admin\Desktop\Project_1\flask_1\static\text_files\demo"+counter+"..csv", 'w') as outfile:
        stripped = (line.strip() for line in infile)
        lines = (line.split(",") for line in stripped if line)
        writer = csv.writer(outfile)
        writer.writerows(lines)
    with open(r"C:\Users\admin\Desktop\Project_1\flask_1\static\text_files\demo"+counter+"..csv", 'r') as f_in, open(r"C:\Users\admin\Desktop\Project_1\flask_1\static\text_files\demo"+counter+".csv", "w") as f_out:
        reader = csv.reader(f_in, delimiter=" ")
        writer = csv.writer(f_out, delimiter=",")
        writer.writerows(reader)

