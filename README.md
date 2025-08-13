# Banana Leaf Disease Detection

## Datasets Used

The model was trained on a **combined dataset** from two sources:

1. [Banana Leaf Disease Dataset - Kaggle](https://www.kaggle.com/datasets/shifatearman/bananalsd)  
2. [Mendeley Banana Leaf Dataset](https://data.mendeley.com/datasets/79w2n6b4kf/1)

the combined dataset includes the following **7 classes**:
- Sigatoka
- Moko
- Insect Pest
- pestalotiopsis
- Bract Mosaic Virus 
- cordana
- Healthy
<img width="2313" height="399" alt="sample_image" src="https://github.com/user-attachments/assets/0c820156-775b-4201-9db8-ed26cbdfa086" />

## Models Used

The following CNN architectures were fine-tuned for classification:

- VGG16  
- ResNet152V2  
- InceptionV3  
- MobileNetV2  
- LeNet (custom implementation)
<img width="4000" height="2400" alt="VGG_loss_plot" src="https://github.com/user-attachments/assets/29546539-777e-4482-b2e3-6e821812bad0" />
<img width="4000" height="2400" alt="ResNet_loss_plot" src="https://github.com/user-attachments/assets/03bc311c-1eb2-47f4-b572-8cf3a43cd0ee" />
<img width="4000" height="2400" alt="GoogLeNet_loss_plot" src="https://github.com/user-attachments/assets/48148d63-ec99-405b-86c8-2dd9922df25e" />
<img width="4000" height="2400" alt="LeNet_loss_plot" src="https://github.com/user-attachments/assets/43ef73ad-f510-44c6-a5d0-68a22c400aea" />
<img width="4000" height="2400" alt="MobileNet_loss_plot" src="https://github.com/user-attachments/assets/32cf61e6-bdc8-4d4b-b6a6-590c214a6ac7" />

The best performing model - VGG16 is saved as `model.h5` for inference in the web application.

## Workflow of Proposed Model
<img width="1065" height="540" alt="image" src="https://github.com/user-attachments/assets/1d904c5d-12c1-4d8a-bcda-64c9be1e3035" />

## Setup

Follow these steps to set up the project on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/Manoj632004/Banana_plant_decease_detection
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
