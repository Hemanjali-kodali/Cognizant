products = [
    "Laptop",
    "Smartphone",
    "Headphones",
    "Smartwatch",
    "Keyboard",
    "Mouse"
]

keyword = input("Enter product name: ")

found = False

for product in products:
    if keyword.lower() in product.lower():
        print(product)
        found = True

if not found:
    print("No matching products found.")