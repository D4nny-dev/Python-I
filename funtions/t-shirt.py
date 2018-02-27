def make_shirt_1 (size,message):
    """Summarize the shirt that's going to be made."""
    print("\nI'm going to make a " + size + " t-shirt.")
    print('It will say, "' + message + '"')

make_shirt_1("large","I love Python!")
make_shirt_1(size="medium",message="I love Python!")


def make_shirt_2(message,size='large'):
    print("\nI'm going to make a " + size + " t-shirt.")
    print('It will say, "' + message + '"')

make_shirt_2(message='Bazinga!')
make_shirt_2(size='medium',message='Bazinga!')
make_shirt_2('small', 'Programmers are loopy.')


def make_shirt_3(size='large', message='I love Python!'):
    print("\nI'm going to make a " + size + " t-shirt.")
    print('It will say, "' + message + '"')

make_shirt_3()
make_shirt_3(size='medium')
make_shirt_3('small', 'Programmers are loopy.')


    