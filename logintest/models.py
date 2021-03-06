from django.db import models

class Login(models.Model):

	userId = models.CharField(max_length = 50, unique = True)
	password = models.CharField(max_length = 20)
	username = models.CharField(max_length = 50)
	email = models.EmailField(unique=True, null = True)
	fbId = models.CharField(max_length = 50, unique=True, null = True)
	class Meta:
		db_table = "login"

class UserDetails(models.Model):

	uId = models.ForeignKey(Login, on_delete = models.CASCADE)
	address = models.CharField(max_length = 100)
	city = models.CharField(max_length = 50)
	state = models.CharField(max_length = 30)
	country = models.CharField(max_length = 50)
	pin = models.CharField(max_length = 6)
	contactno = models.CharField(max_length = 10)
	class Meta:
		db_table = "userdetails"
