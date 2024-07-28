from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.inception_v3 import preprocess_input
import numpy as np
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static'
# Load the model
model = load_model('Model.h5')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}

# Create a list containing the class labels
class_labels = ['bract mosaic', 'cordana', 'healthy', 'insect pest', 'moko', 'pestalotiopsis', 'sigatoka']

def model_predict(img_path, model):
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    preds = model.predict(x)
    pred = np.argmax(preds, axis=-1)
    return class_labels[pred[0]]

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return render_template('index.html', error='No file part')
        file = request.files['file']
        if file.filename == '':
             return render_template('index.html', error='No selected file')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join('static', filename)
            file.save(file_path)
            prediction = model_predict(file_path, model)
            return render_template('index.html', prediction=prediction, img_path=file_path)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
