''' Create a function called calc_dollars. In the function body, define a dictionary and store it in a variable named piggyBank. The dictionary should have the following keys defined.

1. quarters
2. nickels
3. dimes
4. pennies

Once you have given yourself a large stash of coins in your piggybank, look at each key and perform the appropriate math on the integer value to determine how much money you have in dollars. Store that value in a variable named dollarAmount and print it.
'''
def calc_dollars():
    piggyBank = {
        "pennies": 342,
        "nickels": 9,
        "dimes": 32,
        "quarters": 65,
    }
    dollarAmount = piggyBank["pennies"] / 100 + piggyBank["nickels"] / 20 + piggyBank["dimes"] / 10 + piggyBank["quarters"] / 4
    print(dollarAmount)

calc_dollars()