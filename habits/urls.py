from django.urls import path, include
from . import views

app_name = 'habits'

#router = DefaultRouter()
#router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
    path("", views.HabitListAPIView.as_view(), name="habit_list"),
    path("habit/<int:pk>", views.HabitRetrieveAPIView.as_view(), name="habit_retrieve"),
    path("habit/create", views.HabitCreateAPIView.as_view(), name="habit_create"),
    path("habit/<int:pk>/update", views.HabitUpdateAPIView.as_view(), name="habit_update"),
    path("habit/<int:pk>/delete", views.HabitDestroyAPIView.as_view(), name="habit_delete"),
] #+ router.urls