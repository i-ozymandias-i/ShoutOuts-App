import os,sys
sys.path.insert(0,os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2]))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "moza_django.settings.dev")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
