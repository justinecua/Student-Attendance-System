
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('edit/updateStudent/<int:id>', views.updateStudent, name='updateStudent'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('addStudent', views.addStudent, name='addStudent'),
    path('addStudent/SaveStudent/', views.SaveStudent, name='SaveStudent'),
    path('addSubject/', views.AddSubject, name='add-subject'),
    path('addSubject/SaveAddedSubject/', views.SaveAddedSubject, name='SaveAddedSubject'),
    path('Attendance/', views.AttendancePage, name='Attendance'),
    path('addAttendance/SaveAttendance', views.SaveAttendance, name='SaveAttendance'),
    path('addAttendance', views.addAttendance, name='addAttendance'),
    path('Courses/', views.CoursesPage, name='Courses'),
    path('addCourse', views.AddCourse, name='AddCourse'),
    path('addCourse/SaveCourse', views.SaveCourse, name='SaveCourse'),
    path('Schedule/', views.SchedulePage, name='Schedule'),
    path('addSchedule', views.AddSchedule, name='AddSchedule'),
    path('addSchedule/SaveSchedule', views.SaveSchedule, name='SaveSchedule'),
    path('Students/', views.students, name='Students'),
    path('Subject/', views.Subjects, name='Subject'),
    path('Teachers/', views.TeacherPage, name='Teachers'),
    path('addTeachers', views.AddTeacher, name='AddTeacher'),
    path('addTeachers/SaveTeachers', views.SaveTeacher, name='SaveTeachers'),
    path('YearLevel/', views.YearLevelPage, name='YearLevel'),
    path('addYearLevel/', views.AddYearLevel, name='AddYearlevel'),
    path('addYearLevel/SaveYearLevel', views.SaveYearLevel, name='SaveYearLevel'),
]
