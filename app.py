from flask import Flask, request, render_template
import google.generativeai as genai
import os

#############################
#                           #
#   Initiate model config   #
#                           #
#############################

api = os.getenv("api")

genai.configure(api_key= api)
model = genai.GenerativeModel("gemini-1.5-flash")

#######################
#                     #
#   Initiate Web App  #
#                     #
#######################

app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])
def index():
    return render_template("index.html")

@app.route("/makersuite", methods = ["GET","POST"])
def makersuite():
    return render_template("makersuite.html")

@app.route("/gemini", methods = ["GET","POST"])
def gemini():
    q = request.form.get("q")
    r = model.generate_content(q)
    return render_template("gemini.html", r = r.candidates[0].content.parts[0].text)

if __name__ == "__main__":
    app.run()