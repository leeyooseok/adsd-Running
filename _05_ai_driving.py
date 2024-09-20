import serial
import time

import cv2
import numpy as np

from tensorflow.keras.models import load_model
import tensorflow as tf

import threading
import queue
import sys

cap=cv2.VideoCapture('http://192.168.137.205:8080/video')

mot_serial=serial.Serial('COM6',9600)

t_now=time.time()
t_prev=time.time()
cnt_frame=0

model=load_model('model.keras')

names=['_0_forward','_1_right','2_2_left','_3_stop']

HOW_MANY_MESSAGES=10
mq=queue.Queue(HOW_MANY_MESSAGES)

def cnn_main(args):
    while True:
        frame=mq.get()
        frame_thrown=0
        while not mq.empty():
            frame=mq.get()
            frame_thrown+=1
        print(f'{frame_thrown}frame thrown')
            
        image=frame
        image=image/255
        
        image_tensor=tf.convert_to_tensor(image,dtype=tf.float32)
        
        image_tensor=tf.expand_dims(image_tensor,0)
        
        y_predict=model.predict(image_tensor)
        y_predict=np.argmax(y_predict,axis=1)
        print(names[y_predict[0]],y_predict[0])
        
        cmd=y_predict[0].item()
        
        if cmd==0: command='f'
        elif cmd==1: command='r'
        elif cmd==2: command='l'
        elif cmd==3: command='s'
        else : command='s'
        
        mot_serial.write(command.encode())
            
cnnThread=threading.Thread(target=cnn_main,args=(0,))
cnnThread.daemon=True
cnnThread.start()

while True:
    
    ret, frame=cap.read()
    
    frame=cv2.resize(frame,(640,480))

    cv2.imshow('frame',frame)
    
    frame=cv2.resize(frame,(160,120))
  
    
    mq.put(frame)
    
    key=cv2.waitKey(1)
    if key==27:
        break
    
    cnt_frame+=1
    t_now=time.time()
    if t_now-t_prev>=1.0:
        t_prev=t_now
        print("frame count : %f"%cnt_frame)
        cnt_frame=0
        
mot_serial.write('s'.encode())
mot_serial.close()
cpa.release()
cv2.destroyAllWindows()
sys.exit(0)