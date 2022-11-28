from django.test import SimpleTestCase,TestCase,Client, RequestFactory
from django.urls import reverse, resolve
from Attendance.views import add_schedule,create_dataset,train_model,select_sub
from Attendance.models import TimeTable, Student_attendance
from account.models import User,Teacher, Department, Subject

class TestUrls(SimpleTestCase):
    
    def test_add_schedule_url(self):
        url = reverse("Attendance:add_schedule")
        self.assertEqual(resolve(url).func,add_schedule)

    def test_create_dataset_url(self):
        url = reverse("Attendance:create_dataset")
        self.assertEqual(resolve(url).func,create_dataset)

    def test_train_model_url(self):
        url = reverse("Attendance:train_model")
        self.assertEqual(resolve(url).func,train_model)

    def test_select_sub_url(self):
        url = reverse("Attendance:select_sub")
        self.assertEqual(resolve(url).func,select_sub)

       
class TestModels(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(
            username = "Priya11",
            password = "Singh123",
            email = "priyasingh@gmail.com"
        )
        
    def test_TimeTable(self):

        dept = Department.objects.create(
            department_id = 1,
            department_name = "CS" 
        )
        
        sub = Subject.objects.create(
            subject_id = "IT1SEm6",
            subject_name = "Linux",
            department_id  = dept,
            semester = 6
        )
        
        teach = Teacher.objects.create(
            user = self.user1,
            first_name = "Priya",
            last_name = "Singh"
        )
        
        tt = TimeTable.objects.create(
            time_id = 1,
            day = "Monday",
            start_time = "11:00",
            end_time = "11:50",
            sem = "6",
            department_id = dept,
            subject_id = sub,
            teacher = teach
            )

        self.assertEqual(tt.day,"Monday")

