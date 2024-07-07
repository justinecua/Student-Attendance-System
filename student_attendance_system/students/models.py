from django.db import models

class Course(models.Model):
    course = models.CharField(max_length=255)
    description = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.course}"

class Subject(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    section = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"
    
class YearLevel(models.Model):
    yearlevel = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.yearlevel}"

class Student(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    birthday = models.DateField(max_length=255)
    gender = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contactnumber = models.CharField(max_length=255, null=True)
    course_FK = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)
    yearlevel_FK = models.ManyToManyField(YearLevel)
    
    def __str__(self):  
        return f"{self.firstname} {self.lastname}"

class Teacher(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class Schedule(models.Model):
    timestart = models.TimeField(max_length=255)
    timeend = models.TimeField(max_length=255)
    days = models.CharField(max_length=255)
    subject_FK = models.ForeignKey(Subject, null=True, on_delete=models.CASCADE)
    teacher_FK = models.ForeignKey(Teacher, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.timestart} {self.timeend}"
    
class Attendance(models.Model):
    status = models.CharField(max_length=255)
    student_FK = models.ForeignKey(Student, null=True, on_delete=models.CASCADE)
    schedule_FK = models.ForeignKey(Schedule, null=True, on_delete=models.CASCADE)
    date = models.DateField(null=True)
    time = models.TimeField()

    def __str__(self):
        return f"{self.student_FK}"