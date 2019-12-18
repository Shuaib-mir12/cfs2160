
try:
    number_of_pupils = int (input ('Enter amount of pupils: '))

    if number_of_pupils < 0:
        print ('Error: a positive number of pupils must be required.')
    else:

        number_of_sweets = int(input('Enter the amount of sweets: '))

        if number_of_sweets < 0:
            print('Error: a positive amount of sweets is required')
        else:

            sweets_per_student  = number_of_sweets // number_of_pupils
            if sweets_per_student == 1:
                print ('Each student receives ', sweets_per_student, 'sweet.')
            else:
                print ('Each student receives ', sweets_per_student, 'sweets')
except ValueError:
    print ('Please enter an valid number.')