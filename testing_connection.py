import syncano
import json
password = json.load(open("password.p","rb"))
connection = syncano.connect(email="eric.schles@syncano.com",password=password)
