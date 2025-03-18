from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    images = [f for f in os.listdir('static') if f.endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    return render_template('image_gallery.html', images=images)

if __name__ == "__main__":
    app.run(debug=True)
