# User KYC Verification Platform

## Overview

The **User KYC (Know Your Customer) Verification Platform** is designed to provide a comprehensive and efficient solution for user verification through advanced image recognition techniques. The platform captures a live image of the user, verifies it against an uploaded ID document, and compares a second image against a large database of stored images. It incorporates advanced algorithms for facial recognition, liveness detection, and large-scale image comparisons while maintaining high scalability and performance.

---

## Key Features

### 1. **Live Image Capture and Verification**
   - **Objective**: Ensure the user is physically present during the verification process.
   - The platform captures a live image of the user using a webcam, ensuring that the image is not pre-recorded or a static image (e.g., a photo of a photo).
   - Real-time validation techniques such as **blink detection**, **head movement**, or **on-prompt gestures** (e.g., the user showing a specific gesture on command) are used to confirm the user is genuinely present.

### 2. **Document Upload and Comparison**
   - **Objective**: Verify the user’s identity by comparing their live image with a provided ID document.
   - Users upload an ID document (such as a passport or driver’s license) containing their photo. The platform automatically crops the face from the document for facial recognition purposes.
   - The live image captured during the liveness check is compared to the ID document photo using **facial recognition algorithms** such as those provided by **DeepFace**, utilizing models like **VGG-Face**, **FaceNet**, and **ArcFace**.

### 3. **Database Search for Image Comparison**
   - **Objective**: Check for potential matches between the user’s second uploaded image and a large database of stored images.
   - The second image uploaded by the user (a random image of themselves) is compared against a large-scale image dataset (10,000+ images or more) using **cosine similarity** and **K-nearest neighbors (KNN)** algorithms.
   - To enhance performance, **pre-extracted facial embeddings** are stored in pickle files and indexed using libraries such as **Annoy** or **Faiss** for fast similarity search.

### 4. **Liveness Detection**
   - **Objective**: Ensure the user is not attempting to deceive the system by using static images or pre-recorded videos.
   - The platform implements various techniques for liveness detection, including:
     - **Blink detection**: Eye Aspect Ratio (EAR) is calculated to detect if the user blinks within a specified timeframe.
     - **Head movement tracking**: The system tracks subtle head movements to ensure real-time interaction.
     - **On-prompt gestures**: The user is asked to perform a gesture (e.g., showing a V-sign with fingers) to confirm their physical presence.

### 5. **Scalability and Performance Optimization**
   - **Objective**: Ensure the platform can handle high user volumes and large-scale datasets efficiently.
   - Optimized for scalability, the platform leverages:
     - **Parallel searching** for faster database comparisons.
     - **Top-K cosine similarity** for reduced time complexity (O(n²) to O(n)).
     - **ElasticSearch integration** for highly efficient text-based queries, and **Annoy** or **Faiss** for approximate nearest neighbor searches.

### 6. **Support for Multiple Image Formats**
   - **Objective**: Ensure flexibility in the types of images the platform can handle.
   - The platform supports various image formats (JPEG, PNG, etc.) and adjusts for differences in lighting, angles, and accessories (such as hats or glasses) to maintain high accuracy in facial recognition.

---

## Project Structure

The platform consists of the following key components:

### 1. **Web Service (Flask API)**
   - A RESTful Flask API that handles all client requests for image capture, liveness detection, document upload, and image verification.
   - Endpoints:
     - `/find_neighbors`: For querying the database and finding similar faces.
     - `/cosine_similarity`: For calculating cosine similarity between two embeddings.
     - `/search`: For text-based searches using ElasticSearch.
     - `/health`: For checking the system’s health and verifying that all components are running correctly.

### 2. **Liveness Detection**
   - **Libraries**: OpenCV, Dlib
   - Implements eye-blink detection, head movement tracking, and on-prompt gesture detection using facial landmarks.

### 3. **Facial Recognition Using DeepFace**
   - **Libraries**: DeepFace (VGG-Face, FaceNet, ArcFace models)
   - Compares live images and ID document photos using pre-trained models and similarity metrics such as cosine similarity and Euclidean distance.

