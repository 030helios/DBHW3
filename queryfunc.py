# Remember to put string in '' when writing query

def tryLogin(Acc, pwd):
    import sqlite3
    import hashlib
    m = hashlib.md5()

    data = {'Passed' : False, 'Phone' : ''}
    
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

    if Shop != "":
        query += "shopname like '%" + str(Shop) + "%' and  "
    if City != "All":
        query += "city = '" + str(City) + "' and  "
    if LowPrice != "":
        query += "price >= " + str(LowPrice) + " and  "
    if HighPrice != "":
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


'''
def stockdateinfo(date):
    import sqlite3

    query = \
    "select t.Date_reported as Date, covid19.cases as Total_cases, (tw.International_cases+tw.National_cases) as TW_cases, d.Adj_Close as Dow_AdjClose, t.Adj_Close as TsecIndex_AdjClose\
    from tsec_index as t, dowjone as d, \
	(select covid19.Date_reported as Date, sum(covid19.New_cases)as cases \
	from who_covid_19 as covid19 \
	group by covid19.Date_reported) as covid19, tw_covid_19 as tw\
    where t.Date_reported = d.Date_reported\
    and covid19.Date = d.Date_reported\
    and tw.Date_reported = d.Date_reported\
    and t.Date_reported = '" + str(date) + "'"

    db = sqlite3.connect('data.db')
    cursor = db.execute(query)
    data = {
        'Header': [],
        'Data': []
    }
    header = list(map(lambda x: x[0], cursor.description))
    data['Header'] = header
    for row in cursor:
        tmp = []
        for i in range(len(row)):
            tmp.append(row[i])
        data['Data'].append(tmp)

    #insert the stock query history record    
    if len(data['Data']) != 0:
        date = data['Data'][0][0]
        #print(str(date))
        record = "replace into history values('" + data['Data'][0][0] + "','" + str(data['Data'][0][1]) + "','" + str(data['Data'][0][2]) + "','" + str(data['Data'][0][3]) + "','" + str(data['Data'][0][4]) + "')"
        cursorObj = db.cursor()
        cursorObj.execute(record)
        db.commit()
    db.close()
    return data
    
def worldcovidvsstock():
    import sqlite3
    query = \
    "select WLD.Date as Date, WLD.Cum_case as Daily_cumulative_case, dowjone.Adj_close as DJI\
    from (\
    select Date_reported as Date, SUM(New_cases) as Cum_case from who_covid_19\
    group by Date_reported\
    ) as WLD, dowjone\
    where WLD.Date = dowjone.Date_reported"

    db = sqlite3.connect('data.db')
    cursor = db.execute(query)
    data = {
        'Data': []
    }
    header = list(map(lambda x: x[0], cursor.description))
    data['Data'].append(header)
    for row in cursor:
        tmp = []
        for i in range(len(row)):
            tmp.append(row[i])
        data['Data'].append(tmp)
    db.close()
    return data

def twcovidvsstock():
    import sqlite3
    query = \
    "select substr(t.Date, 1, 6) as Date, covid.cases as Total_Cases, tw.TW_cases as TW_cases, t.TSEC_AdjClose as TSEC_AdjClose\
    from (\
	select SUBSTR(t.Date_reported, 1, 7) as Date, avg(t.Adj_Close) as TSEC_AdjClose\
	from tsec_index as t\
	group by Date\
	) as t,\
	(\
	select SUBSTR(covid19.Date_reported, 1, 7) as Date, Sum(covid19.New_cases) as cases\
	from who_covid_19 as covid19\
	group by Date) as covid,\
	(\
	select SUBSTR(tw.Date_reported, 1, 7) as Date, Sum(tw.International_cases+tw.National_cases) as TW_cases\
	from tw_covid_19 as tw\
	group by Date\
	) as tw\
    where t.Date = covid.Date\
    and tw.Date = covid.Date"

    db = sqlite3.connect('data.db')
    cursor = db.execute(query)
    data = {
        'Data': []
    }
    header = list(map(lambda x: x[0], cursor.description))
    data['Data'].append(header)
    for row in cursor:
        tmp = []
        for i in range(len(row)):
            tmp.append(row[i])
        data['Data'].append(tmp)
    db.close()
    return data

def UScovidvsstock():
    import sqlite3
    query = \
    "select substr(d.Date, 1, 6) as Date, covid.cases as Total_Cases, covid_US.cases as US_Cases, d.Dow_AdjClose as Dow_AdjClose\
    from (\
	select SUBSTR(d.Date_reported, 1, 7) as Date, avg(d.Adj_Close) as Dow_AdjClose\
	from dowjone as d\
	group by Date\
	) as d, \
	(\
	select SUBSTR(covid19.Date_reported, 1, 7) as Date, Sum(covid19.New_cases) as cases, covid19.Country_code as Country\
	from who_covid_19 as covid19\
	where covid19.Country_code = 'US'\
	group by Date) as covid_US,\
	(\
	select SUBSTR(covid19.Date_reported, 1, 7) as Date, Sum(covid19.New_cases) as cases\
	from who_covid_19 as covid19\
	group by Date) as covid\
    where d.Date = covid.Date\
    and d.Date = covid_US.Date"

    db = sqlite3.connect('data.db')
    cursor = db.execute(query)
    data = {
        'Data': []
    }
    header = list(map(lambda x: x[0], cursor.description))
    data['Data'].append(header)
    for row in cursor:
        tmp = []
        for i in range(len(row)):
            tmp.append(row[i])
        data['Data'].append(tmp)
    db.close()
    return data

def commonCountry():
    import sqlite3

    query = \
    "select distinct(who_covid_19.country) as Country\
    from who_covid_19, sars\
    where who_covid_19.Country = sars.Country"

    db = sqlite3.connect('data.db')
    cursor = db.execute(query)
    data = []
    for row in cursor:
        data.append(row[0])
    db.close()
    return data

def countryinfo(country):
    import sqlite3

    query = \
    "select cumulative_data.Country as Country, cumulative_data.covid19_cases as covid19_cumulative_cases, \
	   cumulative_data.covid19_deaths / (cumulative_data.covid19_cases+0.0) as covid19_death_rate, \
	   cumulative_data.sars_cases as sars_cumulative_cases, \
	   cumulative_data.sars_deaths / (cumulative_data.sars_cases+0.0) as sars_death_rate\
    from (\
	    select covid19.Country as Country, MAX(covid19.Cumulative_cases) as covid19_cases, \
	         MAX(covid19.Cumulative_deaths) as covid19_deaths, \
	         Max(sars.Cumulative_cases) as sars_cases, Max(sars.deaths) as sars_deaths\
	    from who_covid_19 as covid19, sars as sars\
	    where covid19.Country = sars.Country\
	    group by covid19.Country\
	    ) as cumulative_data\
    where Country LIKE '" + str(country) + "'"

    db = sqlite3.connect('data.db')
    cursor = db.execute(query)
    data = {
        'Header': [],
        'Data': []
    }
    header = list(map(lambda x: x[0], cursor.description))
    data['Header'] = header
    for row in cursor:
        tmp = []
        for i in range(len(row)):
            tmp.append(row[i])
        data['Data'].append(tmp)
    db.close()
    return data

def historyrecord(): 
    import sqlite3

    query = "select * from history"

    db = sqlite3.connect('data.db')
    cursor = db.execute(query)
    data = {
        'Header': [],
        'Data': []
    }
    header = list(map(lambda x: x[0], cursor.description))
    data['Header'] = header
    for row in cursor:
        tmp = []
        for i in range(len(row)):
            tmp.append(row[i])
        data['Data'].append(tmp)
    db.close()
    return data

def historydel():
    import sqlite3

    query = "delete from history;"
    db = sqlite3.connect('data.db')
    cursorObj = db.cursor()
    cursorObj.execute(query)
    db.commit()
    query = "select * from history;"
    cursor = db.execute(query)
    data = {
        'Header': [],
        'Data': []
    }
    header = list(map(lambda x: x[0], cursor.description))
    data['Header'] = header
    for row in cursor:
        tmp = []
        for i in range(len(row)):
            tmp.append(row[i])
        data['Data'].append(tmp)
    db.close()
    return data

def regionCovid19Case():
    import sqlite3

    query = "select substr(max_data.date, 1, 6) as date, DR_data.region as region, max_data.cases as cases\
    from (\
     select DR_data.date as date, MAX(DR_data.cases) as cases\
     from (\
	      select SUBSTR(covid19.Date_reported, 1, 7) as date, covid19.WHO_region as region, \
	             SUM(covid19.New_cases) as cases\
	      from who_covid_19 as covid19\
	      group by date, region\
          ) as DR_data\
     group by date\
     ) as max_data, \
     (\
     select SUBSTR(covid19.Date_reported, 1, 7) as date, covid19.WHO_region as region, \
	        SUM(covid19.New_cases) as cases\
	 from who_covid_19 as covid19\
	 group by date, region\
     ) as DR_data\
    where DR_data.cases = max_data.cases"\

    db = sqlite3.connect('data.db')
    cursor = db.execute(query)
    data = {
        'Header': [],
        'Data': []
    }
    header = list(map(lambda x: x[0], cursor.description))
    data['Header'] = header
    for row in cursor:
        tmp = []
        for i in range(len(row)):
            tmp.append(row[i])
        data['Data'].append(tmp)
    db.close()
    return data

def regionCovid19Death():
    import sqlite3
    query = "select substr(max_data.date, 1, 6) as date, DR_data.region as region, max_data.deaths as deaths\
    from (\
        select DR_data.date as date, MAX(DR_data.deaths) as deaths\
        from (\
	        select SUBSTR(covid19.Date_reported, 1, 7) as date, covid19.WHO_region as region, \
	             SUM(covid19.New_deaths) as deaths\
	        from who_covid_19 as covid19\
	        group by date, region\
        ) as DR_data\
        group by date\
     ) as max_data, \
     (\
     select SUBSTR(covid19.Date_reported, 1, 7) as date, covid19.WHO_region as region, \
	        SUM(covid19.New_deaths) as deaths\
	 from who_covid_19 as covid19\
	 group by date, region\
     ) as DR_data\
    where DR_data.deaths = max_data.deaths"

    db = sqlite3.connect('data.db')
    cursor = db.execute(query)
    data = {
        'Header': [],
        'Data': []
    }
    header = list(map(lambda x: x[0], cursor.description))
    data['Header'] = header
    for row in cursor:
        tmp = []
        for i in range(len(row)):
            tmp.append(row[i])
        data['Data'].append(tmp)
    db.close()
    return data

def regionMaxDeathMoninfo(region):
    import sqlite3
    query = "select substr(max_data.date,1,6) as date, DR_data.Country as Country, max_data.deaths as deaths\
    from (\
     select DR_data.date as date, MAX(DR_data.deaths) as deaths\
     from (\
	      select SUBSTR(covid19.Date_reported, 1, 7) as date, Country, covid19.WHO_region as region, SUM(covid19.New_deaths) as deaths\
	      from who_covid_19 as covid19\
		  where region = 'EMRO'\
	      group by date, Country\
          ) as DR_data\
     group by date\
     ) as max_data,\
	(\
	select SUBSTR(covid19.Date_reported, 1, 7) as date, Country, covid19.WHO_region as region, SUM(covid19.New_deaths) as deaths\
	from who_covid_19 as covid19\
	where region = '" + str(region) +"'\
    group by date, Country\
	) as DR_data\
    where DR_data.deaths = max_data.deaths"

    db = sqlite3.connect('data.db')
    cursor = db.execute(query)
    data = {
        'Header': [],
        'Data': []
    }
    header = list(map(lambda x: x[0], cursor.description))
    data['Header'] = header
    for row in cursor:
        tmp = []
        for i in range(len(row)):
            tmp.append(row[i])
        data['Data'].append(tmp)
    db.close()
    return data

def regionMaxCaseMoninfo(region):
    import sqlite3
    print(region)
    query = \
    "select substr(max_data.date, 1, 6) as date, DR_data.Country as Country, max_data.cases as cases\
    from (\
        select DR_data.date as date, MAX(DR_data.cases) as cases\
        from (\
	        select SUBSTR(covid19.Date_reported, 1, 7) as date, Country, covid19.WHO_region as region, SUM(covid19.New_cases) as cases\
	        from who_covid_19 as covid19\
		    where region = '"+ str(region)+"'\
	        group by date, Country\
          ) as DR_data\
        group by date\
     ) as max_data,\
	(\
	select SUBSTR(covid19.Date_reported, 1, 7) as date, Country, covid19.WHO_region as region, SUM(covid19.New_cases) as cases\
	from who_covid_19 as covid19\
	where region = '"+ str(region)+"'\
    group by date, Country\
	) as DR_data\
    where DR_data.cases = max_data.cases"

    db = sqlite3.connect('data.db')
    cursor = db.execute(query)
    data = {
        'Header': [],
        'Data': []
    }
    header = list(map(lambda x: x[0], cursor.description))
    data['Header'] = header
    for row in cursor:
        tmp = []
        for i in range(len(row)):
            tmp.append(row[i])
        data['Data'].append(tmp)
    db.close()
    return data

def regionSARSDeath():
    import sqlite3
    with open('sql/region_death_sars.sql') as f:
        query = f.read()
    db = sqlite3.connect('data.db')
    
    cursor = db.execute(query)
    data = {
        'Header': [],
        'Data': []
    }
    header = list(map(lambda x: x[0], cursor.description))
    data['Header'] = header
    for row in cursor:
        tmp = []
        for i in range(len(row)):
            tmp.append(row[i])
        data['Data'].append(tmp)
    db.close()
    return data

def regionSARSCase():
    import sqlite3
    with open('sql/sars_region_cases.sql') as f:
        query = f.read()
    db = sqlite3.connect('data.db')
    
    cursor = db.execute(query)
    data = {
        'Header': [],
        'Data': []
    }
    header = list(map(lambda x: x[0], cursor.description))
    data['Header'] = header
    for row in cursor:
        tmp = []
        for i in range(len(row)):
            tmp.append(row[i])
        data['Data'].append(tmp)
    db.close()
    return data

def regionSARSMaxCaseMoninfo(region):
    import sqlite3
    if region == 'AFRO':
        with open('sql/sars_region_cases_AFRO.sql') as f:
            query = f.read()
    elif region == 'AMRO':
        with open('sql/sars_region_cases_AMRO.sql') as f:
            query = f.read()
    elif region == 'EMRO':
        with open('sql/sars_region_cases_EMRO.sql') as f:
            query = f.read()
    elif region == 'EURO':
        with open('sql/sars_region_cases_EURO.sql') as f:
            query = f.read()
    elif region == 'SEARO':
        with open('sql/sars_region_cases_SEARO.sql') as f:
            query = f.read()
    elif region == 'WPRO':
        with open('sql/sars_region_cases_WPRO.sql') as f:
            query = f.read()
        
    db = sqlite3.connect('data.db')
    cursor = db.execute(query)
    data = {
        'Header': [],
        'Data': []
    }
    header = list(map(lambda x: x[0], cursor.description))
    data['Header'] = header
    for row in cursor:
        tmp = []
        for i in range(len(row)):
            tmp.append(row[i])
        data['Data'].append(tmp)
    db.close()
    return data

def regionSARSMaxDeathMoninfo(region):
    import sqlite3
    if region == 'AFRO':
        with open('sql/sars_region_deaths_AFRO.sql') as f:
            query = f.read()
    elif region == 'AMRO':
        with open('sql/sars_region_deaths_AMRO.sql') as f:
            query = f.read()
    elif region == 'EMRO':
        with open('sql/sars_region_deaths_EMRO.sql') as f:
            query = f.read()
    elif region == 'EURO':
        with open('sql/sars_region_deaths_EURO.sql') as f:
            query = f.read()
    elif region == 'SEARO':
        with open('sql/sars_region_deaths_SEARO.sql') as f:
            query = f.read()
    elif region == 'WPRO':
        with open('sql/sars_region_deaths_WPRO.sql') as f:
            query = f.read()
        
    db = sqlite3.connect('data.db')
    cursor = db.execute(query)
    data = {
        'Header': [],
        'Data': []
    }
    header = list(map(lambda x: x[0], cursor.description))
    data['Header'] = header
    for row in cursor:
        tmp = []
        for i in range(len(row)):
            tmp.append(row[i])
        data['Data'].append(tmp)
    db.close()
    return data




def regionRateinfo(region):
    import sqlite3
    query =\
    "select Date, rate, Dow_Adj_Close_rate\
    from\
	    (select substr(covid19_rate.Date, 1, 6) as Date, covid19_rate.region as region, covid19_rate.rate as rate, \
		dow_rate.rate as Dow_Adj_Close_rate\
	from\
	(\
	select hola.bd as Date, hola.region as region, ((hola.bc-max(hola.ac))/max(hola.ac)) as rate\
	from	(\
	select a.Date as ad, b.Date as bd, a.region as region, a.cases as ac, b.cases as bc\
	from	(\
		select SUBSTR(covid19.Date_reported, 1, 7) as Date, covid19.WHO_region as region, sum(covid19.New_cases) as cases\
		from who_covid_19 as covid19\
		group by Date, region\
		) as a,\
		(\
		select SUBSTR(covid19.Date_reported, 1, 7) as Date, covid19.WHO_region as region, sum(covid19.New_cases) as cases\
		from who_covid_19 as covid19\
		group by Date, region\
		) as b\
	where a.Date < b.Date \
	and a.region = b.region\
	) as hola\
	group by hola.bd, hola.region\
	order by hola.region, hola.bd\
	) as covid19_rate, \
	(\
	select hola.bd as Date, ((hola.avg_close_b-max(hola.avg_close_a))/max(hola.avg_close_a)) as rate\
	from (\
		select month_data_a.Date as ad, month_data_b.Date as bd, month_data_a.avg_close as avg_close_a, month_data_b.avg_close as avg_close_b\
		from (\
			select SUBSTR(dow.Date_reported, 1, 7) as Date, AVG(dow.Adj_Close) as avg_close\
			from dowjone as dow\
			group by Date\
			) as month_data_a,\
			(\
			select SUBSTR(dow.Date_reported, 1, 7) as Date, AVG(dow.Adj_Close) as avg_close\
			from dowjone as dow\
			group by Date\
			) as month_data_b\
		where month_data_a.Date < month_data_b.Date\
		) as hola\
	group by Date\
	order by Date\
	) as dow_rate\
	where covid19_rate.Date = dow_rate.Date\
	order by region, Date\
	) as summary\
    where region = '" + str(region) + "'" 
    db = sqlite3.connect('data.db')
    
    cursor = db.execute(query)
    data = {
        'Data': []
    }
    header = list(map(lambda x: x[0], cursor.description))
    data['Data'].append(header)
    for row in cursor:
        tmp = []
        for i in range(len(row)):
            tmp.append(row[i])
        data['Data'].append(tmp)
    db.close()
    return data 
    '''