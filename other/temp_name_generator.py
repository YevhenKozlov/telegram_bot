import random
import string


class TempNameGenerator:
    """
    Contain methods for generate random names
    """

    @staticmethod
    def get_name(number_of_symbols: int) -> str:
        """
        Method for generate new random name

        :param number_of_symbols: int, length of result string
        :return: str, new name
        """

        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for __ in range(number_of_symbols))
