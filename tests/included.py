from django.conf.urls import include, url
from django.http import HttpResponse


def testify(request):
    return HttpResponse('testify!')


urlpatterns = [
    url(r'^included/', include('tests.included2')),
    url(r'^test/$', testify, name='testify'),
]
