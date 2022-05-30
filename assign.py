# Write a function that accepts any number of integers as positional arguments
#  and any number of a student's attributes as keyword arguments 
#  and prints the result of multiplying all of the integers with a customized greeting 
#  based on the keyword arguments. Name the function multiply_and_greet.
def multiply_and_greet(*age,**kwargs):
    keys = kwargs.keys()
    if "country"and "age" and "name" in keys:
        print(f"Hello {kwargs['name']} you were born in {kwargs['year']} from {kwargs['country']}")
    elif "country" "age" and "name" in keys:
        print(f"Hello {kwargs['name']} from {kwargs['country']}")
    elif "age" in keys:
        print(f"Hello {kwargs['name']} you were born in {kwargs['year']}")
    elif "name" in keys:
        print(f"Hello {kwargs['name']}")
    else:
        print(f"Hello Anonymous")
        # multiply_and_greet(name = "Joel", age = 24, country = "Mozambique") 
