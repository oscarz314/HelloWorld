user_money = float(input("Input your cash amount: "))
user_money_mutable = user_money;
quarters = 0;
dimes = 0;
nickels = 0;
pennies = 0;

#Get quarter count
quarters = int(user_money_mutable / .25)
user_money_mutable -= quarters * .25
#Get dime count
dimes = int(user_money_mutable / .10)
user_money_mutable -= dimes * .10
#Get nickel count
nickels = int(user_money_mutable / .05)
user_money_mutable -= nickels * .05
#Get penny count
pennies = int(user_money_mutable / .01)

print("The minimum amount of coins required is: ")
print(f"{quarters} quarters, {dimes} dimes, {nickels} nickels, {pennies} pennies")




