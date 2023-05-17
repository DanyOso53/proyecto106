import cv2

clasificador=cv2.CascadeClassifier("haarcascade_fullbody.xml")
cara=cv2.VideoCapture("boy.jpg")


while True :   
    ret,img=cara.read()
    gris=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

    detector= clasificador.detectMultiScale(gris,1.1,5)

    for (x,y,w,h) in detector:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow("cara",img)
    
    if cv2.waitKey(0)==32:
        break
       

cara.release()
cv2.destroyAllWindows()