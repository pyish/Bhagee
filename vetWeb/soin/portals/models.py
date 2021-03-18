from django.db import models
from user.models import Farm

SPECIES_CHOICES = (
    ('0', 'cattle'),
    ('1', 'sheep'),
	('2', 'goat'),
	('3', 'donkey'),
	('4', 'dog'),
	('5', 'horse'),
	('6', 'poultry'),
	('7','others')
)

DISEASE_CHOICES = (
	('A','acute'),
	('S','sub_acute')

)

DIAGNOSIS_CHOICES = (
	('C','clinical_signs'),
	('L','laboratory')
)

PROGNOSIS_CHOICES=(
	('G','good'),
	('F','fair'),
	('P','poor')
)


YES_NO_CHOICES = (
	('Y','yes'),
	('N','no')
)


OPERATION_CHOICES=(
	('C','c_section'),
 	('I','interstinal_torsion'),
 	('T','tumor_extraction'),
 	('C','canine_spaying'),
 	('H','hernia'),
 	('W','Warts_etraction'),
 	('C','castration'),
 	('S','skin_injuries'),
 	('F','fructure'),
	('R','rumenatomy'),
 	('O','other'),
)

VACCINATION_CHOICES=(
	('M','Mass_vaccination'),
 	('R','Ring_vaccination'),
 	('I','Individual')
)

SEX_CHOICES = (
 	('M','male'),
 	('F','female')
 )


NATURE_CHOICES=(
 	('A','Alive'),
 	('D','Dead')
 )


COW_CATEGORY=(
	('A','Adult'),
	('H','Heifer')
)


STATUS_CHOICES=(
 	('H','Healthy'),
 	('D','Deformed')
 )

BREECHING_LEVEL=(
 	('F','First'),
 	('S','Second'),
 	('T','Third'),
 	('P','Pedegree')
)

RESULT_CHOICES=(
 	('P','positive'),
 	('N','Negative')
)




class Vet_Forms(models.Model):
	vet_username = models.CharField(max_length=20)
	is_sick_approach_form = models.BooleanField(default=False)
	is_dead_approach_form= models.BooleanField(default=False)
	is_surgical_approach_form = models.BooleanField(default=False)
	is_deworming_form = models.BooleanField(default=False)
	is_vaccination_form = models.BooleanField(default=False)
	is_artificial_insemination_form = models.BooleanField(default=False)
	is_calf_registration_form = models.BooleanField(default=False)
	is_livestock_inventory_form = models.BooleanField(default=False)
	is_farm_consultation = models.BooleanField(default=False)
	is_pregnancy_diagnosis_form = models.BooleanField(default=False)
	report_created_on = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-report_created_on']

	def __str__(self):
		return 'Vet form'	


class Sick_Approach_Form(models.Model):
	vet_form = models.OneToOneField(Vet_Forms, on_delete=models.CASCADE, primary_key=True)
	farmer_username = models.CharField(max_length=12,verbose_name='Farmer Username')
	species_affected = models.CharField(max_length=20, choices=SPECIES_CHOICES, default='0', verbose_name='animal species affected')
	num_of_species_affected = models.PositiveIntegerField(verbose_name='number of species affected')
	id_animal = models.CharField(max_length=100, verbose_name='name of the animal/identification number', null=True, blank=True)
	disease_nature = models.CharField(max_length=20, choices=DISEASE_CHOICES, default='0', verbose_name='nature of the disease')
	clinical_signs = models.CharField(max_length=100)
	disease_diagnosis = models.CharField(max_length=20, choices=DIAGNOSIS_CHOICES, default='0')
	differential_diagnosis = models.CharField(max_length=100, null=True, blank=True)
	final_diagnosis = models.CharField(max_length=100)
	sickness_duration = models.CharField(max_length=100, verbose_name='duration of the sickness')
	sickness_history = models.CharField(max_length=100, null=True, blank=True)
	drug_of_choice = models.CharField(max_length=100, null=True, blank=True)
	treatment_duration = models.CharField(max_length=100)
	start_dose_date = models.DateField()
	prognosis = models.CharField(max_length=20, choices=PROGNOSIS_CHOICES, default='G')
	harmony_with_clinic_signs_and_lab = models.CharField(max_length=5, choices=YES_NO_CHOICES, default='Y',verbose_name='were the pathological signs in harmony with the clinical signs and laboratory reports?')
	cause_of_death_if_in_no_harmony = models.CharField(max_length=100, null=True, blank=True,verbose_name='If no, what could be the cause of the death')
	disease_one_of_the_zoonotic = models.CharField(max_length=5, choices=YES_NO_CHOICES, default='0', verbose_name='is the disease one of the zoonotic?')
	advice_given_if_zoonotic = models.CharField(max_length=100, null=True, blank=True, verbose_name='if yes, what advice did you give the owner and people who handled the carcass')
	relapse = models.CharField(max_length=5, choices=YES_NO_CHOICES, default='0', verbose_name='was there any relapse?')
	cause_if_relapse = models.CharField(max_length=100, null=True, blank=True, verbose_name='if yes, what might be the cause')
	comment = models.CharField(max_length=300,null=True,blank=True,verbose_name='comment')
	
	def __str__(self):
		return self.farmer_username
	

