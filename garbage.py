from ultralytics import YOLO
import cv2
import cvzone
import math, os

#! MODEL NEEDS MORE TRAINING, 'm' OR 'l' MODEL TO BE CONSIDERED, AND MORE DATASETS

cap = cv2.VideoCapture("Workspace/Test/videos/garbage5.mp4")

model = YOLO("Workspace/Trained Models/best.pt")
# model = YOLO(os.path.join(os.getcwd(), 'best.pt')) # ANOTHER METHOD
model.to('cpu')

classNames = ["garbage"]


while True:
    success , img = cap.read()
    results = model(img,stream=True)
    for r in results:
        boxes = r.boxes
        for box in boxes:
            #for boxes
            x1,x2,y1,y2 = box.xyxy[0]
            x1,x2,y1,y2 = int(x1), int(y1) , int(x2), int(y2)
            
            cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,255),3)

            #for confidence

            conf = math.ceil((box.conf[0]*100))/100
            print(conf)

            #for class

            cls = int(box.cls[0])
            cvzone.putTextRect(img,f'{classNames[cls]} {conf}',(max(0,x1),max(35,y1)))



    cv2.imshow("image",img)
    cv2.waitKey(1)