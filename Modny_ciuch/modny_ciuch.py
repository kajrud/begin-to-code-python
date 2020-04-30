import Modny_ciuch.model as mc

dress=mc.Dress("D500", 150, "red", "wieszaki", "bodycon", "M")
dress.add_stock(10)
pants = mc.Pants("P450", 120, "black", "półki koło przymierzalni", "32", "cygaretki", 27)
pants.add_stock(20)
shop = mc.FashionStore("Tani Armani")
shop.store_new_stock_item(dress)
shop.store_new_stock_item(pants)
print(shop)

ui = mc.FashionStoreShellApp(fashionstore.pickle)

