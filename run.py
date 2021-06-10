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
    return jsonify(data)

@app.route('/home')
def homePage():
    if Acc == '':
        return render_template('login.html')
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
    return jsonify(data)

@app.route('/shop')
def shopPage():
    if Acc == '':
        return render_template('login.html')
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
    
# New Stuff!


@app.route('/myOrder')
def myOrder():
    if Acc == '':
        return render_template('login.html')
    Status = ['All','Not Finished','Finished','Cancelled']
    return render_template('myOrder.html',Status=Status)

@app.route('/_searchMyOrderList', methods=['GET'])
def _searchMyOrderList():
    from queryfunc import searchMyOrderList
    Status = request.args.get('Status')
    data = searchMyOrderList(Acc,Status)
    # return like searchShopList
    # orders by this Acc
    # OID Status Start End Shop Total Price
    return jsonify(data)

@app.route('/_searchShopOrderList', methods=['GET'])
def _searchShopOrderList():
    from queryfunc import searchShopOrderList
    _Shop = request.args.get('Shop')
    Status = request.args.get('Status')
    data = searchShopOrderList(_Shop,Status)
    return jsonify(data)

@app.route('/shopOrder')
def shopOrder():
    if Acc == '':
        return render_template('login.html')
    from queryfunc import getAccShops
    Shops = getAccShops(Acc)
    #return all Shops which Acc works in in a list
    Status = ['All','Not Finished','Finished','Cancelled']
    return render_template('shopOrder.html',Status=Status,Shops=Shops)

@app.route('/_Order', methods=['GET'])
def _Order():
    from queryfunc import Order
    Amount = request.args.get('Amount')
    _Shop = request.args.get('Shop')
    data = Order(Acc,_Shop,Amount)
    # return message: success or fail and why
    return jsonify(data)

@app.route('/_DelOrder', methods=['GET'])
def _DelOrder():
    from queryfunc import DelOrder
    OID = request.args.get('OID')
    data = DelOrder(Acc,OID)
    # return message: success or fail and why
    return jsonify(data)

@app.route('/_DoneOrder', methods=['GET'])
def _DoneOrder():
    from queryfunc import DoneOrder
    OID = request.args.get('OID')
    data = DoneOrder(Acc,OID)
    # return message: success or fail and why
    return jsonify(data)

@app.route('/_DoneAllOrder', methods=['GET'])
def _DoneAllOrder():
    from queryfunc import DoneAllOrder
    print(("here"))
    OIDs = request.args.get('OIDs').split()
    data = DoneAllOrder(Acc,OIDs)
    # return message: success or fail and why
    return jsonify(data)

@app.route('/_DelAllOrder', methods=['GET'])
def _DelAllOrder():
    from queryfunc import DelAllOrder
    print(("=============================="))
    OIDs = request.args.get('OIDs').split()
    print(OIDs)
    print(("=============================="))
    data = DelAllOrder(Acc,OIDs)
    # return message: success or fail and why
    return jsonify(data)
