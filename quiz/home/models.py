from django.db import models
import uuid
import random


# Create your models here.
class BaseModel(models.Model):
    uid=models.UUIDField(primary_key=True, default=uuid.uuid4)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)

    class Meta:
        abstract= True

class Category(BaseModel):
    category_name=models.CharField(max_length=100)

    def __str__(self):
        return self.category_name
    



class Question(BaseModel):
    category=models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    question=models.CharField(max_length=100)
    marks=models.IntegerField(default=5)

    def __str__(self):
        return self.question
    
    def get_answer(self):
        # Get only answers related to this question
        answer_obj = list(self.question_answer.all())  # using related_name
        random.shuffle(answer_obj)

        # Return only the first 4 answers
        data = []
        for ans in answer_obj[:4]:  # Limit to 4
            data.append({
                'answer': ans.answer,
                'is_correct': ans.is_correct,
            })

        return data
    
    


class Answer(BaseModel):
    question=models.ForeignKey(Question, on_delete=models.CASCADE,related_name='question_answer')
    answer=models.CharField(max_length=100)
    is_correct=models.BooleanField(default=False)  


    def __str__(self):
        return self.answer

