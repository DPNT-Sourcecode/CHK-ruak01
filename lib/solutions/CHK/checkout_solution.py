# noinspection PyUnusedLocal
# skus = unicode string


from signal import ITIMER_REAL


def sanityCheck(skus):
    # empty basket
    if not skus:
        return 0
    # malformed token
    if not skus.isupper():
        return -1
    else:
        return 1


def collateItemAmounts(skus, single_items):
    item_amounts = {}

    for item in skus:
        # Not in the basket
        if not item in single_items:
            return -1

        # Add item to the item amounts, or increment
        if item in item_amounts:
            item_amounts[item] = item_amounts[item] + 1
        else:
            item_amounts[item] = 1
    return item_amounts


#Offer for one item with multiple prices
def applySpecialOfferA(item_amounts):
    addition = 0
    if item_amounts["A"] >= 5:
        # How many times does the special offer fit?
        offer_amount = (item_amounts["A"] - item_amounts["A"] % 5) / 5
        # Remove this many items from the item amounts, and add
        # sum to basket:
        addition += offer_amount * 200
        item_amounts["A"] = item_amounts["A"] - offer_amount * 5

    if item_amounts["A"] >= 3:
        # How many times does the special offer fit?
        offer_amount = (item_amounts["A"] - item_amounts["A"] % 3) / 3
        # Remove this many items from the item amounts, and add
        # sum to basket:
        addition += offer_amount * 130
        item_amounts["A"] = item_amounts["A"] - offer_amount * 3
    return addition

#Simple multi-item offer
def applySpecialOfferB(item_amounts):
    addition = 0
    if item_amounts["B"] >= 2:
        # How many times does the special offer fit?
        offer_amount = (item_amounts["B"] - item_amounts["B"] % 2) / 2
        # Remove this many items from the item amounts, and add
        # sum to basket:
        addition += offer_amount * 45
        item_amounts["B"] = item_amounts["B"] - offer_amount * 2
    return addition

#Offer giving free other items. These go first, in order.
def applySpecialOfferE(item_amounts):
    # How this will work is that
    # For each pair of E's, we can remove one B, as long as there are B's to remove
    if item_amounts["E"] >= 2:
        # How many times does the special offer fit?
        offer_amount = (item_amounts["E"] - item_amounts["E"] % 2) / 2
        if "B" in item_amounts:
            item_amounts["B"] = item_amounts["B"] - offer_amount
    if "B" in item_amounts:
        if item_amounts["B"] < 0:
            item_amounts["B"] = 0
    return 0


#Offer giving free other items. These go first, in order.
def applySpecialOfferN(item_amounts):
    # How this will work is that
    # For each pair of E's, we can remove one B, as long as there are B's to remove
    if item_amounts["N"] >= 3:
        # How many times does the special offer fit?
        offer_amount = (item_amounts["N"] - item_amounts["N"] % 3) / 3
        if "M" in item_amounts:
            item_amounts["M"] = item_amounts["M"] - offer_amount
    if "M" in item_amounts:
        if item_amounts["M"] < 0:
            item_amounts["M"] = 0
    return 0

#Offer giving free other items. These go first, in order.
def applySpecialOfferR(item_amounts):
    if item_amounts["R"] >= 3:
        # How many times does the special offer fit?
        offer_amount = (item_amounts["R"] - item_amounts["R"] % 3) / 3
        if "Q" in item_amounts:
            item_amounts["Q"] = item_amounts["Q"] - offer_amount
    if "Q" in item_amounts:
        if item_amounts["Q"] < 0:
            item_amounts["Q"] = 0
    return 0



#Offer giving free items if we already have enough
def applySpecialOfferF(item_amounts):
    offer_amount=0
    #For each triplet of F's, remove three and ad 2Xfprice to basket
    if item_amounts["F"] >= 3:
        # How many times does the special offer fit?
        offer_amount = (item_amounts["F"] - item_amounts["F"] % 3) / 3
        item_amounts["F"]=item_amounts["F"]-3*offer_amount
    return 20*offer_amount


#Offer giving free items if we already have enough
def applySpecialOfferU(item_amounts):
    offer_amount=0
    #For each triplet of F's, remove three and ad 2Xfprice to basket
    if item_amounts["U"] >= 3:
        # How many times does the special offer fit?
        offer_amount = (item_amounts["U"] - item_amounts["U"] % 3) / 3
        item_amounts["U"]=item_amounts["U"]-3*offer_amount
    return 80*offer_amount

def checkout(skus):
    # First, we sum all possible amounts of items. Then, if
    # A special offer for an item exists, we try to fit that first. If not, then go with the normal price table
    # Writing tests to test_sum.py in order to stay on top of things
    # Write tests first, and adapt a TDD-approach

    # Assume that each basket is a string of characters, each
    # an individual item: for instance, "AABBCC"


    if not sanityCheck(skus)==1:
        return sanityCheck(skus)
    # Formulate a hashmap for single items, and another for special offers


#Writing tests fof all these cases is going to be difficult
#Have to trust our old tests are good enough for now.


    single_items = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40, "F": 10,"G":20,"H":10,"I":35,"J":60,"K":80,"L":90,"M":15,"N":40,"O":10,"P":50,"Q":30,"R":50,"S":30,"T":20,"U":40,"V":50,"W":20,"X":90,"Y":10,"Z":50}

    # We do all non-special offer tests first.
    # Testing works now. Now to start with the first cases: iterate all the items, and
    # Add their prices into the basket.
    # If we find an item that is not in basket, return -1

    # Keep running tests after every change when reformatting



    """
    | H    | 10    | 5H for 45, 10H for 80  |
    | K    | 80    | 2K for 150             |
    | P    | 50    | 5P for 200             |
    | Q    | 30    | 3Q for 80              |
    | V    | 50    | 2V for 90, 3V for 130  |
    """

    item_amounts = collateItemAmounts(skus, single_items)
    basket = 0
    # First, we try to fit the special offers in:

    #A one with multiple prices, B simple bulk,
    #E gives free others,
    #F gives free if we buy bulk
    #H is archetype A, K is archetype B,
    # P is archetype B,
    # Q is archetype B,
    # U is archetype F, V is archetype A

    if "N" in item_amounts:
        basket += applySpecialOfferN(item_amounts)
    if "R" in item_amounts:
        basket += applySpecialOfferN(item_amounts)
    if "E" in item_amounts:
        basket += applySpecialOfferE(item_amounts)



    if "F" in item_amounts:
        basket += applySpecialOfferF(item_amounts)
    if "U" in item_amounts:
        basket += applySpecialOfferU(item_amounts)

    # Multiprice
    if "A" in item_amounts:
        basket += applySpecialOfferA(item_amounts)


    # Simple bulk
    if "B" in item_amounts:
        basket += applySpecialOfferB(item_amounts)

    # rest of the items:
    for key in item_amounts.keys():
        if item_amounts[key] >= 0:
            basket += single_items[key] * item_amounts[key]

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





