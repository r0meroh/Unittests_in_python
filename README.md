# Unittests_in_python
Small program that includes pythonic implementations of classes, objects, inheratince, and unittests.


![directory](https://github.com/r0meroh/Unittests_in_python/blob/master/images/directory.png)


The names.py is the object class that includes only a first name and a last name.
Name class includes a fillin function to return variables for logical operations. Also 
the __str__ function returns the formatted string when a name object is printed instead of the default
object's bytecode.


![names](https://github.com/r0meroh/Unittests_in_python/blob/master/images/name_class.png)


loops.py includes a function loop that utilizes names.py to create name objects and name them 
independantly for later purposes if need be. This is important because normally, unless modified,
objects created in loops are unnamed and generic making it difficut to access created objects after
the loop is completed.
The object variables are stored within independent lists that run in parallel.


![loop](https://github.com/r0meroh/Unittests_in_python/blob/master/images/original_loop.png)



Inherited from names.py is name_with_middle which inludes the addition of a middle name.


![name_with_middle](https://github.com/r0meroh/Unittests_in_python/blob/master/images/inherited_name.png)


Other additions to the names_with_middle is the fillin function and __str__ functions.


![additions](https://github.com/r0meroh/Unittests_in_python/blob/master/images/inherited_return.png)


loop_with_middle is a modified instance of the original loop() to accommodate the additional functionality 
of the name_with_middle object.


![loop_with_middle](https://github.com/r0meroh/Unittests_in_python/blob/master/images/loop_with_middle.png)


format_a_name.py takes in both types of objects and returns a formatted string to be printed out. This
is accomplished by making two of the arguments in the function parameters be empty default strings.


![format](https://github.com/r0meroh/Unittests_in_python/blob/master/images/format_a_name.png)


The main class handles both types of objects differently. For the names.py class it uses polymorphism 
to create a dictionary of first names as keys and last names as values. 
For the names_with_middle , all three parallel lists are passed into the function.


![main](https://github.com/r0meroh/Unittests_in_python/blob/master/images/main_class.png)


finally, we test both objects using unittests.


![test](https://github.com/r0meroh/Unittests_in_python/blob/master/images/test_class.png)

