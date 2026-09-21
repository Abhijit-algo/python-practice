
def calculate_total(price, discount_percentage=0):
    """Calculates the final price after applying a percentage discount."""
    if discount_percentage < 0 or discount_percentage > 100:
        return "Error: Discount must be between 0 and 100."

    discount_amount = price * (discount_percentage / 100)
    final_price = price - discount_amount
    return final_price



print("--- Welcome to the Store Checkout System ---")

try:
    
    raw_price = float(input("Enter the item price: $"))
    raw_discount = float(
        input("Enter discount percentage (0 for none, e.g., 15): ")
    )

    
    total = calculate_total(raw_price, raw_discount)

    
    if isinstance(total, str):
        print(total)  
    else:
        print(f"Final Total Price: ${total:.2f}")

except ValueError:
    print("Invalid input. Please enter numbers only.")