class Death_Approach_Form(models.Model):
	vet_form = models.OneToOneField(Vet_Forms, on_delete=models.CASCADE, primary_key=True)
	farmer_username = models.CharField(max_length=12,verbose_name='Farmer Username')
	name_of_the_animal = models.CharField(max_length=30,null=True,blank=True,verbose_name='Name or identification number')
	sex_of_the_animal = models.CharField(max_length=20,choices=SEX_CHOICES,default='M',verbose_name='Sex of the animal')
	num_of_species_dead = models.IntegerField(default=1,null=True,verbose_name='Number of animals dead')
	case_history = models.CharField(max_length=100, default='When was the case reported')
	mortality_rate = models.CharField(max_length=100, default='State the mortality rate of the case reported')
	death_time = models.DateField(verbose_name='At what time the animal the animals died')
	signs_of_cadever_on_the_ground = models.CharField(max_length=200,verbose_name='What are the signs of signs of the cadever on the ground')
	carcass_opened_for_the_pm = models.CharField(max_length=5, choices=YES_NO_CHOICES,default='Y',verbose_name='Did you open up the carcass fo PM?')
	if_yes_pathological_signs = models.CharField(max_length=100, null=True, blank=True,verbose_name='If yes,what were the signs of the pathological conditions?')
	if_no_reason = models.CharField(max_length=100, null=True, blank=True,verbose_name='If no,what could have been the reason?')
	sample_sent_lab = models.CharField(max_length=5, choices=YES_NO_CHOICES, default='Y',null=True,verbose_name='Did you send any sample to the laboratory?')
	if_yes_lab_report = models.CharField(max_length=100, null=True, blank=True,verbose_name='if yes,what was the laboratory report?')
	death_cause_notifiable = models.CharField(max_length=5, choices=YES_NO_CHOICES, default='Y',verbose_name='Is the cause of dead notifiable?')
	if_yes_message_to_relevant_body = models.CharField(max_length=100, null=True, blank=True,verbose_name='If yes,send message to the relevant body.')
	intervention_regards_to_death = models.CharField(max_length=100, null=True, blank=True,verbose_name='What were the necessary intervention in regard to the cause of the dead')
	comment = models.CharField(max_length=300,null=True,blank=True,verbose_name='comment')

	def __str__(self):
		return f'Name of form: Death Approach Form'


class Surgical_Approach_Form(models.Model):
	vet_form = models.OneToOneField(Vet_Forms, on_delete=models.CASCADE, primary_key=True)
	farmer_username = models.CharField(max_length=12,verbose_name='Farmer Username', default='')
	species_operated_on = models.CharField(max_length=20, choices=SPECIES_CHOICES, default='0',verbose_name='Animal species naffected')
	if_other_specify = models.CharField(max_length=100, null=True, blank=True,verbose_name='If,other specify.')
	sex_of_the_animal = models.CharField(max_length=20,choices=SEX_CHOICES, default='M', verbose_name='Sex of the animal')
	name_of_the_animal = models.CharField(max_length=30,null=True,blank=True,verbose_name='Name or identification number')
	operation_nature= models.CharField(max_length=20, choices=OPERATION_CHOICES,default='C', verbose_name='Nature of operation')
	if_other_specify = models.CharField(max_length=100, null=True, blank=True,verbose_name=True)
	operation_date = models.DateField()
	post_operation_management = models.CharField(max_length=100, default='',null=True,verbose_name='Post operation management')
	prognosis = models.CharField(max_length=100, default='',null=True,verbose_name='Prognosis')
	comment = models.CharField(max_length=100, null=True, blank=True)

	def __str__(self):
		return f'Name of form: Surgical Approach Form'


