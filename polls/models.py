from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=100)#required parameter, column in models
    pub_date = models.DateTimeField('date published')#optional param is prompt
    #classes separated by 2 \n
    
    def __str__(self):
        return "Question:{}".format(self.question_text) #<Question: Question:qwqw>


class Choice(models.Model):
     #no primary key because automatically added int auto increment django
    question = models.ForeignKey(Question,on_delete=models.CASCADE)#uppercase word is constant, whenever question is deleted, all connected choices deleted
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


#to make migration files change python3 manage.py makemigrations polls
#^will make migration files in polls/migrations/0001_initial.py, can delete for as long as di pa na migrate
# to apply migrations use python3 manage.py migrate

"""
SAVING
from django.utils import timezone as tz
from polls.models import Question
q=Question(question_text="abc?",pub_date = tz.now())
q.pub_date
q.save()
"""
"""
GETTING
from polls.models import Question
Question.objects.all()>>queryset object

Question.objects.get(id=1)>>primary key,starts at 1, returns question class, id can be any field, will return ONE object

Question.objects.filter(something = something )>>  returns queryset of all matching properties
"""
"""
EDITING
q=Question(question_text="abc?",pub_date = tz.now())
q.save()
q.question_text="aaa"
q.save()

q=Question.objects.get(id=1)
q.property="blabla"
q.save()
"""
