from cv2 import imread
from pyscreenshot import grab
from time import sleep
from os import environ
from keyboard import read_key
from sys import exit
import pyautogui
import pytesseract
import random
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
environ['OMP_THREAD_LIMIT'] = '1'

#press enter to start
if read_key() == "enter":

	while True:

		#variables
		h = random.uniform(.2, .25)
		v = random.randint(1, 6)
		z = 0

		#get screenshot
		img = grab(bbox=(550, 723, 1350, 910))
		img.save("box.png")
		img = imread("box.png")

		#convert image to text
		text = pytesseract.image_to_string(img)
		newtext = text.replace("\n", " ")

		#random mistakes
		for z in range (v):
			z += 1
			x = random.randint(1, 75)
			y = chr(random.randint(ord('a'), ord('z')))
			newtext = newtext[:x] + y + newtext[x:] 
		print(newtext)

		#type the text
		sleep(.5)
		pyautogui.press('enter')
		sleep(.1)
		pyautogui.typewrite(newtext, interval=h)

		#clicks
		pyautogui.click(x=86, y=45)
		sleep(2.5)
		pyautogui.click(x=1243, y=861)
		sleep(2)
		pyautogui.click(x=805, y=615)
		sleep(11)
		pyautogui.click(x = 992, y = 757)