### 4. **Database Search and Image Matching**
   - **Libraries**: Annoy, Faiss, ElasticSearch
   - **Techniques**: Top-K cosine similarity, KNN
   - The system indexes the embeddings from the database of images and efficiently searches for the most similar images to the second user-uploaded image.

---

## APIs and Endpoints

### 1. **Liveness Detection**
   - **Endpoint**: `/liveness_check`
   - Verifies whether the user is live and present using blink detection, head movement, and gesture prompts.

### 2. **Document Verification**
   - **Endpoint**: `/verify_document`
   - Compares the live image captured from the user with the cropped face from the ID document for identity verification.

### 3. **Find Neighbors (Database Search)**
   - **Endpoint**: `/find_neighbors`
   - Compares the second image uploaded by the user with a large-scale dataset to find the top-K most similar faces using cosine similarity.

### 4. **Cosine Similarity Calculation**
   - **Endpoint**: `/cosine_similarity`
   - Accepts two vectors and calculates the cosine similarity between them for image embedding comparisons.

### 5. **ElasticSearch Query**
   - **Endpoint**: `/search`
   - Provides text-based search functionality using the ElasticSearch engine to query indexed data based on a given query.

### 6. **Health Check**
   - **Endpoint**: `/health`
   - A simple GET endpoint to check the health of the service, confirming whether embeddings are loaded and the service is operational.

---

## Setup and Installation

### Prerequisites:
- **Python 3.7+**
- **Elasticsearch** (for text-based searches)
- **Annoy/Faiss** (for fast nearest neighbor searches)
- **Flask** (for API services)
- **OpenCV** and **Dlib** (for liveness detection)
- **DeepFace** (for facial recognition)

### Steps to Set Up:
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/KYC-Verification-Platform.git
   cd KYC-Verification-Platform
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up **Elasticsearch**:
   - Ensure Elasticsearch is running locally at `http://localhost:9200`. You can also configure it in the Flask app if using a different setup.

4. Run the Flask app:
   ```bash
   python app.py
   ```

5. Access the platform via `http://localhost:5000`.

---

## Future Scopes

1. **Switch to ResNet-50 for AI Models**:
   - Improve facial recognition accuracy by replacing MobileNet with ResNet-50 for better handling of complex image conditions.

2. **Enhanced Liveness Detection**:
   - Add depth mapping, micro-expression detection, and 3D face mapping to further prevent spoofing.

3. **Client-Side Processing**:
   - Shift some facial recognition and liveness detection tasks to the client-side using **TensorFlow.js** to reduce server load and improve scalability.

4. **AI-Based Fake Image Detection**:
   - Implement deepfake detection algorithms to prevent the submission of AI-generated or manipulated images.

5. **OCR for Document Verification**:
   - Add Optical Character Recognition (OCR) capabilities to automatically extract and verify textual information from ID documents.

---

## Performance and Time Estimation

### Liveness Detection:
- Current performance allows for **real-time checks** with blink detection, head movement, and gesture prompts, ensuring a **response time of ~0.5 to 1 second**.

### Verification Using DeepFace:
- **Cosine similarity** and **Euclidean distance** are used for facial verification, with response times **reduced to 0.9 seconds** using **pre-extracted embeddings** and optimized model performance.

### ElasticSearch Microservice:
- Provides **text-based search** functionality with response times typically ranging from **0.1 to 1 second**, depending on the size of the index and complexity of the query.

---

## Conclusion

The **User KYC Verification Platform** is a powerful and scalable solution for identity verification through facial recognition. By combining **liveness detection**, **document verification**, and **database image comparisons**, the platform ensures robust security while maintaining performance. The integration of advanced algorithms, such as **DeepFace** and **Elasticsearch**, allows for efficient and reliable user verification in real time, making it a cutting-edge solution for KYC compliance.

