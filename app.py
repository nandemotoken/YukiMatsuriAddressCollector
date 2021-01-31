import os
from flask import request
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def address_collector():
  with open( "addresses.txt" , 'a') as f:
    try:
      f.writelines( request.args.get('address') + "\n" )
    except:
      return 'Error! data registration is crashed!' 
  if( request.args.get('address')[1] == 'x'):
    return '<html><head><title>YukiMatsuri</title></head><body bgColor="rgb(131,209,229)">あなたのアドレスがブロックチェーンに登録されました！<img src="https://raw.githubusercontent.com/nandemotoken/YukiMatsuriAddressCollector/gh-pages/snowman.png"></body></html>'
  else:
    return 'エラー！再度お試しください…'

@app.route('/list')
def address_list():
  addresslistmulti = []
  with open( "addresses.txt" , 'r') as f:
    try:
      for l in f:
        addresslistmulti.append(l.strip())
      addresslistorig = list(set(addresslistmulti))
      return str(addresslistorig).replace("'" , '"')
    except:
      return 'Error!'
