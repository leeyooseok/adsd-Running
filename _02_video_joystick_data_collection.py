from mydatacollectionapp import MyDataCollectionApp
import serial

mot_serial=serial.Serial('COM3',9600)

def cbJoyPos(joystickPosition,app=None):
    posX,posY=joystickPosition
    
    speed=0
    if app!=None : speed=app.getSpeed()
    
    command='s'
    collect_data=1
    if posY<-0.5:
        command='b' #brake
        collect_data=0
    elif posY>0.15:
        if -0.15<=posX<=0.15:
            command='f'
        elif posX<-0.15:
            command='l'
        elif posX>0.15:
            command='r'
    else :#-0.5<=posY<=0.15
        command='s'
        collect_data=0
    
    if command=='f': right,left=0,0
    elif command=='l': right,left=1,0
    elif command=='r': right,left=0,1
    elif command=='s': right,left=1,1
    else: right,left=1,1    
    
    rl=collect_data<<2|right<<1|left
    myDataCollectionApp.setRL(rl)
    mot_serial.write(command.encode())

myDataCollectionApp=MyDataCollectionApp(cbJoyPos=cbJoyPos)
myDataCollectionApp.run()
    
        

