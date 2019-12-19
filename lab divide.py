pcs_in_lab = 24

try:
    number_of_students = int (input ('Enter the amount of students: '))

    if number_of_students < 0:
        print ('Error: please input a positive number of students')
    else:
        number_of_labs = number_of_students // pcs_in_lab

        if number_of_students % pcs_in_lab != 0:
            number_of_labs += 1

        if number_of_labs == 1:
            print ('you need ' + number_of_labs.__str__() + ' lab to hold this many students')
        else:
            print ('you need ' + number_of_labs.__str__() +  ' labs to hold this many students')

except ValueError:
    print ('Please enter a valid number.')