import cv2

#ourimage
#img_file = "car.jgp"

im = cv2.imread(r'car.jpg')

#our pre-trained car classifier
#classifier_file = 'car_detector.xml'

#convert to gray scale
#black_n_white = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#create a car classifier
#car_tracker = cv2.CascadeClassifier(classifier_field)
#Display the image

cv2.imshow('CAR DETECTION',im)
cv2.waitKey() #Milliseconds