class Deworming_Form(models.Model):
	vet_form = models.OneToOneField(Vet_Forms, on_delete=models.CASCADE, primary_key=True)
	farmer_username = models.CharField(max_length=12,verbose_name='Farmer Username')
	species_targeted = models.CharField(max_length=20, choices=SPECIES_CHOICES, default='0',verbose_name='Species targetted')
	number_of_adults = models.PositiveIntegerField(default=1,null=True,verbose_name='Number of adults')
	number_of_young_ones = models.PositiveIntegerField(default=1,null=True,verbose_name='Number of young ones')
	body_condition_of_the_animal = models.CharField(max_length=20, choices=PROGNOSIS_CHOICES, default='G',verbose_name='Body condition of the animal(s)')
	date_of_deworming = models.DateField()
	drug_choices = models.CharField(max_length=100, default='',verbose_name='Drug of choice')
	target_parasites = models.CharField(max_length=100, null=True, blank=True,verbose_name='Target parasite')
	withdrawal_period = models.DurationField()
	side_effects = models.CharField(max_length=100, null=True, blank=True,verbose_name='Any side effect?')
	next_date_deworming = models.DateField(verbose_name='Next date of deworming')
	comment = models.CharField(max_length=100, null=True, blank=True)

	
	def __str__(self):
		return f'Name of form: Deworming Approach Form'


class Vaccination_Form(models.Model):
	vet_form = models.OneToOneField(Vet_Forms, on_delete=models.CASCADE, primary_key=True)
	farmer_username = models.CharField(max_length=12,verbose_name='Farmer Username')
	species_targeted = models.CharField(max_length=20, choices=SPECIES_CHOICES, default='0',verbose_name='Animal species targetted')
	if_other_specify = models.CharField(max_length=100, null=True, blank=True,verbose_name='If other specify')
	number_of_animals_vaccinated= models.IntegerField(default=1,null=True,blank=True,verbose_name='Number of animals vaccinated.')
	age_of_animal = models.PositiveIntegerField(default=1,null=True,blank=True,verbose_name='Age of animal')
	sex_of_the_animal = models.CharField(max_length=20,choices=SEX_CHOICES,default='M', verbose_name='Sex of the animal')
	animal_breed = models.CharField(max_length=100, null=True, blank=True,verbose_name='Breed of the animal')
	animal_colour = models.CharField(max_length=100,null=True,verbose_name='Colour of the animal')
	other_description = models.CharField(max_length=100,null=True,blank=True,verbose_name='other description')
	targetted_disease = models.CharField(max_length=20,null=True,verbose_name='The disease target')
	vaccines_used = models.CharField(max_length=100, null=True, blank=True,verbose_name='Vaccine used')
	date_of_vaccination = models.DateField()
	next_date_of_vaccination = models.DateTimeField()
	name_of_the_crush = models.CharField(max_length=100, null=True, blank=True,verbose_name='Name of the crush')
	nature_of_the_vacination_program = models.CharField(max_length=200, choices=VACCINATION_CHOICES, default='M',verbose_name='Nature of the vaccination program')
	comment = models.CharField(max_length=100, null=True, blank=True)

	
	def __str__(self):
		return f'Name of form: Vaccination Approach Form'


