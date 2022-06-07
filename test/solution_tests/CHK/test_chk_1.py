from tabnanny import check
from requests import check_compatibility
from solutions.CHK import checkout_solution


class TestCHK():
    """Test single item, no special offers
    """
    def test_chk1_single(self):
        assert checkout_solution.checkout("A") == 50


    """Test multiple of the same item without special offers
    """
    def test_chk1_multiple(self):
        assert checkout_solution.checkout("AA")==100

    """Test multiple different items without special offer
    """
    def test_chk1_mixed(self):
        assert checkout_solution.checkout("ABC")==100

    """Test a special offer only buy for single offer
    """
    def test_chk1_special_simple(self):
        assert checkout_solution.checkout("AAA")==130

    """Test a case with multiple special offers and nothing else
    """
    def test_chk1_special_two_offers(self):
        assert checkout_solution.checkout("AAAAAA")==260

    """Test a mixed basket with special offers and single items
    """
    def test_chk1_special_mixed(self):
        assert checkout_solution.checkout("AAABBABCD")==290





