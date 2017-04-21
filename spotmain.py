# spotmain.py

import globalspot
import colorpick 
import os

globalspot.init()
index = 0
print("setting up..")
for f in os.listdir(os.getcwd()):
    index += 1
    print(str(index) + " // " + f)
    colorpick.computeContours(f)
    print("DONE\n\n")


# colorpick.computeContours("/home/wangbri/Desktop/spotfolder/labspots2.png")
# colorpick.computeContours("/home/wangbri/Desktop/spotfolder/labspots.png")

print
print("Total spots: " + str(globalspot.spotcount))
