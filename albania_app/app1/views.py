from django.shortcuts import render
from .models import FormQuestion
from datetime import datetime
# Create your views here.


def index_page(request):
    return render(request, 'index.html')


def tour_page(request):
    return render(request, 'tour.html')


def visit_page(request):
    return render(request, 'visit.html')


def review_page(request):
    all_comments = FormQuestion.objects.all

    if request.method == "POST":
        name = request.POST['name']
        surname = request.POST['surname']
        email = request.POST['email']
        comment = request.POST['comment']
        time = datetime.now()
        question = FormQuestion(revName=name, revSurname=surname, revEmail=email, revQuestion=comment, revTime=time)
        question.save()

    return render(request, 'review.html', {'all': all_comments})
