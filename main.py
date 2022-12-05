import cv2
import matplotlib.pyplot as plt


cap = cv2.VideoCapture("./files/video.mp4")
cv2.namedWindow("frames", cv2.WINDOW_KEEPRATIO)
while cap.isOpened():
    ret, frame = cap.read()
    
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray,(5,5),0)
        ret, th = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        
        contours = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]

        perimeter = 0

        for i in range(len(contours)):
            perimeter += cv2.arcLength(contours[i], True)
            cv2.drawContours(frame, contours, i, (255, 0, 0), 1)
        
        #print(perimeter)
        
        if(perimeter > 7000):
            cv2.putText(frame, "It's my picture!", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0))
        #    cv2.imwrite("pares/12.03/files/mytest.png", frame)

        cv2.imshow("frames", frame)
        
        
        key = cv2.waitKey(25)
        if key == ord('q'):
            break
        
        if key == ord('s'):
            cv2.imwrite("pares/12.03/files/myframe.png", frame)
    
    else: 
        break

    
cap.release()
cv2.destroyAllWindows()
