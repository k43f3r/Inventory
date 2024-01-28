import mysql.connector
from datetime import datetime

database = mysql.connector.connect(
    host="localhost",
    user="inventory",
    passwd="inventory",
    database="inventory"
)

mycursor = database.cursor(buffered=True)

# mycursor.execute("CREATE TABLE Hardware (equipmentnr int UNSIGNED, geraetenr int UNSIGNED, name VARCHAR(50)")
mycursor.execute("DESCRIBE Hardware")

# insert
#mycursor.excecute("INSERT INTO Hardware (equipmentnr, geraetenr, name) VALUES ('123456', '123', 'Antenne X')")
#mycursor.execute("INSERT INTO Hardware (equipmentnr NOT NULL, geraetenr, name, created datetime NOT NULL) VALUES (%s,%s,%s)", (123456, 123, "Antenne X"))
# datetime.now()
#database.commit()

# mycursor.execute("SELECT * FROM Inventory, x, ... WHERE equipmentnr = '123456' ORDER BY equipmentnr DESC/AESC")
# mycursor.execute("ALTER TABLE Inventory ADD COLUMN quantity VARCHAR(59) NOT NULL")
# mycursor.execute("SELECT * FROM Hardware")
mycursor.execute("ALTER TABLE Inventory DROP quantity")
mycursor.execute("ALTER TABLE Inventory CHANGE name first;name VARCHAR(50)")


for x in mycursor:
    print(x)