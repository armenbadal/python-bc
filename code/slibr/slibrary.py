import bibitem



class Library:
    def __init__(self):
        self.items = {}

    def addItem(self, item):
        self.items[item] = 1
    







#
#
#
b0 = bibitem.Book('A', 'B', 'C', 1900)
j0 = bibitem.asJson(b0)
print(j0)

b1 = bibitem.Magazine('D', 1920, 4)
j1 = bibitem.asJson(b1)
print(j1)


