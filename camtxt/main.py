import cv2
import PIL import Image
from pytesseract import pytesseract

camera=cv2.VideoCapture(0)
while True:
    -,image=camera.read()
    cv2.imshow('Text Detect',image)
    if cv2.waitkey(1)& 0xFF==ord('s'):
        cv2.imwrite('test1.jpg',image)
        break
camera.release()
cv2.destroyAllWindow()
def tesseract():
    path_to_tesseract=r"C:\Users\placement\Downloads\tesseract-ocr-w64-setup-5.3.1.20230401.exe"
    Imagepath='test1.png'
    pytesseract.tesseract_cmd=path_to_tesseract
    text=pytesseract.image_to_string(Image.open(Imagepath))
    print(text[:-1])
    tesseract()


