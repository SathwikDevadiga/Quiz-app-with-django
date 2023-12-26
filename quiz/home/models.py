from django.db import models
import uuid
import random
class BaseModel(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    uid = models.UUIDField(primary_key=True , default=uuid.uuid4)

    class Meta:
        abstract = True
class Category(BaseModel):
    category_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.category_name
    

class Question(BaseModel):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='category')
    question = models.CharField(max_length=100)
    marks = models.IntegerField(default=5)

    def __str__(self) -> str:
        return self.question
    def get_answer(self):
        answer_objs = Answer.objects.filter(question=self)
        
        data=[]
        for answer_obj in answer_objs:
            data.append({
                'answer':answer_obj.answer,
                'is_correct':answer_obj.is_correst,
            })
        return data
class Answer(BaseModel):
    question = models.ForeignKey(Question,on_delete=models.CASCADE,related_name='question_answer')
    answer = models.CharField(max_length=100)
    is_correst = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.answer

