from flask import Flask, request, render_template
import csv

application = Flask(__name__)

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/', methods=['POST', 'GET'])
def index_post():
    list = []
    name = []
    sale = []
    market = []
    year = []
    sector = []
    industry = []
    text = request.form['symbol']
    processed_text = text.upper()
    with open('companylist.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            list.append(line[0])
    with open('companylist.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        if processed_text in list:
            for line in csv_reader:
                if processed_text == line[0]:
                    name.append(line[1])
                    sale.append(line[2])
                    market.append(line[3])
                    year.append(line[5])
                    sector.append(line[6])
                    industry.append(line[7])

        else:
            return render_template("Unknown.html")
    return render_template('result.html', name=name, sale=sale, market=market, year=year, sector=sector, industry=industry)

if __name__ == '__main__':
    application.run()
