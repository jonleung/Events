from django.db import models
import datetime

class Event(models.Model):
	date = models.DateField()
	time = models.TimeField()
	title = models.CharField(max_length=50)
	location = models.CharField(max_length=50)
	url = models.CharField(max_length=4000, blank=True)
	
	def dotw_month(self):
		weekday = self.date.weekday()
		
		if(weekday == 0):
			dotw = 'Mon'
		elif(weekday == 1):
			dotw = 'Tue'
		elif(weekday == 2):
			dotw = 'Wed'
		elif(weekday == 3):
			dotw = 'Thu'
		elif(weekday == 4):
			dotw = 'Fri'
		elif(weekday == 5):
			dotw = 'Sat'
		elif(weekday == 6):
			dotw = 'Sun'
		
		month_num = self.date.month
		 
		if(month_num == 0):
			month = 'Jan'
		elif(month_num == 1):
			month = 'Feb'
		elif(month_num == 2):
			month = 'Mar'
		elif(month_num == 3):
			month = 'Apr'
		elif(month_num == 4):
			month = 'May'
		elif(month_num == 5):
			month = 'Jun'
		elif(month_num == 6):
			month = 'Jul'
		elif(month_num == 7):
			month = 'Aug'
		elif(month_num == 8):
			month = 'Sep'
		elif(month_num == 9):
			month = 'Oct'
		elif(month_num == 10):
			month = 'Nov'
		elif(month_num == 11):
			month = 'Dec'
		
		return dotw + ' ' + month
			
	def day(self):
		return self.date.day
		
	def start_time(self):
		return self.time.strftime("%I:%M%p")
	
	def __unicode__(self):
		return self.title + ' on ' + str(self.date)  + ' @ ' + str(self.time)
		
#Mon
#Tue
#Wed
#Thu
#Fri
#Sat
#Sun

#Jan
#Feb
#Mar
#Apr
#May
#Jun
#Jul
#Aug
#Sep
#Oct
#Nov
#Dec