from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Course, Attendance

def attendance_list(request):
    attendance_records = Attendance.objects.all()
    return render(request, 'attedance/attendance_list.html', {'attendance_records': attendance_records})

def attendance_mark(request):
    students = Student.objects.all()
    courses = Course.objects.all()
    if request.method == 'POST':
        student_id = request.POST['student']
        course_id = request.POST['course']
        date = request.POST['date']
        status = request.POST['status']
        Attendance.objects.create(student_id=student_id, course_id=course_id, date=date, status=status)
        return redirect('attendance_list')
    return render(request, 'attedance/attendance_form.html', {'students': students, 'courses': courses})


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'attedance/course_list.html', {'courses': courses})

def course_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        Course.objects.create(name=name, description=description, start_date=start_date, end_date=end_date)
        return redirect('course_list')
    return render(request, 'attedance/course_form.html')

def course_edit(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.name = request.POST['name']
        course.description = request.POST['description']
        course.start_date = request.POST['start_date']
        course.end_date = request.POST['end_date']
        course.save()
        return redirect('course_list')
    return render(request, 'attedance/course_form.html', {'course': course})

def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    course.delete()
    return redirect('course_list')

# Create your views here.
def student_list(request):
    students = Student.objects.all()
    return render(request, 'attedance/student_list.html',{'students':students})

def student_create(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        Student.objects.create(first_name=first_name, last_name=last_name, email=email)
        return redirect('student_list')
    return render(request, 'attedance/student_form.html')

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('student_list')