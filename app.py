from flask import Flask , flash, redirect, render_template, request, session, url_for
from flask_session import Session
from passlib.apps import custom_app_context as pwd_context
from tempfile import mkdtemp
from helpers import *
#from .helpers import *


import datetime
# configure application
from flask import Flask,session
#from flaskext.mysql import MySQL
import pymysql
import datetime
from datetime import timedelta
import pymongo




app = Flask(__name__)

cart={}
time =""
# ensure responses aren't cached
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

# configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"


class Database:
    def __init__(self):
        host = "127.0.0.1"
        user = "root"
        password = "root1234"
        db = "OnlineShopping"

        self.con = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.
                                   DictCursor)
        self.cur = self.con.cursor()


Session(app)
db = Database()


# res = db.list_artists()
# app.run()

@app.route('/home')
def home():
    return render_template("Homepage.html")


@app.route("/")
@login_required
def index():
    db.cur.execute("SELECT categoryname FROM category")
    category = db.cur.fetchall()
    return render_template("Home_afterlogin.html", category=category)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in."""
    # forget any user_id
    session.clear()

    # if user reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username")

        # ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password")

        # query database for username
        db.cur.execute("SELECT * FROM customer WHERE cname = %s", ((str(request.form.get("username")))))
        rows = db.cur.fetchall()
        ''''''

        ''''''
        db.con.commit()
        # ensure username exists and password is correct


        db.cur.execute("SELECT * FROM administrators WHERE adminname = %s", ((str(request.form.get("username"))),))
        rows1 = db.cur.fetchall()

        db.con.commit()

        # ensure username exists and password is correct
        flag = 0
        if len(rows) != 1 or not (pwd_context.verify(request.form.get("password"), rows[0]["password"])):
            flag = 1

        if (flag == 1) and (len(rows1) != 1 or not (str(request.form.get("password")) == str(rows1[0]["password"]))):
            return apology("invalid username and/or password")
        # remember which user has logged in

        if(flag==0):
            # redirect user to home page
            session["user_id"] = rows[0]["cid"]
            return redirect(url_for("index"))
        else:
            return redirect(url_for("admin"))
        # remember which user has logged in

        # redirect user to home page

    # else if user reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("loginsam.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user."""
    # forget any user_id
    session.clear()
    # if user reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username")

        # ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password")

        elif request.form.get("password") != request.form.get("retype-password"):
            return apology("passwords do not match")

        elif not request.form.get("email"):
            return apology("must provide email")

        hash1 =pwd_context.hash(request.form.get("password"))
        result = db.cur.execute("INSERT INTO customer (cname,password,email,phone) VALUES(%s, %s,%s,%s)", (
        request.form.get("username"),hash1 , request.form.get("email"),
        request.form.get("phone")))
        print("I AM PRINTING RESULT HERE!!!!!!!!!!!!!!!!!")
        print(result)

        if result == 0:
            return apology("username already exists")

        db.cur.execute("SELECT * FROM customer WHERE cname = %s", request.form.get("username"))
        rows = db.cur.fetchall()
        print(str(rows))
        db.con.commit()
        session["user_id"] = rows[0]["cid"]

        return redirect(url_for("index"))

    else:
        return render_template("register.html")

@app.route("/admin")
def admin():

    # gets u all the distinct category id of product present in the phistory table
    db.cur.execute("select  distinct catid as cid from product,phistory where product.pid = phistory.pid   group by phistory.pid ")
    cids = db.cur.fetchall()

    # schema-> pid |pname |priceperunit |cid |totalQuantity |totalprice (of each product buyd)
    db.cur.execute("select  phistory.pid,pname,priceperunit,product.catid,category.categoryname, sum(quantity) as totalQuantity,sum(quantity)*priceperunit as totalPrice from product,phistory,category where product.pid = phistory.pid and category.catid=product.catid group by phistory.pid order by product.catid,totalQuantity desc")
    History = db.cur.fetchall()

    #category name from cid
    db.cur.execute(
    "select  * from category")
    catlist = db.cur.fetchall()

    #compute total sales
    total =0;
    for i in History:
        for key, value in i.items():
            if key == "totalPrice":
                total += int(value)

    #compute total price(sales) of every category
    totalPriceCategory=0
    catPrice ={}
    for j in cids:
        for k,v in j.items():
            totalPriceCategory =0;
            for i in History:
                for key, value in i.items():
                    if v == value:
                        totalPriceCategory += int(i['totalPrice'])
            #print("totalPriceCategory =", totalPriceCategory)
            #catPrice[v] = totalPriceCategory
            catPrice[i['categoryname']] = totalPriceCategory
            print(i['categoryname'])
            print("totalPriceCategory =", totalPriceCategory)



    print("catPrice= ",catPrice)
    print("cids=",cids)
    print("History=",History)
    print("total=",total)


    return render_template("admin.html")

@app.route("/logout")
def logout():
    """Log user out."""

    # forget any user_id
    session.clear()

    # redirect user to login form
    return redirect(url_for("login"))

