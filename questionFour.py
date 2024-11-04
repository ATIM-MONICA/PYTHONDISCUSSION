#Question 4(i)
# Create a list of five of your favorite foods. Write a Python program to:
# Add two more items to the list.
# Remove one item from the list.
# Print the updated list.

# Initial list of five favorite foods
favorite_foods = ["Chicken", "Yorghurt", "Burgers", "Pasta", "Ice Cream"]
print(f"List of favorite foods: {favorite_foods}")

# Add two more items to the list
favorite_foods.append("Matooke")
favorite_foods.append("Salad")
print(f"\nAdding more 2 items to the list: {favorite_foods}")

# Remove one item from the list
favorite_foods.remove("Pasta")

# Print the updated list
print(f"\nUpdated favorite foods list: {favorite_foods}\t")



#Question 4(ii)
# Given the list numbers = [2, 5, 8, 10, 3, 6], write a Python program to:
# Print the first and last elements of the list.
# Print the list in reverse order.
# Calculate and print the sum of all the elements in the list.

numbers = [2, 5, 8, 10, 3, 6]

# Print the first and last elements of the list
first_element = numbers[0]
last_element = numbers[-1]
print(f"First element: {first_element}")
print(f"Last element: {last_element}")
#print the last in reversed order
reversed_list = numbers[::-1]
print(f"Reversed list: {reversed_list}")
#print the sum of all the elements in the list
sum_of_elements = sum(numbers)
print(f"Sum of all elements: {sum_of_elements}")

