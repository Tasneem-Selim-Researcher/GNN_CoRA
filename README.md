# Cora Node Classification Challenge (GCN-Based)

## 📌 Overview

This repository hosts the **Cora Node Classification Challenge**, a graph machine learning competition based on the **Cora citation network**. Participants are required to design and train **Graph Neural Network (GNN)** models to classify scientific papers into research topics using node features and graph structure.

## 🏆 Leaderboard
- Leaderboard scores are automatically updated based on accuracy.
- View the live leaderboard:  
👉 **[Leaderboard](https://tasneem-selim-researcher.github.io/GNN_CoRA/final_leaderboard.html)**

---

## 🧠 Task Description

* Each node represents a **scientific publication**.
* Edges represent **citation relationships** between papers.
* Each node belongs to **one of 7 classes**.

### Objective

Train a model that accurately predicts the class labels of **unlabeled test nodes**, using:

* Node features
* Graph connectivity

---

## 📊 Dataset Details

⚠️ Note on Dataset Difficulty

To increase the difficulty level and encourage robust model design, controlled noise has been added to the dataset.

The provided dataset is NOT identical to the original Cora benchmark

Participants must work with the provided files

Replacing the data with the original Cora dataset is not allowed

## 📊 Dataset Details

The dataset is derived from the **Cora citation network**.

| Property      | Value                |
| ------------- | -------------------- |
| Nodes         | 2,708                |
| Edges         | 5,429 (undirected)   |
| Node features | 1,433 (bag-of-words) |
| Classes       | 7                    |

### Data Splits (Standard Cora Protocol)

* **Training nodes**: 140 (20 per class)
* **Validation nodes**: 500 
* **Test nodes**: 1,000 (labels hidden)

---

### Public Files:
the dataset is hosted externally on **Google Drive**.

### 🔗 **Download Link**
➡️ [Click here to access the Adjacency Matrix](https://drive.google.com/file/d/17SKE86QU9bBahpdUIeFNjJqRg05QFFfx/view?usp=sharing)

➡️ [Click here to access the Train and Validation data](https://drive.google.com/file/d/1ruYD0JdX_yGv1of_EUM9lcv0t6lmZ3tX/view?usp=sharing)

➡️ [Click here to access the Test features only](https://drive.google.com/file/d/19AdwSvFBT_3n0wiQ_rwkSWBD97nwAdpt/view?usp=sharing)

### Private Files:
- Test_label → Hidden ground-truth data used for automatic evaluation  

---
## 📝 How to Submit Your Results

Follow the steps below to submit your predictions to the competition leaderboard.

---

### Step 1: Fork the Repository

### Step 2: Navigate to Your Forked Repository

### Step 3: Go to the Submission Folder

### Step 4: Upload Your Submission File

📌 **File naming rule (mandatory):** yourName **Example:** `MonaAli.csv`

### Step 5: Commit Your File

### Step 6: Create a Pull Request

✅ Your submission will be reviewed and evaluated, and the results will be added to the leaderboard.

---


## 📝 Submission Format

Participants must submit a CSV file named **`YourName.csv`** with the following format:

```csv
id,target
1708,3
1709,1
1710,6
...
```

### Rules

* `id` must match the provided test node IDs
* `target` must be an integer in `{0, 1, 2, 3, 4, 5, 6}`

---

## 📈 Evaluation Metric

Submissions are evaluated using:

* **Accuracy** 

Evaluation is performed on a **hidden test set** to prevent data leakage.

---

## ✅ Allowed Methods

* Any **Graph Neural Network** architecture 
* Feature preprocessing and normalization
* Hyperparameter tuning

## ❌ Not Allowed

* Using test labels
* Modifying test node IDs
* Training on test nodes

---

## 🏆 Baseline

The provided starter code implements a **2-layer Graph Convolutional Network (GCN)** as a baseline.

Participants are encouraged to improve upon this baseline using:

* Deeper architectures
* Attention mechanisms
* Regularization techniques

---



## 📚 References

* Kipf, T. N., & Welling, M. (2017). *Semi-Supervised Classification with Graph Convolutional Networks*. ICLR.
  
- **GNNs Tutorials (YouTube) – BASIRA Lab**:  
  [https://www.youtube.com/@BASIRALab](https://www.youtube.com/playlist?list=PLug43ldmRSo14Y_vt7S6vanPGh-JpHR7T)
  

- **GNN Tutorials (GitHub) – BASIRA Lab**:  
  https://github.com/basiralab
---

## 👩‍💻 Organizer

**Tasneem Selim**
Teaching Assistant & Researcher in Computer Vision and Graph Machine Learning
If you face issues with the repository or evaluation: 
- Contact me at tasneem.mselim@gmail.com 

---

Good luck, and happy graph learning 🚀
