# Banana Leaf Disease Detection

## Datasets Used

The model was trained on a **combined dataset** from two sources:

1. [Banana Leaf Disease Dataset - Kaggle](https://www.kaggle.com/datasets/shifatearman/bananalsd)  
2. [Mendeley Banana Leaf Dataset](https://data.mendeley.com/datasets/79w2n6b4kf/1)

the dataset includes the following **7 classes**:
- Black Sigatoka
- Yellow Sigatoka
- Banana Bunchy Top Virus (BBTV)
- Banana Streak Virus (BSV)
- Banana Bract Mosaic Virus (BBMV)
- Fusarium Wilt
- Healthy

## Models Used

The following CNN architectures were fine-tuned for classification:

- VGG16  
- ResNet152V2  
- InceptionV3  
- MobileNetV2  
- LeNet (custom implementation)

The best performing model - VGG16 is saved as `model.h5` for inference in the web application.


## Installation

Follow these steps to set up the project on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/banana-leaf-disease-detection.git
cd banana-leaf-disease-detection
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```
### 3. Train Model

- Run the run.ipynb notebook to train your desired CNN model.
- Export the model as model.h5

### 4. Set Up Static Folder for Uploads
```bash
mkdir static
```

### 5. Run the Flask App
```bash
python app.py
```
