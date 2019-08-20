from flask import Flask
from flask import request
from flask import Blueprint
import sqlite3
from objectifier import Objectifier
from datetime import datetime
from uuid import uuid1
from flask import jsonify
import json


dataAPI_Blueprint = Blueprint('data',__name__)

@dataAPI_Blueprint.route('/data', methods = ['POST'])
def store_data():
    incoming_data = request.get_json()
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
    cur.execute("select ID from HOSTS where HostName =?", (incoming_data['hostname'],) )
    id = cur.fetchall()
    if(id.__len__()==0):
        return "VM not registered! ",404
    else:
        VM_ID = id[0][0]
        cur.execute("insert into data values(?,?,?,?)",(str(uuid1()) , json.dumps(incoming_data), datetime.now(), VM_ID ) ) 
        conn.commit()
    conn.close()
    return jsonify({"msg":"OK"})


@dataAPI_Blueprint.route('/data', methods =['GET'])
def get_data():
    query_params = request.args.get('vm')
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    cur.execute("select data from data where vm_id = ( select id from hosts where hostname = ? ) order by createdat desc limit 1", (query_params,) )
    data = cur.fetchall()
    if(data.__len__()==0):
        return "VM not found ",404
    else:
        data = json.loads(data[0][0])
        return jsonify(data)
