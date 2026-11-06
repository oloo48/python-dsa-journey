print("=" * 60)
print("   PART 1 sets ")
print("=" * 60)
#CREATING A SET
print("\n----1. CREATING  SETS----")
numbers_list = [1, 2, 2, 3,3, 3, 4, 4, 4, 5, 5, 5, 5]
print("List:", numbers_list)
numbers_set = set(numbers_list)
print("Original list:", numbers_list)
print("As a set :", numbers_set)
print("Duplicates are removed from a list when it's converted to a set.")
#Direct creation of a set using gcurly braces
fruits={"apple", "banana", "cherry", "apple", "banana"}
print("\nFruits set:", fruits)
print("Duplicates are removed from a set when it's created with  the curly braces(directly).")
empty_set=set()
print ("\nEmpty set:", empty_set)
print("\nIt's noticable that an empty set is created using the set() function rather than the curly braces {}. The curly braces are used to create an empty dictionary.")
print("\n----2. ADD & REMOVE OPERATIONS----")
colours=set()
colours.add("red")
colours.add("orange")
colours.add("yellow")
print("\nColours set:", colours)
colours.remove("red")
print("After removing 'red':", colours)
colours.add("red")
print("After adding 'red':", colours)
print("\n----It is noticeable that after adding red again, the set does not contain duplicate values. The set only contains unique values.----")
colours.remove("orange")
print("After removing 'orange':", colours)
#Safe remove,no error is raised if the item is not present in the set
colours.discard("purple")
print("After discarding 'purple':", colours)
print("after discarding 'purple', no error is raised even though 'purple' is not present in the set.")
print("\n-----3. Fast lookup(0(1))----") 
print("red in coulours:", "red" in colours)
print("purple in colours:", "purple" in colours)
print("\n-----4. SET OPERATIONS-----")
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print("\nSet A:", A)
print("Set B:", B)
print("\nUnion of A and B:", A | B)
print("Intersection of A and B:", A & B)
print("Difference of A and B:", A - B)
print("Symmetric difference of A and B:", A ^ B)
print("\n -----5.PRACTICE :REMOVE DUPLICATES FROM A LIST USING SETS------")
Emails=[
    "oloo@gmail.com",
    "omondi@gmail.com",
    "oloo@gmail.com",
    "willy@gmail.com"
]
print("Real world example: Removing duplicates from a list of emails using sets")
unique_emails = list(set(Emails))
print("Original list:", Emails)
print("Unique emails:", unique_emails)
print("\n-----it is notable that sets do not preserve order. For odered unique items, use the dictionaries instead")
unique_odered=list(dict.fromkeys(Emails))
print("Unique ordered emails:", unique_odered)

print("\n" + "=" * 60)
print("   PART 2: Tuples ")
print("\n-------CREATING TUPLES-------")
#CREATING TUPLES USING PARENTHESIS ()_ LIKE A LOCKED LIST
coordinates=(1.2921,36.8126)
print("Nairobi coordinates:",coordinates)
print("Type:", type(coordinates))
#We can create a tuple without using parenthesis as well
colors="red", "green", "blue"
person ="oloo48",21,"Kenya"
print("\nColors tuple:", colors)
print("Person tuple :",person)
#Even a single item tuple requiers a comma after the item to differentiate it from a regular variable
single_item_tuple=(5,)
print("\nSingle item tuple:", single_item_tuple)
# accessing tuple item using indexing
print("\n----accessing tuple items using indexing----")
print("First item in colors tuple:", colors[0]) 
print("Last item in colors tuple:", colors[-1])
print("\n----accessing tuple items using slicing----")
print("First two items in colors tuple:", colors[0:2])
print("Items from index 1 to 2 in colors tuple:", colors[1:3])
print("\n----3 . IMMUTABILITY OF TUPLES----")
print("Tuples are immutable, meaning that once they are created, their elements cannot be changed, added, or removed.")
print("Trying to change an item in a tuple will raise a TypeError. For example, attempting to change the first item in the colors tuple will result in an error:")
try:
    colors[0] = "yellow"
except TypeError as e:
    print("Error:", e)
    print("Tuples are locked lists, and their elements cannot be modified after creation. This immutability makes tuples useful for storing data that should not be changed, such as coordinates or fixed configurations.")
    print("\n-----4. Unpacking tuples-----")
    name, age, country = person
    print(f"Name: {name}, Age: {age}, Country: {country}")

    print("\n-----swapping values using tuples-----")
    a = 5
    b = 10
    print(f"Before swapping: a = {a}, b = {b}")
    a, b = b, a
    print(f"After swapping: a = {a}, b = {b}")
    print("\n-----5.Tuples as dictionary keys-----")
    locations = {
                       ("Nairobi", "Kenya"): 4_500_000,
                      ("Kisumu", "Kenya"): 1_200_000,
                      ("Mombasa", "Kenya"): 1_100_000
    }
    print("Nairobi population:", locations[("Nairobi", "Kenya")])
    print("✅✅Tuples make perfect compound keys for dictionaries because they are immutable and can be used to represent composite data, such as coordinates or pairs of values.")
    print("\n-----6. Tuples for multiple return values-----")
    def calculate(a, b):
        sum_result = a + b
        product_result = a * b
        return sum_result, product_result
    result_sum, result_product = calculate(5, 10)
    print(f"Sum: {result_sum}, Product: {result_product}")
    print("✅✅Tuples are often used to return multiple values from a function, allowing for easy unpacking and assignment of the returned values.")
    
          