class Artificial_Insemination_Form(models.Model):
	vet_form = models.OneToOneField(Vet_Forms, on_delete=models.CASCADE, primary_key=True)
	farmer_username = models.CharField(max_length=12,verbose_name='Farmer Username')
	Name_of_the_cow = models.CharField(max_length=12,verbose_name='Name of the cow or identification number of the cow')
	time_of_heat_sign = models.DateField(verbose_name='Time of heat sign')
	time_of_insemination = models.DateField(verbose_name='Time of insemination')
	date_of_insemination = models.DateField(verbose_name='Date of insemination')
	nature_of_the_breeding = models.CharField(max_length=100, null=True, blank=True,verbose_name='Nature of breeding')
	sire_name = models.CharField(max_length=200,null=True,blank=True,verbose_name='Nature of breeding')
	sire_origin = models.CharField(max_length=200,null=True,blank=True,verbose_name='Sires name')
	bull_code= models.CharField(max_length=100, null=True, blank=True,verbose_name='Bull code')
	sex_of_the_calf_born = models.CharField(max_length=20, choices=SEX_CHOICES, default='M',verbose_name='Sex of the calf born')
	date_of_birth = models.DateField(verbose_name='Date of birth')
	nature_of_birth = models.CharField(max_length=20, choices=NATURE_CHOICES, default='A',verbose_name='Nature of birth')
	number_of_repeat = models.CharField(max_length=100, null=True, blank=True,verbose_name='Number of repeat')
	abortion_rate = models.CharField(max_length=100, null=True, blank=True,verbose_name='Abortion rate')
	reason_for_the_cause_of_abortion = models.CharField(max_length=100, null=True, blank=True,verbose_name='reason for abortion')
	breed_used = models.CharField(max_length=100, null=True, blank=True,verbose_name='Breed used')
	source_of_semen = models.CharField(max_length=100, null=True, blank=True,verbose_name='Source of the semen')
	date_of_repeat_checked = models.DateField(verbose_name='Date of repeat check')
	date_of_pregnancy_diagnosis = models.DateField(verbose_name='Date of pregnancy')
	expected_date_of_calving = models.DateField(verbose_name='expected date of calving')
	comment = models.CharField(max_length=100, null=True, blank=True)

	
	def __str__(self):
		return f'Name of form: Artificial Approach Form'


class Calf_Registration_Form(models.Model):
	vet_form = models.OneToOneField(Vet_Forms, on_delete=models.CASCADE, primary_key=True)
	farmer_username = models.CharField(max_length=12,verbose_name='Farmer Username', default='')
	date_of_birth = models.DateField(verbose_name='Date of birth')
	sex_of_the_calf = models.CharField(max_length=20, choices=SEX_CHOICES, default='M',verbose_name='Sex of the calf')
	birth_weight = models.IntegerField(verbose_name='Birth weight')
	breed_of_the_calf = models.CharField(max_length=20,verbose_name='breed of the calf')
	colour_of_the_breed= models.CharField(max_length=20,verbose_name='Colour of the breed')
	status_of_the_calf = models.CharField(max_length=100, choices=STATUS_CHOICES, default='H',verbose_name='Status of the calf')
	breeching_level_of_the_calf = models.CharField(max_length=100, choices=BREECHING_LEVEL, default='F',verbose_name='Breeching level of the calf')
	sire_details = models.CharField(max_length=100, null=True, blank=True)
	expected_date_of_weaning = models.DateField(verbose_name='Expected date of weaning')
	comment = models.CharField(max_length=100, null=True, blank=True)

	
	def __str__(self):
		return f'Name of form: Calf Registration Approach Form'


class Livestock_Inventory_Form(models.Model):
	vet_form = models.OneToOneField(Vet_Forms, on_delete=models.CASCADE, primary_key=True)
	farmer_username = models.CharField(max_length=12,verbose_name='Farmer Username')
	species_targeted = models.CharField(max_length=20, choices=SPECIES_CHOICES, default='0',verbose_name='Species targetted')
	name_of_the_animal = models.CharField(max_length=30,null=True,blank=True,verbose_name='Name or identification number')
	number_of_the_male_animals= models.IntegerField(default=1,null=True,blank=True,verbose_name='Number of male animals')
	number_of_the_female_animals= models.IntegerField(default=1,null=True,blank=True,verbose_name='Number of female animals')
	number_of_live_animals= models.IntegerField(default=1,null=True,blank=True,verbose_name='Number of live animals')
	number_of_dead_animals= models.IntegerField(default=1,null=True,blank=True,verbose_name='Number of dead animals')
	specify_the_cause_of_the_dead = models.CharField(max_length=100, null=True, blank=True,verbose_name='Specify the cause of dead')
	is_your_animals_insured = models.CharField(max_length=20, choices=YES_NO_CHOICES, default='Y',verbose_name='Has your animals been insured?')
	if_yes_give_insuring_company = models.CharField(max_length=100, null=True, blank=True,verbose_name='If yes,give the insuring company')
	date_of_culling = models.DateField(verbose_name='Date of culling')
	give_reason_for_culling = models.CharField(max_length=200,null=True,blank=True,verbose_name='Give reason for culling')
	Attach_photos_of_your_animal = models.ImageField(upload_to='vet_photos', height_field=None, width_field=None, max_length=100,verbose_name='Upload photos')
	comment = models.CharField(max_length=100, null=True, blank=True)
	

	def __str__(self):
		return f'Name of form: Livestock Inventory Approach Form'