@app.route("/Homeafterlogin")
def homeafterlogin():
    return render_template("Home_afterlogin.html")

@app.route("/categoryis/<item>" ,methods=["GET", "POST"])
def distplayCard(item):
    db.cur.execute("select * from product  where catid in (select catid from category where categoryname=%s )",item)
    productlist = db.cur.fetchall()
    print(productlist)
    return render_template("card.html", item=item , productlist = productlist )
    #return render_template("card(test).html")




@app.route("/productDetail/<item>")
def productDetail(item):
    db.cur.execute("select * from product  where pname = %s ", item)
    list = db.cur.fetchall()
    return render_template("cardDetailed.html", item=item, list=list)


@app.route("/view/<item>")
def profile(item):
    if (item == "administrators"):
        db.cur.execute("select * from administrators ")
    elif (item == "category"):
        db.cur.execute("select * from category")
    elif (item == "customer"):
        db.cur.execute("select * from customer")
    elif (item == "livedelivery"):
        db.cur.execute("select * from livedelivery")
    elif (item == "order"):
        db.cur.execute("select * from orders")
    elif (item == "product"):
        db.cur.execute("select * from product ")
    elif (item == "supplier"):
        db.cur.execute("select * from supplier")

    list = db.cur.fetchall()
    return render_template("table.html",item=item,list=list)
''''''''''''''''''''''''''''''''''''''''''''''''''''''


@app.route("/adminInsert")
def adminInsert():
    return render_template("adminaddForm.html")


@app.route("/saveadmininsert", methods=["GET", "POST"])
def saveadminInsert():
    session.clear()
    if request.method == "POST":
        result = db.cur.execute("INSERT INTO administrators (adminname,password) VALUES(%s,%s)",
                                ( request.form.get("adminname"), request.form.get("adminpassword")))
        db.con.commit()
        return "<h1>ADDED SUCCESSFULLY<h1>"
    else:
        return apology("could not add")
'''
@app.route("/billdelete")
def admindelete():
    return render_template("admindeleteForm.html")


@app.route("/unsaveadmin", methods=["GET", "POST"])
def unsavecategory():
    session.clear()
    if request.method == "POST":
        result = db.cur.execute("DELETE FROM administrator WHERE adminname=%s and password=%s",
                                ( request.form.get("adminname"),
                                (request.form.get("password"))
                                )
                                )
        db.con.commit()
        return "<h6>DELETED SUCCESSFULLY<h6>"
    else:
        return apology("could not DELETE")
'''
''''''''''''''''''''''''''''''''''''''''''''''''''''''
@app.route("/categoryInsert")
def categoryinsert():
    return render_template("categoryForm.html")

    #return render_template("categoryForm.html")



@app.route("/savecategoryInsert", methods=["GET", "POST"])
def savecategoryinsert():
    session.clear()
    if request.method == "POST":
        result = db.cur.execute("INSERT INTO category (categoryname) VALUES(%s)", ( request.form.get("categoryname")))
        db.con.commit()
        return "<h1>ADDED SUCCESSFULLY<h1>"
    else:
        return apology("could not add")


@app.route("/categorydelete")
def categorydelete():
    return render_template("categorydeleteForm.html")


@app.route("/unsavecategory", methods=["GET", "POST"])
def unsavecategory():
    session.clear()
    if request.method == "POST":
        result = db.cur.execute("DELETE FROM Category WHERE categoryname=%s", ( request.form.get("categoryname")))
        db.con.commit()
        return "<h6>DELETED SUCCESSFULLY<h6>"
    else:
        return apology("could not DELETE")
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


@app.route("/productInsert")
def productinsert():
    return render_template("productForm.html")



@app.route("/saveproductInsert", methods=["GET", "POST"])
def saveproductinsert():
    session.clear()
    if request.method == "POST":
        result = db.cur.execute("INSERT INTO product ( catid, priceperunit, pname, stockleft, productdesc, imagesrc )  VALUES(%s,%s,%s,%s,%s,%s)",
                                ( request.form.get("catid"),
                                  request.form.get("priceperunit"),
                                  request.form.get("pname"),
                                  request.form.get("stockleft"),
                                  request.form.get("productdesc"),
                                  request.form.get("imagesrc"))
                                )
        db.con.commit()
        return "<h1>ADDED SUCCESSFULLY<h1>"
    else:
        return apology("could not add")


@app.route("/productdelete")
def productdelete():
    return render_template("productdeleteForm.html")

    #return render_template("categoryForm.html")


@app.route("/unsaveproduct", methods=["GET", "POST"])
def unsaveproduct():
    session.clear()
    if request.method == "POST":
        result = db.cur.execute("DELETE FROM product WHERE pid=%s", ( request.form.get("pid")))
        db.con.commit()
        return "<h1>DELETED SUCCESSFULLY<h1>"
    else:
        return apology("could not DELETE")


