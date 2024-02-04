from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=60)  # Elektron pochta uchun, unik bo'lishi kerak
    phone_number = models.IntegerField()  # Telefon raqami matn bo'lishi kerak
    password = models.CharField(max_length=10)  # Maxsus parol uchun, uzunlikni o'zgartiring
    course_type = models.CharField(max_length=50)

    def __str__(self):
        return self.name


