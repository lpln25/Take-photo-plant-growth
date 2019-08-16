import picamera
from datetime import datetime
import time

# Adress File
addressImage = "/home/pi/Project/test2/Image/"
addressVideo = "/home/pi/Desktop/Login/Video/"
# user
user = "Mohamad ganji "
# Id capture
ID_ = '766156045529'
# Mode Effect
mode0 = "none"
mode1 = "negative"
mode2 = "solarize"
mode3 = "sketch"
mode4 = "denoise"
mode5 = "emboss"
mode6 = "oilpaint"
mode7 = "hatch"
mode8 = "gpen"
mode9 = "pastel"
mode10 = "watercolor"
mode11 = "film"
mode12 = "blur"
mode13 = "saturation"
mode14 = "colorswap"
mode15 = "washedout"
mode16 = "posterise"
mode17 = "colorpoint"
mode18 = "colorbalance"
mode19 = "cartoon"
mode20 = "deinterlace1"
mode21 = "deinterlace2"
#********************
#      function
#********************
# get time now
def timeNow():
    DT = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #DT = datetime.now().strftime('%Y-%m-%d')
    return DT

# capture image
def capture_():
    print("ready")
    DataTimeNow = timeNow()
    camera = picamera.PiCamera()
    camera.vflip = True
    ms = "take : "
    #0
    name = addressImage + "/" + mode0 + "/" + user + mode0 + DataTimeNow + ".jpg"
    print(ms,mode0)
    camera.image_effect = mode0
    camera.sharpness = 50
    camera.capture(name)
    #1
    name = addressImage + "/" + mode1 + "/" + user + mode1 + DataTimeNow + ".jpg"
    print(ms,mode1)
    camera.image_effect = mode1
    camera.sharpness = 0
    camera.capture(name)
    #2
    name = addressImage + "/" + mode2 + "/" + user + mode2 + DataTimeNow + ".jpg"
    print(ms,mode2)
    camera.image_effect = mode2
    camera.sharpness = 0
    camera.capture(name)
    #3
    name = addressImage + "/" + mode3 + "/" + user + mode3 + DataTimeNow + ".jpg"
    print(ms,mode3)
    camera.image_effect = mode3
    camera.sharpness = 0
    camera.capture(name)
    #4
    name = addressImage + "/" + mode4 + "/" + user + mode4 + DataTimeNow + ".jpg"
    print(ms,mode4)
    camera.image_effect = mode4
    camera.sharpness = 0
    camera.capture(name)
    #5
    name = addressImage + "/" + mode5 + "/" + user + mode5 + DataTimeNow + ".jpg"
    print(ms,mode5)
    camera.image_effect = mode5
    camera.sharpness = 0
    camera.capture(name)
    #6
    name = addressImage + "/" + mode6 + "/" + user + mode6 + DataTimeNow + ".jpg"
    print(ms,mode6)
    camera.image_effect = mode6
    camera.sharpness = 0
    camera.capture(name)
    #7
    name = addressImage + "/" + mode7 + "/" + user + mode7 + DataTimeNow + ".jpg"
    print(ms,mode7)
    camera.image_effect = mode7
    camera.sharpness = 0
    camera.capture(name)
    #8
    name = addressImage + "/" + mode8 + "/" + user + mode8 + DataTimeNow + ".jpg"
    print(ms,mode8)
    camera.image_effect = mode8
    camera.sharpness = 100
    camera.capture(name)
    #9
    name = addressImage + "/" + mode9 + "/" + user + mode9 + DataTimeNow + ".jpg"
    print(ms,mode9)
    camera.image_effect = mode9
    camera.sharpness = 0
    camera.capture(name)
    #10
    name = addressImage + "/" + mode10 + "/" + user + mode10 + DataTimeNow + ".jpg"
    print(ms,mode10)
    camera.image_effect = mode10
    camera.sharpness = 0
    camera.capture(name)
    #11
    name = addressImage + "/" + mode11 + "/" + user + mode11 + DataTimeNow + ".jpg"
    print(ms,mode11)
    camera.image_effect = mode11
    camera.sharpness = 0
    camera.capture(name)
    #12
    name = addressImage + "/" + mode12 + "/" + user + mode12 + DataTimeNow + ".jpg"
    print(ms,mode12)
    camera.image_effect = mode12
    camera.sharpness = 0
    camera.capture(name)
    #13
    name = addressImage + "/" + mode13 + "/" + user + mode13 + DataTimeNow + ".jpg"
    print(ms,mode13)
    camera.image_effect = mode13
    camera.sharpness = 0
    camera.capture(name)
    #14
    name = addressImage + "/" + mode14 + "/" + user + mode14 + DataTimeNow + ".jpg"
    print(ms,mode14)
    camera.image_effect = mode14
    camera.sharpness = 0
    camera.capture(name)
    #15
    name = addressImage + "/" + mode15 + "/" + user + mode15 + DataTimeNow + ".jpg"
    print(ms,mode15)
    camera.image_effect = mode15
    camera.sharpness = 100
    camera.capture(name)
    #16
    name = addressImage + "/" + mode16 + "/" + user + mode16 + DataTimeNow + ".jpg"
    print(ms,mode16)
    camera.image_effect = mode16
    camera.sharpness = 100
    camera.capture(name)
    #17
    name = addressImage + "/" + mode17 + "/" + user + mode17 + DataTimeNow + ".jpg"
    print(ms,mode17)
    camera.image_effect = mode17
    camera.sharpness = 0
    camera.capture(name)
    #18
    name = addressImage + "/" + mode18 + "/" + user + mode18 + DataTimeNow + ".jpg"
    print(ms,mode18)
    camera.image_effect = mode18
    camera.sharpness = 0
    camera.capture(name)
    #19-1
    name = addressImage + "/" + mode19 + "/" + user + mode19 + "_0" + DataTimeNow + ".jpg"
    print(ms,mode19,"_0")
    camera.image_effect = mode19
    camera.sharpness = 0
    camera.capture(name)
    #19-2
    name = addressImage + "/" + mode19 + "/" + user + mode19 + "_100" + DataTimeNow + ".jpg"
    print(ms,mode19,"_100")
    camera.image_effect = mode19
    camera.sharpness = 100
    camera.capture(name)
    #20
    name = addressImage + "/" + mode20 + "/" + user + mode20 + DataTimeNow + ".jpg"
    print(ms,mode20)
    camera.image_effect = mode20
    camera.sharpness = 0
    camera.capture(name)
    #21
    name = addressImage + "/" + mode21 + "/" + user + mode21 + DataTimeNow + ".jpg"
    print(ms,mode21)
    camera.image_effect = mode21
    camera.sharpness = 0
    camera.capture(name)
    
    camera.close()
    print("success")
#********************
#      main
#********************
if __name__ == "__main__" :
    # capture Loop
    capture_()