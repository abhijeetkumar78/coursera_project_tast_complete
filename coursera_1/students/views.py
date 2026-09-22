from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Student
from .forms import StudentForm


def student_list(request):
    """List all students - READ (list)"""
    students = Student.objects.all()
    context = {
        'students': students,
        'title': 'All Students',
        'total_count': students.count(),
    }
    return render(request, 'students/student_list.html', context)


def student_detail(request, pk):
    """View a single student - READ (detail)"""
    student = get_object_or_404(Student, pk=pk)
    context = {
        'student': student,
        'title': f'Student: {student.get_full_name()}',
    }
    return render(request, 'students/student_detail.html', context)


def student_create(request):
    """Create a new student - CREATE"""
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            messages.success(request, f'Student "{student.get_full_name()}" was added successfully!')
            return redirect('students:student_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = StudentForm()

    context = {
        'form': form,
        'title': 'Add New Student',
        'action': 'Create',
    }
    return render(request, 'students/student_form.html', context)


def student_update(request, pk):
    """Update an existing student - UPDATE"""
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, f'Student "{student.get_full_name()}" was updated successfully!')
            return redirect('students:student_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = StudentForm(instance=student)

    context = {
        'form': form,
        'student': student,
        'title': f'Edit Student: {student.get_full_name()}',
        'action': 'Update',
    }
    return render(request, 'students/student_form.html', context)


def student_delete(request, pk):
    """Delete a student with confirmation - DELETE"""
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        name = student.get_full_name()
        student.delete()
        messages.success(request, f'Student "{name}" was deleted successfully!')
        return redirect('students:student_list')

    context = {
        'student': student,
        'title': f'Delete Student: {student.get_full_name()}',
    }
    return render(request, 'students/student_confirm_delete.html', context)
