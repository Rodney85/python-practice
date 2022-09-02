#ask for the name
#remove whitespace from str and capitalized 

name = input("> What is your Full Name??\n").strip().title()

#split to 1st and last name
first , Last = name.split(" ") 

#say hello to user
print("•‿• Hello," + first + "\n>>That's a Cute Name your know")

#know how there day is 

print("◠‿• So,How is your day?" + first)
x=int(input("On a scale of 1 to 5?\n"))

#if 1$2 its bad how can i cheer you up
if x<=2:
 print("Damn, seems you have had a bad day.I can try cheering you up\n ")

#if 3 seems you had a good and bad day
elif x==3:
 print("Seems like a mixed day.\n")

#if 4$5 had a great day tell me about it

elif x==4:
  print("seems like a good day atleast.\n")

elif x<=5:
 print ("Sheeeesh some seems to have a Fucking great day.\n")
