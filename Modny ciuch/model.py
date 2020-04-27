class StockItem():
    """
    Towar magazynowy sklepu odziezowego
    """

    min_price = 0.5
    max_price = 500.0

    def __init__(self, stock_ref, price, color):
        self.stock_ref = stock_ref
        self.color = color
        self.__price = price
        self.__stock_level = 0

    @property
    def price(self):
        return self.__price

    @property
    def stock_level(self):
        return self.__stock_level

    @property
    def item_name(self):
        return "Towar magazynowy"

    def __str__(self):
        template = """
        Numer magazynowy: {0}
        Typ: {1}
        Cena: {2}
        Stan magazynowy: {3}
        Kolor: {4}"""
        return template.format(self.stock_ref, self.item_name, self.price, self.stock_level, self.color)

    def check_version(self):
        #ver1
        pass

class Dress(StockItem):
    """
    Sukienki
    """

    def __init__(self, stock_ref, price, color, pattern, size):
        super().__init__(stock_ref=stock_ref, price=price, color=color)
        self.pattern = pattern
        self.size = size

    @property
    def item_name(self):
        return "Sukienka"

    def __str__(self):
        stock_details = super().__str__()
        template = """
        {0}
        Fason: {1}
        Rozmiar: {2}"""
        return template.format(stock_details, self.pattern, self.size)

    def check_version(self):
        super().check_version()


class Pants(StockItem):
    """
    Spodnie
    """

    def __init__(self, stock_ref, price, color, length, pattern, waist):
        super().__init__(stock_ref=stock_ref, price=price, color=color)
        self.pattern = pattern
        self.length = length
        self.waist = waist

    @property
    def item_name(self):
        return "Spodnie"

    def __str__(self):
        stock_details = super().__str__()
        template = """
        {0}
        Fason: {1}
        Rozmiar talia/długość: {2} / {3}"""
        return template.format(stock_details, self.pattern, self.waist, self.length)

    def check_version(self):
        super().check_version()