class Pregnancy_Diagnosis_Form(models.Model):
	vet_form = models.OneToOneField(Vet_Forms, on_delete=models.CASCADE, primary_key=True)
	farmer_username = models.CharField(max_length=12,verbose_name='Farmer Username')
	cow_name = models.CharField(max_length=20,null=True,blank=True,verbose_name='Name or idenfication number of the cow')
	cow_category = models.CharField(max_length=50,choices = COW_CATEGORY,default='H', verbose_name='Cow`s category')
	date_of_insemination = models.DateField(verbose_name='Date of insemination')
	date_of_pregnancy_diagnosis = models.DateField(verbose_name='date of pregnancy diagnosis')
	result_of_diagnosis = models.CharField(max_length=20, choices = RESULT_CHOICES, verbose_name='Results of diagnosis')
	if_positive = models.CharField(max_length=100,null=True,blank=True,verbose_name='If the result is positive give the approximate age of the fetus.')
	if_result_is_negative_give_observation = models.CharField(max_length=100, null=True, blank=True,verbose_name='If the result test negative give your observation')
	next_date_of_pregnancy_diagnosis = models.DateField(verbose_name='Next date of pregnancy diagnosis')
	expected_date_of_delivery = models.DateField(verbose_name='Expected date of delivery')
	comment = models.CharField(max_length=100, null=True, blank=True,verbose_name='Comment')

	def __str__(self):
		return f'Name of form: Pregnancy Diagnosis Form'

class Farm_Consultation(models.Model):
	vet_form = models.OneToOneField(Vet_Forms, on_delete=models.CASCADE, primary_key=True)
	farmer_username = models.CharField(max_length=12,verbose_name='Farmer Username')
	Dairy_cows = models.CharField(max_length=12,null=True,blank=True,verbose_name='Dairy cows unit')
	beef_production = models.CharField(max_length=20,null=True,blank=True,verbose_name='Beef production unit')
	poultry = models.CharField(max_length=30,null=True,blank=True,verbose_name='Poultry production unit')
	sheep = models.CharField(max_length=50,null=True,blank=True,verbose_name='Sheep production unit')
	goat = models.CharField(max_length=100,null=True,blank=True,verbose_name='Goat production unit')
	canine = models.CharField(max_length=100,null=True,blank=True,verbose_name='Canine keeping')
	other = models.CharField(max_length=100,null=True,blank=True,verbose_name='Other livestock')
	give_recommendation = models.CharField(max_length=100,null=True,blank=True,verbose_name='Give recommendation.')
	grazing = models.CharField(max_length=200, null=True, blank=True, verbose_name='Grazing system and pasture management.')
	disease = models.CharField(max_length=100, null=True, blank=True,verbose_name='Disease control.')
	farm = models.CharField(max_length=100, null=True, blank=True, verbose_name='Farm biosecurity')
	culling_selection = models.CharField(max_length=100, null=True,blank=True, verbose_name='Culling and Selection.')
	by_veterinary_officer = models.CharField(max_length=20, choices=YES_NO_CHOICES, default='Y',verbose_name='Is the farm manged by a veterinary officer or livestock officer?')
	if_no = models.CharField(max_length=100, null=True,blank=True, verbose_name='If no,who is the farm consultant?')
	name_incharge = models.CharField(max_length=100, null=True, blank=True,verbose_name='Name of the veterinary officer incharge.')
	reg_number = models.CharField(max_length=100, null=True, blank=True,verbose_name='Registration number.')
	comment = models.CharField(max_length=100, null=True, blank=True)

	def __str__(self):
		return f'Name of form: farm consultation'





