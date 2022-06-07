

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

    basket=0
    for item in skus:
        #Not in the basket
        if not item in single_items:
            return -1

        #Add item to the item amounts, or increment
        if item in item_amounts:
            item_amounts[item]=item_amounts[item]+1
        else:
            item_amounts[item]=1

        #basket+=single_items[item]
    #print(item_amounts)

    #First, we try to fit the special offers in:
    

    #return basket


    

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
