from flask import Flask
import credit_card_validation as ccv

app = Flask(__name__)
app.config["DEBUG"] = True

# Gets the checksum value for credit card no.
@app.route('/getChecksum/<cardNumber>', methods=['GET'])
def checksum(cardNumber):
    cardNumber = cardNumber.replace(" ","")

     # to check if there are only numbers
    if cardNumber.isnumeric() != True:
    	return "Invalid card number"
    return str(ccv.checksum(str(cardNumber)))

# checks if the no. is valid or not
@app.route('/isValid/<cardNumber>', methods=['GET'])
def is_valid(cardNumber):
    return str(ccv.is_valid(str(cardNumber)))

# Gets the brand of the credit card based on card no. and cvv
@app.route('/getBrand/<cardNumber>/<cvv>', methods=['GET'])
def get_brand(cardNumber, cvv):
    return str(ccv.get_brand(str(cardNumber), str(cvv)))

if __name__=="__main__":
	app.run()