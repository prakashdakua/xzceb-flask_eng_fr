from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishtofrench")
def englishtofrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return render_template("index.html", translated_text = englishtofrench(textToTranslate))

@app.route("/frenchtoenglish")
def frenchtoenglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return render_template("index.html", translated_text = frenchtoenglish(textToTranslate))

@app.route("/")
@app.route("/index")
def renderIndexPage():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
