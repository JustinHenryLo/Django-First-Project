from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Question
from .forms import QuestionModelForm

# Create your views here.
def index(request):
    context = {} #params
    questions = Question.objects.all()
    context['questions']=questions
    return render(request,"index.html",context) #request shows http stuff


def help(request):
    return HttpResponse("Help page")

def detail(request, question_id):
    context={}
    context['question'] = Question.objects.get(id=question_id)
    return render(request,'detail.html',context)

def update(request,question_id):
    if(request.method == 'POST'):
        question = Question.objects.get(id=question_id)
        form = QuestionModelForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
        return HttpResponse('Question updated')
       
    else:
        question = Question.objects.get(id = question_id)
        context = {}
        context['form'] =QuestionModelForm(instance=question)
        context['q_id'] =question_id
        return render(request,"update.html",context)