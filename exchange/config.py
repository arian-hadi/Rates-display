API_KEY = "password"
API_URL = "http://data.fixer.io/api/latest?access_key="
url = API_URL + API_KEY

EMAIL_RECEIVER = "arianhadi2003@gmail.com"

rules = {
    "archive" : True,
    "send_mail" : True,
    "preferred" : {'BTC', 'IRR', "IQD", "USD", "CAD", "AED"} 
}
