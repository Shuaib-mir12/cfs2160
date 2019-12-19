
try:
    number_of_pupils = int (input ('Enter amount of pupils: '))

    if number_of_pupils < 0:
        print ('Error: a positive amount of students must be entered.')
    else:

        number_of_sweets = int(input('Enter the amount of sweets: '))

        if number_of_sweets < 0:
            print('Error: a positive amount of sweets must be entered')
        else:

            sweets_per_student  = number_of_sweets // number_of_pupils
            if sweets_per_student == 1:
                print ('Each student will receive ', sweets_per_student, 'sweet.')
            else:
                print ('Each student will receive ', sweets_per_student, 'sweets')
except ValueError:
    print ('Please enter a valid number.')