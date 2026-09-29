# Shopping Cart Project
# Using Python List and Dictionary

products = {
    1: {"name": "Laptop", "price": 800},
    2: {"name": "Mouse", "price": 20},
    3: {"name": "Keyboard", "price": 40},
    4: {"name": "Headphones", "price": 60},
    5: {"name": "USB Cable", "price": 10}
}

cart = []


def show_products():
    print("\n--- Available Products ---")
    for product_id, product in products.items():
        print(f"{product_id}. {product['name']} - ${product['price']}")


def add_to_cart():
    show_products()

    try:
        product_id = int(input("\nEnter product ID: "))
        quantity = int(input("Enter quantity: "))

        if product_id not in products:
            print("Invalid product ID.")
            return

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            return

        # Check if product is already in cart
        for item in cart:
            if item["id"] == product_id:
                item["quantity"] += quantity
                print("Quantity updated successfully.")
                return

        # Add new product to cart
        cart.append({
            "id": product_id,
            "name": products[product_id]["name"],
            "price": products[product_id]["price"],
            "quantity": quantity
        })

        print("Product added to cart.")

    except ValueError:
        print("Please enter a valid number.")


def view_cart():
    print("\n--- Shopping Cart ---")

    if not cart:
        print("Your cart is empty.")
        return

    total = 0

    for item in cart:
        subtotal = item["price"] * item["quantity"]
        total += subtotal

        print(
            f"{item['name']} | "
            f"Price: ${item['price']} | "
            f"Quantity: {item['quantity']} | "
            f"Subtotal: ${subtotal}"
        )

    print("-" * 40)
    print(f"Total: ${total}")


def remove_from_cart():
    if not cart:
        print("\nYour cart is empty.")
        return

    view_cart()

    try:
        product_id = int(input("\nEnter product ID to remove: "))

        for item in cart:
            if item["id"] == product_id:
                cart.remove(item)
                print("Product removed from cart.")
                return

        print("Product not found in cart.")

    except ValueError:
        print("Please enter a valid product ID.")


def checkout():
    if not cart:
        print("\nYour cart is empty.")
        return

    view_cart()

    print("\nThank you for shopping!")
    cart.clear()


# Main program
while True:
    print("\n====== SHOPPING CART ======")
    print("1. Show Products")
    print("2. Add to Cart")
    print("3. View Cart")
    print("4. Remove from Cart")
    print("5. Checkout")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_products()

    elif choice == "2":
        add_to_cart()

    elif choice == "3":
        view_cart()

    elif choice == "4":
        remove_from_cart()

    elif choice == "5":
        checkout()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
