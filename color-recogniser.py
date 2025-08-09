import cv2
from PIL import Image
from Utils import get_limits

color = [0, 255, 255] # BGR Color Space <----- Enter codes for desired color
cap = cv2.VideoCapture(0)

while True:
	
	ret, frame = cap.read()
	hsvimg = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	
	lowerlimit, upperlimit = get_limits(color=color)
	mask = cv2.inRange(hsvimg, lowerlimit, upperlimit )

	mask_ = Image.fromarray(mask)
	box = mask_.getbbox()

	print(box)
	if box is not None:
		x1, y1, x2, y2 = box

		frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 4)

	# To Show the mask ie. B&W differentiation of color and non color area
	cv2.imshow("Captured Frame", mask)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()