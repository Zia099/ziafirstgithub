# applicant_age=4
# required_age_at_school=5

# # question: Is hammad eligible for school admission

# if applicant_age==required_age_at_school:
#     print("Congratulation! Applicant eligible")
# elif applicant_age>required_age_at_school:
#     print("Not eligible, Recomended to join high school")
# elif applicant_age<=3:
#     print("not eligible, still baby")
# else:
#     print("Not eligible")

# # use input function to ask the age from user user 
""" required_age_at_school=5
applicant_age=input("what is the age of the applicant? ")
applicant_age=int(applicant_age) """

# # question: Is hammad eligible for school admission

""" if applicant_age==required_age_at_school:
     print("Congratulation! Applicant eligible")
elif applicant_age>=6:
     print("Not eligible, Recomended to join high school")
elif applicant_age<=3:
     print("not eligible, still baby")
else:
     print("Not eligible") """

#Practice
required_age_at_school=5
age_of_applicant=input("What is the age of applicant? ")
age_of_applicant=int(age_of_applicant)
if age_of_applicant==required_age_at_school:
    print("congratulation! You are eligible")
elif age_of_applicant>=8:
    print("Recomended to higher school")
elif age_of_applicant<=3:
    print("Still baby")
else:
    print("Not eligible")