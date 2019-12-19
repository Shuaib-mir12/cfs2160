
"""
  Calculate the area of a rectangle with given side measurements
"""
try:
    x_measurement = int (input ('Enter side X in CM: '))

    if x_measurement < 0:
        print ('Error: a positive measurement is required for side X.')
    else:
        y_measurement = int(input('Enter side Y in CM: '))

        rectangle_area = x_measurement * y_measurement

        print("Rectangle area is : " + rectangle_area.__str__() + "cm²")
except ValueError:
    print ('enter a valid number.')