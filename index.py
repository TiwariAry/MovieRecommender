from flask import Flask, render_template, request, redirect, url_for
from recommender import recommender_function

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home_page():
	if request.method == 'POST':
		movie_name = request.form['movie']
		return redirect(url_for('results', movie=movie_name))
	return render_template('index.html')

@app.route('/results/<string:movie>')
# Expects one argument as specified by the route
def results(movie):
	movie_list = recommender_function(movie)
	return render_template('results.html', movies=movie_list)


if __name__ == "__main__":
	app.run(debug=True)
