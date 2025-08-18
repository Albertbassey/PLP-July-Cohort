def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    Applies discount only if it's 20% or higher.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount = float(input("Enter the discount percentage: "))

    # Calculate and display the final price
    final_price = calculate_discount(original_price, discount)

    if discount >= 20:
        print(f"Discount applied! Final price: ₦{final_price:.2f}")
    else:
        print(f"No discount applied. Final price: ₦{original_price:.2f}")

except ValueError:
    print("Please enter valid numbers for price and discount.")
