from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.utils.timezone import now, localtime
import json, os
from .forms import UserRegisterForm
from .forms import ProfileForm
from .forms import WeightForm
from .forms import Lift2Form
from .models import Profile
from .models import WeightRecord
from .models import LiftRecord2


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            messages.info(request, "Thanks for registering. You are now logged in.")
            new_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, new_user)
            return redirect('profile')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form' : form})

def login2(request, user):
    return render(request, 'users/login.html')

@login_required
def profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)




    if request.method == 'POST' and 'form_submit' in request.POST:
        profForm = ProfileForm(request.POST, instance = profile)
        if profForm.is_valid():
            stillValid = True
            try:
                if profForm.cleaned_data['daily_cal_in'] < 0:
                    #messages.warning(request, "Please enter a valid number of calories.", extra_tags='danger')
                    stillValid = False
                if profForm.cleaned_data['daily_carbs'] < 0:
                    messages.error(request, "Please enter a valid number of carbohydrates.", extra_tags='danger')
                    stillValid = False
                if profForm.cleaned_data['daily_fat'] < 0:
                    messages.error(request, "Please enter a valid number of fats.", extra_tags='danger')
                    stillValid = False
                if profForm.cleaned_data['daily_protein'] < 0:
                    messages.error(request, "Please enter a valid number of proteins.", extra_tags='danger')
                    stillValid = False
                if profForm.cleaned_data['goal_weight_change'] < 0:
                    messages.error(request, "Please enter a valid weight.", extra_tags='danger')
                    stillValid = False
                if profForm.cleaned_data['activity_level'] < 0:
                    messages.error(request, "Please enter a valid activity level.", extra_tags='danger')
                    stillValid = False
                if stillValid:
                    profForm.save()
                    messages.success(request, "Successfully updated profile!", extra_tags='success')
            except TypeError:
                messages.error(request, "Please re-enter valid information.", extra_tags='danger')

        else:
            messages.error(request, "Please re-enter valid information.", extra_tags='danger')

    form = ProfileForm()
    data = Profile.objects.filter(user=request.user)

    rec_calories = rec_carbs = rec_fats = rec_protein = goal_weight = curr_weight = activity = carb_percent = fat_percent = protein_percent = calories = carbs = fats = protein = {}
    for e in data:
        activity = e.activity_level
        goal_weight = e.goal_weight_change
        curr_weight = e.current_weight
        calories = e.daily_cal_in
        carbs = e.daily_carbs
        fats = e.daily_fat
        protein = e.daily_protein
        carb_percent = e.carb_percent
        fat_percent = e.fat_percent
        protein_percent = e.protein_percent
        rec_calories = (e.current_weight*10*e.activity_level)+(goal_weight*500)
        rec_carbs = round((calories*carb_percent)/400, 1)
        rec_fats = round((calories*fat_percent)/900,1)
        rec_protein = round((calories*protein_percent)/400,1)

   # weightList = []
  #  weights = WeightRecord.objects.filter(user=request.user).order_by('-date')
    #for e in weights:
       # weightList.append(e)
   # if len(weightList) != 0:
      #  currWeight = weightList[0].lbs
    context = {
        'loggedIn': False,
        'form': form,
        'calories' : calories,
        'carbs' : carbs,
        'fats' : fats,
        'protein' : protein,
        'activity' : activity,
        'goal_weight' : goal_weight,
        'curr_weight' : curr_weight,
        'carbPercent': carb_percent,
        'fatPercent': fat_percent,
        'proteinPercent': protein_percent,
        'rec_calories' : rec_calories,
        'rec_carbs': rec_carbs,
        'rec_fats': rec_fats,
        'rec_protein': rec_protein
    }
    if request.user.is_authenticated:
        context['loggedIn'] = True




    if request == 'POST' and 'calculate' in request.POST:
        context['goal_weight'] = profForm.cleaned_data['goal_weight_change']
        context['rec_fats'] = profForm.cleaned_data['daily_fat']


        rec_calories = (profForm.cleaned_data['daily_cal_in'] * 10 * profForm.cleaned_data['activity_level']) + (profForm.cleaned_data['goal_weight_change'] * 500)
        rec_carbs = round((rec_calories * profForm.cleaned_data['carb_percent']) / 400, 1)
        rec_fats = round((calories * profForm.cleaned_data['fat_percent']) / 900, 1)
        rec_protein = round((calories * profForm.cleaned_data['protein_percent']) / 400, 1)

        # weightList = []
        #  weights = WeightRecord.objects.filter(user=request.user).order_by('-date')
        # for e in weights:
        # weightList.append(e)
        # if len(weightList) != 0:
        #  currWeight = weightList[0].lbs
        context = {
            'loggedIn': False,
            'form': form,
            'calories': profForm.cleaned_data['daily_cal_in'],
            'carbs': profForm.cleaned_data['daily_carbs'],
            'fats': profForm.cleaned_data['daily_fat'],
            'protein': profForm.cleaned_data['daily_protein'],
            'activity': profForm.cleaned_data['activity_level'],
            'goal_weight': profForm.cleaned_data['goal_weight_change'],
            'curr_weight': profForm.cleaned_data['current_weight'],
            'carbPercent': profForm.cleaned_data['carb_percent'],
            'fatPercent': profForm.cleaned_data['fat_percent'],
            'proteinPercent': profForm.cleaned_data['protein_percent'],
            'rec_calories': rec_calories,
            'rec_carbs': rec_carbs,
            'rec_fats': rec_fats,
            'rec_protein': rec_protein
        }

    return render(request, 'users/profile.html', context)

@login_required
def weight(request):
    weightrecord = WeightRecord(user=request.user)
    if request.method == 'POST' and 'form_submit' in request.POST:
        lbForm = WeightForm(request.POST, instance = weightrecord)
        if lbForm.is_valid():
            lbForm.save()
        else:
            messages.error(request, "Please re-enter valid information.", extra_tags='danger')
    form = WeightForm()
    data = WeightRecord.objects.filter(user = request.user).order_by('-date')
    context = {
        'form' : form,
        'weights' : data,
    }
    return render(request, 'users/weight.html', context)
  
@login_required
def macros(request):
    return render(request, 'users/macros.html')
    
@login_required
def exercises(request, active_exercises=0):
    exercise_list = []

    with open(os.path.dirname(os.path.realpath(__file__)) + '/Exercises.json') as f:
        data = json.load(f)

    if (active_exercises == 100):
        exercise_list = data

    liftrecord2 = LiftRecord2(user=request.user)
    if request.method == 'POST' and 'form_submit' in request.POST:
        liftForm = Lift2Form(request.POST, instance = liftrecord2)
        if liftForm.is_valid():
            liftForm.save()
        else:
            messages.error(request, "Please re-enter valid information.", extra_tags='danger')
    form = Lift2Form()
    data = LiftRecord2.objects.filter(user = request.user).order_by('-date')
    context = {
        'exercises': exercise_list,
        'title': 'Exercises',
        'active_exercise': active_exercises, #exercise_list[0].group,
        'form' : form,
        'lifts' : data,
    }

    return render(request, 'users/exercises.html', context)



@login_required
def meals(request):
    return render(request, 'users/meals.html')

