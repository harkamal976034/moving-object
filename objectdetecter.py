import  cv2

#making backgound image for image detection
background=cv2.imread("C:/Users/harkamal singh/Desktop/back2.png")
background=cv2.GaussianBlur(background,(21,21),0)
background=cv2.cvtColor(background,cv2.COLOR_BGR2GRAY)
#resizing the image
background=cv2.resize(background,(1000,600))

#capturing the video
cap=cv2.VideoCapture("C:/Users/harkamal singh/Desktop/testvid.mp4")

while True:
    ret,frame=cap.read()
#converting original image to gray and adding blur to it
    gray=cv2.GaussianBlur(frame,(21,21),0)
    gray=cv2.cvtColor(gray,cv2.COLOR_BGR2GRAY)
#resizing the image
    gray = cv2.resize(gray, (1000,600))
#diff is to find the absolute difference between two photos
    diff=cv2.absdiff(background,gray)
#threshold function is used to find the threshold pixels
    _,thresh=cv2.threshold(diff,30,255,cv2.THRESH_BINARY)
#dilate is use to minimize the pixels
    thresh=cv2.dilate(thresh,None,iterations=4)
#contours is to find the region of interest , i am using the retr_external method ans chain approx
    cnts,res=cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for contour in cnts:
        if cv2.contourArea(contour)<20000:
            continue
        (x,y,w,h)=cv2.boundingRect(contour)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
#showing the video
    cv2.imshow("cctv footage",frame)
    #cv2.imshow("diff video",thresh)
    #cv2.imshow("blurred video",gray)
#waitkey is used to close the program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyWindow