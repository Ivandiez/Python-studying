import sys # system with so many items

def hello(name):
    if name == 'Ivan' or name == 'Alena':
        print('Alert, Ivan mode')
        name = name + '???'
    else:
        DoesNotExist(name)
    name = name + '!!!!!'
    print('Hello', name)


# define a main() function that prints the greeting
def main():
    hello(sys.argv[1])


# This is the standard boilerplate that calls the main function
if __name__ == '__main__':
    main()
