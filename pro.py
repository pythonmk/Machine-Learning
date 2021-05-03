import cv2

#ourimage
img_file = "car2.jgp"
video = cv2.VideoCapture('Road.mp4')

#create opencv image
img= cv2.imread(r'car2.jpg')

#our pre-trained car classifier
car_tracker_file = 'car_detector.xml'

#create a car classifier
car_tracker = cv2.CascadeClassifier(car_tracker_file)

# run forever until video ends
while True:
	#Read the current frame
	(read_successful, frame) = video.read() 

	#Safe coding
	if read_successful:
		grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	else:
		break

	#detect car and pedestrian from video
	cars = car_tracker.detectMultiScale(grayscaled_frame)
	

	#Draw a rectangle around cars
	for(x, y, w, h) in cars:
		#xcv2.rectangle(frame, (x+1, y+2), (x+w, y+h), (225, 0, 0), 2)
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 225, 225), 2)	
		print(frame)

	#Draw a rectangle around pedestrians
	#for(x, y, w, h) in pedestrians:
		#cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 225, 225), 2)


	#display image with face spotted
	cv2.imshow('VEHICLE DETECTION', frame )

	#Dont auto close wait here for key
	key=cv2.waitKey(2)

	if key==81 or key==113:
		break

video.release()

