from tabnanny import check
from requests import check_compatibility

import unittest
import sys

sys.path.append("../../../lib/solutions/CHK")

# from solutions.solutions_CHK import checkout_solution
import checkout_solution



class TestCHK(unittest.TestCase):



    """erroring case
    """
    def test_free_item_only_not_in_basket(self):
        assert checkout_solution.checkout("a")==40


    """Test single item, no special offers"""

    def test_chk1_single(self):
        assert checkout_solution.checkout("A") == 50

    """Test multiple of the same item without special offers
    """

    def test_chk1_multiple(self):
        assert checkout_solution.checkout("AA") == 100

    """Test multiple different items without special offer
    """

    def test_chk1_mixed(self):
        assert checkout_solution.checkout("ABC") == 100

    """Test a special offer only buy for single offer
    """

    def test_chk1_special_simple(self):
        assert checkout_solution.checkout("AAA") == 130

    """Test a case with multiple special offers and nothing else
    """

    def test_chk1_special_two_offers_multiprice(self):
        assert checkout_solution.checkout("AAAAAAAA") == 330

    """Test a mixed basket with special offers and single items
    """

    def test_chk1_special_mixed(self):
        assert checkout_solution.checkout("AAABBABCD") == 290

    """Free item without it being in the basket
    """
    def test_free_item_only_not_in_basket(self):
        assert checkout_solution.checkout("EE")==80


    """Free item with it it being in the basket
    """
    def test_free_item_only_in_basket(self):
        assert checkout_solution.checkout("EEB")==80



    """Free item with it being in the basket, with other items
    """
    def test_free_item_in_basket(self):
        assert checkout_solution.checkout("EEBA")==130


    
    """Free item with it being in the basket, with another 
    """
    def test_free_item_in_basket_other_offers(self):
        assert checkout_solution.checkout("EEBABB")==175



    """Special offer F: only one, nnnnnno discount
    """
    def test_f_no_discount(self):
        assert checkout_solution.checkout("F")==10


    """Special offer F: three, so discount
    """
    def test_f_discount(self):
        assert checkout_solution.checkout("FFF")==20

        
    """Special offer F: four, so discount plus one
    """
    def test_f_discount_and_more(self):
        assert checkout_solution.checkout("FFFF")==30


    """Special offer F: Four, and a lot of other stuff
    """
    def test_f_discount_and_other_offers(self):
        assert checkout_solution.checkout("FFFEEBABB")==195

        

        

