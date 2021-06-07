# Remember to put string in '' when writing query

def prevent(target):
    if target.find('=') != -1 or target.find("'") != -1 or target.find('#') != -1:
        return False  #Illegal character detected
    else:
        return True

def tryLogin(Acc, pwd):
    import sqlite3
    import hashlib
    m = hashlib.md5()

    data = {'Passed' : False, 'Phone' : ''}

    if prevent(Acc) == False or prevent(pwd) == False:
        print("Not passed")
        return data        
    
    query = \
        "select username, pwd, phone \
        from user \
        where username = '" + str(Acc) + "'"

    db = sqlite3.connect("data.db")
    cursor = db.cursor()
    cursor.execute(query)
    row = cursor.fetchone()

    print(row)

    if row == None:
        print("Not passed")
        db.close()
        return data
    
    else:
        m.update(pwd.encode('utf-8'))
        h = m.hexdigest()

        if h == row[1]:
            print("Passed")
            db.close()
            data['Passed'] = True
            data['Phone'] = row[2]
            return data
        else:
            print("Not passed")
            db.close()
            return data


def tryRegister(Acc, Pwd, ConPwd, Phone):
    import sqlite3
    import hashlib
    import random
    m = hashlib.md5()

    data = {'0': "", '1': "", '2': "", '3': ""}

    noEx = True

    if Acc == "":
        data['0'] = "Required!"
        noEx = False
    if Pwd == "":
        data['1'] = "Required!"
        noEx = False
    if ConPwd == "":
        data['2'] = "Required!"
        noEx = False
    if Phone == "":
        data['3'] = "Required!"
        noEx = False
    if Pwd != ConPwd:
        data['2'] = "Password_mismatch"
        noEx = False
    if Pwd.isalnum() == False and Pwd != "":
        data['1'] = "Invalid password format"
        noEx = False
    if Phone.isdigit() == False and Phone != "":
        data['3'] = "Invalid phone format"
        noEx = False
    #error here when register
        '''
    if target(Acc) == False:
        data['0'] = "Illegal character detected"
        noEx = False     
        ''' 

    if not noEx:
        return data

    query1 = \
    "select username\
    from user\
    where username = '" + str(Acc) + "'"

    print(query1)

    db = sqlite3.connect("data.db")
    print(db)
    cursor = db.cursor()
    print(cursor)
    cursor.execute(query1)
    #error here no such column username

    row = cursor.fetchall()
    print(row)

    if row != []:
        print("repeated")
        data['0'] = "Username is repeated"
        noEx = False
    
    if noEx:
        data['0'] = "Register success!"
        print("insert")
        m.update(Pwd.encode('utf-8'))
        h = m.hexdigest()

        U_ID = str(random.randint(1000000,9999999))

        query2 = "insert into user\
        values('" + U_ID + "','" + str(Acc) + "','" + str(h) + "','" + str(Phone) + "')"
        print(query2)

        cursor.execute(query2)
        db.commit()       
        
    db.close()
    return data


def tryRegisterShop(Shop,City,Price,Amount,name):
    import sqlite3
    import random
    Price.replace(' ','')
    Amount.replace(' ','')
    data = {'0': "", '1': "", '2': "", '3': ""}
    noEx = True
    db = sqlite3.connect("data.db")

    if Shop == "":
        data['0'] = "Required!"
        noEx = False
    if City == "":
        data['1'] = "Required!"
        noEx = False
    if Price == "":
        data['2'] = "Required!"
        noEx = False
    if Amount == "":
        data['3'] = "Required!"
        noEx = False
    if Price.isdigit() == False:
        data['2'] = "Invalid format"
        noEx = False
    if Amount.isdigit() == False:
        data['3'] = "Invalid format"
        noEx = False
    #error name target is not defined
    if target(Shop) == False:
        data['0'] = "Illegal character detected"
        noEx = False        
    
    if noEx == False:
        db.close()
        return data

    query1 = "select shopname\
        from shop\
        where shopname = '" + str(Shop) + "'"

    cursor = db.cursor()
    cursor.execute(query1)

    if cursor.fetchone() != None:
        data['0'] = "Shopname repeated"
        db.close()
        return data
    else:
        S_ID = str(random.randint(100000, 999999))
        query2 = "insert into shop\
            values('" + S_ID + "','" + str(Shop) + "','" + str(City) + "','" + str(name) + "'," + str(Price) + "," + str(Amount) + ")" 
        cursor.execute(query2)
        db.commit()   
        data['0'] = 'Register Success'
    db.close()
    return data


