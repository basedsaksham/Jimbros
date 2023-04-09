import matplotlib.pyplot as plt

# Get input from the user for 7 days of calorie and macro intake
days = ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5', 'Day 6', 'Day 7']
calories = []
protein = []
carbs = []
fat = []
for day in days:
    print(f"Enter calorie and macro intake for {day}:")
    c = int(input("Calories: "))
    p = int(input("Protein: "))
    cr = int(input("Carbs: "))
    f = int(input("Fat: "))
    calories.append(c)
    protein.append(p)
    carbs.append(cr)
    fat.append(f)

# Create a bar graph for calorie intake
plt.bar(days, calories, color=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
plt.xlabel('Days of the Week')
plt.ylabel('Calories')
plt.title('Calorie Intake for the Week')
plt.show()

# Create a pie chart for macro intake
macro_labels = ['Protein', 'Carbs', 'Fat']
macro_colors = ['red', 'yellow', 'green']
macro_data = [sum(protein), sum(carbs), sum(fat)]
plt.pie(macro_data, labels=macro_labels, colors=macro_colors, autopct='%1.1f%%')
plt.title('Macro Intake for the Week')
plt.show()
