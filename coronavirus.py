import  pyautogui, time
x = 0
while True:
	x += 1
	click = x % 20 
	pyautogui.press('enter') 
	pyautogui.write("""qQwWeErRtTyYuUiIoOpPaAsSdDfFgGhHjJkKlL;:'"zZxXcCvVbBnNmM,.? !1234567890-""") #types the text
	time.sleep(2)
	if click == 0: 
		pyautogui.click(x = 987, y = 955)	
	if click != 0: 
		{
		}
else:
	print('why did u break the bot')
