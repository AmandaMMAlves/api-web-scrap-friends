from flask import Flask
from flask import jsonify
from WebScrap.web_scrap_service import get_friends_episodes

app = Flask(__name__)

@app.route('/episodes/season/<int:season>')
def web_scrap_friends_episodes_from_season(season):	
	
	return jsonify(get_friends_episodes(season))


if __name__ == "__main__":
	app.run()