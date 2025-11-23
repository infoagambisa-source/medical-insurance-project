# -------------------------
# Medical Insurance Project
# -------------------------

# Create the initial variables below
# Variables represent the individual's characteristics
age = 28                # Age in years
sex = 0                 # 0 = female, 1 = male
bmi = 26.2              # Body Mass Index
num_of_children = 3     # Number of children
smoker = 0              # 0 = non-smoker, 1 = smoker

# Add insurance estimate formula below
# Formula estimates the yearly insurance cost based on the factors
insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
print("This person's insurance cost is " + str(insurance_cost) + " dollars.")

# -------------------------
# Age Factor
# -------------------------
# Investigate how increasing age affects insurance cost
age += 4
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in cost of insurance after increasing the age by 4 years is " + str(change_in_insurance_cost) + " dollars.")

# -------------------------
# BMI Factor
# -------------------------
# Reset age to original value
age = 28
# Investigate how increasing BMI affects insurance cost
bmi += 3.1
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in cost of insurance after increasing BMI by 3.1 is " + str(change_in_insurance_cost) + " dollars.")

# -------------------------
# Male vs. Female Factor
# -------------------------
# Reset BMI to original value
bmi = 26.2
# Change sex to male and calculate new insurance cost
sex = 1
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in estimated cost for being male instead of female is " + str(change_in_insurance_cost) + " dollars.")

# -------------------------
# Children Factor (Extra Practice)
# -------------------------
# Reset sex to female
sex = 0
# Investigate how increasing the number of children affects insurance cost
num_of_children += 2
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in cost of insurance after increasing the number of children by 2 is " + str(change_in_insurance_cost) + " dollars.")

# -------------------------
# Smoker vs. Non-Smoker Factor (Extra Practice)
# -------------------------
# Reset number of children to original value
num_of_children = 3
# Change smoker status to 1 (smoker) and calculate new insurance cost
smoker = 1
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in estimated cost for being a smoker instead of non-smoker is " + str(change_in_insurance_cost) + " dollars.")
