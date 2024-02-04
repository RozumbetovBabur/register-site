from django.shortcuts import render
from .models import Student
from django.shortcuts import redirect
# Create your views here.


def index_page(request):
    if request.POST:
        model = Student()
        model.name = request.POST['name']
        model.email = request.POST['email']
        model.phone_number = request.POST['phone_number']
        model.password = request.POST['password']
        model.course_type = request.POST['course_type']
        model.save()
        print(request.POST.get('course_type',None))
    return render(request,"register.html")


def get_user_name(request):
    querset = Student.objects.all()
    return render(request,"get_user.html",{"student":querset})

def delete_user(request,user_id):
    student = Student.objects.get(id=user_id)
    student.delete()
    return redirect('get_user.html')