def getCities():
    import sqlite3
    query = "select distinct city \
    from shop"

    data = []

    db = sqlite3.connect("data.db")
    cursor = db.execute(query)
    for row in cursor:
        print(str(row[0]))
        data.append(str(row[0]))
    return data


def searchShopList(Shop,City,LowPrice,HighPrice,Amount,only,name):
    import sqlite3
    data = {'data':[]}
    query = \
    "select shopname, city, price, amount \
    from shop\
    where "
    if LowPrice != "" and HighPrice != "":
        if int(LowPrice) > int(HighPrice):
            tmp = LowPrice
            LowPrice = HighPrice
            HighPrice = tmp

    if Shop != "" and prevent(Shop) != False:
        query += "shopname like '%" + str(Shop) + "%' and  "
    if City != "All":
        query += "city = '" + str(City) + "' and  "
    if LowPrice != "" and prevent(LowPrice) != False:
        query += "price >= " + str(LowPrice) + " and  "
    if HighPrice != "" and prevent(HighPrice) != False:
        query += "price <= " + str(HighPrice) + " and  "
    if Amount != "All":
        if Amount == "0":
            query += "amount = 0 and  "
        if Amount == "1~99":
            query += "amount >= 1 and amount <= 99 and  "
        if Amount == "100+":
            query += "amount >= 100 and  "
    if only == "true":
        query += "( shopname in (select shopname from shop natural join employee where username = '" + str(name) + "') or shopname in (select shopname from shop where shopowner = '" + str(name) + "') )      "
    query = query[0:-6]

    print(query)
    db = sqlite3.connect("data.db")
    cursor = db.execute(query)
    for row in cursor:
        insert = []
        for i in range(len(row)):
            insert.append(row[i])
        data['data'].append(insert)

    return data


def EmployeesOfShop(Shop):
    import sqlite3
    query = "select username, phone\
    from employee natural join user \
    where shopname = '" + str(Shop) + "'"

    data = []

    db = sqlite3.connect("data.db")
    cursor = db.execute(query)
    for row in cursor:
        insert = []
        insert.append(row[0])
        insert.append(row[1])
        data.append(insert)

    return data


def hasShop(name):
    import sqlite3
    data = {'HasShop': False , 'Shop': "", 'City': "", 'Price': 0, 'Amount': 0 }

    query = "select shopname, city, price, amount \
    from shop \
    where shopowner = '" + str(name) + "'"

    db = sqlite3.connect("data.db")
    cursor = db.cursor()
    cursor.execute(query)
    row = cursor.fetchone()

    if row != None:
        data['HasShop'] = True
        data['Shop'] = row[0]
        data['City'] = row[1]
        data['Price'] = row[2]
        data['Amount'] = row[3]

    return data


def AddEmployee(shop, employee):
    import sqlite3
    data = {"data": ""}

    db = sqlite3.connect("data.db")

    query = "select username\
        from user\
        where username = '" + str(employee) + "'"
    cursor = db.execute(query)
    if cursor.fetchone() == None:
        data["data"] = "No result"
        return data        

    query1 = "select shopname, username\
        from employee\
        where shopname = '" + str(shop) + "' and username = '" + str(employee) + "'"
    cursor = db.execute(query1)

    if cursor.fetchone() != None:
        data["data"] = str(employee) + " is already in " + str(shop)
        return data
    else:
        query2 = "insert into employee\
            values('" + str(employee) + "','" + str(shop) + "')"
        cursor = db.execute(query2)
        db.commit()
        data["data"] = "Employee successfully added"
        return data


