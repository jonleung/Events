import os, sys
sys.path.append('/home/jonathan/Events')
sys.path.append('/home/jonathan/Events/events')

os.environ['DJANGO_SETTINGS_MODULE'] = 'Events.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
