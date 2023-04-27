import mysql.connector


def insertProduct(name, price,imageUrl, description):
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Ysfsql!03",
        database = "node-app"
    )
    cursor = connection.cursor()

    sql = "insert into products (name , price, imageurl, description) values (%s,%s,%s,%s)"
    values = (name, price, imageUrl, description)

    cursor.execute(sql,values)
    
    try:
        connection.commit()
        print(cursor.rowcount,"tane kayıt eklendi")  #rowcount eklenen satır sayısını belirtir
        print("son eklenen ürürünü Id'si:", cursor.lastrowid)
    except mysql.connector.Error as err:
        print("hata", err)
    finally:
        connection.close()
        print("database bağlantısı kapatıldı") 

def insertProducts(list):
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Ysfsql!03",
        database = "node-app"
    )
    cursor = connection.cursor()

    sql = "insert into products (name , price, imageurl, description) values (%s,%s,%s,%s)"
    values = list

    cursor.executemany(sql,values)
    
    try:
        connection.commit()
        print(cursor.rowcount,"tane kayıt eklendi")  #rowcount eklenen satır sayısını belirtir
        print("son eklenen ürürünü Id'si:", cursor.lastrowid)
    except mysql.connector.Error as err:
        print("hata", err)
    finally:
        connection.close()
        print("database bağlantısı kapatıldı") 

def getProducts(): #Select function getting records from db
    connection = mysql.connector.connect(host = "localhost",user = "root",password = "Ysfsql!03",database = "node-app")
    cursor = connection.cursor()

    #cursor.execute("select * from products") #yyyy
    cursor.execute("select name,price from products") #xxx

    #result = cursor.fetchall() #allcolums
    result = cursor.fetchone() #one column
    print("name:",result[0],",price:",result[1])
    # for i in result:
    #     #print(i)
    #     # print("name:",i[1],",price:",i[2]) #yyyy
    #      print("name:",i[0],",price:",i[1])  #xxx
    # #print(result)

getProducts()