import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_title ON Products(title)")
    products = [
                ("Product1", "Витамин Д3 для вашей радости", "100"),
                ("Product2", "Витамин Железо для борьбы с анемией", "200"),
                ("Product3", "Коллаген для здоровой кожи, волос и ногтей", "300"),
                ("Product4", "Цинк в сезон простуд для иммунитета", "400")
            ]

    cursor.executemany(f"INSERT INTO Products(title, description, price) VALUES (?,?,?)", products )
    connection.commit()
def get_all_products():
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    connection.commit()
    connection.close()
    return products

if __name__ == "__main__":
    initiate_db()
    all_products = get_all_products()
    for product in all_products:
        print(product)

