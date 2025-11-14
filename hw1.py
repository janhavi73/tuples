def generate_odd_numbers_list_simple():

    limit = int(input("Enter an integer: "))

    odd_numbers = [num for num in range(limit) if num % 2 != 0]
    return odd_numbers
def capitalize_fruits_list(fruits_list):
 
    capitalized_fruits = [fruit.capitalize() for fruit in fruits_list]
    return capitalized_fruits




