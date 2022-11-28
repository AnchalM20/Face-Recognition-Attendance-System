from imutils.video import VideoStream
import imutils
import time
import cv2
import os

	
def function(name):
	detector = cv2.CascadeClassifier('E://anchal/FinalYearProject/FaceAttendance/Attendance/face_recognition/haarcascade_frontalface_default.xml')
	print("[INFO] starting video stream...")
	vs = VideoStream(src=0).start()
	time.sleep(2.0)
	total = 0
	path = 'E://anchal/FinalYearProject/FaceAttendance/Attendance/face_recognition/dataset'
	new_folder = name
	create_folder = os.path.join(path, new_folder)
	os.mkdir(create_folder)

	while True:
		frame = vs.read()
		orig = frame.copy()
		frame = imutils.resize(frame, width=400)
		rects = detector.detectMultiScale(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), 
											scaleFactor=1.1,minNeighbors=5, minSize=(30, 30))
		for (x, y, w, h) in rects:
			cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
			
		cv2.imshow("Frame", frame)
		key = cv2.waitKey(1) & 0xFF
		new_path="E://anchal/FinalYearProject/FaceAttendance/Attendance/face_recognition/dataset"+"/"+ new_folder
		if key == ord("k"):
			p = os.path.sep.join([new_path, "{}.png".format(str(total).zfill(5))])
			cv2.imwrite(p, orig)
			total += 1		
		elif key == ord("q"):
			break

	cv2.destroyAllWindows()
	vs.stop()