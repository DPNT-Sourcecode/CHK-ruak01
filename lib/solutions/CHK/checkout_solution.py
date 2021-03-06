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
def applySpecialOfferH(item_amounts):
    addition = 0
    if item_amounts["H"] >= 10:
        # How many times does the special offer fit?
        offer_amount = (item_amounts["H"] - item_amounts["H"] % 10) / 10
        # Remove this many items from the item amounts, and add
        # sum to basket:
        addition += offer_amount * 80
        item_amounts["H"] = item_amounts["H"] - offer_amount * 10

    if item_amounts["H"] >= 5:
        # How many times does the special offer fit?
        offer_amount = (item_amounts["H"] - item_amounts["H"] % 5) / 5
        # Remove this many items from the item amounts, and add
        # sum to basket:
        addition += offer_amount * 45
        item_amounts["H"] = item_amounts["H"] - offer_amount * 5
    return addition




def applySpecialOfferV(item_amounts):
    addition = 0
    if item_amounts["V"] >= 3:
        # How many times does the special offer fit?
        offer_amount = (item_amounts["V"] - item_amounts["V"] % 3) / 3
        # Remove this many items from the item amounts, and add
        # sum to basket
        addition += offer_amount * 130
        item_amounts["V"] = item_amounts["V"] - offer_amount * 3

    if item_amounts["V"] >= 2:
        # How many times does the special offer fit?
        offer_amount = (item_amounts["V"] - item_amounts["V"] % 2) / 2
        # Remove this many items from the item amounts, and add
        # sum to basket:
        addition += offer_amount * 90
        item_amounts["V"] = item_amounts["V"] - offer_amount * 2
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

def applySpecialOfferK(item_amounts):
    addition = 0
    if item_amounts["K"] >= 2:
        # How many times does the special offer fit?
        offer_amount = (item_amounts["K"] - item_amounts["K"] % 2) / 2
        # Remove this many items from the item amounts, and add
        # sum to basket:
        addition += offer_amount * 150
        item_amounts["K"] = item_amounts["K"] - offer_amount * 2
    return addition

def applySpecialOfferP(item_amounts):
    addition = 0
    if item_amounts["P"] >= 5:
        # How many times does the special offer fit?
        offer_amount = (item_amounts["P"] - item_amounts["P"] % 5) / 5
        # Remove this many items from the item amounts, and add
        # sum to basket:
        addition += offer_amount * 200
        item_amounts["P"] = item_amounts["P"] - offer_amount * 5
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

def applySpecialOfferK(item_amounts):
    addition = 0
    if item_amounts["K"] >= 2:
        # How many times does the special offer fit?
        offer_amount = (item_amounts["K"] - item_amounts["K"] % 2) / 2
        # Remove this many items from the item amounts, and add
        # sum to basket:
        addition += offer_amount * 150
        item_amounts["K"] = item_amounts["K"] - offer_amount * 2
    return addition

def applySpecialOfferP(item_amounts):
    addition = 0
    if item_amounts["P"] >= 5:
        # How many times does the special offer fit?
        offer_amount = (item_amounts["P"] - item_amounts["P"] % 5) / 5
        # Remove this many items from the item amounts, and add
        # sum to basket:
        addition += offer_amount * 200
        item_amounts["P"] = item_amounts["P"] - offer_amount * 5
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

def applySpecialOfferK(item_amounts):
    addition = 0
    if item_amounts["K"] >= 2:
        # How many times does the special offer fit?
        offer_amount = (item_amounts["K"] - item_amounts["K"] % 2) / 2
        # Remove this many items from the item amounts, and add
        # sum to basket:
        addition += offer_amount * 120
        item_amounts["K"] = item_amounts["K"] - offer_amount * 2
    return addition

def applySpecialOfferP(item_amounts):
    addition = 0
    if item_amounts["P"] >= 5:
        # How many times does the special offer fit?
        offer_amount = (item_amounts["P"] - item_amounts["P"] % 5) / 5
        # Remove this many items from the item amounts, and add
        # sum to basket:
        addition += offer_amount * 200
        item_amounts["P"] = item_amounts["P"] - offer_amount * 5
    return addition


