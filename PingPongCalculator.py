# PingPongCalculator.py
# Billy Ridgeway
# Calculates your height and weight in Ping Pong balls.

def convert_in2cm(inches):  # Defines the function to convert inches to centimeters.
    return inches * 2.54
def convert_lb2kg(pounds):  # Defines the function to convert pounds to kilograms.
    return pounds / 2.2

height_in = int(input("Enter your height in inches: "))
weight_lb = int(input("Enter your weight in pounds: "))

height_cm = convert_in2cm(height_in)
weight_kg = convert_lb2kg(weight_lb)

ping_pong_tall = round(height_cm / 4)           # Converts your height from centimeters to Ping Pong balls.
ping_pong_heavy = round(weight_kg * 1000 / 2.7) # Converts your weight from kilograms to Ping Pong balls.

feet = height_in // 12  # Finds the quotient.
inch = height_in % 12   # Finds the remainder.

print("At", feet, "feet", inch, "inches tall, and", weight_lb,
      "pounds,")
print("you measure", ping_pong_tall, "Ping-Pong balls tall, and ")
print("you weigh the same as", ping_pong_heavy, "Ping-Pong balls!")
