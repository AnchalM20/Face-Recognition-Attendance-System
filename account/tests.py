from django.test import SimpleTestCase,TestCase,Client, RequestFactory
from django.urls import reverse, resolve
from account.views import student_login,admin_login,student_register,teacher_login,teacher_register,change_password
from account.models import User,Teacher,Student,Department,Subject


class TestUrls(SimpleTestCase):

    def test_student_login_url(self):
        url = reverse("account:student_login")
        self.assertEqual(resolve(url).func,student_login)

    def test_admin_login_url(self):
        url = reverse("account:admin_login")
        self.assertEqual(resolve(url).func,admin_login)

    def test_student_register_url(self):
        url = reverse("account:student_register")
        self.assertEqual(resolve(url).func.view_class,student_register)

    def test_teacher_login_url(self):
        url = reverse("account:teacher_login")
        self.assertEqual(resolve(url).func,teacher_login)

    def test_teacher_register_url(self):
        url = reverse("account:teacher_register")
        self.assertEqual(resolve(url).func.view_class,teacher_register)
    
    def test_change_password_url(self):
        url = reverse("account:change_password")
        self.assertEqual(resolve(url).func,change_password)



class TestViews(SimpleTestCase):

    def setup(self):
        self.client = Client()
        self.user1 = User.objects.create(
            username = "madhu1",
            password = "maurya11"
        )

    def test_student_login_GET(self):
        response = self.client.get(reverse('account:student_login'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'account/student_login.html')

    def test_teacher_login_GET(self):
        response = self.client.get(reverse('account:teacher_login'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'account/teacher_login.html')
   
    def test_admin_login_GET(self):
        response = self.client.get(reverse('account:admin_login'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'account/admin_login.html')
    
    # def test_student_login_POST(self):        
    #     response = self.client.post(reverse('account:student_login'),{'user':user1})
    #     self.assertEquals(response.status_code,302)
        
    

class TestModels(TestCase):
    
    def setUp(self):
        self.user1 = User.objects.create(
            username = "madhu11",
            password = "singh1111",
            email = "madhu@gmail.com"
        )
    
    def test_Student(self):
        dept = Department.objects.create(
            department_id = 1,
            department_name = "CS" 
        )
        Student.objects.create(
            user = self.user1,
            first_name = "Madhu",
            last_name = "Maurya",
            department = dept,
            contact_no = 9090909090,
            roll_no = 457,
            semester = 7
        )
        self.assertEqual(self.user1.is_teacher,0)


    def test_Teacher(self):

        self.dept = Department.objects.create(
            department_id = 1,
            department_name = "CS" 
        )

        self.sub = Subject.objects.create(
            subject_id = "IT1SEm6",
            subject_name = "Linux",
            department_id  = self.dept,
            semester = 6
        )
       
        self.teach = Teacher.objects.create(
            user = self.user1,
            first_name = "Madhu",
            last_name = "Maurya",
            department = self.dept,
        )

        self.teach.subject.add(self.sub)
        self.assertEqual(self.user1.is_student,0)


