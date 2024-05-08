from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.http import Http404
from django.template import loader
# Create your views here.

def sayHello(request):
    return HttpResponse('<h1 style="color:red">My First Project in Django at Aurora web LAbs.</h1>')

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)


# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "HelloWorld_App/index.html", context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "HelloWorld_App/detail.html", {"question": question})