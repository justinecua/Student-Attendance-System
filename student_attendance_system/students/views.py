from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Student, Subject, Schedule, Course, Attendance, YearLevel, Teacher
from django.contrib import messages
from django.shortcuts import render

#-------------------------Students------------------------
def students(request):
    student_with_yearlevel = Student.objects.prefetch_related('yearlevel_FK').all()
    count_student = Student.objects.count()
    context ={
        'students_list': student_with_yearlevel,
        'count_student': count_student
    }
    return render(request, 'students.html', context)

def edit(request, id):
    students = Student.objects.get(id=id)
    template = loader.get_template('student_editInfo.html')
    context = {
        'students_list': students,
    }
    return HttpResponse(template.render(context, request))

def delete(request, id):
  students = Student.objects.get(id=id)
  students.delete()
  messages.success(request, 'Deleted successfully!')
  return HttpResponseRedirect(reverse('students'))

def updateStudent(request, id):
    name2 = request.POST['name']
    course2 = request.POST['course']
    age2 = request.POST['age']
    address2 = request.POST['address']
    status2 = request.POST['status']
    
    students = Student.objects.get(id=id)
    students.name = name2
    students.course = course2
    students.age = age2
    students.address = address2
    students.status = status2
    students.save()
    messages.success(request, 'Updated successfully!')
    return HttpResponseRedirect(reverse('students'))

def addStudent(request):
  courses = Course.objects.all()
  yearlevel = YearLevel.objects.all().values()

  context = {
    'select_yearlevel': yearlevel,
    'courses_list': courses
  }
  return render(request, 'add-students.html', context)

def SaveStudent(request):
  firstname = request.POST['firstname']
  lastname = request.POST['lastname']
  birthday = request.POST['birthday']
  gender = request.POST['gender']
  address = request.POST['address']
  contactnumber = request.POST['contactnumber']
  course_id = request.POST['course_id']
  yearLevel_id = request.POST['yearlevel_id']
  
  if not all([firstname, lastname, birthday, gender, address, contactnumber, course_id, yearLevel_id]):
    messages.error(request, 'Please fill in all fields')
    return HttpResponseRedirect(reverse('Students'))
  
  course = Course.objects.get(pk=course_id)
  yearLevel = YearLevel.objects.get(pk=yearLevel_id)

  students = Student.objects.create(
      firstname=firstname,
      lastname=lastname,
      birthday=birthday,
      gender=gender,
      address=address,
      contactnumber=contactnumber,
      course_FK=course,
  )

  students.yearlevel_FK.add(yearLevel)

  messages.success(request, 'Added successfully!')
  return HttpResponseRedirect(reverse('Students'))

#-------------------------Subjects------------------------
def Subjects(request):
    subjects = Subject.objects.all()
    count_subjects = Subject.objects.count()
    template = loader.get_template('subjects.html')
    context ={
        'subject_list': subjects,
        'count_subjects': count_subjects
    }
    return HttpResponse(template.render(context, request))

def AddSubject(request):
  template = loader.get_template('add-subjects.html')
  return HttpResponse(template.render({}, request))

def SaveAddedSubject(request):
  name = request.POST['name']
  description = request.POST['description']
  section = request.POST['section']
  
  if not all([name, description, section]):
    messages.error(request, 'Please fill in all fields')
    return HttpResponseRedirect(reverse('Subjects'))
  
  students = Subject(name=name, description=description, section=section)
  students.save()
  messages.success(request, 'Added successfully!')
  return HttpResponseRedirect(reverse('Subject'))

#-------------------------Home------------------------
def Home(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render({}, request))

#-------------------------Attendance------------------------
def AttendancePage(request):
    attendance_count = Attendance.objects.count()
    attendance_with_student = Attendance.objects.select_related(
      'schedule_FK__subject_FK', 
      'student_FK__course_FK',
    ).all()
    template = loader.get_template('Attendance.html')
    context = {
        'attendance_with_student': attendance_with_student,
        'attendance_count': attendance_count
    }
    return HttpResponse(template.render(context, request))

def addAttendance(request):
  students = Student.objects.all().values()
  subjects_with_schedule = Schedule.objects.select_related('subject_FK').all()
  template = loader.get_template('add-attendance.html')

  context = {
      'select_students': students,
      'select_subjects': subjects_with_schedule
  }
  
  return HttpResponse(template.render(context, request))

