from django.forms import ModelForm
from .models import Question
#template forms from models
class QuestionModelForm(ModelForm):#convetion is model..modelform
    class Meta:#inner class of model form class
        model = Question
        #fields = ['question_text','pub_date']<like include
        #include = ['question_text']<includes only question_text
        #exclude =['id']<all but id
        exclude = ['id']

# to be imported in views