from names import Names


def loop():
    """
    The loop function takes in answers to prompts from the user and
    individually creates name objects named after the first name of the
    names object.
    """
    print('Press "xx" at anytime to quit')

    input_from_user = input('Enter a first name\n')

    """
    The variables for the name object are separately stored in individual
    lists named accordingly.
    """
    first_names = []
    last_names = []

    while (input_from_user != 'xx'):
        input_from_user1 = input_from_user
        input_from_user1 = Names()
        input_from_user1.first = input_from_user
        first_names.append(input_from_user)
        input_from_user = input('enter a last name\n')
        input_from_user1.last = input_from_user
        last_names.append(input_from_user)
        print(input_from_user1)
        input_from_user = input('Enter a first name\n')

    return first_names, last_names


def loop_with_middle():
    """
    This is the same function as 'loop' but it includes the added
    implementation for a middle name. This prevents us of the previous
    methodology of using a dictionary with first names as keys and
    last names as values.
    """
    first_names = []
    middle_names = []
    last_names = []

    print('Press "xx" at anytime to quit')

    input_from_user = input('Enter a first name\n')

    while (input_from_user != 'xx'):
        input_from_user1 = input_from_user
        input_from_user1 = Names()

        input_from_user1.first = input_from_user
        first_names.append(input_from_user)
        input_from_user = input('Enter a middle name, press enter'
                                ' if none exist:\n')
        middle_names.append(input_from_user)
        input_from_user = input('enter a last name\n')
        input_from_user1.last = input_from_user
        last_names.append(input_from_user)
        print(input_from_user1)
        input_from_user = input('Enter a first name\n')

    return first_names, middle_names, last_names
