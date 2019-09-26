# OnlineGroceryShopping 

## Introduction

This is an online shopping website with 2 modes 
  1. user_mode
     * choose different products from different category and put it to cart
     * buy from cart
  2. admin_mode
     * view users
     * add another admin
     * add or delete  product, category 

## Prerequisites

Things you need to install

1. sql workbench
2. pycharm (can work without this but recommended)


## Installing

Download my repo into local machine

1. sql workbench
   * after download ,set user name as 'root' & and password as 'root1234' ( or change it in code, in app.py :)                 
    **Importing Database**: 
   * server -> Data Import ( u must c a dataimport page ) 
   * check  'import from self-contained file' and choose .sql file in Database folder that is downloaded from my repo
   * create new 'Default Target Schema' and name it 'OnlineShopping' ( if u want some other name change in code , app.py)
   * make sure 'dump-structure and data' is selected
   * press 'start import'
   * u should hv ur database ready!!!
2. pycharm
   * open 'code' folder using pycharm
   * install some packages imported in 'app.py'
   * go to 'app.py' , rightclick->run  ( make sure ur sql workbench server is running )
   * u must see a localhost link as output, click on it to load the website on ur browser
   * yea !!!
   
## Functionality

1. User_mode
    * sign up as a new user or login to access shopping as a user
    * visit all category and see the items available 
    * Add them to cart and view cart
    * u can also buy cart
2. Admin_mode
    * default username = 'rahul' , password = 'rahul123'
    * u can add or delete  product,category as an admin and see the respective changes in DB(using sql workbench) 
    * u can also add a new admin 
  
## Built With

* Flask python-framework
* HTML ,CSS

# ThankYou
