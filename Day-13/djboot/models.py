from django.db import models

# Create your models here.

class Student(models.Model):
	name = models.CharField(max_length=200)
	rollno =models.CharField(max_length=10)
	branch = models.CharField(max_length=50) 
	year = models.IntegerField(default=3)   

	#def __str__(self):
	#	return str(self.id)+'  '+self.name

class StudentInfo(models.Model):
	phno = models.CharField(max_length=10)
	emailid = models.EmailField()

	class Meta:
		db_table = 'StudentInfo'