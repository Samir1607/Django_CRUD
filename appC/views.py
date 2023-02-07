from django.shortcuts import render, redirect
from django.views import View
from .models import Student
from .form import AddStudentForm


class Home(View):
    def get(self, request):
        stu_data = Student.objects.all()
        return render(request, 'appC/home.html', {'studata': stu_data})


class Add_Student(View):
    def get(self, request):
        fm = AddStudentForm()
        return render(request, 'appC/add-student.html', {'form': fm})

    def post(self, request):
        fm = AddStudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        else:
            return render(request, 'appC/add-student.html', {'form': fm})


class Delete_Student(View):
    def post(self, request):
        data = request.POST
        id = data.get('id')
        studata = Student.objects.get(id=id)
        studata.delete()
        return redirect('/')


class EditStudent(View):
    def get(self, request, id):
        stu = Student.objects.get(id=id)
        fm = AddStudentForm(instance=stu)
        return render(request, 'appC/edit-student.html', {'form': fm})

    def post(self, request, id):
        stu = Student.objects.get(id=id)
        fm = AddStudentForm(request.POST, instance=stu)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        else:
            return redirect('/')     # else statement is reductable if you don't want this is just for completing code


