from django.conf import settings
from django.http import HttpResponse


def favicon(request):
    data = open(settings.STATIC_DIR / "favicon/favicon.ico", "rb").read()
    return HttpResponse(data, content_type="image/x-icon")
