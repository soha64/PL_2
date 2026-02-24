
from tempreature import C_to_F
from tempreature import C_to_K
from tempreature import F_to_C

print("Temperature Converter")
print("1. celcius to farenhite")
print("2. celcius to kelvin")
print("3. farenhite to celcius")

choice = int(input("Enter your choice: from 1 to 3 "))

if choice == 1:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = C_to_F.convert(celsius)
    print(f"{celsius}°C is equal to {fahrenheit}°F")        

elif choice == 2:
    celsius = float(input("Enter temperature in Celsius: "))
    kelvin = C_to_K.convert(celsius)
    print(f"{celsius}°C is equal to {kelvin} K")

elif choice == 3:
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = F_to_C.convert(fahrenheit)
    print(f"{fahrenheit}°F is equal to {celsius}°C")

else:
    print("Invalid choice.")

