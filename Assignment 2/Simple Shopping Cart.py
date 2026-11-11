
# Simple Shopping Cart Program

# 1. Customer Information
customer_name = input("Enter Customer Name: ")

# 2. Product Information
product1 = input("\nEnter Product 1 Name: ")
price1 = float(input("Enter Product 1 Price: "))

product2 = input("\nEnter Product 2 Name: ")
price2 = float(input("Enter Product 2 Price: "))

product3 = input("\nEnter Product 3 Name: ")
price3 = float(input("Enter Product 3 Price: "))

# 3. Calculate Subtotal
subtotal = price1 + price2 + price3

# 4. Calculate Discount
if subtotal >= 5000:
    discount_rate = 0.20
elif subtotal >= 3000:
    discount_rate = 0.10
elif subtotal >= 1000:
    discount_rate = 0.05
else:
    discount_rate = 0

discount = subtotal * discount_rate

# 5. Calculate Final Total
final_total = subtotal - discount


print(f"Customer Name: {customer_name}")


print(f"Product 1: {product1} Price: {price1:.2f}")
print(f"Product 2: {product2} Price: {price2:.2f}")
print(f"Product 3: {product3} Price: {price3:.2f}")


print(f"Subtotal:     {subtotal:.2f}")
print(f"Discount:     {discount:.2f}")
print(f"Final Total:  {final_total:.2f}")


