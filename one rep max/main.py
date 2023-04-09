# Define the weight lifted and number of reps performed
weight_lifted = float(input("Enter the weight lifted: "))
reps_performed = int(input("Enter the number of reps performed: "))

# Calculate one rep max using the Epley formula
one_rep_max = weight_lifted * (1 + (reps_performed / 30))

# Print the result
print("Your estimated one rep max is: {:.2f} kgs "
      "*Caution: The predictions might vary from real life results, so always take the necessary precautions before "
      "attempting your 1RP*".format(one_rep_max))
print("Calorie Burn Calculator for Cardio Workout")

# Get user inputs
duration = float(input("Enter the duration of your workout in minutes: "))
intensity = float(input("Enter the intensity level of your workout (1-10): "))
weight = float(input("Enter your weight in kilograms: "))

# Calculate calories burnt
MET = 4.0 + 0.1 * intensity
calories_burnt = MET * weight * (duration / 60)

# Display results
print("Calories burnt:", round(calories_burnt, 2))
