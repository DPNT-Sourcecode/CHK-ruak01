

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    #First, we sum all possible amounts of items. Then, if
    #A special offer for an item exists, we try to fit that first. If not, then go with the normal price table
    #Writing tests to test_sum.py in order to stay on top of things
    #Write tests first, and adapt a TDD-approach


    #Assume that each basket is a string of characters, each 
    #an individual item: for instance, "AABBCC"


    #Formulate a hashmap for single items, and another for special offers
    single_items={"A":50,"B":30,"C":20,"D":15}

    #First, check if skus only includes uppercase letters
    if not skus.isupper():
        return -1


    #We do all non-special offer tests first.
    #Testing works now. Now to start with the first cases: iterate all the items, and
    #Add their prices into the basket.
    #If we find an item that is not in basket, return -1



    #Now all the basic cases are there.
    #In order to utilize the  special offers, we collect amounts of items to another map
    item_amounts={}

    for item in skus:
        #Not in the basket
        if not item in single_items:
            return -1

        #Add item to the item amounts, or increment
        if item in item_amounts:
            item_amounts[item]=item_amounts[item]+1
        else:
            item_amounts[item]=1


    basket=0
    #First, we try to fit the special offers in:
    #If the amount of items is geq 3, recude

    if "A" in item_amounts:
        if item_amounts["A"]>=3:
            #How many times does the special offer fit?
            offer_amount=(item_amounts["A"]-item_amounts["A"]%3)/3
            #Remove this many items from the item amounts, and add
            #sum to basket:
            basket+=offer_amount*130
            item_amounts["A"]=item_amounts["A"]-offer_amount*3

    #Same with the other one:
    if "B" in item_amounts:
        if item_amounts["B"]>=2:
            #How many times does the special offer fit?
            offer_amount=(item_amounts["B"]-item_amounts["B"]%2)/2
            #Remove this many items from the item amounts, and add
            #sum to basket:
            basket+=offer_amount*45
            item_amounts["B"]=item_amounts["B"]-offer_amount*2


    #rest of the items:
    for item in item_amounts.keys():
        print(item)    
        #basket+=single_items[item]
    #print(item_amounts)





    return basket


    

"""
+------+-------+----------------+
| Item | Price | Special offers |
+------+-------+----------------+
| A    | 50    | 3A for 130     |
| B    | 30    | 2B for 45      |
| C    | 20    |                |
| D    | 15    |                |
+------+-------+----------------+
"""

