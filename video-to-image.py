
# Video to Images
from __future__ import division
import os
import cv2
import numpy as np

import re



try:

    # creating a folder named data
    if not os.path.exists('dataimg'):
        os.makedirs('dataimg')

    # if not created then raise error
except OSError:
    print('Error: Creating directory of data')


label = []
d = os.listdir('datavideo')
f = []
data = []
len_f = []
for file in d:
 #   frames = []
    path = 'datavideo' + file
    paths=file
    cam = cv2.VideoCapture(path)

    # frame
    currentframe = 0

    while (True):

    # reading from frame
      ret, frame = cam.read()

      if ret:
        # if video is still left continue creating images
        name = './dataimg/' + paths[0:11] + '_' + str(currentframe) + '.jpg'
       # print('Creating...' + name)
        if (currentframe % 2) == 0:

        # writing the extracted images
           cv2.imwrite(name, frame)
        else:
            print("*")

        # increasing counter so that it will
        # show how many frames are created
        currentframe += 1
      else:
        break

# Release all space and windows once done
    cam.release()
    cv2.destroyAllWindows()


i=0
j=0
image_new=[]
for i in data:
  n=len(i)
# for j in i:
#   print(leni)
  s=sum(i)
  image_n=s/n
  # image_n=[sum(e) / len(e) for e in zip(*i)]
  image_new.append(image_n)
  name = './dataimg2/' + str(j)  + '.jpg'
  cv2.imwrite(name,image_new)
  j+=1
