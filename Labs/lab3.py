"""Irakli Okruashvili
    I pledge my honor that I have abided by the Stevens Honor System - I.O.
    """


"""Takes amount and list of coins, outputs the least amount of coins needed for the amount"""
def change(amt, coins):
    if(amt <= 0):
        return 0
    if(amt != 0 and coins == []):
        return float("inf")
    elif(coins[0] > amt):
        return change(amt, coins[1:])
    else:
        use_it = 1 + change(amt-coins[0], coins)
        lose_it = change(amt, coins[1:])
        return min(use_it, lose_it)
