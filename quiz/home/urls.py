from django.urls import path
from . import views
urlpatterns = [
   path('',views.home,name='home'),
   path('quiz/<str:category>/',views.quiz,name='quiz'),
   path('quiz/<str:category>/result',views.quiz,name='quiz'),
   path('api/get-quiz/', views.get_quiz,name="get_quiz")
]