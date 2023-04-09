workout_split = input("Enter your preferred workout split (3 day, 4 day or 6 day): ")
exercise_type = input("Do you want to do bodyweight exercises or go to the gym? ")

if workout_split == "3 day" or workout_split == "3":
    print("You have chosen a 3 day workout split.")
elif workout_split == "4 day" or workout_split == "4":
    print("You have chosen a 4 day workout split.")
elif workout_split == "5 day" or workout_split == "5":
    print("You have chosen a 5 day workout split.")
elif workout_split == "6 day" or workout_split == "6":
    print("You have chosen a 6 day workout split.")
else:
    print("Invalid workout split entered. Please choose from 3 day, 4 day or 6 day.")

if exercise_type == "bodyweight":
    print("You have chosen to do bodyweight exercises.")
    print("Do the following exercises: \n "
          "1. Push ups \n "
          "2. Dips \n "
          "3. Pull ups \n "
          "4. Squats \n "
          "5. Lunges \n"
          "6. Wide grip push ups \n"
          "7. Pike push ups \n"
          "8. Calves raises \n")
elif exercise_type == "gym" and (workout_split == "6 day" or workout_split == "6") :
    print("You have chosen to go to the gym for 6 days a week. \n "
          """workout plan (Push Pull Legs x Arnold Split)
6 day split
Day 1: Push Day
10min stretching
2x10 bodyweight push ups
1 warmup set with light weights bench press
5x 5-8 reps barbell bench press
5x 5-8 reps inclined barbell bench press
4x10-15 reps cable/pec dec machine chest flies
5x 10-15 reps lateral raises cable/dumbell
5 x 10-15 reps triceps extensions cable/dumbell
5x 10-15 reps cable triceps push downs

Day 2: Pull Day

10min stretching
1 warmup set with light weights lat pulldowns
3xfailure bodyweight pull ups
5x 8-12 reps lat pulldowns
5x8-12 reps chest supported rows/cable rows/barbell rows/dumbell rows
3x10-15 reps trap shrugs
3x10-15 stiff arm pulldowns
4x10-15 reps cable/dumbell bicep curls
4x 10-15 reps seated inclined bicep curls
4x10-15  reps reverse pec dec rear delt flies
3x10 sets forearm curls
3x10 sets reverse forearm curls

Day 3: Legs

10min stretching
2x10 bodyweight squats
2 warmup sets with light weights squats
4x8-10 reps barbell squats
4x8-10 hacksquats/ smith machine squats/lunges
4x10-15 legs extensions
4x10-15 hamstring curls
4x10-15 calves raises
4x8-12 overhead press(front delts)

Day 4: Chest + back
10min stretching
2x10 bodyweight push ups
1 warmup set with light weights bench press
1 warmup set with light weights lat pulldowns
5x 5-8 reps barbell bench press
5x 8-12 reps lat pulldowns
5x 5-8 reps inclined barbell bench press
5x8-12 reps chest supported rows/cable rows/barbell rows/dumbell rows
4x10-15 reps cable/pec dec machine chest flies
3x10-15 stiff arm pulldowns
3x10-15 reps trap shrugs
 
Day 5: Arms and delts
10min stretching
4x8-12 overhead press(front delts)
4x10-15 reps cable/dumbell bicep curls
5x 10-15 reps lateral raises cable/dumbell
5 x 10-15 reps triceps extensions cable/dumbell
4x10-15  reps reverse pec dec rear delt flies
4x 10-15 reps seated inclined bicep curls
5x 10-15 reps cable triceps push downs
3x10 sets forearm curls
3x10 sets reverse forearm curls

Day 6: Legs

10min stretching
2x10 bodyweight squats
2 warmup sets with light weights squats
4x8-10 reps barbell squats
4x8-10 hacksquats/ smith machine squats/lunges
4x10-15 legs extensions
4x10-15 hamstring curls
4x10-15 calves raises
3x10-15 cable abs crunches
3x10-15 lying leg raises""")
elif exercise_type == "gym" and (workout_split == "4 day" or workout_split == "4"):
    print("You have chosen to go to the gym for 4 days a week. \n "
          """workout plan 2:
4 day split(Upper/Lower)
Day 1: Upper Body
10min stretching
2x10 bodyweight push ups
1 warmup set with light weights bench press
1 warmup set with light weights lat pulldowns
5x 5-8 reps barbell bench press
5x 8-12 reps lat pulldowns
5x 5-8 reps inclined barbell bench press
5x8-12 reps chest supported rows/cable rows/barbell rows/dumbell rows
4x10-15 reps cable/pec dec machine chest flies
3x10-15 reps cable/dumbell bicep curls
3x10-15 reps triceps extensions cable/dumbell
3x10-15 reps seated inclined bicep curls
3x 10-15 reps cable triceps push downs

Day 2: Lower Body
10min stretching
2x10 bodyweight squats
2 warmup sets with light weights squats
4x8-10 reps barbell squats
4x8-10 hacksquats/ smith machine squats/lunges
4x10-15 legs extensions
4x10-15 hamstring curls
4x10-15 calves raises
3x10-15 cable abs crunches
3x10-15 lying leg raises

Day 3: Upper body
Day 4: Lower body""")
elif exercise_type == "gym" and (workout_split == "3 day" or workout_split == "3"):
    print("You have chosen to go to the gym for 3 days a week. \n "
          """Workout A
Squats: 3×6-8
Bench Press: 3×6-8
Pull-Ups or Lat Pull-Downs: 3×8-10
Shoulder Press: 3×8-10
Leg Curls: 3×8-10
Biceps Curls: 3×10-15
Face Pulls: 3×10-15
Workout B
Romanian Deadlift: 3×6-8
Seated Cable Rows: 3×6-8
Incline Dumbbell Press: 3×8-10
Leg Press or Split Squats: 3×10-12
Lateral Raises: 3×10-15
Triceps Pushdowns: 3×10-15
Standing Calf Raises: 4×6-10""")
else:
    print("Invalid exercise type entered. Please choose from bodyweight or gym.")