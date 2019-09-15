from flask import Flask
import urllib
import json 
import os
import math
from flask import request
from flask import make_response
from dateutil.parser import parse
app=Flask(__name__)
@app.route('/webhook',methods=['POST'])
def webhook():
    req=request.get_json(silent=True,force=True)
    print("hi m in function webhook")
    res=makeWebhookResult(req)
    res=json.dumps(res,indent=4)
    r=make_response(res)
    r.headers['Content-Type']='application/json'
    return r

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
import datetime as dt
import json 
str_end = "\n\nIs there anything else you would like to know?"
strEndHin="\n\nक्या कुछ और है जो आप जानना चाहेंगे?"
hinDay={"Sunday":"रविवार","Monday":"सोमवार","Tuesday":"मंगलवार","Wednesday":"बुधवार","Thursday":"गुरुवार","Friday":"शुक्रवार","Saturday":"शनिवार"}
def checkJsonMeal(weekno,today,lang):
    if(lang=="hi"):
        with open('dataIconicGirlsHin.json') as json_file:
            data=json.load(json_file)
            ls=data[str(weekno)][hinDay.get(today.strftime("%A"))]
            s='\n'
            for key in ls.keys():
                s+="\n" + key + ":\n"
                s+='\n'.join(ls[key])
            return ("आपका भोजन," + str(today.date()) + ":" + s +  strEndHin)
    else:
        with open('data_iconicGirls.json') as json_file:
        	data=json.load(json_file)
        	ls=data[str(weekno)][today.strftime("%A")]
        	s='\n'
        	for key in ls.keys():
        		s+="\n" + key + ":\n"
        		s+='\n'.join(ls[key])
        	return ("Your meal for " + str(today.date()) + " is " + s + str_end)
def checkJsonfood(weekno,today,foodType,lang):
    if(lang=="hi"):
        with open('dataIconicGirlsHin.json') as json_file:
            data=json.load(json_file)
            ls=data[str(weekno)][hinDay.get(today.strftime("%A"))][foodType]
            s='\n'.join(ls)
            return("आपका  "+foodType+","+str(today.date()) +" : "+s+strEndHin) 
    else:
    	with open('data_iconicGirls.json') as json_file:
    		data=json.load(json_file)
    		ls=data[str(weekno)][today.strftime("%A")][foodType]
    		s='\n'.join(ls)
    		return("Your "+foodType+" for "+str(today.date()) +" is "+s+str_end) 
def makeWebhookResult(req):
    ref_date=dt.datetime(2019,3,11).date()
    result=req.get("queryResult")
    print(result)
    parameters=result.get("parameters")
    lang=result.get("languageCode") ####
    if req.get("queryResult").get("action")=="intent.messMenu":
        takeTime=parameters.get("date")
        if(takeTime==""):
        	today=datetime.now()
        else:
        	today =parse(takeTime)
        weekno=(abs(math.floor(((today.date()-ref_date).days)/7)))%2
        speech=checkJsonMeal(weekno,today,lang)
        print("response from action messMenu")
        print(speech) 
        return{
            "fulfillmentText":speech,
            "source":"ThaparMessbot"
        }
    if req.get("queryResult").get("action")=="intent.foodTime":
        takeTime=parameters.get("date")
        today =parse(takeTime)
        if(takeTime==""):
        	today=datetime.now()
        else:
        	today =parse(takeTime)
        foodType=parameters.get("food")
        weekno=(abs(math.floor(((today.date()-ref_date).days)/7)))%2
        speech=checkJsonfood(weekno,today,foodType,lang)
        print("response from action foodtime")
        print(speech) 
        return{
        	"fulfillmentText":speech,
            "source":"ThaparMessbot"
        }  
    
if __name__ =='__main__':
    port=int(os.getenv('PORT',80))
    print("Starting app on port %d" %(port))
    app.run(debug=True,port=port,host='0.0.0.0')
    

        
         
            
            
            
            
        
        
        
        
        
        

