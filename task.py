while True:
    try:
        a = int(input('Enter even number: '))
        if a % 2 == 1: raise ValueError('You entered an odd number: ')
        else: break
    except ValueError as ve:
        print(ve)