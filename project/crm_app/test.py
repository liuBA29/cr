import cv2
import sys


imgPath = input("введите путь к картинке: ")
faceCascade = cv2.CascadeClassifier(
    cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

img = cv2.imread(imgPath)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(
    imgGray,
    scaleFactor=1.1,
    minNeighbors=7,
    minSize=(30,30),
    flags = cv2.CASCADE_SCALE_IMAGE
)

print(f"Найдено лиц: {len(faces)}")

if(len(faces)):
    print("Вывожу результат обнаружения на экран...")
    for (x ,y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 5)

    cv2.imshow("Найденные лица", img)
    cv2.waitKey(0)
else:
    print("нет никого...")