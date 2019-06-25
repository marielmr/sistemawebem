from django.db import models

# Create your models here.

class person(models.Model):
	idperson=models.AutoField(primary_key=True)
	firstname=models.CharField(max_length=50)
	lastname=models.CharField(max_length=50)
	birthdate=models.DateField()

class user(models.Model):
	iduser=models.AutoField(primary_key=True)
	user=models.CharField(max_length=20)
	password=models.CharField(max_length=8)
	img=models.URLField()
	idperson=models.ForeignKey(person,on_delete=models.CASCADE)


class doctor(models.Model):
	iddoctor=models.AutoField(primary_key=True)
	speciality=models.CharField(max_length=30)
	idperson=models.ForeignKey(person,on_delete=models.CASCADE)


class patient(models.Model):
	idpatient=models.AutoField(primary_key=True)
	idperson=models.ForeignKey(person,on_delete=models.CASCADE)
	weight=models.FloatField()
	cutes=models.IntegerField()


class medicalvisit(models.Model):
	idmedicalvisit=models.AutoField(primary_key=True)
	idperson=models.ForeignKey(person,on_delete=models.CASCADE)
	idpatient=models.ForeignKey(patient,on_delete=models.CASCADE)
	comentary=models.TextField(max_length=300)
	date=models.DateField()

class cut(models.Model):
	idcut=models.AutoField(primary_key=True)
	idmedicalvisit=models.ForeignKey(medicalvisit,on_delete=models.CASCADE)
	url=models.URLField()
	numbercut=models.IntegerField()

		
		
		