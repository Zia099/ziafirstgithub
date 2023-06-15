#logical operators are either "true or false" or "yes or no" or "0 or 1"
# equal to                     ==
# not equal to                 !=
# less than                    <
# greater than                 >
# less than and equal to       <=
# greater than and equal to    >= 

#  Is 4 equal to 4?
print (4==4)
print (4!=4)
print (4>3)
print (3<4)
print (3>6)
print (3<=5)
print (5>=4)

# application of logical operators
hammad_age=6
age_at_school=5
print(hammad_age>=age_at_school)

# input function and logical operator
age_at_school=5
applicant_age = input ("what is the age of applicant? ") # input function is used for asking some infomation
# from user.
print(type(applicant_age))
applicant_age=int(applicant_age)
print(type(applicant_age))
print(applicant_age==age_at_school) #logical operator