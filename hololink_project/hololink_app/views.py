from django.shortcuts import render
from .models import Question


def frontpage(requests):
    question = Question.objects.get(name='Nerissa Ravencroft')
    return render(requests, "frontpage.html", {"question": question})
