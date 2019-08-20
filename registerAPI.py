from flask import Flask
from flask import request
from flask import Blueprint
import sqlite3
from objectifier import Objectifier
from datetime import datetime
from uuid import uuid1
from flask import jsonify

#app = Flask(__name__)

registerAPI_blueprint = Blueprint('register',__name__)

@registerAPI_blueprint.route('/')
def hello():
    return """
    Register Client: POST /register
        {
            "host":"",
            "user":"",
            "password":"",
            "domain":""
        }
    """



@registerAPI_blueprint.route('/data', methods = ['POST'])
def post_data():
    pass



@registerAPI_blueprint.route('/register', methods =['POST'])
def register_client():
    """
        {
            "host":"",
            "user":"",
            "password":"",
            "domain":""
        }
    """
    
    data_object = Objectifier(request.get_json())
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
    cur.execute("select id from hosts where HostName = ?", (data_object.host,) )
    id = cur.fetchall()
    if(id.__len__()==0):
        id = str (uuid1())
        cur.execute("insert into hosts values(?,?,?)",(id, data_object.host , datetime.now() ) )
        conn.commit()
        cur.execute("insert into cred values (?,?,?,?)",( id , data_object.domain , data_object.user , data_object.password) )
        conn.commit()
        conn.close()
        return jsonify({"id":id})
    else:
        query_data = request.get_json()
        query_data.pop('host')
        for items in query_data.keys():
            cur.execute("update cred set "+items+"=? where id = ?", (str(query_data[items]) , id[0][0]) )
        if(cur.rowcount ==0):
            cur.execute("insert into cred values (?,?,?,?)",( id[0][0] , data_object.domain , data_object.user , data_object.password) )
        conn.commit()                    
        conn.close()
        return jsonify({"id":id[0][0]})


