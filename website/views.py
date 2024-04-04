from flask import Blueprint, render_template, request, flash, jsonify, redirect,url_for
from flask_login import login_required, current_user
from .import db, tables_dict, mysql
import MySQLdb.cursors
import json
from datetime import datetime
import re

views = Blueprint('views', __name__)

@views.route('/',methods=['GET','POST'])
def index():
  return render_template("index.html",user = current_user)

@views.route("/display")
@login_required
def display():
  return render_template('display.html', user = current_user, usertype="Admin")

@views.route("/where_display")
@login_required
def where_display():
  return render_template('where_display.html', tables_dict = tables_dict,user = current_user)

@views.route("/rename_display")
@login_required
def rename_display():
  return render_template('rename_display.html', tables_dict = tables_dict,user = current_user, usertype="Admin")
@views.route("/view_tables")
def view_tables():
  table_data = {}
  cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
  for table_name in tables_dict:
    sql_query = "select * from {}".format(table_name)
    resultValue = cursor.execute(sql_query)

    current_table_data = []
    if resultValue > 0:
      current_table_data = cursor.fetchall()
      table_data[table_name] = list(current_table_data)
    mysql.connection.commit()
  return render_template('view_tables.html', tables_dict = tables_dict, table_data = table_data,user = current_user, usertype="Admin")
@views.route("/update_display")
@login_required
def update_display():
  return render_template('update_display.html', tables_dict = tables_dict,user = current_user, usertype="Admin")
@views.route("/delete_display")
@login_required
def delete_display():
  return render_template('delete_display.html',  tables_dict = tables_dict, keys=tables_dict.keys(),user = current_user, usertype="Admin")
@views.route("/insert", methods=['GET','POST'])
@login_required
def insert():
  msg =''
  table_data = {}
  cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
  for table_name in tables_dict:
    sql_query = "select * from {}".format(table_name)
    resultValue = cursor.execute(sql_query)

    current_table_data = []
    if resultValue > 0:
      current_table_data = cursor.fetchall()
      table_data[table_name] = list(current_table_data)
    mysql.connection.commit()

  if request.method == 'POST':
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    table_name = request.form.get('keyaa')
    table_name = re.sub('<[^>]*>', '', table_name)

    column_name =tables_dict[table_name]
    data = []

    sql_query_insert = "INSERT INTO "+table_name+" VALUES ("+"% s,"*(len(column_name)-1)+"% s)"
    for i in column_name:
      data_val = request.form[i]
      data_val = re.sub('<[^>]*>', '', data_val)      
      data.append(data_val)

    data = tuple(data)
    try:
      cursor.execute(sql_query_insert,data)
      mysql.connection.commit()
      msg='Data inserted'
      print(msg)      
    except:
      msg = 'Data already exists'
      print(msg)

  return render_template('insert.html', tables_dict = tables_dict, keys=tables_dict.keys(), table_data = table_data, user = current_user, msg =msg,usertype="Admin")

@views.route('/delete/<string:table_name>', methods=['GET', 'POST'])
@login_required
def delete(table_name):
  if request.method == 'GET':
    args = request.args
    field_lst = []
    for attr in tables_dict[table_name]:
        field_name = attr
        field_value = args[field_name]
        if (field_value == 'None' or field_value == None):
          field_value = None
        field_lst.append([attr, field_value])
    try:
      cur = mysql.connection.cursor()
      sql_query = 'delete from {} where '.format(table_name)
      for i in range(len(field_lst) - 1):
        if (field_lst[i][1]):
          sql_query = sql_query + field_lst[i][0] + '=' + '"' + field_lst[i][1] + '"' + ' and '
      if (field_lst[-1][1]):
        sql_query = sql_query + field_lst[-1][0] + '=' + '"' + field_lst[-1][1] + '";'
      elif (len(sql_query) > 4):
        sql_query = sql_query[:-5]
      cur.execute(sql_query)
      mysql.connection.commit()
      cur.close()
      return redirect('/insert#' + str(table_name))
    except Exception as e:
      return 'There was an issue adding the entry:' + str(e)
  return redirect('/insert#' + str(table_name))