def DelEmployee(shop, employee):
    import sqlite3
    data = {"data": ""}

    db = sqlite3.connect("data.db")
    query1 = "select shopname, username\
        from employee\
        where shopname = '" + str(shop) + "' and username = '" + str(employee) + "'"
    cursor = db.execute(query1)

    if cursor.fetchone() == None:
        data["data"] = str(employee) + " is not in " + str(shop)
        return data
    else:
        query2 = "delete from employee\
            where shopname = '" + str(shop) + "' and username = '" + str(employee) + "'"
        cursor = db.execute(query2)
        db.commit()
        data["data"] = "Employee successfully deleted"
        return data

def PriceChange(Shop, Price):
    import sqlite3
    Price.replace(' ','')
    data = {"data": ""}
    db = sqlite3.connect("data.db")

    if Price.isdigit() == False:
        data["data"] = "Invalid format"
        return data
    if int(Price) < 0:
        data["data"] = "Invalid value"
        return data
    
    query = "update shop\
        set price = " + str(Price) + " where shopname = '" + str(Shop) + "'"
    cursor = db.execute(query)
    db.commit()
    data["data"] = "Price succesfully changed"
    return data


def AmountChange(Shop, Amount):
    import sqlite3
    Amount.replace(' ','')
    data = {"data": ""}
    db = sqlite3.connect("data.db")

    if Amount.isdigit() == False:
        data["data"] = "Invalid format"
        return data
    if int(Amount) < 0:
        data["data"] = "Invalid value"
        return data

    query = "update shop\
        set amount = " + str(Amount) + " where shopname = '" + str(Shop) + "'"
    cursor = db.execute(query)
    db.commit()
    data["data"] = "Amount succesfully changed"
    return data

# return like searchShopList
# OID Status Start End Shop Total Price
def searchShopOrderList(Shop,Status):
    import sqlite3
    data = {'data':[]}

    print(Shop)
    print(Status)

    query = \
    "select ID, stat, time_start, time_end, shopname, order_amount, price\
    from (order_ natural join shop)\
    where "
    if Shop != "All":
        query += "shopname like '%" + str(Shop) + "%' and  "
    if Status != "All":
        query += "stat = '" + str(Status) + "' and  "
    query = query[0:-6]

    print(query)

    db = sqlite3.connect("data.db")
    cursor1 = db.execute(query)

    for row in cursor1:
        insert = []
        for i in range(len(row) - 1):
            insert.append(row[i])
        price = int(row[-1]) * int(row[-2])
        insert.append(price)
        data['data'].append(insert)

    return data

#return all Shops in a list
def getShops():
    import sqlite3
    data = []
    query = \
    "select shopname\
    from shop"

    db = sqlite3.connect("data.db")
    cursor = db.execute(query)

    for row in cursor:
        data.append(str(row[0]))
    
    return data

# return message: success or fail and why
def Order(Shop,Amount):
    import sqlite3
    data = {"data": ""}
    if Amount.isdigit() == False or int(Amount) < 0:
        data["data"] = "Illegal input Amount"
        return data
    
    query = "select amount\
    from shop\
    where shopname = '" + str(Shop) + "'"

    db = sqlite3.connect("data.db")
    cursor = db.execute(query)
    row = cursor.fetchone()

    inventory = int(row[0])

    if int(Amount) > inventory:
        data["data"] = "Amount is larger than the inventory of the shop"
        return data
    
    data = "Successfully ordered"

    '''change = inventory - int(Amount)

    query = "update shop\
    set amount = " + str(change) + " where shopname = '" + str(Shop) + "'" 
    cursor = db.execute(query)
    db.commit()
    data["data"] = "Amount succesfully changed"'''

    return data

# return message: success or fail and why
def DelOrder(OID):
    import sqlite3
    data = {"data": ""}
    query = "select ID\
    from order_\
    where ID = '" + str(OID) + "'"

    db = sqlite3.connect("data.db")
    cursor = db.execute(query)
    row = cursor.fetchone()

    if row == None:
        data["data"] = "Order doesn't exist"

    query1 = "delete from order_\
    where ID = '" + str(OID) + "'"
