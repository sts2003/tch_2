from django.shortcuts import render
from students import models as student_models


def homeRender(request):

    stu_list = student_models.StudentModel.objects.all()

    return render(request, "screens/home.html", context={"stu_list": stu_list})
