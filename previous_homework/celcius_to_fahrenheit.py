
# celcius_to_fahrenheit

def celsius_to_fahrenheit(celsius_temp):
    return ((9/5)*celsius_temp) + 32


celsius_input = int(input("Enter your Celsius temperature: "))

print(celsius_input, "degree celsius is equivalent to ", celsius_to_fahrenheit(celsius_input),"fahrenheit degree")