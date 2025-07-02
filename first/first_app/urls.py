
from django.conf.urls import url
from django.contrib import admin
from .views import form,log_in,user_login
app_name="first_app"
urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^login/',user_login,name='login'),
    url(r'^form/',form,name='form'),
    url(r'^log_in/',log_in,name='log_in'),

]
