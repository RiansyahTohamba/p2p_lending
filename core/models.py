from django.db import models

# harus spesifik nama_folder dimana migrasi berada

# python3 manage.py makemigrations core
class Borrower(models.Model):
	name = models.CharField(max_length=255)
	city_id = models.SmallIntegerField()
	
class Credit(models.Model):
	loan_amnt = models.DecimalField(max_digits=6, decimal_places=2)
	funded_amnt_inv = models.DecimalField(max_digits=6, decimal_places=2)		