#https://www.itread01.com/content/1542441903.html
from flask import Flask,render_template,g,request
import sqlite3
from datetime import datetime
app=Flask(__name__)
def connect_db():
    sql=sqlite3.connect('food_log.db')
    sql.row_factory=sqlite3.Row
    return sql
def get_db():
    if not hasattr(g,'sqlite3.db'):
        g.sqlite_db=connect_db()
    return g.sqlite_db
@app.teardown_appcontext
def close_db(error):
    if hasattr(g,'sqlite_db'):
        g.sqlite_db.close()
@app.route('/',methods=['POST','GET'])
def index():
    db=get_db()
    if request.method=='POST':
        date=request.form['date']
        dt=datetime.strptime(date,'%Y-%m-%d')
        database_date=datetime.strftime(dt,'%Y%m%d')
        db.execute('INSERT INTO log_date(entry_date)VALUES(?)',[database_date])
        db.commit()
    cur=db.execute('SELECT entry_date FROM log_date')
    results=cur.fetchall()
    pretty_test=[]
    for i in results:
        single_date={}
        
        #return database_date
    return render_template('home.html')
@app.route('/view')
def view():
    return render_template('day.html')
@app.route('/food',methods=['GET','POST'])
def food():
    db = get_db()
    print(dir(g))#print兩次表示運行了兩次 一次URL的get一次html的action url_for的jinjia語法 POST請求#['__class__', '__contains__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'get', 'pop', 'setdefault']
    if request.method=='POST':
        #db=get_db()
        name=request.form['food-name']
        protein=int(request.form['protein'])
        carbohydrates=int(request.form['carbohydrates'])
        fat=int(request.form['fat'])
        calories=protein*4+carbohydrates*4+fat*9
        db.execute('insert into food(name,protein,carbohydrates,fat,calories) values(?,?,?,?,?)',[name,protein,carbohydrates,fat,calories])
        db.commit()
    cur=db.execute('SELECT name,protein,carbohydrates,fat,calories FROM food')#首頁就已經先fetch之前所有資料了#select from等同SELECT FORM
    results=cur.fetchall()
    print(results)#[<sqlite3.Row object at 0x0000024B93113310>, <sqlite3.Row object at 0x0000024B93113330>, <sqlite3.Row object at 0x0000024B931131F0>, <sqlite3.Row object at 0x0000024B93113650>, <sqlite3.Row object at 0x0000024B93113570>, <sqlite3.Row object at 0x0000024B93113350>, <sqlite3.Row object at 0x0000024B93113590>, <sqlite3.Row object at 0x0000024B93113390>, <sqlite3.Row object at 0x0000024B93113550>]
    return render_template('add_food.html',results=results)
if __name__=='__main__':
    app.run(debug=True)
