# Number of people in the family
num_people = 4

# Input slices each person eats
slices_person1 = int(input("How many slices does person 1 eat? "))
slices_person2 = int(input("How many slices does person 2 eat? "))
slices_person3 = int(input("How many slices does person 3 eat? "))
slices_person4 = int(input("How many slices does person 4 eat? "))

# Total slices needed
total_slices_needed = slices_person1 + slices_person2 + slices_person3 + slices_person4

# Number of slices per pizza
slices_per_pizza = 8

# Number of pizzas required
pizzas_required = total_slices_needed // slices_per_pizza
# Check if there are leftovers
if total_slices_needed % slices_per_pizza != 0:
    pizzas_required += 1

# Calculate leftover slices
total_slices_available = pizzas_required * slices_per_pizza
leftover_slices = total_slices_available - total_slices_needed

print(f"Total slices needed: {total_slices_needed}")
print(f"Number of pizzas required: {pizzas_required}")
print(f"Leftover slices: {leftover_slices}")
