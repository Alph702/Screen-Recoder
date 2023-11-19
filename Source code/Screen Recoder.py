import cv2
import numpy as np
from PIL import ImageGrab
from win32api import GetSystemMetrics
import datetime

time = datetime.datetime.now().strftime('%d-%m-%Y %I-%M-%S')
file_name = f'E:\\Screen Recoder\\video\\{time}.mp4'
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
cap_video = cv2.VideoWriter(file_name,fourcc,10,(width,height))

while True:

	Screen_img = ImageGrab.grab(bbox=(0,0,width,height))
	array_img = np.array(Screen_img)
	color_img = cv2.cvtColor(array_img,cv2.COLOR_BGR2RGB)
	cap_video.write(color_img)
	cv2.imshow('Screen Recorder by Amanat',color_img)
	if cv2.waitKey(1)==ord('q'):
		break
