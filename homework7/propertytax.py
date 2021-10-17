
def assessment(propertyValue):
    return (propertyValue * 60) / 100

def property_tax(assessment_amount):
    return (assessment_amount / 100) * .72

def main():
    property_value_amount = int(input("please enter your property value "))

    assessment_value = assessment(property_value_amount)

    output = ""
    output += "Assessment value: " + str(assessment_value) + "\n"
    output += "property tax: " + format(property_tax(assessment_value), '.2f')
    output += "."

    print(output)


main()
