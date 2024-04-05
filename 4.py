
class BookStore:
    def __init__(self, name: str, author: str, year: int, price: float) -> None:
        
        self.bookname = name
        self.bookauthor = author
        self.year = year
        self.price = price
        
class Library(BookStore):
    def __init__(self, name: str , author: str, year: int, price: float, sale: int) -> None:
        super().__init__(name, author, year, price)
        self.sale = sale
        
        
    def info(self):
        sale = self.price - (self.price//100) * self.sale
        return(f'''{self.bookname} {self.bookauthor} {self.year} {sale} ''')
  
# lis = []

# book = Library('hamsa', 'alisher navoiy', 2000, 500, 15)
# lis.append(book)
# book = Library('otkan kunlar', 'abdulla qodiriy', 2001, 100, 10)
# lis.append(book)
# book = Library('sariqdev ', 'xudoyberdi toxtaboyev', 2000, 200, 5)
# lis.append(book)
# book = Library('Boburnoma', 'Zahiriddin bobur', 2005, 300, 25)
# lis.append(book)
# book = Library('koinot', 'Mirzo Ulugbek', 2006, 400, 17)
# lis.append(book)
    
# for i in lis:
#     print(i.info())
 
# lis = []  
     
# for i in range(5):
#     name = input("Name: ")
#     author = input("Author: ")
#     year = int(input("Year: "))
#     price = float(input("Price: "))
#     sale = int(input("Sale: "))
    
#     book = Library(name, author, year, price, sale)
#     lis.append(book)

# for i in lis:
#     i.info()


