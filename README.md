# 🌱 AI Weed Detection System

An AI-powered computer vision system that detects weeds in agricultural field images using a deep learning object detection model.

This project combines **YOLO-based deep learning**, a **FastAPI backend**, and a **React frontend** to provide a complete end-to-end weed detection system for precision agriculture.

The system allows users to upload a field image and instantly detect weeds with bounding boxes drawn around them.

---

# 📌 Project Motivation

Weeds compete with crops for nutrients, sunlight, and water, reducing agricultural productivity. Manual weed detection is time-consuming and inefficient.

Recent advancements in **deep learning and computer vision** enable automated weed detection directly from images captured in fields. These systems help farmers make faster and more accurate decisions about weed management. :contentReference[oaicite:0]{index=0}

This project demonstrates how AI can be integrated with a web application to support **precision agriculture**.

---

# 🧠 Model Used

This system uses the **YOLO (You Only Look Once) object detection model** for real-time weed detection.

YOLO models are widely used for agricultural object detection tasks because they can detect multiple objects in a single image efficiently and in real time. :contentReference[oaicite:1]{index=1}

### Model Features

- Deep Learning Object Detection
- Real-time inference
- Bounding box prediction
- High efficiency for real-world applications

---

# 🏗 System Architecture


### Components

**Frontend**
- React.js
- Image upload UI
- Detection result display

**Backend**
- FastAPI
- Image processing
- Model inference

**Model**
- YOLO-based object detection model
- Trained on agricultural weed dataset

FastAPI is commonly used to deploy machine learning models as high-performance APIs due to its speed and simplicity. :contentReference[oaicite:2]{index=2}

---

# 📊 Dataset

The model was trained on an agricultural weed detection dataset containing images of crops and weeds.

Dataset preprocessing included:

- Image annotation
- Train/Validation/Test split
- Dataset rebalancing
- Data augmentation

The dataset itself is **not included in this repository** due to size limitations.

---

# ⚙️ Model Weights

The trained model weights are available here:

📥 **Download Model**

https://drive.google.com/drive/folders/1Wn5OxZ2hHjXUaXZhRHsvsjFjHkmfFt9M?usp=sharing

---

# 📸 Project Demo

### Landing Page

![Landing Page](assets/hero.png)

---

### Upload Field Image

Upload an agricultural field image and adjust the confidence threshold for detection.

![Upload Image](assets/upload.png)

---

### Detection Result

The AI model analyzes the image and highlights weeds using bounding boxes.

The system also returns:

• Number of weeds detected  
• Processing time for inference  

![Detection Result](assets/result.png)

---

# 📸 Application Workflow

1️⃣ Upload an agricultural field image  
2️⃣ Adjust confidence threshold  
3️⃣ Click **Detect Weeds**  
4️⃣ The AI model analyzes the image  
5️⃣ Bounding boxes highlight detected weeds  

---

# 🛠 Tech Stack

### Machine Learning

- Python
- YOLO Object Detection
- PyTorch

### Backend

- FastAPI
- Uvicorn

### Frontend

- React.js
- Axios

### Tools

- Git
- GitHub
- VS Code

---

# 🌾 Applications

This system can be used for:

- Smart farming
- Precision agriculture
- Automated weed detection
- Agricultural research
- Crop monitoring systems

---

# 🔮 Future Improvements

Potential enhancements:

- Mobile app integration
- Drone image analysis
- Real-time video detection
- Edge AI deployment
- Automatic weed spraying integration

---

# 👨‍💻 Author

**Aniket Singh**

Final Year Engineering Project  
AI / Machine Learning Enthusiast

GitHub  
https://github.com/aniket1920

---

# ⭐ If you found this project useful

Please consider **starring the repository**.


# 🏗 System Architecture
