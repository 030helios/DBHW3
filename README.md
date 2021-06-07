組員：凃少麒 賴士維

網站使用Flask架設

下載dependencies
```
pip install -r requirements.txt
```
開啟網站
```
FLASK_APP=run.py flask run
```

The way to create "data.db"
1. Open the terminal under ./data
2. run "sqlite3 data.db"
3. run ".mode csv", ".separator ","", ".import EMPLOYEE.csv employee", ".import USER.csv user", ".import SHOP.csv shop", ".import ORDER.csv order_", ".exit"

