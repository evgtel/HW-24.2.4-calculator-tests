
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator()

    def test_adding(self):
        assert self.calc.adding(1, 1) == 2

    def test_subtraction(self):
        assert self.calc.subtraction(5, 4) == 1

    def test_multiply(self):
        assert self.calc.multiply(7, 3) == 21

    def test_zero_division(self):
        assert self.calc.division( 115, 5) == 23

    def teardown(self):
        print('Teardown endly')


