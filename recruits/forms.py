from django import forms
from recruits.models import Planet, Sith, Recruit

class RecruitForm(forms.ModelForm):
    recruit_name = forms.CharField(label='Name', max_length=200)
    recruit_age = forms.IntegerField(label='Age')
    recruit_email = forms.EmailField(label='Email')
    recruit_planet = forms.ModelChoiceField(queryset=Planet.objects.all())

    class Meta:
        model = Recruit
        fields = ['recruit_name', 'recruit_age', 'recruit_email', 'recruit_planet']


class SithForm(forms.Form):
    name = forms.ModelChoiceField(queryset=Sith.objects.all())