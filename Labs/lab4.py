"""Irakli Okruashvili
    I pledge my honor that I have abided by the Stevens Honor System - I.O.
    """


"""returns best combination of values in 2D itemList, without exceeding 'cap'acity"""
def knapsack(cap, itemList): 
    if(cap <= 0 or itemList == []):
        return [0,[]]
    elif(itemList[0][0] > cap):
        return knapsack(cap, itemList[1:])
    else:
        use_it = knapsack(cap-itemList[0][0], itemList[1:])
        lose_it = knapsack(cap, itemList[1:])
        x = itemList[0][1] + use_it[0]
        if(x > lose_it[0]):
            return [x, [itemList[0]] + use_it[1]]
        else:
            return lose_it


    #itemList = [[2, 100], [3, 112], [4, 125]]
