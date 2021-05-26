from flask import Flask, render_template, request, jsonify
from datetime import timedelta
import json

app = Flask(__name__)

#config
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)
Acc = ''
Phone = ''
Shop = ''
#helios
@app.route('/')
def loginPage():
    global Acc
    global Phone
    global Shop
    Acc = ''
    Phone = ''
    Shop = ''
    return render_template('login.html')

@app.route('/_login', methods=['GET'])
def index():
    from queryfunc import tryLogin
    global Acc
    global Phone
    Acc = request.args.get('Account')
    Password = request.args.get('Password')
    data = tryLogin(Acc,Password)
    if data['Passed']:
        Phone = data['Phone']
    return jsonify(data)

@app.route('/register')
def registerPage():
    return render_template('register.html')

@app.route('/_register', methods=['GET'])
def _tryRegister():
    from queryfunc import tryRegister
    Acc = request.args.get('Account')
    Pwd = request.args.get('Password')
    ConPwd = request.args.get('ConfirmPassword')
    Phone = request.args.get('PhoneNumber')
    data = tryRegister(Acc,Pwd,ConPwd,Phone)
    #data = {0:'',1:'yoyo',2:'3030',3:'400'}
    return jsonify(data)

@app.route('/home')
def homePage():
    from queryfunc import getCities
    Cities = getCities()
    Cities.insert(0,'All')
    Amounts = ['All','0','1~99','100+']
    return render_template('index.html',Acc=Acc,Phone=Phone,Cities = Cities,Amounts = Amounts)

@app.route('/_searchShopList', methods=['GET'])
def _searchShopList():
    from queryfunc import searchShopList
    Shop = request.args.get('Shop')
    City = request.args.get('City')
    LowPrice = request.args.get('LowPrice')
    HighPrice = request.args.get('HighPrice')
    Amount = request.args.get('Amount')
    WorkOnly = request.args.get('WorkOnly')
    data = searchShopList(Shop,City,LowPrice,HighPrice,Amount,WorkOnly,Acc)
    #data = {'data':[['a','b','c','d'],['f','g','h','j']]}
    return jsonify(data)

@app.route('/shop')
def shopPage():
    from queryfunc import EmployeesOfShop, hasShop, getCities
    global Shop
    Cities = getCities()
    dic = hasShop(Acc)
    HasShop = dic['HasShop']
    MyShop = dic['Shop']
    MyCity = dic['City']
    MyPrice = dic['Price']
    MyAmount = dic['Amount']
    Employees = EmployeesOfShop(MyShop)
    #Employees = [['helios','0900'],['helios','09002']]
    if(HasShop==True):
        Shop = MyShop
        return render_template('shop.html',MyShop=MyShop,MyCity=MyCity,MyPrice = MyPrice,MyAmount = MyAmount,Employees=Employees)
    return render_template('registerShop.html',Cities=Cities)

@app.route('/_registerShop', methods=['GET'])
def _tryRegisterShop():
    from queryfunc import tryRegisterShop
    Shop = request.args.get('Shop')
    City = request.args.get('City')
    Price = request.args.get('Price')
    Amount = request.args.get('Amount')
    data = tryRegisterShop(Shop,City,Price,Amount,Acc)
    #data = {0:'',1:'yoyo',2:'3030',3:'400'}
    return jsonify(data)

@app.route('/_AddEmployee', methods=['GET'])
def _AddEmployee():
    from queryfunc import AddEmployee
    Employee = request.args.get('Employee')
    data = AddEmployee(Shop,Employee)
    return jsonify(data)

@app.route('/_DelEmployee', methods=['GET'])
def _DelEmployee():
    from queryfunc import DelEmployee
    Employee = request.args.get('Employee')
    data = DelEmployee(Shop,Employee)
    return jsonify(data)

@app.route('/_PriceChange', methods=['GET'])
def _PriceChange():
    from queryfunc import PriceChange
    Price = request.args.get('Price')
    data = PriceChange(Shop,Price)
    return jsonify(data)

