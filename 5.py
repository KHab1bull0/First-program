import mysql.connector
from colorama import Fore, init
init(autoreset=True)

class Database:
    def __init__(self) -> None:
        self.db = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'rootor'
        )
           
        self.cursor = self.db.cursor()
        
        self.createdb()
        self.create_table()
        
    def createdb(self):
        try:
            query = 'CREATE DATABASE IF NOT EXISTS EXAM;'
        
            self.cursor.execute(query)
            print(Fore.GREEN + 'Ulandi')
        except:
            print(Fore.RED + 'Ulanmadi')
            
            
    def create_table(self):
        try:
            query = """
            CREATE TABLE IF NOT EXISTS BOOKSHOP(
                ID INT AUTO_INCREMENT PRIMARY KEY,
                Name VARCHAR(50),
                Author VARCHAR(50),
                Year INT,
                Price REAL,
                Sale INT,
                Genre VARCHAR(50),
                Page  INT
            );"""
            
            self.cursor.execute(query)
            self.db.commit()
            
            print(Fore.GREEN + 'Succes table')
        except:
            print(Fore.RED + 'Error')
        
        
    def insert(self):
        
        query = 'INSERT INTO '
        
        
if __name__ == "__main__":
    db = Database()