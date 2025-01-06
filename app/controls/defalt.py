from app import app, render_template, request as req
from app.controls.mp3 import download_audio

@app.route("/", methods=("GET","POST"))
def home():
    if req.method == "POST":
        url = req.form["url"]
        try:
            download_audio(url)
        except Exception as erro:
            print(erro)
    return render_template("index.html")