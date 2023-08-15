def calculate_calories():
    print("Calorie Calculator")

    num_of_products = int(input("Enter the number of products: "))

    products = []
    total_calories = 0

    for i in range(num_of_products):
        product_name = input("Enter the product name: ")
        product_calories = float(input("Enter the calorie count for the product: "))

        products.append((product_name, product_calories))
        total_calories += product_calories

    print("\nProduct list and their calories:")
    for product in products:
        print(f"{product[0]}: {product[1]} calories")

    print(f"\nTotal calories: {total_calories}")


if __name__ == '__main__':
    calculate_calories()
