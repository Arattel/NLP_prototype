from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
app.config["CACHE_TYPE"] = "null"


@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/results/", methods=['POST'])
def add_message():
    dict_resp = {
        "class":"pont"
    }
    text_for_classification = request.get_json(force=True)['text']
    return jsonify(dict_resp)

if __name__ == "__main__":
    app.run()
