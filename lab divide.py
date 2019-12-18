number_of_pcs_in_lab = 24

try:
    number_of_students = int (input ('Enter the number of students: '))

    if number_of_students < 0:
        print ('Error: A positive number of students is required')
    else:
        number_of_labs = number_of_students // number_of_pcs_in_lab

        if number_of_students % number_of_pcs_in_lab != 0:
            number_of_labs += 1

        if number_of_labs == 1:
            print (number_of_labs, 'is required to hold this many students')
        else:
            print (number_of_labs, 'is required to hold this many students')

except ValueError:
    print ('Please enter a valid number.')