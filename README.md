# Alumni-Relations-Database
This repository contains the source code for all Assignment 3 of the Databases (CS 432) course by Prof. Mayank Singh.
The goal is to develop a DBMS using Flask and MySQl

## Getting Started

To set up the environment to run the assignment codes follow the below steps:

- You must have [Python](https://www.python.org/) and pip installed on your laptop/desktop. Run the following commands to check the whether you have them installed or not.
```
python --version
pip --version
```

- Install the packages from requirements.txt
```
pip install -r requirements.txt
```

- You must also have MySQL Workbench installed on your laptop/desktop.
## Creating and opening virtual environment

```
pip install virtualenv
python3 -m venv myenv
``` 
For macOS and linux:
```
source myvenv/bin/activate
```
For Windows:
```
myenv\Scripts\activate
```
## Running the Web App

In order to run the Web App you can run the following command in your terminal or run main.py file

- Run main.py file 
```
python main.py
```
<br>

![Alt text](screenshots/terminal.png)
<br>
- Open the link for the Web Server present in your terminal or you can copy the following link:
```
http://127.0.0.1:5000/
```
![Alt text](screenshots/index.png)
<br>
- The link will direct you to Home page of our WebApp. Click the login button will direct you to our login page.

## User Login 
<br>

![Alt text](screenshots/user_login.png)
- You can login as existing user if you already have an account or you can Sign Up by selecting the Sign up button in the navigation bar. (By signing up your details are going to get stored in the users table of our database)
<br>

![Alt text](screenshots/signup.png)
- Upon successfull login or signup we get user profile page as shown
<br>

![Alt text](screenshots/Loggedin.png)
- On the navbar we can see view tables which redirects us to the following page where we can only view certain number of tables as we were logged in as user. All the CRUD operations are restricted for user login.
<br>
![Alt text](screenshots/view_tables.png)
<br>
<br>

## Admin Login

- You can also Login as Admin. In the navigation bar select Admin Login. In the login form enter the following credentials for login.
![Alt text](screenshots/admin_login.png)
```
Email: admin@iitgn.ac.in
Password: 123456789
```

- Once you have logged in successfully. The Display page will appear in which you can view , insert/delete, update, rename, where options.
![Alt text](screenshots/display.png)

Below are the screenshots of successfully executed queries in the database:

## Insert
<br>
As you can see from the picture that we are able to insert data in the table using our Web App.
<br>

![Alt text](screenshots/before_insert.png)
![Alt text](screenshots/inserted.png)
![Alt text](screenshots/dbinserted.png)
<br>
<br>

## Update 
<br>
The figure shows successful running of the update query. We are able to update data present in the table.
<br>

![Alt text](screenshots/before_update.png)
![Alt text](screenshots/updated.png)
![Alt text](screenshots/dbupdated.png)
<br>
<br>

## Delete
<br>
We have implemented a delete button in front of every row of table. It allows us to delete a particular row of the selected table. 
<br>

![Alt text](screenshots/updated.png)
![Alt text](screenshots/after_delete.png)
![Alt text](screenshots/dbdeleted.png)
<br>
<br>

## Rename
<br>
By selecting rename in the display page it then redirects to another page in which you can change the name of table present.
<br>
We are renaming belongs_to page to belongsto
<br>

![Alt text](screenshots/rename.png)
![Alt text](screenshots/after_rename.png)
![Alt text](screenshots/dbrenamed.png)
<br>
<br>

## Where
<br>
By clicking on the where option in display page, you are redirected to a different page in which you can provide the field name and value for implementing the where query.
<br>

![Alt text](screenshots/where_query.png)
![Alt text](screenshots/where.png)
![Alt text](screenshots/dbwhere.png)
<br>
## Work Distribution
# Reddybathuni Venkat:
Worked on backend routes.<br>
Worked on Flash integration and integrating database in a web app using MySQL.<br>
Contributed to the creation of HTML pages that are displayed on the web application.<br>
Worked on github management
<br>
# Naga Bhuvith Nakka:
Helped in integrating database in a web app using MySQL.<br>
Developed an idea for the Front-end.<br>
Also worked on the UPDATE function and helped on the backend part.
<br>
# Kaila Uday Vardhan Reddy:
Worked on the Front-end of the Web app using HTML.<br>
Worked on some part of the combined work of G1&G2.<br>
Contributed to the Front-end development of these HTML pages using CSS.
<br>
# Koleti Eswar Sai Ganesh:
Helped in fixing some errors.<br>
Assisted with integrating Flask with MySQL.<br>
Also worked on the backend part (Delete function).
<br>
# Chakradhar Basani:
Helped in the documentation and worked on the README file.<br>
Taken screenshots.<br>
Also helped in debugging errors during testing.<br>
Worked on authentication in flask
<br>
# Vubbani Bharath Chandra: 
Tested and ran the web application.<br>
Also clicked screenshots of successful executions.<br>
Also helped in fixing & debugging errors.
<br> 
# Sai Charan Miriyala:
Entered some dummy values and showed these dummy entries on the web page.<br>
Established necessary connections to thoroughly test both our database and the web application.<br>
Contributed to the Front-end development of these HTML pages using CSS.<br>

