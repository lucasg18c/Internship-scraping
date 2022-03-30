from flask import Flask, abort, jsonify
from flask_cors import CORS

from internships import InternshipComponent


app = Flask(__name__)
CORS(app)
internships = InternshipComponent()


@app.route('/api/v1/internships/new/<int:newest_id>')
def get_new(newest_id: int):
    if newest_id < 0:
        return {"reason": "Invalid internship id"}, 404

    return jsonify(internships.get_newer(newest_id))


@app.route('/api/v1/internships')
def get_internships():
    return jsonify(internships.get_all())


@app.route('/api/v1/internships/<int:internship_id>')
def get_internship(internship_id):
    if internship_id < 0:
        return {"reason": "Invalid internship id"}, 404

    found = internships.get(internship_id)
    if not found:
        return {"reason": "Internship not found"}, 404

    return found


if __name__ == "__main__":
    app.run(host='0.0.0.0')
