from solutions.CHK import checkout_solution


class TestCHK():
    #Test single item for CHK1, no bulk buys

    
    def test_chk1_single(self):
        assert checkout_solution.checkout("AA") == 100

