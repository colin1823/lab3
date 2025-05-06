def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight/(height**2)
    return bmi
   
def classify_bmi(bmi_value):
    if(bmi_value < 18.5 ):
        print("UNDERWEIGHT!")
        return -1
    if(bmi_value >= 18.5 and bmi_value <=25.0):
        print("normal weight")
        return 0
    else: 
        print("OVERWEIGHT")
        return 1



def main ():
    bmi_output = calculate_bmi(1.8,90)
    print("bmi_value:" +str(bmi_output))
    classify_bmi(bmi_output)

if __name__ == "__main__":
    main()
    