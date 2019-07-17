from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
#from passlib.apps import custom_app_context as pwd_context
from tempfile import mkdtemp
from helpers import *
import datetime
# configure application
from flask import Flask
#from flaskext.mysql import MySQL
import pymysql

app = Flask(__name__)

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
        password = "ROOT"
        db = "onlineshopping"

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
        db.cur.execute("SELECT * FROM customer WHERE cname = %s", ((str(request.form.get("username"))),))
        rows = db.cur.fetchall()
        ''''''

        ''''''
        db.con.commit()
        # ensure username exists and password is correct
        if len(rows) != 1 or not (str(request.form.get("password")) == str(rows[0]["password"])):
            return apology("invalid username and/or password")
        # remember which user has logged in
        session["user_id"] = rows[0]["cid"]

        # redirect user to home page
        return redirect(url_for("index"))

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

        # hash1=pwd_context.hash(request.form.get("password"))
        result = db.cur.execute("INSERT INTO customer (cname,password,email,phone) VALUES(%s, %s,%s,%s)", (
        request.form.get("username"), request.form.get("password"), request.form.get("email"),
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
    return render_template("admin.html")

@app.route("/logout")
def logout():
    """Log user out."""

    # forget any user_id
    session.clear()

    # redirect user to login form
    return redirect(url_for("login"))


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

    #return render_template("categoryForm.html")


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

'''''''''''''''
    @app.route("/orderInsert")
    def orderinsert():
        return render_template("productForm.html")

    @app.route("/saveorder", methods=["GET", "POST"])
    def saveorder():
        session.clear()
        if request.method == "POST":
            result = db.cur.execute(
                "INSERT INTO product ( catid, priceperunit, pname, stockleft, productdesc, imagesrc )  VALUES(%s,%s,%s,%s,%s,%s)",
                (request.form.get("catid"),
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

'''
# if __name__ == "__main__":
#    app.run()
# @app.route("/")
# @login_required
# def index():
#    return "Aashish"



