from django.http import Http404
from django.shortcuts import get_object_or_404, render

from .models import Questions, Choice


# This function gets called when the user hits the /polls route
# It then renders the template specified in the second paramter of the render funtion

# get questions and display them
def index(request):
    # variableName = ModelName.objects.sqlQuery
    latest_question_list = Questions.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}

    return render(request, 'polls/index.html', context)
# context is always passed as an dictionary or object

# show specific question and objects


def detail(request, question_id):
    print('in here')
    try:
        question = Questions.objects.get(pk=question_id)
        print(question.id)
    except Questions.DoesNotExist:
        raise Http404('Question does not exist')
    return render(request, 'polls/details.html', {'question': question})

# get question and display them
# def results(request,question_id):
#     question = get_object_or_404(Questions,pk =question_id)
#     return render(request, 'polls/results.html',{'question':question})


def help(request):
    # ! Injecting variables in django templates
    profile_name = "Varun Dhand"
    profile_age = 16
    profile_is_active = True
    profile_interests = ['gigi hadid', 'kendall jenner', 'kelly kapoor']
    context = {'name': profile_name, 'age': profile_age,
               'is_active': profile_is_active, 'interests': profile_interests}
    return render(request, 'polls/help.html', context)


def practise(request):
    my_practise = 'wassupp'
    context = {'prac': my_practise}
    return render(request, 'polls/myPractise.html', context)


def home(request):
    return render(request, 'polls/exampleOne.html')
