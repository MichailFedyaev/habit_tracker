from rest_framework import generics
from .models import Habit
from .serializers import HabitSerializer


class HabitCreateAPIView(generics.CreateAPIView):
    """Создание"""
    serializer_class = HabitSerializer


class HabitUpdateAPIView(generics.UpdateAPIView):
    """Редактирование"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitDestroyAPIView(generics.DestroyAPIView):
    """Удаление"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """Одна привычка"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitListAPIView(generics.ListAPIView):
    """Список привычек"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()