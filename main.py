# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
print("Leap year checker!")
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("It is a leap Year!")
    else:
      print("Not a leap year")
  else:
    print("It is a leap year!")
else:
  print("It is not a leap year!")

  

