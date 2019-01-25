def age_calc(year_of_birth):
    age = 2019 - year_of_birth
    #return age

    if age < 18:
        print("You are a minor")
    elif age < 35:
        print("You are a youth and you are {}".format(age))
    else:
        print("You are an elder with {} years".format(age))
    

year_of_birth = int(input("Please enter your year of birth: ")) 
age_calc(year_of_birth)
