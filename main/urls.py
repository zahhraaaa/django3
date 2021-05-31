from django.urls import path
from .views import main_list , main_detail
app_name = 'main'
urlpatterns = [
 # post views
    path('',main_list, name='main_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:main>/',
    main_detail,
    name='main_detail'),
    ]