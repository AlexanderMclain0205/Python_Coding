# Initialize inventory
muffins = 10
cupcakes = 10

# Function to handle customer purchases
def process_purchase(item):
    global muffins, cupcakes
    if item == "muffin":
        if muffins > 0:
            muffins -= 1
        else:
            print("Out of stock")
    elif item == "cupcake":
        if cupcakes > 0:
            cupcakes -= 1
        else:
            print("Out of stock")

# Main loop to process customer inputs
while True:
    item = input("Enter item to buy ('muffin', 'cupcake') or '0' to finish: ").strip().lower()
    if item == "0":
        break
    process_purchase(item)

# Print remaining quantities
print(f"muffins: {muffins} cupcakes: {cupcakes}")
