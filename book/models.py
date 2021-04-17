from django.db import models

#Home Models

class Book(models.Model):
	name = models.CharField(max_length = 50)
	picture = models.ImageField()
	file= models.FileField()
	author = models.CharField(max_length = 30, default='anonymous')
	email = models.EmailField(blank = True)
	describe = models.TextField(default = 'Chethan Django ')


class Reg(models.Model):
    user=models.CharField(primary_key=True,max_length=20)
    pwd=models.CharField(max_length=20)

def __str__(self):
	return self.name
