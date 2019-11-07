from django.db import models
from django.urls import reverse

# Create your models here.
class Planet(models.Model):
    planet_name = models.CharField(max_length=300)

    def __str__(self):
        return self.planet_name


class Recruit(models.Model):
    recruit_name = models.CharField(max_length=200, primary_key=True)
    recruit_age = models.IntegerField(default=0)
    recruit_email = models.EmailField()
    recruit_planet = models.CharField(max_length=100, null=True)
    recruit_test = models.TextField()

    def __str__(self):
        return '%s %s %s %s %s' % (self.recruit_name, self.recruit_age, self.recruit_email, self.recruit_planet, self.recruit_test)

    def get_absolute_url(self):
        return reverse('show', args=[str(self.recruit_name)])


class Sith(models.Model):
    sith_name = models.CharField(max_length=200)
    sith_planet = models.ForeignKey(Planet, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.sith_name


class ShadowHands(models.Model):
    code_test = models.IntegerField(default=0)
    test = models.TextField()

    def __str__(self):
        return self.code_test


class Question(models.Model):
    question = models.CharField(max_length=300)

    def __str__(self):
        return self.question


class ChoiceQuestion(models.Model):
    question_choice = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    choice_text = models.TextField()
    answer_true = models.CharField(max_length=100)

    def __str__(self):
        return '%s %s' % (self.choice_text, self.answer_true)

