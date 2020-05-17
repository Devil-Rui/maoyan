from flask import Flask, jsonify,render_template,request
import code.dataService as dataservice
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/score_page')
def score_page():
    return render_template('score.html',categories=dataservice.get_categories(),districts=dataservice.get_districts())

@app.route('/film')
def film():
    return render_template('film.html',films = dataservice.getFilm(1,10),film_length=100,page_span=10)

@app.route('/category',methods=["get"])
def category():
    data = dataservice.category_op()
    return jsonify(data)

@app.route('/area',methods=["get"])
def area():
    return jsonify(dataservice.get_money())

@app.route('/country',methods=["get"])
def country():
    data = dataservice.area_op()
    return jsonify(data)

@app.route('/year',methods=["get"])
def year():
    data = dataservice.year_op()
    return jsonify(data)

@app.route('/length',methods=['get'])
def length():
    data = dataservice.length_op()
    return jsonify(data)


@app.route('/score',methods=['get'])
def score():
    data = dataservice.score_op()
    return jsonify(data)

@app.route('/scoreWithCategory',methods=['get'])
def scoreWithCategory():
    category = request.values.get('category')
    l = [dataservice.scoreWithYearByCatetory(category),dataservice.scoreWithLengthByCatetory(category)]
    return jsonify(l)

@app.route('/scoreWithCountry',methods=['get'])
def scoreWithCountry():
    country = request.values.get('country')
    l = [dataservice.scoreWithYearByCountry(country),dataservice.scoreWithLengthByCountry(country)]
    return jsonify(l)

@app.route('/averageWithCategory',methods=['get'])
def averageWithCategory():
    country = request.values.get('country')
    return jsonify(dataservice.get_average(country))


@app.route('/keyword',methods=['post'])
def keyword():
    keyword = request.values.get('keyword')
    return jsonify(dataservice.getFilmByKey(keyword))

@app.route('/page',methods=['get'])
def page():
    page = request.values.get('page')
    return jsonify(dataservice.getFilm(int(page),10))






if __name__ == '__main__':
    app.run()



