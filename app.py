# This file will contain the code required to process the images and thier comparisons
import cv2
import numpy


def main():
    image_name = "face2.jpg"
    image = cv2.imread(image_name)
    face = crop_face(image)
    print(type(face))
    compute_emotion(face)


def compute_emotion(image):
    cv2.imshow("face", image)
    cv2.waitKey(0)


def crop_face(image):
    cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    grayImg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(grayImg, 1.1, 5)
    if len(faces) > 1:
        print("More than one face found. Please use a single face per picture")
        exit()
    x, y, w, h = faces[0]
    # cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 0), 3)
    crop_image = image[y:y + h, x:x + w]
    # cv2.imshow('face', image)
    # cv2.imshow("cropped", crop_image)
    return crop_image


if __name__ == '__main__':
    main()
