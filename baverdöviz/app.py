from flask import Flask
from flask import Flask, render_template, request
import requests

api_key = "d4e1a3a3e8e80029a64067fa152faf45"
url = "http://data.fixer.io/api/latest?access_key="+api_key


app = Flask(__name__)

@app.route("/",methods = ["GET","POST"])
def index():
    if request.method == "POST":
        firstCurrency = request.form.get("firstCurrency") 
        secondCurrency = request.form.get("secondCurrency") 
        amount = request.form.get("amount") 
 
        response = requests.get(url) # getting currency values with api
        app.logger.info(response) # checking currency values

        infos =  response.json() # converging response to json

        # Finding currency in the api.
        firstValue = infos["rates"][firstCurrency]
        secondValue = infos["rates"][secondCurrency]

        
        result = (secondValue / firstValue) * float(amount) # Calculating amount value.

        # Creating dictionary for send it to main.html with currency infos.
        currencyInfo = dict()
        currencyInfo["firstCurrency"] = firstCurrency
        currencyInfo["secondCurrency"] = secondCurrency
        currencyInfo["amount"] = amount
        currencyInfo["result"] = result

        return render_template("main.html",info = currencyInfo)

    # showing main.html   
    else:
        return render_template("main.html" )



if __name__ == "__main__":
    app.run(debug=True)