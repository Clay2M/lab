class Account:
    """
    A class representing details for an account object
    """

    def __init__(self, name: str) -> None:
        """
        Constructor to create initial state of an account object.
        :param name: Account holder's name.
        """
        self.__account_name: str = name
        self.__account_balance: float = 0

    def deposit(self, amount: float) -> bool:
        """
        Method to add money to an account's balance.
        :param amount: Amount to be added.
        :return: Method's status. Returns True if successful.
        """
        if amount <= 0:
            return False
        else:
            self.__account_balance += amount
            return True

    def withdraw(self, amount: float) -> bool:
        """
        Method to subtract money from an account's balance.
        :param amount: Amount to be subtracted.
        :return: Method's status. Returns True if successful.
        """
        if amount <= 0 or amount > self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self) -> float:
        """
        Method to access an account's balance.
        :return: Account's balance.
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Method to access an account holder's name.
        :return: Account holder's name.
        """
        return self.__account_name
