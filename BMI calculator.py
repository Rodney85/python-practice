#Tracking your BMI is a useful way of checking if you’re maintaining a healthy weight. It’s calculated using a person's weight and height, using this formula: 

#>>weight / height²

#Underweight = less than 18.5
#Normal = more or equal to 18.5 and less than 25
#Overweight = more or equal to 25 and less than 30
#Obesity = 30 or more

x = float(input("What is your weight\n"))
y = float(input("What is your height\n"))

total=x/(y**2)

if total >= 0 and total <=18.5:
   print("Underweight")
elif total >=18.5 and total <=25:
   print("Normal")
elif total >=25 and total <=30:
   print("Overweight")
elif total >=30:
   print("Obesity")