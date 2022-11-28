from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from Attendance.face_recognition import custom_dataset as cd
from Attendance.face_recognition import encode_faces as ef
from student.views import student_dashboard
from Attendance.face_recognition import face_identify as fi
from student.forms import SelectSubForm
from Attendance.models import Student_attendance, TimeTable
from django.contrib import messages
from datetime import datetime

@login_required
def add_schedule(request):
    return render(request,"Attendance/add_schedule.html")

@login_required
def create_dataset(request):
    if request.user.is_authenticated and request.user.is_superuser == 1:
        name = request.user.student.first_name
        cd.function(name)
    else:
        return HttpResponse("<h1>You are not allowed!!!</h1>")
    return redirect('Attendance:attendance')

@login_required
def train_model(request):
    if request.user.is_authenticated:
        path = 'E://anchal/FinalYearProject/FaceAttendance/Attendance/face_recognition/dataset'
        ef.train_models(path)
    return redirect('Attendance:attendance') 


@login_required
def test_model(request):
    if request.user.is_authenticated:
        fi.test_models()
    return redirect('Attendance:attendance') 

@login_required
def attendance(request):
    return render(request,'Attendance/attendance.html')

@login_required
def select_sub(request):
    if request.method == "POST":
        form = SelectSubForm(request.user,request.POST)
        if form.is_valid():
            sub = form.cleaned_data.get('subject')
            print("OPENING CAMERA.......\n\n\n")
            if request.user.is_authenticated:
                today = datetime.now()
                day = today.strftime("%A")
                if((day == 'Saturday') or (day == 'Sunday')):
                    messages.success(request, 'Today is holiday..!!')                    
                    return redirect('student:student_dashboard')
                try:
                    m1 = TimeTable.objects.get(day = day, subject_id = sub)
                except:
                    messages.success(request, f"There is no lecture of {sub}..!!")                    
                    return redirect('student:student_dashboard')

                now = datetime.now() 
                curr = now.strftime("%H:%M")
                s = datetime.strptime(str(curr), "%H:%M")#12 formate
                current_time = str(s.strftime("%I:%M"))#final
                ct = str(current_time).split(":")
                tt = '01:50'.split(":")#09:50
                print(current_time,"\n\nhhhhhh")

                if(ct[0] == tt[0] and int(ct[1]) <= int(int(tt[1])+5)):
                    matched_name = fi.test_models()                           
                    if(matched_name == request.user.username):        
                        attend = Student_attendance(subject = sub,status = True,student = request.user.student)
                        attend.save() 
                        messages.success(request, 'Your attendance has been marked..!!')
                    else:
                        messages.success(request, 'You are not authenticated for attendance..!!')
                    return redirect('student:student_dashboard') 
                
                else:
                    messages.success(request, 'This time you are not allowed to give attendance..!!')
                    return redirect('student:student_dashboard') 

        else:
            form = SelectSubForm(request.user)
            messages.success(request,f"Please select subject!!")
            return render(request,'student/select_sub.html',{'fm':form})
    else:
        form = SelectSubForm(request.user)
        return render(request,'student/select_sub.html',{'fm':form})












































































































    # face_recognizer=cv2.face.LBPHFaceRecognizer_create()
    # face_recognizer.read('Attendance/trainingData.yml')

    # name={2:"Ujala",1:"Anchal"}

    # cap = cv2.VideoCapture(0)

    # while True:
        
    #     ret,test_img=cap.read()# captures frame and returns boolean value and captured image
    #     faces_detected,gray_img=fr.faceDetection(test_img)

    #     for face in faces_detected:
    #         (x,y,w,h)=face
    #         roi_gray=gray_img[y:y+w, x:x+h]
    #         label,confidence=face_recognizer.predict(roi_gray)#predicting the label of given image
    #         print("confidence:",confidence)
    #         print("label:",label)
    #         fr.draw_rect(test_img,face)
    #         predicted_name=name[label]
    #         if confidence <= 50:#If confidence less than 37 then don't print predicted face text on screen
    #             fr.put_text(test_img,predicted_name,x,y)
    #         else:
    #             if confidence > 50:#If confidence less than 37 then don't print predicted face text on screen
    #                 fr.put_text(test_img,"Unknown",x,y)

    #         attendstudent = predicted_name

    #     resized_img = cv2.resize(test_img, (1000, 700))
    #     cv2.imshow('face recognition tutorial ',resized_img)
    #     if cv2.waitKey(10) == ord('q'):#wait until 'q' key is pressed
    #         break

    # cap.release()
    # cv2.destroyAllWindows
    # return redirect('student:student_dashboard')