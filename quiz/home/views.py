from django.shortcuts import HttpResponse ,render ,redirect
from .models import *
import random
from django.http import JsonResponse
from django.db.models import Q
import requests
from icecream import ic 
import ast


# Create your views here.
def home(request):
    context = {'categories': Category.objects.all()}

    if request.GET.get('category'):
        category_param = request.GET.get('category')
        return redirect('quiz', category=category_param)

    return render(request, 'home.html', context)

def quiz(request,category):
    
    api_url = f"http://127.0.0.1:8000/api/get-quiz/?category={category}"
    response = requests.get(api_url)
    data = response.json()
    l = {}
    score = 0
    if request.method=="POST":
        for i in data['data']:
            x = (i['uid'])
            
            result = ast.literal_eval(request.POST.get(str(x)))
            ic(result)
            if result[0]=='True':
                 score = score + 1
            
            l[i["question"]] = {"answers":i['answer'],
                                "option_selected":result[1],
                                }

        
        payload = {'data': data['data'],'category':category,'score':score,'res' : l}   
        return render(request, 'score.html', payload)
    payload = {'data': data['data'],'category':category}
    
    return render(request, 'quiz.html', payload)

def result(request):
     
     return render(request)

def get_quiz(request):
        question_objs = Question.objects.all()       
        if request.GET.get('category'):
            question_objs = question_objs.filter(category__category_name__icontains =request.GET.get('category'))
        question_objs = list(question_objs)
           
        data = []
        random.shuffle(question_objs)
        for question_obj in question_objs:
            data.append({
                 'uid':question_obj.uid,
                'category':question_obj.category.category_name,
                'question':question_obj.question,
                'marks':question_obj.marks,
                'answer':question_obj.get_answer()
                
            })

        payload = {'data':data}

        return JsonResponse(payload)
   
