

print("This is a program that calculates a child's 'Body Mass Index' based on gender,\nage, weight and height.")

print("Based on a child's BMI, we are able to determine within which national percentile range\nthe child falls and their respective 'Weight Status Category.'")

##print("Weight Status Categories are defined as either 'Underweight', 'Normal',\n'Healthy Weight', 'Overweight', or 'Obese'.")

    
    
##age = input("Please enter the child's age (2-5): ")
##
##weight = input("Please enter the child's weight in lbs: ")
##
##height = float(input("Please enter the child's height in ft: ")
##
    

while True:
    
    def convert_to_inches(ft):
        '''(number) -> number
        Converts feet to inches.
        >>> convert_to_inches(6)
        72
        >>> convert_to_inches(5)
        60
        '''
        child_in = ft * 12
        return child_in

##        child_ht = convert_to_inches(float(input("Please enter the child's height in ft: ")))
    
    def child_gender(gender):
##        gender = child_gender(input("Please enter the child's gender (1 for Male or 2 for Female): "))
        if gender == '1':
            s = 1
        elif gender == '2':
            s = 2
        else:
            print("Please enter 1 for Male or 2 for Female: ")
            
 
    
    def body_mass_index(height, weight):
        '''(number, number) -> number

        Precondition: height is in inches and weight is in lbs.
        Returns the BMI based on height and weight.
    
        >>> body_mass_index(36, 28)
        15.18827160493827
        >>> body_mass_index(32, 34)
           23.341796875
           '''
        return ((weight / height ** 2) * 703)
    
    child_age = int(input("Please enter the child's age 2-5 (whole years only): ")
    child_ht = convert_to_inches(float(input("Please enter the child's height in ft: ")))
    child_weight = input("Please enter the child's weight in pounds (lbs): ")
    gender = child_gender(input("Please enter the child's gender (1 for Male or 2 for Female): "))

    bmi = body_mass_index(child_ht, child_weight)
    a = child_age

    print("Your child's bmi is ", bmi,")

## Health Status Male (2-5 yo)
          
    if bmi < 14.7 and a == 2 and s == 1:
          print("Your child is UNDERWEIGHT for their sex and age.")
          print("UNDERWEIGHT children are more likely to face health problems.")
          print("Please see a doctor or seek medical advice.")
    elif 14.7 <= bmi < 18.2 and a == 2 and s == 1:
          print("Your child is NORMAL or HEALTHY WEIGHT for their sex and age.")
          print("Children who are NORMAL or HEALTY WEIGHT are less likely to face health problems.")
          print("However, do NOT neglect to take your child to their doctor regulary.")
    elif 18.2 <= bmi < 19.3 and a == 2 and s == 1:
          print("Your child is OVERWEIGHT for their sex and age.")
          print("Children who are OVERWEIGHT are more likely to face health problems.")
          print("Please see a doctor or seek medical advice.")
    elif bmi >= 19.3 and a == 2 and s == 1:
          print("Your child is OBESE for their sex and age.")
          print("Children who are OBESE are more likely to face health problems.")
          print("Please see a doctor or seek medical advice.")
    elif bmi < 14.4 and a == 3 and s == 1
          print("Your child is UNDERWEIGHT for their sex and age.")
          print("UNDERWEIGHT children are more likely to face health problems.")
          print("Please see a doctor or seek medical advice.")
    elif 14.4 <= bmi < 17.4 and a == 3 and s == 1:
          print("Your child is NORMAL or HEALTHY WEIGHT for their sex and age.")
          print("Children who are NORMAL or HEALTY WEIGHT are less likely to face health problems.")
          print("However, do NOT neglect to take your child to their doctor regulary.")
    elif 17.4 <= bmi < 18.3 and a == 3 and s == 1:
          print("Your child is OVERWEIGHT for their sex and age.")
          print("Children who are OVERWEIGHT are more likely to face health problems.")
          print("Please see a doctor or seek medical advice.")
    elif bmi >= 18.3 and a == 3 and s == 1:
          print("Your child is OBESE for their sex and age.")
          print("Children who are OBESE are more likely to face health problems.")
          print("Please see a doctor or seek medical advice.")
    elif bmi < 14.1 and a == 4 and s == 1:
          print("Your child is UNDERWEIGHT for their sex and age.")
          print("UNDERWEIGHT children are more likely to face health problems.")
          print("Please see a doctor or seek medical advice.")
    elif 14.1 <= bmi < 16.9 and a == 4 and s == 1:
          print("Your child is NORMAL or HEALTHY WEIGHT for their sex and age.")
          print("Children who are NORMAL or HEALTY WEIGHT are less likely to face health problems.")
          print("However, do NOT neglect to take your child to their doctor regulary.")
    elif 16.9 <= bmi < 17.8 and a == 4 and s == 1:
          print("Your child is OVERWEIGHT for their sex and age.")
          print("Children who are OVERWEIGHT are more likely to face health problems.")
          print("Please see a doctor or seek medical advice.")
    elif bmi >= 17.8 and a == 4 and s == 1:
          print("Your child is OBESE for their sex and age.")
          print("Children who are OBESE are more likely to face health problems.")
          print("Please see a doctor or seek medical advice.")
    elif bmi < 13.9 and a == 5 and s == 1:
          print("Your child is UNDERWEIGHT for their sex and age.")
          print("UNDERWEIGHT children are more likely to face health problems.")
          print("Please see a doctor or seek medical advice.")
    elif 13.9 <= bmi < 16.8 and a == 5 and s == 1:
          print("Your child is NORMAL or HEALTHY WEIGHT for their sex and age.")
          print("Children who are NORMAL or HEALTY WEIGHT are less likely to face health problems.")
          print("However, do NOT neglect to take your child to their doctor regulary.")
    elif 16.8 <= bmi < 17.9 and a == 5 and s == 1:
          print("Your child is OVERWEIGHT for their sex and age.")
          print("Children who are OVERWEIGHT are more likely to face health problems.")
          print("Please see a doctor or seek medical advice.")
    elif bmi >= 17.9 and a == 5 and s == 1:
          print("Your child is OBESE for their sex and age.")
          print("Children who are OBESE are more likely to face health problems.")
          print("Please see a doctor or seek medical advice.")
          
          
    

          

          

          
          

    
