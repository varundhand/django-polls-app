# this file will hold a list of database tables...all these tables will inhert from 'models.Model' class
from django.db import models

# class TableName(models.Model):
#   field_name = models.DataType(optional_params)


class Questions(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data publshied')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
