students = {}

number = input('Number: ')
name = input('Name: ')
surname = input('Surname: ')
telephone = input('Telephone :')

students.update({
    number: {
        'Name' : name ,
        'Surname' : surname ,
        'Telephone' : telephone 
    }
})

number = input('Number: ')
name = input('Name: ')
surname = input('Surname: ')
telephone = input('Telephone :')

students.update({
    number: {
        'Name' : name ,
        'Surname' : surname ,
        'Telephone' : telephone 
    }
})


number = input('Number: ')
name = input('Name: ')
surname = input('Surname: ')
telephone = input('Telephone :')

students.update({
    number: {
        'Name' : name ,
        'Surname' : surname ,
        'Telephone' : telephone 
    }
})

print('*' * 100)

stdnumber = input('Which number you want to check? :')

print(f"Number you check is {stdnumber}, name of the student {students[stdnumber]['Name']}, surname of the student {students[stdnumber]['Surname']}, telephone number of the student {students[stdnumber]['Telephone']}.")
