import cv2 #pip install opencv2
from playsound import playsound #pip install playsound
fire_cascade = cv2.CascadeClassifier('fire_detection.xml') #Using this line we can access GUI XML File  
cap = cv2.VideoCapture(0)  #(0,1) use to access web camera
#===== For laptop use 0 and for usb web cam use 1 =====#
while(True):
    ret, frame = cap.read() #to read video Frame by frame 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #To convert Color image into Gray Scale Image
    fire = fire_cascade.detectMultiScale(frame, 1.2, 5)#to detect the Fire 
    for (x,y,w,h) in fire:
        cv2.rectangle(frame,(x-20,y-20),(x+w+20,y+h+20),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        print("Fire is Detected") #It will Print the Notification
        playsound('audio.mp3')# It will Play the Alert Sound
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): # To Close the Pop Up Window
        break