from flask import Flask, render_template, request, url_for
import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()
TENOR_API_KEY = os.getenv("TENOR_API_KEY")


app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""

    #An API call for trending GIFs
    trending_response = requests.get(f"https://api.tenor.com/v1/trending?key={TENOR_API_KEY}&limit=10")
    #Returns jason data
    gifs_trending = json.loads(trending_response.content)

    return render_template("index.html", gif_url_list=gifs_trending['results'])

@app.route('/gifs')
def gifsearch():
    # TODO: Extract query term from url
    #"Request user input"
    search_term = request.args.get("q")
   # if search_term != search_term.isalpha():
    #    return False
    # TODO: Make an API call to Tenor using the 'requests' library
    response = requests.get(f'https://api.tenor.com/v1/search?q={search_term}&key=P7Z5S0UI3LE8&limit=10')
    # TODO: Get the first 10 results from the search results
    gifs = json.loads(response.content)
    return render_template("base.html", gif_url_list=gifs['results'])

    

if __name__ == '__main__':
    app.run(debug=True)


