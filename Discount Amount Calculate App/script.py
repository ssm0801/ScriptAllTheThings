price = int(input("Input Price : "));
discount_percentage = 5.99;
discount_amount = 0;
discounted_price = 0;

discount_amount = (discount_percentage*price)/100;
discounted_price = (price-discount_amount);
print("Discount Amount: ", discount_amount);
print("Discounted Price: ", discounted_price);
