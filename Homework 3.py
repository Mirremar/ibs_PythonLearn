from test.test_long import truediv

numbers = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]

def noteven(x):
    return (x%2!=0) and (x>50)

print(list(filter(noteven,numbers)))