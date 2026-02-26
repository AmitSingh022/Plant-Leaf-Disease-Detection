🌿 Plant Leaf Disease Detection System

A Deep Learning–based web application built with Django + TensorFlow + Keras to detect plant leaf diseases from images.
The model is trained on a Kaggle Plant Leaf Disease dataset containing 24+ classes of healthy and diseased plant leaves.

📌 Features

Upload plant leaf image
Predict disease using trained CNN / MobileNetV2 model
Supports 24+ plant disease classes
Django-based web interface
Image upload & preview
Model prediction display

📂 Dataset
You can download the Plant Disease Leaf Dataset from Kaggle:
👉 Search on Kaggle:
"Plant leaf Dataset"
The dataset includes:
24+ classes
Healthy and diseased leaves
Training & validation images

After downloading:
dataset/
│
├── train/
├── validation/

Place the dataset inside your project directory before training.

⚙️ Installation Guide
1️⃣ Clone Repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2️⃣ Create Virtual Environment
python -m venv venv
Activate it:
Windows
venv\Scripts\activate
Mac/Linux
source venv/bin/activate

3️⃣ Install Requirements
Create a file named:
📄 requirements.txt
absl-py==2.4.0
asgiref==3.8.1
astunparse==1.6.3
certifi==2026.2.25
charset-normalizer==3.4.4
contourpy==1.3.3
cycler==0.12.1
Django==5.1.4
django-autoslug==1.9.9
django-tinymce==5.0.0
djongo==1.3.7
flatbuffers==25.12.19
fonttools==4.61.1
gast==0.7.0
google-pasta==0.2.0
grpcio==1.78.1
h5py==3.15.1
idna==3.11
keras==3.13.2
kiwisolver==1.4.9
libclang==18.1.1
Markdown==3.10.2
markdown-it-py==4.0.0
MarkupSafe==3.0.3
matplotlib==3.10.8
mdurl==0.1.2
ml_dtypes==0.5.4
mysqlclient==2.2.8
namex==0.1.0
numpy==2.4.2
opencv-python==4.13.0.92
opt_einsum==3.4.0
optree==0.19.0
packaging==26.0
pandas==3.0.1
pillow==11.1.0
protobuf==6.33.5
Pygments==2.19.2
pymongo==3.11.4
PyMySQL==1.1.2
pyparsing==3.3.2
python-dateutil==2.9.0.post0
pytz==2025.2
requests==2.32.5
rich==14.3.3
setuptools==82.0.0
six==1.17.0
sqlparse==0.5.3
tensorboard==2.20.0
tensorboard-data-server==0.7.2
tensorflow==2.20.0
termcolor==3.3.0
typing_extensions==4.15.0
tzdata==2024.2
urllib3==2.6.3
Werkzeug==3.1.6
wheel==0.46.3
wrapt==2.1.1

Then install:
pip install -r requirements.txt

🚀 How to Run Project
Run Django Server
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

Open browser:
http://127.0.0.1:8000/

🌱 How to Predict Plant Leaf Disease

Step 1: Train Model (if not trained)
This will:
Load dataset
Train CNN
Save model file (model.keras or .h5)

Step 2: Upload Leaf Image
Open website
Go to prediction page
Upload plant leaf image
Click predict

Step 3: Model Prediction
The system will:
Preprocess image
Resize to required input shape
Normalize pixel values

Run model prediction
Display predicted disease name

🧠 Model Architecture
Custom CNN:
Conv2D
MxPooling
Flatten
Dense Layers
Optimizer:
Adam
Loss Function:
Categorical Crossentropy

📊 Technologies Used
Python
Django
TensorFlow
Keras
OpenCV
NumPy
Matplotlib

Pandas
