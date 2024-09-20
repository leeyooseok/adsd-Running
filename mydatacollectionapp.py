from myjoystickcamapp import MyJoystickCamApp
import time
import os
import cv2

class MyDataCollectionApp(MyJoystickCamApp):
    def __init__(self,cbJoyPos=None):
        super().__init__(cbJoyPos)
        
        self.rl=0
        self.cnt_frame_total=0
        self.cnt_frame = 0
        self.t_prev = time.time()
        
        self.datadir='data.%f'%(time.time())
        os.mkdir(self.datadir)
        os.mkdir(os.path.join(self.datadir,'_0_forward'))
        os.mkdir(os.path.join(self.datadir,'_1_right'))
        os.mkdir(os.path.join(self.datadir,'_2_left'))
        os.mkdir(os.path.join(self.datadir,'_3_stop'))
        
        self.names=['_0_forward','_1_right','_2_left','_3_stop']
    
    def setRL(self,rl):
        self.rl=rl
        
    def collectData(self,frame):
        rl=self.rl
        collect_data=(rl&4)>>2
        if collect_data==1:
            frame=cv2.resize(frame,(160,120))
            rl=rl&3
            road_file='%f.png'%(time.time())
            cv2.imwrite(
                os.path.join(
                os.path.join(
                    self.datadir,self.names[rl]),
                    road_file),frame)
            self.cnt_frame_total+=1
    def checkFrameRate(self): #overriding
        self.cnt_frame+=1
        t_now=time.time()
        if t_now-self.t_prev>=1.0:
            self.t_prev=t_now
            print("frame count : %d" %self.cnt_frame, \
                      "total frame : %d" %self.cnt_frame_total)
            self.cnt_frame=0
        
