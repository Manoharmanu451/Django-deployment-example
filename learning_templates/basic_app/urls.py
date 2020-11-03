from django.conf.urls import url
from basic_app import views

# Template Tagging
app_name = 'basic_app'

urlpatterns = [
    url('',views.relative,name = 'relative'),
    url('',views.other,name = 'other'),
]
