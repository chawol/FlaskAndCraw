from bs4 import BeautifulSoup
import requests as rq
import json
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
url = "http://www.leonland.de/elements_by_price/en/list"
response = rq.get(url).text
soap = BeautifulSoup(response, 'html.parser')
table = soap.find(id='tlst')
json_data = {}
datas = []
for i in table.find_all('tr')[1:]:
    ele = i.find_all('td')
    data = {"id": ele[0].text, "Price": ele[3].text}
    datas.append(data)

    # j = {"id": ele[0].text, "value": ele[3].text}
    # print(ele[0].text + ":" + ele[3].text)
json_data = json.dumps(datas)


@app.route("/")
def json():
    return json_data


if __name__ == "__main__":
    app.run()
