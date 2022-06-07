

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
    if not all(skus.isupper()):
        return -1

    #We do all non-special offer tests first:
    basket=0
    for item in skus:
        print(item)


    

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
