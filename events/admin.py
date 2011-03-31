from events.models import Event
from django.contrib import admin

class EventAdmin(admin.ModelAdmin):
	list_display = ('date', 'time', 'title', 'location')
	list_filter = ['date','time']
	search_fields = ['date','time','title','location','url']
	
admin.site.register(Event, EventAdmin)