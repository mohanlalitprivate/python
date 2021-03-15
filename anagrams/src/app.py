from flask import Flask, jsonify
from flask_restful import Resource, Api
from anagrams_finder import read_words_from_file, find_anagrams

app = Flask(__name__)

api = Api(app)

read_anagrams = read_words_from_file("dictionary.txt")

# Do not want to sort json at this time
app.config['JSON_SORT_KEYS'] = False

# Simple just let user know we are ready
@app.route("/")
def hello():
    return jsonify(
        {'message': 'Welcome to the Anagram finder', 'uses': '/anagrams/<your_word>', 'example': 'http://localhost:5000/anagrams/stop'})


class Anagrams(Resource):
    def get(self, word: str) -> str:
        if len(read_anagrams) >= 1:
            found_anagrams = find_anagrams(read_anagrams, word)
            if len(found_anagrams) > 0:
                return jsonify({'user_input': word, 'anagrams': list(found_anagrams)})
            else:
                return jsonify({'user_input': word, 'message': 'No anagram found'})
        else:
            return jsonify({'user_input': word, 'error': 'We are having trouble in loading data, please check back latter'})


api.add_resource(Anagrams, '/anagrams/<string:word>')

#for out side docker use following to run at localhost
app.run(port=5000)
# for docker use
#app.run(host='0.0.0.0')
#docker run --publish 5000:5000 --name python-anagram-container -d python-anagram-docker # -d for detach