@app.route("/cart/<itemname>", methods=["GET", "POST"])
def cart(itemname):
    customerid = session['user_id']
    session.clear()
    if request.method == "POST":
        db.cur.execute("select * from product where pname = %s",(str(itemname)));
        lis = db.cur.fetchall()
        lis1 =lis[0]
        quantity=(request.form.get("quantitylist"))
        result = db.cur.execute("INSERT INTO cart (cid,pid,quantity,amount) VALUES(%s,%s,%s,%s)",
                                (
                                customerid,
                                lis1['pid'],
                                 quantity ,
                                int(lis1['priceperunit'])*int(quantity)
                                ))
        db.con.commit()
        session['user_id']=customerid
        return  "<h1>ADDED TO CART</h1>"
    else:
        return apology("could not add to cart")


@app.route("/viewcart")
def buy():
    db.cur.execute("select pname,quantity from cart,product where product.pid=cart.pid and cart.cid=%s ", session['user_id']);
    list = db.cur.fetchall()
    return render_template("buy.html", list=list)

@app.route("/bill0", methods=["GET", "POST"])
def bill0():
    return render_template("extrabilldetail.html")

@app.route("/bill1", methods=["GET", "POST"])
def bill1():
    if request.method == "POST":
        tim=request.form.get("tim")
        db.cur.execute("select SUM(amount) as total1 from cart  where cid=%s", session['user_id'])
        total = db.cur.fetchall()  #total amount

        db.cur.execute("select pname,quantity,amount from cart,product where product.pid=cart.pid and cart.cid=%s ", session['user_id'])
        list = db.cur.fetchall()   #contains billing details

        db.cur.execute("select * from cart where cid=%s ", session['user_id']);
        lis = db.cur.fetchall()
        print("list=", list)
        productlis = []
        quantitylis = []
        for i in lis:
            for key, value in i.items():
                if key == "pid":
                    productlis.append(value)
                elif key == "quantity":
                    quantitylis.append(value)

        print('productlis=',productlis)
        print("quantitylis",quantitylis)
        res = db.cur.execute("INSERT INTO orders (cid,productidlist,quantitylist,orderdate,deleveryTime) VALUES(%s,%s,%s,%s,%s)",
                             (
                                 session['user_id'],
                                 str(productlis),
                                 str(quantitylis),
                                 datetime.datetime.now(),
                                 tim
                             ))
        db.con.commit()
        for i, j in zip(productlis, quantitylis):
            db.cur.execute("INSERT INTO phistory (pid,quantity) VALUES(%s,%s)",(i,j))
        db.con.commit()

        if not res:
            return apology("could not place order")
        else:

            for i, j in zip(productlis,quantitylis):
                print('i=',i," j=",j)
                db.cur.execute("update product set stockleft=stockleft-'"+j+"' where pid=%s",i)
                db.con.commit()

            db.cur.execute("select cname from customer where cid=%s" ,session['user_id'])
            name = db.cur.fetchall()
            db.cur.execute("select oid,orderdate from orders where cid=%s",session['user_id'])
            orderlis = db.cur.fetchall()
            print("list=",list)

            db.cur.execute("select product.pid ,pname,quantity,amount,stockleft from cart,product where product.pid=cart.pid and stockleft < 0 and cart.cid=%s ", session['user_id'] )
            pendinglist = db.cur.fetchall()
            print("pending list=",pendinglist)

            db.cur.execute( "select product.pid ,pname,quantity,amount,stockleft from cart,product where product.pid=cart.pid  and cart.cid=%s ",session['user_id'])
            currentorder = db.cur.fetchall()
            print("pending list=", pendinglist)
            pendingidlist=[]
            pendingquantitylist=[]
            for i in pendinglist:
                pendingidlist.append(i['pid'])
                pendingquantitylist.append(i['quantity'])

            print("penlist=",pendingidlist)
            print("penquant=",pendingquantitylist)

            db.cur.execute("Insert into pendingorder (cid,pidlist,quantitylist) values(%s,%s,%s)",(session['user_id'],str(pendingidlist),str(pendingquantitylist)))
            db.con.commit()

            db.cur.execute("update product set stockleft=0 where stockleft<0")
            db.con.commit()

            deleveryDate = orderlis[0]['orderdate']+ timedelta(days=2)

            client = pymongo.MongoClient()
            db1=client.livedell
            db1.live.insert({"status":0})
            st= db1.live.find_one()
            n=int(st["status"])
            print("pendinglist :",pendinglist)
            print("currentorder :",currentorder)

            db.cur.execute("SELECT productidlist, quantitylist FROM orders")
            print(db.cur.fetchall())
            return render_template("bill2.html",
               currentorder=currentorder, list=pendinglist, total=total, tim=tim, name=name, orderlis=orderlis ,deleveryDate=deleveryDate,pendinglist=pendinglist,n=n)

@app.route('/history')
def history():
    db.cur.execute("select cname,phone,productlist,quantitylist,orderdate from orders,customer where orders.cid=customer.cid")
    return render_template("historyoforder.html",list=list)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")



if __name__ == "__main__":
    app.run()
# @app.route("/")
# @login_required
# def index():
#    return "Aashish"



