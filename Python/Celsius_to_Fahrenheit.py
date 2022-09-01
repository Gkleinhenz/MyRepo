#num1 = 32 input ("Celsius to Fahrenheit ")
#num2 = 0 input ("Fahrenheit to celsius ") 

#num1 = ("Zero degrees celsius = 32 degress Farenheit ")

#if num1 < num2:
    #print("Cesius = 0, Fahrenheit = 32 ")

'''

#Choice = input("Press 1 for Celsius to fahrenheit or Press 2 for fahrenheit to Celsius ")

#if Choice == 1:
    #Celsius = input("What is the temperature in Celsius ")
    #Cmath = (Celsius * 9/5) + 32

    '''
   
    #Psydocode

## Get user input on what kind of conversion 
## If/Else to go between Fhight and Cles
## ROund to the conversion 
## Output to the user 
'''

## question is set equal to the input "Do you want to convert 1. 'F to C' or 2. 'C to F'" 
## if option 1
    #Covert F to C 
    #Output to the user calculation 

# else if option 2 
    # Convert C to F 
    # Output to user the calculation 
'''

question = input( "How would you like to convert:\n(1) from Fahrenheit to Celsius\n(2) from Celsius to Fahrenheit\nYour Choice: ")
print(question)
if question == "1": 
    Fahrenheit =float(input("What is the temperature in Fahrenheit "))
    Celsius = (Fahrenheit - 32) * 5/9
    print(str(Fahrenheit) + " degrees Fahrenheit convers to " + str(round(Celsius, 1)) + "degrees Celsius . ")


elif question == "2": 
    Celsius =float(input("What is the temperature in Celsius "))
    Fahrenheit = (Celsius * 1.8) + 32
print(str(Celsius) + " degrees Celsius convers to " + str(round(Fahrenheit, 1)) + "degrees Fahrenheit . ")