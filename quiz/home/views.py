from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
import random

# Home view
def home(request):
    context = Category.objects.all()
    
    # Fix: Correct usage of quotes inside f-string
    if request.GET.get('category'):
        return redirect(f'/quiz/?category={request.GET.get("category")}')

    return render(request, 'home.html', {'data': context})


# Quiz view - show questions based on the selected category
def quiz(request):
    category_name = request.GET.get('category')
    questions = Question.objects.filter(category__category_name=category_name)

    return render(request, 'quiz.html', {'questions': questions, 'category': category_name})

def get_quiz(request):
    try:
        # Start with a queryset
        question_obj = Question.objects.all()

        # Apply category filter if provided
        category = request.GET.get('category')
        if category:
            question_obj = question_obj.filter(category__category_name__icontains=category)

        # Convert to list after filtering
        question_obj = list(question_obj)
        random.shuffle(question_obj)

        data = []
        for i in question_obj:
            data.append({
                'category': i.category.category_name,
                'question': i.question,
                'marks': i.marks,
                'answer': i.get_answer(),
            })

        payload = {'status': True, 'data': data}
        return JsonResponse(payload)

    except Exception as e:
        print(e)
        return HttpResponse('Something went wrong')
    
def submit_quiz(request):
    if request.method == 'POST':
        score = 0
        questions = Question.objects.all()
        
        # Loop through questions and check the submitted answers
        for question in questions:
            correct_answer = question.question_answer.filter(is_correct=True).first()
            
            # Check if a correct answer exists for the question
            if correct_answer:
                selected_answer = request.POST.get(f'question_{question.uid}')
                
                if selected_answer == correct_answer.answer:
                    score += question.marks

        return render(request, 'result.html', {'score': score})
    else:
        return HttpResponse('Invalid request method', status=400)
   
    