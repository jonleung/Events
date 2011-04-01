from django.db import models
from datetime import datetime, date, time, timedelta
import re, string

class Event(models.Model):
	date = models.DateField()
	time = models.TimeField()
	title = models.CharField(max_length=50)
	subtext = models.CharField(max_length=100, blank=True)
	location = models.CharField(max_length=50)
	url = models.CharField(max_length=4000)
	
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
		time = self.time.strftime("%I:%M%p").lower()
		if time[0] == '0':
			time = time[1:]
		return time
	
	def httpafy(self):
		return_url = self.url
		if self.url[0:7] != "http://":
			return 'http://' + return_url
		return return_url
	
	def __unicode__(self):
		return self.title + ' on ' + str(self.date)  + ' @ ' + str(self.time)
	
	def google_calendar(self):
		
		safe_title = self.title.replace(r' ',r'%20')
		safe_location = self.location.replace(r' ',r'%20')
		safe_subtext = self.subtext.replace(r' ',r'%20')
		
		o = r'http://www.google.com/calendar/event?action=TEMPLATE&text='
		o+= safe_title
		o+= r'&dates='
		o+= self.date.strftime('%Y%m%d')
		o+= r'T'
		o+=(datetime.combine(self.date, self.time) + timedelta(hours=4)).strftime('%H%M%S')
		o+= r'Z/'
		o+= self.date.strftime('%Y%m%d')
		o+= 'T'
		o+=(datetime.combine(self.date, self.time) + timedelta(hours=5)).strftime('%H%M%S')
		o+= r'Z'
		
		if self.subtext:
			o+= r'&details=' + safe_subtext
			
		o+= r'&location=' + safe_location
		o+= r'&trp=false'
		
		if self.url:
			o+=r'&sprop=' + self.url
		o+= r''
		
		return o
		
		
		
		
		
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