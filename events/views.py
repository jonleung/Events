from django.http import HttpResponse
from events.models import Event
from django.template import Context, loader
import datetime

def page(request):
    events = Event.objects.filter(date__gte=datetime.date.today()).order_by('date', 'time')
    t = loader.get_template('events/index.html')
    c = Context({
        'events': events,
    })
    return HttpResponse(t.render(c))