#Write a program to calculate the bill amount for an item given its quantity sold, 
#value, discount, and tax. Given a string s = "1234" and an integer n = 5678, 
#concatenate them as a single string and then convert the result back to an integer. 
#What is the final integer value?
def calculate_bill(quantity, unit_price, discount, tax):
    # Calculate the total value before discount and tax
    total_value = quantity * unit_price
    
    # Apply discount
    discount_amount = total_value * (discount / 100)
    value_after_discount = total_value - discount_amount
    
    # Apply tax
    tax_amount = value_after_discount * (tax / 100)
    total_bill_amount = value_after_discount + tax_amount
    
    return total_bill_amount

unit_price = float(input("Enter the Unit Price:"))
quantity = float(input("Enter Quantity:"))
discount = float(input("Enter the Discount: "))
tax = float(input("Enter the Tax value:"))

bill_amount = calculate_bill(quantity, unit_price, discount, tax)
print(f"The total bill amount is: rs{bill_amount:.2f}")



# Given values
s = "1234"
n = 5678

# Convert integer n to string and concatenate
concatenated_str = s + str(n)

# Convert the concatenated string back to an integer
final_integer = int(concatenated_str)

print(f"The final integer value is: {final_integer}")
