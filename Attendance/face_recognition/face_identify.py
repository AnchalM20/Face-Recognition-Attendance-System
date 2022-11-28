from imutils.video import VideoStream
import face_recognition
import imutils
import pickle
import time
import cv2
from Attendance.face_recognition import dataset
from Attendance.face_recognition import output

def test_models():
	display = 1
	# load the known faces and embeddings
	print("[INFO] loading encodings...")
	data = pickle.loads(open('E://anchal/FinalYearProject/FaceAttendance/Attendance/face_recognition/encodings.pickle', "rb").read())
	# initialize the video stream and pointer to output video file, then
	# allow the camera sensor to warm up
	print("[INFO] starting video stream...")
	vs = VideoStream(src=0).start()
	writer = None
	time.sleep(2.0)

	# loop over frames from the video file stream
	while True:
		# grab the frame from the threaded video stream
		frame = vs.read()	
		rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
		rgb = imutils.resize(frame, width=750)
		r = frame.shape[1] / float(rgb.shape[1])
		# detect the (x, y)-coordinates of the bounding boxes
		# corresponding to each face in the input frame, then compute
		# the facial embeddings for each face
		boxes = face_recognition.face_locations(rgb, model="hog")
		encodings = face_recognition.face_encodings(rgb, boxes)
		
		for encoding in encodings:
			matches = face_recognition.compare_faces(data["encodings"], encoding)
			name = "Unknown"
			if True in matches:
				matchedIdxs = [i for (i, b) in enumerate(matches) if b]
				counts = {}			

				# loop over the matched indexes and maintain a count for
				# each recognized face face
				for i in matchedIdxs:
					name = data["names"][i]
					counts[name] = counts.get(name, 0) + 1

				# determine the recognized face with the largest number
				# of votes (note: in the ev ent of an unlikely tie Python
				# will select first entry in the dictionary)
				name = max(counts, key=counts.get)
			
			# update the list of names
			names.append(name)

			# loop over the recognized faces
		for ((top, right, bottom, left), name) in zip(boxes, names):

			# rescale the face coordinates
			top = int(top * r)
			right = int(right * r)
			bottom = int(bottom * r)
			left = int(left * r)

			# draw the predicted face name on the image
			cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
			y = top - 15 if top - 15 > 15 else top + 15
			cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

		
		if display > 0:
			cv2.imshow("Frame", frame)
			key = cv2.waitKey(1) & 0xFF
			
			# if the `q` key was pressed, break from the loop
			if key == ord("q"):
				break
				
	# do a bit of cleanup
	cv2.destroyAllWindows()
	vs.stop()
	
	return name