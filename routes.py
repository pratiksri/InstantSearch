from flask import Flask,render_template,redirect, url_for, request
from SearchProcessor import SearchProcessor

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/search", methods = ['POST'])
def searchMain():
	search_str = request.form['search_str']
	if len(search_str) >= 3:
		return redirect(url_for('initiateSearch',str = search_str))
	else:
		return 'String too small'

@app.route('/search/<str>')
def initiateSearch(str):
	searchProcessor = SearchProcessor(str)
	df = searchProcessor.startSearch()
	if df.shape[0] > 0:
		return render_template('searchResults.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)
	else:
		return "No matching results found"
 
if __name__ == "__main__":
	app.run(debug=True)