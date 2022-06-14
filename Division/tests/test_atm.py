from unittest import TestCase, main
from division_coins import ATM


class ATMTest(TestCase):
    def test_negative_amount(self):
        with self.assertRaises(ValueError) as ex:
            ATM.divides_amount_into_coins(-100)
        self.assertEqual("Amount value entered is negative: -100", ex.exception.args[0])

    def test_result(self):
        self.assertEqual(ATM.divides_amount_into_coins(166), [100, 25, 25, 10, 5, 1])
        self.assertEqual(ATM.divides_amount_into_coins(100), [100])

if __name__ == "__main__":
    main()
