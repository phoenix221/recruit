from django.shortcuts import render_to_response, render, redirect
from .forms import RecruitForm, SithForm
from .models import ChoiceQuestion, Recruit


# Create your views here.

def Index(request):
    recruit = "Для Рекрутов"
    sith = "Для Ситхов"
    return render_to_response('index.html', {'Recruit': recruit, 'Sith': sith})

def RecForm(request):
    if request.method == 'POST':
        form = RecruitForm(request.POST)
        if form.is_valid():
            form.save('recruit')
            request.session['global'] = request.POST['recruit_name']
            return redirect('/test')
    else:
        form = RecruitForm()
    return render (request, 'recruits_form.html', {'form': form})

def TestPage(request):
    question = ChoiceQuestion.objects.all()
    return render(request, 'test_page.html', {'q': question})


def Result(request):
    question = ChoiceQuestion.objects.all()
    if request.method == 'POST':
        name = request.session.get('global')
        check_value = request.POST.getlist('question[]')
        recruit = Recruit.objects.all()
        for r in recruit:
            if r.recruit_name == name:
                r.recruit_test = check_value
        r.save()
    return render_to_response('result.html', {'rightquestion': question, 'result': check_value})

def Sith(request):
    if request.method == 'POST':
        form = SithForm(request.POST)
        if form.is_valid():
            return redirect('/mainrecruit')
    else:
        form = SithForm()
    return render(request, 'sith.html', {'form': form})

def RecruitMain(request):
    main = Recruit.objects.all()
    return render_to_response('recruit_main.html', {'main': main})

def ShowRecruit(request, args):
    recruit = Recruit.objects.get(recruit_name=args)
    return render_to_response('show.html', {'show': recruit})