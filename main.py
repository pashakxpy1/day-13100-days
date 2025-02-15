# L-13
# ---------------------------------
#  to type in 
# - the name of a test, 
# - maximum score they could receive,  
# - how many points they received
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

test_name=input("Enter the name of the test: ")
max_score=int(input("Enter the maximum score: "))
score=int(input("Enter the score received: : "))

percentage=round(score/max_score*100,2)

#if percentage>=90:
#  print("You are got an A+")

if final_number >= .90:
  print("Your letter score is an A+")
elif final_number >= .80 and final_number <= .89:
  print("Your letter grade is an A-.")
elif final_number >= .70 and final_number <= .79:
  print("Your letter score is a B.")
elif final_number >= .60 and final_number <= .69:
  print("Your letter grade is a C.")
elif final_number >= .50 and final_number <= .59:
  print("Your letter grade is a D.")
elif final_number <= .49:
  print("Your letter grade is a U.")
else: 
  print("Try again!")
  

