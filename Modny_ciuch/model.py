import pickle

class StockItem():
    """
    Towar magazynowy sklepu odziezowego
    """

    min_price = 0.5
    max_price = 500.0
    max_stock_add = 100

    show_instrumentation = False

    def __init__(self, stock_ref, price, color, location):
        if StockItem.show_instrumentation:
            print("** Wywołano metodę __init__ klasy StockItem")
        self.stock_ref = stock_ref
        self.color = color
        self.__price = price
        self.__stock_level = 0
        self.location = location

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
        Kolor: {4}
        Lokalizacja: {5}"""
        return template.format(self.stock_ref, self.item_name, self.price, self.stock_level, self.color, self.location)

    def check_version(self):
        #ver1
        pass

    def add_stock(self, count):
        """
        Dostawa towaru do magazynu
        :param count: liczba sztuk towaru do dodania
        Zgłasza wyjątek, jeśli liczba jest nieprawidłowa
        """
        if count <0 or count >StockItem.max_stock_add:
            raise Exception ("Nieprawidłowa liczba sztuk towaru do dodania")

        self.__stock_level += count

    def sell_stock(self, count):
        """
        Funkcja sprzedaży - aktualizacja stanów magazynowych
        :param count: liczba sprzedanych sztuk
        """
        if count <1:
            raise Exception ("Nieprawidłowa liczba sztuk towaru do sprzedaży")

        if count > self.__stock_level:
            raise Exception ("Za mało towaru w magazynie")

        self.__stock_level -= count

class Dress(StockItem):
    """
    Sukienki
    """

    def __init__(self, stock_ref, price, color, location, pattern, size):
        if StockItem.show_instrumentation:
            print('** Wywołano metodę __init__ klasy Dress')
        super().__init__(stock_ref=stock_ref, price=price, color=color, location=location)
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

    def __init__(self, stock_ref, price, color, location, length, pattern, waist):
        if StockItem.show_instrumentation:
            print('** Wywołano metodę __init__ klasy Pants')
        super().__init__(stock_ref=stock_ref, price=price, color=color, location=location)
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


class Hats(StockItem):
    def __init__(self, stock_ref, price, color, location, size, decoration):
        if StockItem.show_instrumentation:
            print('** Wywołano metodę __init__ klasy Hats')
        super().__init__(stock_ref=stock_ref, price=price, color=color, location=location)
        self.size = size
        self.decoration = decoration

    @property
    def item_name(self):
        return "Kapelusz"

    def __str__(self):
        hat_details = super().__str__()
        template = """
            {0}
            Rozmiar: {1}
            Dekoracja: {2}"""
        return template.format(hat_details, self.size, self.decoration)

    def check_version(self):
        super().check_version()


class Blouse():
    def __init__(self, stock_ref, price, color, location, size, sleeve):
        if StockItem.show_instrumentation:
            print('** Wywołano metodę __init__ klasy Blouse')
        super().__init__(stock_ref=stock_ref, price=price, color=color, location=location)
        self.size = size
        self.sleeve = sleeve

    @property
    def item_name(self):
        return "Bluzka"

    def __str__(self):
        blouse_details = super().__str__()
        template = """
                {0}
                Rozmiar: {1}
                Rękaw: {2}"""
        return template.format(blouse_details, self.size, self.sleeve)

    def check_version(self):
        super().check_version()

class Jeans(Pants):
    def __init__(self, stock_ref, price, color, location, length, pattern, waist, style):
        if StockItem.show_instrumentation:
            print('** Wywołano metodę __init__ klasy Jeans')
        super.__init__(stock_ref, price, color, location, length, pattern, waist)
        self.style = style
        self.Jeans_ver = 1

    @property
    def item_name(self):
        return "Dżinsy"

    def __str__(self):
        pants_details = super().__str__()
        template = """
            {0}
            Styl = {1}"""
        return template.format(pants_details, self.style)

    def check_version(self):
        super().check_version()

class FashionStore:

    show_instrumentation = False

    def __init__(self, name):
        if FashionStore.show_instrumentation:
            print('** Wywołano metodę __init__ klasy FashionStore')
        self.__stock_dict = {}
        self.name = name

    def save(self, file):
        """
        Zapisuje dane do pliku pickle.
        Jeśli zapis się nie powiedzie, zgłasza wyjątki
        :return: pickle file
        """
        if FashionStore.show_instrumentation:
            print('** Wywołano metodę save klasy FashionStore')
        with open (file, 'wb') as out_file:
            pickle.dump(self, out_file)

    @staticmethod
    def load(file):
        """
        Buduje bazę z pliku pickle
        Jeśli wczytywanie się nie powiedzie, zgłasza wyjątki
        :param file: pickle file
        :return:
        """
        if FashionStore.show_instrumentation:
            print('** Wywołano metodę load klasy FashionStore')
        with open(file, "rb") as input_file:
            result = pickle.load(input_file)
        return result

    def store_new_stock_item(self, stock_item):
        """
        Utworzenie nowego towaru w aplikacji
        Indeks zapisany w atrybucie stock_ref
        Jeśli towar istnieje, zgłasza wyjątek
        :param item: instancja klasy StockItem lub jednej z klas-dzieci
        :return:
        """
        if FashionStore.show_instrumentation:
            print('** Wywołano metodę store_new_stock_item klasy FashionStore')
        if stock_item.stock_ref in self.__stock_dict:
            raise Exception ("Towar już istnieje!")
        self.__stock_dict[stock_item.stock_ref] = stock_item

    def find_stock_item(self, stock_ref):
        """
        Pobiera towar z magazynu
        Jeśli towar nie istnieje zwraca None
        :param stock_ref: atrybut stock_ref szukanego towaru
        :return:
        """
        if FashionStore.show_instrumentation:
            print('** Wywołano metodę find_stock_item klasy FashionStore')
        if stock_ref in self.__stock_dict:
            return self.__stock_dict[stock_ref]
        else:
            return None

    def __str__(self):
        stock = map(str, self.__stock_dict.values())
        stock_list = '\n'.join(stock)
        template = """Witaj w sklepie {0}. Towary w magazynie: {1}"""
        return template.format(self.name, stock_list)

class FashionStoreShellApp():
    def __init__(self, filename):
        """
        Powłoka do zarządzania sklepem
        :param filename: plik z zatowarowaniem
        """
        self.__filename = filename
        try:
            self.__shop = FashionStore.load(filename)
        except:
            print("Ladowanie danych nie powiodło się")
            print("Tworzenie pustego sklepu")
            self.__shop = FashionStore()

    def create_new_stock_item(self):
        """
        Tworzy nowy towar i dodaje go do magazynu.
        :return:
        """
        print("""
            Tworzenie nowego towaru
            1: Sukienka
            2: Spodnie
            3: Kapelusz
            4: Bluzka
            5: Dżinsy
            """)
        item = int(input("Jaki rodzaj towaru chcesz dodać? "))
        if item == 1:
            print("Dodawanie sukienki")
            stock_ref = input("Podaj numer magazynowy: ")
            price = float(input("Podaj cenę: "))
            color = input("Podaj kolor: ")
            location = input("Podaj lokalizację: ")
            pattern = input("Podaj fason: ")
            size = input("Podaj rozmiar: ")
            stock_item = Dress(stock_ref=stock_ref,
                               price=price,
                               color=color,
                               location=location,
                               pattern=pattern,
                               size=size)

        elif item == 2:
            print("Dodawanie spodni")
            stock_ref = input("Podaj numer magazynowy: ")
            price = float(input("Podaj cenę: "))
            color = input("Podaj kolor: ")
            location = input("Podaj lokalizację: ")
            pattern = input("Podaj fason: ")
            length = input("Podaj długość nogawki: ")
            waist = input("Podaj obwód pasa: ")
            stock_item = Pants(stock_ref=stock_ref,
                               price=price,
                               color=color,
                               location=location,
                               pattern=pattern,
                               length=length,
                               waist=waist)

        elif item == 3:
            print("Dodawanie kapelusza")
            stock_ref = input("Podaj numer magazynowy: ")
            price = float(input("Podaj cenę: "))
            color = input("Podaj kolor: ")
            location = input("Podaj lokalizację: ")
            size = input("Podaj rozmiar: ")
            decoration = input("Podaj zdobienie: ")
            stock_item = Hats(stock_ref=stock_ref,
                              price=price,
                              color=color,
                              location=location,
                              size=size,
                              decoration=decoration)

        elif item == 4:
            print("Dodawanie bluzki")
            stock_ref = input("Podaj numer magazynowy: ")
            price = float(input("Podaj cenę: "))
            color = input("Podaj kolor: ")
            location = input("Podaj lokalizację: ")
            size = input("Podaj rozmiar: ")
            sleeve = input("Podaj dlugość rękawa: ")
            stock_item = Hats(stock_ref=stock_ref,
                              price=price,
                              color=color,
                              location=location,
                              size=size,
                              sleeve=sleeve)

        elif item == 5:
            print("Dodawanie dżinsów")
            stock_ref = input("Podaj numer magazynowy: ")
            price = float(input("Podaj cenę: "))
            color = input("Podaj kolor: ")
            location = input("Podaj lokalizację: ")
            pattern = input("Podaj fason: ")
            length = input("Podaj długość nogawki: ")
            waist = input("Podaj obwód pasa: ")
            style = input("Podaj model: ")
            stock_item = Pants(stock_ref=stock_ref,
                               price=price,
                               color=color,
                               location=location,
                               pattern=pattern,
                               length=length,
                               waist=waist,
                               style=style)
        try:
            self.__shop.store_new_stock_item(stock_item)
            print("Dodano produkt")
        except Exception as e:
            print (f"Dodawanie nie powiodło się, błąd {e}")


    def add_stock(self):
        """
        Znajduje towar w magazynie, a następnie
        dodaje do magazynu liczbę sztuk istniejącego już towaru
        :return:
        """
        item_stock_ref = input("Podaj numer magazynowy: ")
        item = self.__shop.find_stock_item(item_stock_ref)

        if item == None:
            print ("Nie znaleziono towaru")
            return

        print(item)

        number_to_add = int(input("Podaj ilość towaru do dodania: "))
        if number_to_add == 0:
            print ("Nic nie dodano")

        elif number_to_add > StockItem.max_stock_add:
            print(f"Zbyt duża liczba, maksymalnie możesz dodać {StockItem.max_stock_add} sztuk towaru")

        else:
            item.add_stock(number_to_add)
            print(item)

    def sell_stock(self):
        """
        Sprzedaż towaru. Wyszukuje towar, następnie odczytuje liczbę sztuk na sprzedaż.
        Pozwala na zakup maksymalnie takiej ilości jaka jest w magazynie.
        :return:
        """
        print("Sprzedaż")

        item_stock_ref = input("Podaj numer magazynowy: ")
        item = self.__shop.find_stock_item(item_stock_ref)

        if item == None:
            print ("Nie znaleziono towaru")
            return

        print(f"Sprzedaż {item}")
        if item.__stock_level == 0:
            print("Brak towaru w magazynie")
            return

        number_sold = int(input("Ile sztuk sprzedano? (0 aby wyjść): "))

        if number_sold == 0:
            print("Zaniechano sprzedaży")
            return

        if number_sold > item.__stock_level:
            print(f"Brak wystarczającej ilości towaru w magazynie. Maksymalna ilość: {item.stock_level}")
            return

        item.sell_stock(number_sold)
        print("Sprzedano towar")

    def do_report(self):
        print("Raport magazynowy")
        print(self.__shop)

    def main_menu(self):
        prompt = """Sklep odzieżowy
        1. Stwórz nowy towar magazynowy
        2. Dostawa towaru do magazynu
        3. Sprzedaż towaru
        4. Raport magazynowy
        5. Wyjście
        Wprowadź polecenie: """

        while True:
            try:
                command = int(prompt)
                if command == 1:
                    self.create_new_stock_item()
                elif command == 2:
                    self.add_stock()
                elif command == 3:
                    self.sell_stock()
                elif command == 4:
                    self.do_report()
                elif command == 5:
                    self.__shop.save(self.__filename)
                    print ("Zapisano dane sklepu")
                    break
                else:
                    print("Coś poszło nie tak, spróbuj jeszcze raz")
                    continue
            except:
                print("Coś poszło nie tak, spróbuj jeszcze raz")
                continue


ui = FashionStoreShellApp("fashionstore.pickle")