def applySpecialOfferQ(item_amounts):
    addition = 0
    if item_amounts["Q"] >= 3:
        # How many times does the special offer fit?
        offer_amount = (item_amounts["Q"] - item_amounts["Q"] % 3) / 3
        # Remove this many items from the item amounts, and add
        # sum to basket:
        addition += offer_amount * 80
        item_amounts["Q"] = item_amounts["Q"] - offer_amount * 3
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
    if item_amounts["U"] >= 4:
        # How many times does the special offer fit?
        offer_amount = (item_amounts["U"] - item_amounts["U"] % 4) / 4
        item_amounts["U"]=item_amounts["U"]-4*offer_amount
    return 120*offer_amount

def groupOffer(item_amounts):
    #We want to offer the most expensive items for free
    #Z>TSY>X
    #First, use all Z's, then use all T's/S's/Y's, doesnt matter. Then use all X's
    addition=0
    groupitems=item_amounts["T"]+item_amounts["S"]+item_amounts["X"]+item_amounts["Y"]+item_amounts["Z"]
    while groupitems>=3:
        #Need to use group offer:
        to_remove=3
        while to_remove>0:
            if item_amounts["Z"]>0:
                item_amounts["Z"]=item_amounts["Z"]-1
            elif item_amounts["T"]>0:
                item_amounts["T"]=item_amounts["T"]-1
            elif item_amounts["S"]>0:
                item_amounts["S"]=item_amounts["S"]-1
            elif item_amounts["Y"]>0:
                item_amounts["Y"]=item_amounts["Y"]-1
            elif item_amounts["X"]>0:
                item_amounts["X"]=item_amounts["X"]-1
            to_remove-=1
        addition+=45
        groupitems-=3
    return addition
            



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


    single_items = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40, "F": 10,"G":20,"H":10,"I":35,"J":60,"K":70,"L":90,"M":15,"N":40,"O":10,"P":50,"Q":30,"R":50,"S":20,"T":20,"U":40,"V":50,"W":20,"X":17,"Y":20,"Z":21}

    # We do all non-special offer tests first.
    # Testing works now. Now to start with the first cases: iterate all the items, and
    # Add their prices into the basket.
    # If we find an item that is not in basket, return -1

    # Keep running tests after every change when reformatting



    """
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

    if "S" or "T" or "X" or "Y" or "Z" in item_amounts:
        if "S" not in item_amounts:
            item_amounts["S"]=0
        if "T" not in item_amounts:
            item_amounts["T"]=0
        if "X" not in item_amounts:
            item_amounts["X"]=0
        if "Y" not in item_amounts:
            item_amounts["Y"]=0
        if "Z" not in item_amounts:
            item_amounts["Z"]=0


            
        basket+=groupOffer(item_amounts)

    if "N" in item_amounts:
        basket += applySpecialOfferN(item_amounts)
    if "R" in item_amounts:
        basket += applySpecialOfferR(item_amounts)
    if "E" in item_amounts:
        basket += applySpecialOfferE(item_amounts)



    if "F" in item_amounts:
        basket += applySpecialOfferF(item_amounts)
    if "U" in item_amounts:
        basket += applySpecialOfferU(item_amounts)


    # Multiprice
    if "A" in item_amounts:
        basket += applySpecialOfferA(item_amounts)
    if "H" in item_amounts:
        basket += applySpecialOfferH(item_amounts)
    if "V" in item_amounts:
        basket += applySpecialOfferV(item_amounts)

    # Simple bulk
    if "B" in item_amounts:
        basket += applySpecialOfferB(item_amounts)
    if "K" in item_amounts:
        basket += applySpecialOfferK(item_amounts)
    if "P" in item_amounts:
        basket += applySpecialOfferP(item_amounts)
    if "Q" in item_amounts:
        basket += applySpecialOfferQ(item_amounts)



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

