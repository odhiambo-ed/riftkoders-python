print("-----------------------------------------------------------")
print("-----------------------------------------------------------")
print("I am a calculator. Use me to calculate your math problems.")
print("-----------------------------------------------------------")
print("-----------------------------------------------------------" + "\n")

answer_one = input("What is your first number? ")
answer_two = input("What is your second number? ")
answer_three = input("What is your operator of choice? ")

if answer_three == "+":
  print(int(answer_one) + int(answer_two))
  print("-----------------------------------------------------------")
elif answer_three == "-":
  print(int(answer_one) - int(answer_two))
  print("-----------------------------------------------------------")
elif answer_three == "*":
  print(int(answer_one) * int(answer_two))
  print("-----------------------------------------------------------")
elif answer_three == "/":
  print(int(answer_one) / int(answer_two))
  print("-----------------------------------------------------------")
else:
  print("Invalid operator")
  print("-----------------------------------------------------------")