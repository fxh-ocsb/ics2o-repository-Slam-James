# Samuel James
# Quiz1B  
# April 19, 2023
# Read a sentance about a birth year
import random

Birth_Year = int(input("What Year Were You Born:"))

print("Cool!", Birth_Year, "Was a pretty cool year!")

Random_Year = random.randint(2050, 2075)

Age = Random_Year - Birth_Year

print("Did you know that in", Random_Year, "you will be:", Age, "Years Old!!!")