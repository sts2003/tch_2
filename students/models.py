from django.db import models


class StudentModel(models.Model):
    stu_name = models.CharField(max_length=10)
    grade = models.IntegerField()
    school = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "학생 관리"

    def __str__(self):
        return self.stu_name
