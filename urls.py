from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name='Home'),
    path('Login',views.Userlogin,name='Userlogin'),
    path('Admin/Home',views.Admin_home,name='Admin_home'),
    path('Teacher/Register',views.Admin_Teacher_Register,name='Admin_Teacher_Register'),
    path('Teacher/View',views.Admin_ViewTeacher,name='Admin_ViewTeacher'),
    path('TeacherDelete/<int:id>',views.Admin_DeleteTeacher,name='Admin_DeleteTeacher'),
    path('TeacherEdit/<int:id>',views.Admin_EditTeacher,name='Admin_EditTeacher'),
    path('Teacher/Home',views.Teacher_home,name='Teacher_home'),
    path('TeacherViewTeacher',views.Teacher_ViewTeacher,name='Teacher_ViewTeacher'),
    path('TeacherEditTeacher/<int:id>',views.Teacher_EditTeacher,name='Teacher_EditTeacher'),
    path('Student/Register',views.StudentRequest,name='StudentRequest'),
    path('Student_accept_reject',views.Student_Accept_Reject,name='Student_Accept_Reject'),
    path('Student_accept/<int:id>',views.Admin_AcceptRequest,name='Admin_AcceptRequest'),
    path('Student_reject/<int:id>',views.Admin_RejectRequest,name='Admin_RejectRequest'),
    path('Student/Home',views.Student_home,name='Student_home'),
    path('AdminViewStudent',views.Admin_ViewStudent,name='Admin_ViewStudent'),
    path('StudentViewStudent',views.Student_ViewStudent,name='Student_ViewStudent'),
    path('StudentEditStudent/<int:id>',views.StudentEditStudent,name='StudentEditStudent'),
    path('StudentViewTeacher',views.StudentViewTeacher,name='StudentViewTeacher'),
    path('TeacherViewStudent',views.Teacher_ViewStudent,name='Teacher_ViewStudent'),
    path('Logouts',views.logouts,name='logouts'),
    path('Student/Home',views.Student_home,name='Student_home'),
    path('Admin/StudentDelete/<int:id>',views.Admin_StudentDelete,name='Admin_StudentDelete'),
    path('Admin/StudentEdit/<int:id>',views.Admin_StudentEdit,name='Admin_StudentEdit'),
]