@app.route('/_AmountChange', methods=['GET'])
def _AmountChange():
    from queryfunc import AmountChange
    Amount = request.args.get('Amount')
    data = AmountChange(Shop,Amount)
    return jsonify(data)
'''
@app.route('/disease')
def index2():
    from queryfunc import commonCountry
    Countrylist = commonCountry()
    return render_template('index2.html', Countrylist=Countrylist)


#page 1
@app.route('/_stockdate', methods=['GET'])
def stockdateinfoquery():
    from queryfunc import stockdateinfo
    specdate = request.args.get('Date')
    data = stockdateinfo(specdate)
    print(data)
    return jsonify(data)


@app.route('/_history', methods=['GET'])
def historyquery():
    from queryfunc import historyrecord
    data = historyrecord()
    #print(data)
    return jsonify(data)

@app.route('/_historydel')
def historydelquery():
    from queryfunc import historydel
    data = historydel()
    #print(data)
    return jsonify(data)

@app.route('/_worldcovidvsstock', methods=['GET'])
def worldcovidvsstockquery():
    from queryfunc import worldcovidvsstock
    data = worldcovidvsstock()
    #print(data)
    return jsonify(data)

@app.route('/_UScovidvsstock', methods=['GET'])
def UScovidvsstockquery():
    from queryfunc import UScovidvsstock
    data = UScovidvsstock()
    #print(data)
    return jsonify(data)

@app.route('/_twcovidvsstock', methods=['GET'])
def twcovidvsstockquery():
    from queryfunc import twcovidvsstock
    data = twcovidvsstock()
    #print(data)
    return jsonify(data)

@app.route('/_regionRate', methods=['GET'])
def regionRatequery():
    from queryfunc import regionRateinfo
    region = request.args.get('Region')
    data = regionRateinfo(region)
    #print(data)
    return jsonify(data)

#page 2
@app.route('/_regionCovid19Case')
def regionCovid19Casequery():
    from queryfunc import regionCovid19Case
    data = regionCovid19Case()
    #print(data)
    return jsonify(data)

@app.route('/_regionCovid19Death')
def regionCovid19Deathquery():
    from queryfunc import regionCovid19Death
    data = regionCovid19Death()
    #print(data)
    return jsonify(data)

@app.route('/_regionMaxDeathMon', methods=['GET'])
def regionMaxDeathMonquery():
    from queryfunc import regionMaxDeathMoninfo
    region = request.args.get('Region')
    data = regionMaxDeathMoninfo(region)
    #print(data)
    return jsonify(data)

@app.route('/_regionMaxCaseMon', methods=['GET'])
def regionMaxCaseMonquery():
    from queryfunc import regionMaxCaseMoninfo
    region = request.args.get('Region')
    data = regionMaxCaseMoninfo(region)
    #print(data)
    return jsonify(data)

@app.route('/_regionSARSCase')
def regionSARSCasequery():
    from queryfunc import regionSARSCase
    data = regionSARSCase()
    #print(data)
    return jsonify(data)

@app.route('/_regionSARSDeath')
def regionSARSDeathquery():
    from queryfunc import regionSARSDeath
    data = regionSARSDeath()
    #print(data)
    return jsonify(data)

@app.route('/_regionSARSMaxCaseMon', methods=['GET'])
def regionSARSMaxCaseMonquery():
    from queryfunc import regionSARSMaxCaseMoninfo
    region = request.args.get('Region')
    data = regionSARSMaxCaseMoninfo(region)
    #print(data)
    return jsonify(data)

@app.route('/_regionSARSMaxDeathMon', methods=['GET'])
def regionSARSMaxDeathMonquery():
    from queryfunc import regionSARSMaxDeathMoninfo
    region = request.args.get('Region')
    data = regionSARSMaxDeathMoninfo(region)
    #print(data)
    return jsonify(data)

@app.route('/_countryinfo', methods=['GET'])
def countryinfoquery():
    from queryfunc import countryinfo
    country = request.args.get('Country')
    data = countryinfo(country)
    #print(data)
    return jsonify(data)
    '''