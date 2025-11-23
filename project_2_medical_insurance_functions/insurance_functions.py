# -------------------------------
# Medical Insurance Cost Functions
# -------------------------------

# Function to calculate insurance cost
def calculate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
    # Insurance formula
    estimated_cost = (
        250 * age
        - 128 * sex
        + 370 * bmi
        + 425 * num_of_children
        + 24000 * smoker
        - 12500
    )

    # Output message
    print(f"The estimated insurance cost for {name} is {estimated_cost} dollars.")
    return estimated_cost


# Function to calculate the difference between costs
def diff_insurance_cost(insurance_cost1, insurance_cost2):
    diff = insurance_cost1 - insurance_cost2
    print(f"The difference in insurance cost is {diff} dollars.")
    return diff


# ----------------------------------------
# Insurance cost calculations for examples
# ----------------------------------------

# Maria's insurance cost
maria_insurance_cost = calculate_insurance_cost(
    name="Maria",
    age=28,
    sex=0,
    bmi=26.2,
    num_of_children=3,
    smoker=0,
)

# Omar's insurance cost
omar_insurance_cost = calculate_insurance_cost(
    name="Omar",
    age=35,
    sex=1,
    bmi=22.2,
    num_of_children=0,
    smoker=1,
)

# Difference in costs
insurance_diff = diff_insurance_cost(maria_insurance_cost, omar_insurance_cost)