def SaveAttendance(request):
  student_name = request.POST.get('student_name')
  subject = request.POST.get('subject')
  date = request.POST.get('date')
  time = request.POST.get('time')
  status = request.POST.get('status')

  if not all([student_name, subject, date, time, status]):
    messages.error(request, 'Please fill in all fields')
    return HttpResponseRedirect(reverse('Attendance'))
  
  student_id = Student.objects.get(pk=student_name)
  schedule_id = Schedule.objects.get(pk=subject)

  Attendance1 = Attendance(
      status = status,
      student_FK = student_id,
      schedule_FK = schedule_id,
      date = date,
      time = time
  )

  Attendance1.save()
  messages.success(request, 'Added successfully!')
  return HttpResponseRedirect(reverse('Attendance'))
#-------------------------Course------------------------
def CoursesPage(request):
  courses = Course.objects.all()
  count_courses = Course.objects.count()
  template = loader.get_template('Courses.html')
  context ={
      'list_courses': courses,
      'count_courses': count_courses

  }
  return HttpResponse(template.render(context, request))

def AddCourse(request):
  template = loader.get_template('add-course.html')
  return HttpResponse(template.render({}, request))

def SaveCourse(request):
  course = request.POST.get('course')
  description = request.POST.get('description')

  if not all([course, description]):
    messages.error(request, 'Please fill in all fields')
    return HttpResponseRedirect(reverse('Attendance'))
  
  course = Course(
      course = course,
      description = description,
  )

  course.save()
  messages.success(request, 'Added successfully!')
  return HttpResponseRedirect(reverse('Courses'))
#-------------------------Schedule------------------------
def SchedulePage(request):
  sched_with_subj = Schedule.objects.select_related('subject_FK').select_related('teacher_FK').all()
  count_sched = Schedule.objects.count()
  template = loader.get_template('Schedules.html')
  context ={
      'sched_with_subj': sched_with_subj,
      'count_sched': count_sched
  }
  return HttpResponse(template.render(context, request))

def AddSchedule(request):
  subjects = Subject.objects.all().values()
  teachers = Teacher.objects.all().values()
  
  context = {
    'select_subjects': subjects,
    'select_teachers': teachers
  }
  return render(request, 'add-schedule.html', context)

def SaveSchedule(request):
  timestart = request.POST['timestart']
  timeend = request.POST['timeend']
  day = request.POST['day']
  subject_id = request.POST['subject_id']
  teacher_id = request.POST['teacher_id']

  if not all([timestart, timeend, day, subject_id, teacher_id]):
    messages.error(request, 'Please fill in all fields')
    return HttpResponseRedirect(reverse('Schedule'))
  
  subjectFK = Subject.objects.get(pk=subject_id)
  teacherFK = Teacher.objects.get(pk=teacher_id)

  schedule = Schedule(
      timestart = timestart,
      timeend = timeend,
      days = day,
      subject_FK = subjectFK,
      teacher_FK = teacherFK
  )

  schedule.save()
  messages.success(request, 'Added successfully!')
  return HttpResponseRedirect(reverse('Schedule'))

#-------------------------Teacher------------------------
def TeacherPage(request):
  teachers = Teacher.objects.all().values()
  count_teachers = Teacher.objects.count()
  template = loader.get_template('Teachers.html')

  context = {
    'teacher_list': teachers,
    'count_teachers': count_teachers
  }

  return HttpResponse(template.render(context, request))

def AddTeacher(request):
  template = loader.get_template('add-teachers.html')
  return HttpResponse(template.render({}, request))

def SaveTeacher(request):
  firstname = request.POST['firstname']
  lastname = request.POST['lastname']
 
  if not all([firstname, lastname]):
    messages.error(request, 'Please fill in all fields')
    return HttpResponseRedirect(reverse('Schedule'))
  
  teacher = Teacher(
      firstname = firstname,
      lastname = lastname,
  )

  teacher.save()
  messages.success(request, 'Added successfully!')
  return HttpResponseRedirect(reverse('Teachers'))
#-------------------------Year Level------------------------
def YearLevelPage(request):
  yearlevel_count = YearLevel.objects.count()
  yearLevel = YearLevel.objects.all().values()
  template = loader.get_template('YearLevel.html')

  context = {
    'yearlevel_list': yearLevel,
    'yearlevel_count': yearlevel_count
  }

  return HttpResponse(template.render(context, request))

def AddYearLevel(request):
  template = loader.get_template('add-yearlevel.html')
  return HttpResponse(template.render({}, request))

def SaveYearLevel(request):
  yearlevel = request.POST['yearlevel']

  if not all([yearlevel]):
    messages.error(request, 'Please fill in all fields')
    return HttpResponseRedirect(reverse('Schedule'))
  
  yearLevel = YearLevel(
      yearlevel = yearlevel,
  )

  yearLevel.save()
  messages.success(request, 'Added successfully!')
  return HttpResponseRedirect(reverse('YearLevel'))