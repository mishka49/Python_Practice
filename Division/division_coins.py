from mylist_sort import List
from typing import List


class ATM:
    _coins = [100, 25, 10, 5, 1]

    @staticmethod
    def divides_amount_into_coins(amount: int) -> List[int]:
        if amount < 0:
            raise ValueError(f"Amount value entered is negative: {amount}")

        result_coins = []
        for coin in ATM._coins:
            while (amount - coin) >= 0:
                result_coins.append(coin)
                amount -= coin

        if amount != 0:
            raise ValueError(f"Unable to pick up a set of coins")
        return result_coins


if __name__ == "__main__":
    amount = input("Enter the desired amount: ")
    print(ATM.divides_amount_into_coins(int(amount)))
