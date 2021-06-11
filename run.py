from flask import Flask, render_template, request, jsonify
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from datetime import timedelta
import json

app = Flask(__name__)
app.secret_key = 'dd06be55a06c03312b2ab109b5f8f6ab'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = "strong"
login_manager.login_view = 'logout'

# config
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)
class User(UserMixin):
    pass

# users to [phone,shop]
users = {}


@login_manager.user_loader
def user_loader(username):
    if username not in users:
        return

    user = User()
    user.id = username
    return user


@login_manager.request_loader
def request_loader(request):
    username = request.form.get('user_id')
    if username not in users:
        return

    user = User()
    user.id = username
    user.is_authenticated = request.form['password'] == users[username]['password']

    return user


@app.route('/')
def logout():
    logout_user()
    return render_template('login.html')


@app.route('/_login', methods=['GET'])
def index():
    from queryfunc import tryLogin
    Acc = request.args.get('Account')
    Password = request.args.get('Password')

    data = tryLogin(Acc, Password)
    if data['Passed']:
        Phone = data['Phone']
        users[Acc] = [Phone,'']
        user = User()
        user.id = Acc
        login_user(user)

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
    data = tryRegister(Acc, Pwd, ConPwd, Phone)
    return jsonify(data)


@app.route('/home')
@login_required
def homePage():
    from queryfunc import getCities
    Cities = getCities()
    Cities.insert(0, 'All')
    Amounts = ['All', '0', '1~99', '100+']
    Acc = current_user.get_id()
    return render_template('index.html', Acc=Acc, Phone=users[Acc][0], Cities=Cities, Amounts=Amounts)


@app.route('/_searchShopList', methods=['GET'])
def _searchShopList():
    from queryfunc import searchShopList
    Shop = request.args.get('Shop')
    City = request.args.get('City')
    LowPrice = request.args.get('LowPrice')
    HighPrice = request.args.get('HighPrice')
    Amount = request.args.get('Amount')
    WorkOnly = request.args.get('WorkOnly')
    Acc = current_user.get_id()
    data = searchShopList(Shop, City, LowPrice,HighPrice, Amount, WorkOnly, Acc)
    return jsonify(data)


@app.route('/shop')
@login_required
def shopPage():
    from queryfunc import EmployeesOfShop, hasShop, getCities
    Acc = current_user.get_id()
    Cities = getCities()
    dic = hasShop(Acc)
    HasShop = dic['HasShop']
    MyShop = dic['Shop']
    MyCity = dic['City']
    MyPrice = dic['Price']
    MyAmount = dic['Amount']
    Employees = EmployeesOfShop(MyShop)
    if(HasShop == True):
        users[Acc][1] = MyShop
        return render_template('shop.html', MyShop=MyShop, MyCity=MyCity, MyPrice=MyPrice, MyAmount=MyAmount, Employees=Employees)
    return render_template('registerShop.html', Cities=Cities)


@app.route('/_registerShop', methods=['GET'])
def _tryRegisterShop():
    from queryfunc import tryRegisterShop
    Shop = request.args.get('Shop')
    City = request.args.get('City')
    Price = request.args.get('Price')
    Amount = request.args.get('Amount')
    Acc = current_user.get_id()
    data = tryRegisterShop(Shop, City, Price, Amount, Acc)
    return jsonify(data)


@app.route('/_AddEmployee', methods=['GET'])
def _AddEmployee():
    from queryfunc import AddEmployee
    Employee = request.args.get('Employee')
    Acc = current_user.get_id()
    Shop = users[Acc][1]
    data = AddEmployee(Shop, Employee)
    return jsonify(data)


@app.route('/_DelEmployee', methods=['GET'])
def _DelEmployee():
    from queryfunc import DelEmployee
    Employee = request.args.get('Employee')
    Acc = current_user.get_id()
    Shop = users[Acc][1]
    data = DelEmployee(Shop, Employee)
    return jsonify(data)


