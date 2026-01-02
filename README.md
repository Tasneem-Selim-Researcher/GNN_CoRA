# Cora Node Classification Challenge (GCN-Based)

## 📌 Overview

This repository hosts the **Cora Node Classification Challenge**, a graph machine learning competition based on the **Cora citation network**. Participants are required to design and train **Graph Neural Network (GNN)** models to classify scientific papers into research topics using node features and graph structure.

The competition follows **standard academic evaluation protocols** used in benchmark GNN literature (e.g., Kipf & Welling, 2017).

---

## 🧠 Task Description

* Each node represents a **scientific publication**.
* Edges represent **citation relationships** between papers.
* Each node belongs to **one of 7 classes**.

### Objective

Train a model that accurately predicts the class labels of **unlabeled test nodes**, using:

* Node features
* Graph connectivity

The final ranking is based on **Macro F1-score** on a hidden test set.

---

## 📊 Dataset Details

⚠️ Note on Dataset Difficulty (Important)

To increase the difficulty level and encourage robust model design, controlled noise has been added to the dataset.

The provided dataset is NOT identical to the original Cora benchmark

Participants must work with the provided files

Replacing the data with the original Cora dataset is not allowed

This design choice ensures a fair comparison between methods and evaluates the ability of models to generalize under noisy and imperfect real-world conditions.

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

## 📁 Provided Files

```
data/
├── train_val_labeled.csv      # Node features + labels for training & validation
├── test_features_only.csv     # Node features for test nodes (labels hidden)
├── adjacency_matrix.csv       # Graph adjacency matrix

starter_code/
├── gcn_starter.py  (or .ipynb)
├── requirements.txt
```


### Public Files:
the dataset is hosted externally on **Google Drive**.

### 🔗 **Download Link**
➡️ [Click here to access the dataset](
### Public Files:
the dataset is hosted externally on **Google Drive**.

### 🔗 **Download Link**
➡️ [Click here to access the Adjacency Matrix](https://drive.google.com/file/d/17SKE86QU9bBahpdUIeFNjJqRg05QFFfx/view?usp=sharing)
➡️ [Click here to access the Train and Validation data](https://drive.google.com/file/d/1ruYD0JdX_yGv1of_EUM9lcv0t6lmZ3tX/view?usp=sharing)

### Private Files:
- Test_data → Hidden ground-truth data used for automatic evaluation  

---
)
## 🚀 Getting Started

### Run the Starter Code

```bash
python gcn_starter.py
```

This will:

* Load the dataset
* Train a baseline GCN model
* Generate a `submission.csv` file

---

## 📝 Submission Format

Participants must submit a CSV file named **`submission.csv`** with the following format:

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

* **Macro F1-score** (primary metric)
* Accuracy (secondary metric)

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

## 🕐 Submission Limits

- Each Team should name the file something like: **Team1**.
- Only the **latest submission** counts toward the leaderboard.

---

## 🧾 Leaderboard

- Leaderboard scores are automatically updated based on accuracy.
- In case of identical scores, the earlier submission time will be used as a tiebreaker.

---

## 🎓 Academic Integrity

This competition is intended for **educational and research purposes**.

* Plagiarism is not allowed
* External pretrained models using Cora labels are prohibited

---

## 📩 Contact

If you face issues with the repository or evaluation: 
- Contact me at tasneem.mselim@gmail.com 


---

## 📚 References

* Kipf, T. N., & Welling, M. (2017). *Semi-Supervised Classification with Graph Convolutional Networks*. ICLR.

---

## 👩‍💻 Organizer

**Tasneem Selim**
Teaching Assistant & Researcher in Computer Vision and Graph Machine Learning

---

Good luck, and happy graph learning 🚀
