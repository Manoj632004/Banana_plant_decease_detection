# Bananaleaf_decease_detection

dataset used:
https://www.kaggle.com/datasets/shifatearman/bananalsd ; https://data.mendeley.com/datasets/79w2n6b4kf/1

Fine tuned CNN models used are
  - VGG16
  - ResNet152V2
  - Inceptionv3
  - MobileNetV2
  - LeNet

setting up the web app:
- Create virtual environment
- Use 'pip install -r requirements.txt' to install required libraries
- import python files
- compile run.ipynb to get the model.h5 file with the CNN model you wish to run 
- create static folder in your virtual environment for the user uploaded image to store
- Use 'python app.py' to run the web app