@views.route('/update', methods=['POST','GET'])
@login_required
def update():
    msg = ''
    table_data = {}
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    for table_name in tables_dict:
        sql_query = "select * from {}".format(table_name)
        resultValue = cursor.execute(sql_query)

        current_table_data = []
        if resultValue > 0:
            current_table_data = cursor.fetchall()
            table_data[table_name] = list(current_table_data)
        mysql.connection.commit()

    if request.method == 'POST':
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        table_name = request.form.get('keyaa')
        table_name = re.sub('<[^>]*>', '', table_name)

        column_name = tables_dict[table_name]
        data = []

        # Get the condition and set up the update query
        condition = request.form.get('condition')
        update_columns = [f"{col}=%s" for col in column_name]
        update_query = f"UPDATE {table_name} SET {', '.join(update_columns)} WHERE {condition}"

        for i in column_name:
            data_val = request.form[i]
            data_val = re.sub('<[^>]*>', '', data_val)
            data.append(data_val)

        data = tuple(data)
        try:
            cursor.execute(update_query, data)
            mysql.connection.commit()
            msg = 'Data updated'
            print(msg)
        except Exception as e:
            msg = "An error occurred: " + str(e)
            print(msg)

    return render_template('update.html', tables_dict=tables_dict, keys=tables_dict.keys(),
                           table_data=table_data, user=current_user, msg=msg, usertype="Admin")

@views.route('/rename/<string:key>', methods=['GET', 'POST'])
@login_required
def rename(key):
  print(key)
  msg = ''
  if request.method == 'POST':
    new_name = request.form['name']
    new_name = re.sub('<[^>]*>', '', new_name)
    print(new_name)
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    sql_query = 'alter table {0} rename {1};'.format(key, new_name)

    try:
      cur.execute(sql_query)
      msg = 'You have successfully renamed the table !!'
      tables_dict[new_name] = tables_dict[key]
      del tables_dict[key]
      with open('website/tables.json', 'w') as json_file:
        json.dump(tables_dict, json_file)
      mysql.connection.commit()
      cur.close()
      return redirect('/display#' + str(new_name))
    except:
      return redirect(request.url)
  return render_template('rename.html', msg = msg, key = key, user=current_user)

@views.route('/where/<string:key>', methods =['GET', 'POST'])
@login_required
def where(key):
  print(key)
  msg = ''
  try:
    if request.method == 'POST':
      column_name = request.form['Column_Name']
      column_name = re.sub('<[^>]*>', '', column_name)
      print(column_name)
      value = request.form['Value']
      value = re.sub('<[^>]*>', '', value)
      print(value)
      cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
      query1 = "SELECT * FROM {0} WHERE {1} = '{2}'".format(key,column_name,value)
      print(query1)
      resultValue =cursor.execute(query1)
      # mysql.connection.commit()
      msg = 'You have successfully executed where clause on the table !!'
      # return redirect('/display#' + str(key))
      if resultValue > 0:
          userDetails = cursor.fetchall()
          print(userDetails)
          print(tables_dict[key])
          return render_template('output.html',userDetails=userDetails,cols = tables_dict[key],table = key,query = query1, user=current_user,usertype="Admin")
      else:
          msg = "No values found"
  except Exception as e:
     return 'There was an ERROR : ' + str(e) 
  return render_template('where.html', msg = msg, key = key, user=current_user)

@views.route('/user-profile',methods=['GET','POST'])
@login_required
def profile():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    sql_query = "select user_name,email from Users where user_id={}".format(current_user.get_id())
    result = cursor.execute(sql_query)
    if result>0:
      user_data = list(cursor.fetchall())
    mysql.connection.commit()
    
    if request.method == 'POST':
      cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
      data = []
      sql_query_insert = "Update Users Set user_name =%s,email=%s where user_id ={}".format(current_user.get_id())
      user_name_val = request.form["user_name"]
      user_name_val = re.sub('<[^>]*>', '', user_name_val)
      email_val = request.form["email"]
      email_val = re.sub('<[^>]*>', '', email_val)
      data = [user_name_val,email_val]
      
      data = tuple(data)
      if(data[0] != user_data[0]["user_name"] or data[1] != user_data[0]["email"]):
        cursor.execute(sql_query_insert,data)
        msg = "Profile Updated"
        flash(msg,category="success")
        user_data[0]["user_name"] =data[0] 
        user_data[0]["email"] = data[1]
      else:
        msg = "No changes detected"
        flash(msg,category="error")
      print(msg)
      mysql.connection.commit()
      
    return render_template("user_profile.html",user=current_user,uname = user_data[0]["user_name"],usermail=user_data[0]["email"],usertype="User")
