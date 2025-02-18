# 🚀 SPPU-BE-COMPUTER-LAB-CODE-SEM-8 🚀

Welcome to the repository for **SPPU BE Computer Semester 8 Lab Code**! This repository contains Python-based implementations of lab exercises for two subjects: **High Performance Computing (HPC)** and **Deep Learning (DL)**. Below, you will find a detailed description of the topics covered in each subject along with small descriptions.

---

## 📋 Table of Contents

1. [High Performance Computing (HPC)](https://github.com/GauravGhandat-23/SPPU-BE-COMPUTER-LAB-CODE-SEM-8/tree/main/HPC)
   - [1. Parallel BFS and DFS using Python Multiprocessing](https://github.com/GauravGhandat-23/SPPU-BE-COMPUTER-LAB-CODE-SEM-8/blob/main/HPC/HPC_practical_1.py)
   - [2. Parallel Bubble Sort and Merge Sort using Python Multiprocessing](https://github.com/GauravGhandat-23/SPPU-BE-COMPUTER-LAB-CODE-SEM-8/blob/main/HPC/HPC_Practical_2.py)
   - [3. Parallel Reduction for Min, Max, Sum, and Average](https://github.com/GauravGhandat-23/SPPU-BE-COMPUTER-LAB-CODE-SEM-8/blob/main/HPC/HPC_Practical_3.py)
   - [4. CUDA Programs](https://github.com/GauravGhandat-23/SPPU-BE-COMPUTER-LAB-CODE-SEM-8/blob/main/HPC/HPC_Practical_4.py)

2. [Deep Learning (DL)](https://github.com/GauravGhandat-23/SPPU-BE-COMPUTER-LAB-CODE-SEM-8/tree/main/DL)
   - [1. Linear Regression using Deep Neural Networks](https://github.com/GauravGhandat-23/SPPU-BE-COMPUTER-LAB-CODE-SEM-8/tree/main/DL/DL%20PRACTICAL%201)
   - [2. Binary Classification using Deep Neural Networks](https://github.com/GauravGhandat-23/SPPU-BE-COMPUTER-LAB-CODE-SEM-8/tree/main/DL/DL%20PRACTICAL%202)
   - [3. Convolutional Neural Network (CNN)](https://github.com/GauravGhandat-23/SPPU-BE-COMPUTER-LAB-CODE-SEM-8/tree/main/DL/DL%20PRACTICAL%203)
   - [4. Recurrent Neural Network (RNN)](https://github.com/GauravGhandat-23/SPPU-BE-COMPUTER-LAB-CODE-SEM-8/tree/main/DL/DL%20PRACTICAL%204)

---

## 🖥️ High Performance Computing (HPC)

### 1. Parallel BFS and DFS using Python Multiprocessing
- **Objective**: Design and implement parallel versions of Breadth First Search (BFS) and Depth First Search (DFS) using Python's `multiprocessing`.
- **Description**: 
  - BFS and DFS are implemented on a tree or an undirected graph.
  - Parallelization is achieved using Python's `multiprocessing` module to distribute tasks across multiple processes.

| **OUTPUT** |
|-----------------------------|
|  ![HPC Practical 1 output](https://github.com/user-attachments/assets/3b45e7c9-0463-4dba-bf32-0ef9bca6712f) |

### 2. Parallel Bubble Sort and Merge Sort using Python Multiprocessing
- **Objective**: Implement parallel versions of Bubble Sort and Merge Sort using Python's `multiprocessing`.
- **Description**:
  - Compare the performance of sequential and parallel versions of the algorithms.
  - Measure execution time to analyze the speedup achieved through parallelization.
    
| **OUTPUT** |
|-----------------------------|
| ![HPC Practical 2 output](https://github.com/user-attachments/assets/ce067406-edb3-4759-915f-4f202e9f4610) |  

### 3. Parallel Reduction for Min, Max, Sum, and Average
- **Objective**: Perform parallel reduction operations for computing Min, Max, Sum, and Average.
- **Description**:
  - Use Python's `multiprocessing` to perform parallel reduction on arrays.
  - Demonstrate how reduction operations can be efficiently parallelized.
  
### 4. CUDA Programs
#### 4.1 Addition of Two Large Vectors
- **Objective**: Implement vector addition for large vectors using CUDA Python (`numba.cuda`).
- **Description**:
  - Utilize GPU parallelism to add two large vectors.
  - Compare the performance with CPU-based implementation.

| **OUTPUT** |
|-----------------------------|
| ![HPC Practical 3 output](https://github.com/user-attachments/assets/414af1bb-c893-4034-a0d0-a47c7b2bafb0) |  
  
#### 4.2 Matrix Multiplication using CUDA Python
- **Objective**: Implement matrix multiplication using CUDA Python (`numba.cuda`).
- **Description**:
  - Leverage GPU threads to perform matrix multiplication in parallel.
  - Analyze the performance improvement over sequential matrix multiplication.

| **OUTPUT** |
|-----------------------------|
| ![HPC Practical 4 output](https://github.com/user-attachments/assets/ec464c5c-5c9c-4406-8873-1e9193a77654) |  

---

## 🧠 Deep Learning (DL)

### 1. Linear Regression using Deep Neural Networks
- **Objective**: Predict Boston housing prices using a Deep Neural Network (DNN).
- **Description**:
  - Use the Boston Housing Price Prediction dataset.
  - Build a DNN model to perform linear regression and predict house prices.
  
### 2. Binary Classification using Deep Neural Networks
- **Objective**: Classify movie reviews as "positive" or "negative" using a DNN.
- **Description**:
  - Use the IMDB dataset containing movie reviews.
  - Train a binary classification model to classify reviews based on text content.
  
### 3. Convolutional Neural Network (CNN)
#### 3.1 Plant Disease Detection System using CNN
- **Objective**: Design a plant disease detection system using a CNN.
- **Description**:
  - Use a dataset of plant images with various diseases.
  - Train a CNN model to detect and classify plant diseases.
  
#### 3.2 Fashion Clothing Classifier using MNIST Fashion Dataset
- **Objective**: Create a classifier to categorize fashion clothing using CNN.
- **Description**:
  - Use the MNIST Fashion dataset.
  - Train a CNN model to classify clothing items into categories like T-shirt, Dress, etc.
  
### 4. Recurrent Neural Network (RNN)
- **Objective**: Design a time series analysis and prediction system for Google stock prices using RNN.
- **Description**:
  - Use the Google stock prices dataset.
  - Train an RNN model to analyze historical data and predict future stock prices.

---

## 🛠️ Getting Started

### Prerequisites
- **Python Environment**: For all programs, set up Python with libraries like TensorFlow, Keras, NumPy, Pandas, and Matplotlib.
- **CUDA Toolkit**: For CUDA programs, install the CUDA toolkit and compatible GPU drivers.
- **Datasets**: Download datasets from official sources (e.g., Boston Housing, IMDB, MNIST Fashion, Google Stock Prices).

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/SPPU-BE-COMPUTER-LAB-CODE-SEM-8.git
   cd SPPU-BE-COMPUTER-LAB-CODE-SEM-8
   ```

2. Install dependencies:
   - For Python:
     ```bash
     pip install tensorflow keras numpy pandas matplotlib scikit-learn numba cudatoolkit
     ```

3. Run the programs:
   - Run Python scripts directly:
     ```bash
     python script_name.py
     ```
   - Or use Jupyter notebooks:
     ```bash
     jupyter notebook
     ```

---

Happy Coding! 🚀
