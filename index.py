from flask import Flask

app = Flask(__name__)

@app.route("/")
str_end = "\n Is there anything else you would like to know?"
def index():
	with open('data_iconicGirls.json') as json_file:
		data=json.load(json_file)
		ls=data[str(weekno)][today.strftime("%A")]
		s='\n'
		for key in ls.keys():
			s+="\n" + key + ":\n"
			s+='\n'.join(ls[key])
		return ("Your meal for " + str(today.date()) + " is " + s + str_end)
