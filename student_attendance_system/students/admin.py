from django.contrib import admin
from .models import Student, Course, Subject,Schedule, YearLevel, Attendance, Teacher

class DisplayStudent(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "birthday", "gender", "address", "contactnumber", "course_FK")

class DisplayCourse(admin.ModelAdmin):
    list_display = ("course", "description")

class DisplaySubject(admin.ModelAdmin):
    list_display = ("name", "description", "section")

class DisplaySchedule(admin.ModelAdmin):
    list_display = ("timestart", "timeend", "days", "subject_FK", "teacher_FK")

class DisplayAttendance(admin.ModelAdmin):
    list_display = ("status", "date", "time", "student_FK", "schedule_FK")

class DisplayTeacher(admin.ModelAdmin):
    list_display = ("firstname", "lastname")

admin.site.register(Student, DisplayStudent)
admin.site.register(Course, DisplayCourse)
admin.site.register(Subject, DisplaySubject)
admin.site.register(Schedule, DisplaySchedule)
admin.site.register(YearLevel)
admin.site.register(Attendance, DisplayAttendance)
admin.site.register(Teacher, DisplayTeacher)