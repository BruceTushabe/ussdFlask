
from flask import Flask, request
app = Flask(__name__)

response = ""

@app.route('/', methods=['POST', 'GET'])
def ussd_callback():
  global response
  session_id = request.values.get("sessionId", None)
  service_code = request.values.get("serviceCode", None)
  phone_number = request.values.get("phoneNumber", None)
  text = request.values.get("text", "default")
  
  if text == '':
    response = "CON Welcome to GetCassava, Choose what you want to do?"
    response += "1. Buy Cassava \n"
    response += "2. Sell Cassava"
  
  elif text == '1':
    reponse = "CON What type of cassava do you want?"
    response += "1. Sweet Cassava \n"
    response += "2. Dry Cassava"
    
  elif text == '1*1':
    response = "CON Choose amount in Kg"
    response += "1. 10 Kg \n"
    response += "2. 20 Kg \n"
    
  elif text == '1*1*1':
    response = "This is noted. Thanks"
    
  elif text == '1*1*2':
    response = "Great. Thank you"
    
  elif text == '1*2':
    response = "CON Choose the Kg you are selling"
    response += "1. 50 Kg \n"
    response += "2. 100 Kg"
    
  elif text == '1*2*1':
    response = "This is noted. Thanks"
    
    
  elif text == '1*2*2':
    response = "Great. Thank you"
    
  return response 


if __name__ == '__main__':
  app.run(host="0.0.0.0", port= 5000)