@app.route('/_PriceChange', methods=['GET'])
def _PriceChange():
    from queryfunc import PriceChange
    Price = request.args.get('Price')
    Acc = current_user.get_id()
    Shop = users[Acc][1]
    data = PriceChange(Shop, Price)
    return jsonify(data)


@app.route('/_AmountChange', methods=['GET'])
def _AmountChange():
    from queryfunc import AmountChange
    Amount = request.args.get('Amount')
    Acc = current_user.get_id()
    Shop = users[Acc][1]
    data = AmountChange(Shop, Amount)
    return jsonify(data)

# New Stuff!


@app.route('/myOrder')
@login_required
def myOrder():
    Status = ['All', 'Not Finished', 'Finished', 'Cancelled']
    return render_template('myOrder.html', Status=Status)


@app.route('/_searchMyOrderList', methods=['GET'])
def _searchMyOrderList():
    from queryfunc import searchMyOrderList
    Status = request.args.get('Status')
    Acc = current_user.get_id()
    data1 = searchMyOrderList(Acc, Status)
    data2 = {'data': []}
    for data in data1['data']:
        # return like searchShopList
        # orders by this Acc
        # OID Status Start End Shop Total Price
        data2['data'].append([data[0], data[1], (data[2]+"<br> "+data[3]), (data[4] +"<br> "+data[5]), data[6], ("$"+data[9] + "<br> (" + data[7]+"*$"+data[8]+")")])
    return jsonify(data2)


@app.route('/_searchShopOrderList', methods=['GET'])
def _searchShopOrderList():
    from queryfunc import searchShopOrderList
    _Shop = request.args.get('Shop')
    Status = request.args.get('Status')
    data1 = searchShopOrderList(_Shop, Status)
    data2 = {'data': []}
    for data in data1['data']:
        # return like searchShopList
        # orders by this Acc
        # OID Status Start End Shop Total Price
        data2['data'].append([data[0], data[1], (data[2]+"<br> "+data[3]), (data[4] +"<br> "+data[5]), data[6], ("$"+data[9] + "<br> (" + data[7]+"*$"+data[8]+")")])
    return jsonify(data2)


@app.route('/shopOrder')
@login_required
def shopOrder():
    from queryfunc import getAccShops
    Acc = current_user.get_id()
    Shops = getAccShops(Acc)
    # return all Shops which Acc works in in a list
    Status = ['All', 'Not Finished', 'Finished', 'Cancelled']
    return render_template('shopOrder.html', Status=Status, Shops=Shops)


@app.route('/_Order', methods=['GET'])
def _Order():
    from queryfunc import Order
    Amount = request.args.get('Amount')
    _Shop = request.args.get('Shop')
    Acc = current_user.get_id()
    data = Order(Acc, _Shop, Amount)
    # return message: success or fail and why
    return jsonify(data)


@app.route('/_DelOrder', methods=['GET'])
def _DelOrder():
    from queryfunc import DelOrder
    OID = request.args.get('OID')
    Acc = current_user.get_id()
    data = DelOrder(Acc, OID)
    # return message: success or fail and why
    return jsonify(data)


@app.route('/_DoneOrder', methods=['GET'])
def _DoneOrder():
    from queryfunc import DoneOrder
    OID = request.args.get('OID')
    Acc = current_user.get_id()
    data = DoneOrder(Acc, OID)
    # return message: success or fail and why
    return jsonify(data)


@app.route('/_DoneAllOrder', methods=['GET'])
def _DoneAllOrder():
    from queryfunc import DoneAllOrder
    Acc = current_user.get_id()
    OIDs = request.args.get('OIDs').split()
    data = DoneAllOrder(Acc, OIDs)
    # return message: success or fail and why
    return jsonify(data)


@app.route('/_DelAllOrder', methods=['GET'])
def _DelAllOrder():
    from queryfunc import DelAllOrder
    Acc = current_user.get_id()
    OIDs = request.args.get('OIDs').split()
    data = DelAllOrder(Acc, OIDs)
    # return message: success or fail and why
    return jsonify(data)
