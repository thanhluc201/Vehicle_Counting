
import cv2 as cv # thêm thư viện Opencv
from dem import * # thêm modul dem.py
tracker = EuclideanDistTracker () #khai báo class tracker để đếm
cap = cv.VideoCapture("D:\\XLA\\XLA\\aka\\video\\dio.mp4")# thêm video

object_detector = cv.createBackgroundSubtractorMOG2(history=300,varThreshold=100) #khởi tạo giải thuật Background Subtractor
out = cv.VideoWriter('output.mp4', -1, 20.0, (960,540)) # xuất video ra file output.mp4
while True:

    ret,frame = cap.read() # đọc từng frame trong vòng lặp
    height,width,_=frame.shape
    frame = cv.resize(frame,(960,540)) # thay đôi kích thước video nhỏ hơn
    roi =  frame[250:540,300:500] # tách phần xe đi lại chủ yếu để xử lý đỡ bị nhầm lẫn hơn
    mask = object_detector.apply(roi) #Sử dụng Background subtractor với từng frame của "roi" để thu được Foreground Mask
    _,mask = cv.threshold(mask,254,255,cv.THRESH_BINARY) # frame về đen trắng
    dect = [] # khái báo mảng vị trí x,y,h,w của đối tượng phát hiện đc
    contours,_ =cv.findContours(mask,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)# xác định đường biên
    for cnt in contours:
        #lấy xe
        area = cv.contourArea(cnt)
        if area >2500:
            x,y,h,w = cv.boundingRect(cnt)
            cv.rectangle(roi,(x,y),(x+w,y+h),(0,222,0),3) # vẽ hình chữ nhật bao quanh xe xác đinh được
            dect.append([x,y,h,w])# chèn [x,y,h,w] vào dect
    #xác định đối tượng và đánh số
    boxes_ids = tracker.update(dect)
    for box_id in boxes_ids:
        x, y, h, w, id = box_id
        cv.putText(roi, str(id), (x, y - 15), cv.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
        cv.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 3)
    cv.putText(frame,"Tong so xe :  ",(50,50),cv.FONT_HERSHEY_PLAIN, 2, (0, 255, 204), 2)
    cv.putText(frame,str(id),(300,50),cv.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
    # hiển thị cửa sổ video Frame, roi, Mask 
    cv.imshow('Frame',frame)
    cv.imshow('roi',roi)
    cv.imshow('Mask',mask)
    out.write(frame)
    #thoát băng Esc
    key=cv.waitKey(30)
    if key == 27:
        break
cap.release()
out.release()
cv.destroyAllWindows()