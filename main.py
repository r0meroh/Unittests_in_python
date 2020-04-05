from function_loops import *
from names import Names
from format_a_name import *
from format_name_with_middle import *


def main():
    """
    Main function calls the loop function that creates name objects
    the names class. It then takes the two lists that are created
    and assigns them into a dictionary that is utilized by the
    create_a_name file that returns the formatted names onto the
    console.
    """
    f_names, l_names = loop()

    name_dict = {f_names[i]: l_names[i] for i in range(len(f_names))}

    for fir, las in name_dict.items():
        print(format_name(fir, las))

    print("Let's include names with middle names now")

    f_names, m_names, l_names = loop_with_middle()

    for x in range(len(f_names)):
        print(format_name(f_names[x], m_names[x], l_names[x]))


if __name__ == "__main__":
    main()
