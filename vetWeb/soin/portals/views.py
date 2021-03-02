from django.shortcuts import render, redirect
from user.models import Vet_Officer
from .forms import SickApproachForm, DeathApproachForm, SurgicalApproachForm, DewormingForm, VaccinationForm, ArtificialInseminationForm, CalfRegistrationForm, LivestockInventoryForm, PregnancyDiagnosisForm,FarmConsultationForm
from django.contrib import messages
#from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import user_passes_test
from portals.models import Vet_Forms, Livestock_Inventory_Form


def vet_check(request):
    return request.is_vet_officer

def farmer_check(request):
    return request.is_farmer

def student_check(request):
    return request.is_student    


@user_passes_test(vet_check, login_url='login')
def portal_vet(request):
    vet_officers = Vet_Officer.objects.all()
    context = {
        'all_vets': vet_officers
    }
    return render(request, 'portals/indexvet.html', context)

@user_passes_test(farmer_check, login_url='login')
def portal_farmer(request):
    vet_officers = Vet_Officer.objects.all()
    context = {
        'all_vets': vet_officers
    }
    return render(request, 'portals/indexfarmer.html', context)

@user_passes_test(student_check, login_url='login')
def portal_student(request):
    vet_officers = Vet_Officer.objects.all()
    context = {
        'all_vets': vet_officers
    }
    return render(request, 'portals/indexstudent.html', context)  


@user_passes_test(vet_check, login_url='login')
def clinical_approach(request):
    return render(request, 'portals/clinical_approach.html') 

@user_passes_test(vet_check, login_url='login')
def sick_approach(request):
    if request.method == "POST":
        form = SickApproachForm(request.POST)
        if form.is_valid():
            vet_sick_form = Vet_Forms(is_sick_approach_form=True)
            vet_sick_form.save()
            form.save()
            messages.success(request, 'Details  Succesfully Saved')
            return redirect('vet-portal')    

    else:
        form = SickApproachForm()

    context = {
        'form':form,
        'name':'Sick Approach Form'
         }
    return render(request, 'portals/forms.html', context) 

@user_passes_test(vet_check, login_url='login')
def dead_approach(request):
    if request.method == "POST":
        form = DeathApproachForm(request.POST)
        if form.is_valid():
            vet_death_form = Vet_Forms(is_dead_approach_form=True)
            vet_death_form.save() 
            form.save()
            messages.success(request, 'Details  Succesfully Saved')
            return redirect('vet-portal')    

    else:
        form = DeathApproachForm()

    context = {
        'form':form,
        'name':'Death Approach Form'
         }
    return render(request, 'portals/forms.html', context)   

@user_passes_test(vet_check, login_url='login')
def surgical_approach(request):
    if request.method == "POST":
        form = SurgicalApproachForm(request.POST)
        if form.is_valid():
            vet_surgical_form = Vet_Forms(is_dead_approach_form=True)
            vet_surgical_form.save() 
            form.save()
            messages.success(request, 'Details  Succesfully Saved')
            return redirect('vet-portal')    

    else:
        form = SurgicalApproachForm()

    context = {
        'form':form,
        'name':'Surgical Approach Form'
         }
    return render(request, 'portals/forms.html', context) 

@user_passes_test(vet_check, login_url='login')
def deworming(request):
    if request.method == "POST":
        form = DewormingForm(request.POST)
        if form.is_valid():
            vet_deworming_form = Vet_Forms(is_dead_approach_form=True)
            vet_deworming_form.save() 
            form.save()
            messages.success(request, 'Details  Succesfully Saved')
            return redirect('vet-portal')    

    else:
        form = DewormingForm()

    context = {
        'form':form,
        'name':'Deworming Form'
         }
    return render(request, 'portals/forms.html', context)

@user_passes_test(vet_check, login_url='login')    
def vaccination(request):
    if request.method == "POST":
        form = VaccinationForm(request.POST)
        if form.is_valid():
            vet_vaccination_form = Vet_Forms(is_vaccination_form=True)
            vet_vaccination_form.save() 
            form.save()
            messages.success(request, 'Details  Succesfully Saved')
            return redirect('vet-portal')    

    else:
        form = VaccinationForm()

    context = {
        'form':form,
        'name':'Vaccination Form'
         }
    return render(request, 'portals/forms.html', context)

@user_passes_test(vet_check, login_url='login')
def breeding_record(request):
    ...

@user_passes_test(vet_check, login_url='login')
def artificial_insemination(request):
    if request.method == "POST":
        form = ArtificialInseminationForm(request.POST)
        if form.is_valid():
            vet_ai_form = Vet_Forms(is_artificial_insemination_form=True)
            vet_ai_form.save() 
            form.save()
            messages.success(request, 'Details  Succesfully Saved')
            return redirect('vet-portal')    

    else:
        form = ArtificialInseminationForm()

    context = {
        'form':form,
        'name':'Artificial Insemination Form'
         }
    return render(request, 'portals/forms.html', context) 

@user_passes_test(farmer_check, login_url='login')
def calf_registration(request):
    if request.method == "POST":
        form = CalfRegistrationForm(request.POST)
        if form.is_valid():
            vet_calf_form = Vet_Forms(is_calf_registration_form=True)
            vet_calf_form.save() 
            form.save()
            messages.success(request, 'Details  Succesfully Saved')
            return redirect('vet-portal')    

    else:
        form = CalfRegistrationForm()

    context = {
        'form':form,
        'name':'Calf Registration Form'
         }
    return render(request, 'portals/farmerforms.html', context) 

@user_passes_test(farmer_check, login_url='login')
def livestock_inventory(request):
    if request.method == "POST":
        form = LivestockInventoryForm(request.POST, request.FILES)
        if form.is_valid():
            vet_inventory_form = Vet_Forms(is_livestock_inventory_form=True)
            vet_inventory_form.save() 
            form.save()
            messages.success(request, 'Details  Succesfully Saved')
            return redirect('farmer-portal')

    else:
        form = LivestockInventoryForm()

    context = {
        'form':form,
        'name':'Livestock Inventory Form',
         }
    return render(request, 'portals/farmerforms.html', context) 

@user_passes_test(vet_check, login_url='login')
def pregnancy_diagnosis(request):
    if request.method == "POST":
        form = PregnancyDiagnosisForm(request.POST)
        if form.is_valid():
            vet_preg_form = Vet_Forms(is_pregnancy_diagnosis_form=True)
            vet_preg_form.save() 
            form.save()
            messages.success(request, 'Details  Succesfully Saved')
            return redirect('vet-portal')    

    else:
        form = PregnancyDiagnosisForm()

    context = {
        'form':form,
        'name':'Pregnancy Diagnosis Form'
         }
    return render(request, 'portals/forms.html', context)
 
    
@user_passes_test(vet_check, login_url='login')
def consultation(request):
    if request.method == "POST":
        form = FarmConsultationForm(request.POST)
        if form.is_valid():
            consul_form = Vet_Forms(is_farm_consultation_form=True)
            consul_form.save() 
            form.save()
            messages.success(request, 'Details  Succesfully Saved')
            return redirect('vet-portal')    

    else:
        form = FarmConsultationForm()

    context = {
        'form':form,
        'name':'Farm consultation form'
         }
    return render(request, 'portals/forms.html', context)


def display_images(request):
    inventory = Livestock_Inventory_Form.objects.get(farmer_username=request.user)
    context = {
        'img_obj': inventory
    }
    return render(request, 'portals/gallery.html', context)



     