import imp
from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
urlpatterns = [

  path('apidate', (views.Api.as_view()), name = 'apidate'),

]