import pydicom as dicom
import numpy as np
from PIL import Image
import cv2

def read_img_file(path):
    img = cv2.imread(path)
    img_array = np.asarray(img)
    img2show = Image.fromarray(img_array) 
    img2 = img_array.astype(float) 
    img2 = (np.maximum(img2,0) / img2.max()) * 255.0
    img2 = np.uint8(img2)
    return img2, img2show 


