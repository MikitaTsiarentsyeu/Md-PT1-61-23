number = int(input('Enter the number: '))
degree = int(input('Enter degree')) 

def get_degree_number(number, degree):
    if degree == 1:
        return number
    if degree != 1:
        return number * get_degree_number(number, degree - 1)

print(get_degree_number(number, degree))