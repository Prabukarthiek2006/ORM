from django.db import models
from django.contrib import admin

class Loan(models.Model):
	Name = models.CharField(max_length=30)
	LoanID = models.IntegerField(primary_key="LoanID")
	AccNo = models.IntegerField()
	LoanAmt = models.FloatField()
	

class LoanAdmin(admin.ModelAdmin):
	list_display = ('Name','LoanID','AccNo','LoanAmt')

