# Customer Segmentation using KMeans Clustering

This project demonstrates unsupervised learning by applying KMeans clustering to segment mall customers based on their annual income and spending score. The project is presented both in modular Python files and an interactive Streamlit app.

---

## 📁 Project Structure

```
Unsupervised_Clustering_Project/
├── data_loader.py           # Loads the dataset
├── clustering.py            # Handles KMeans and silhouette scoring
├── visualize.py             # Creates scatter, elbow, and pair plots
├── main.py                  # Streamlit app for user interface
├── mall_customers.csv       # Optional: sample dataset
├── requirements.txt         # Required Python packages
├── README.md                # Documentation
└── .gitignore               # Ignore Python cache files, etc.
```

---

## 📊 Dataset Details

Dataset: `mall_customers.csv`  
Key columns used:

- **Age**
- **Annual_Income**
- **Spending_Score**

---

## 🚀 How to Run This Project

### 1. Clone the Repo
```bash
git clone https://github.com/yourusername/Unsupervised_Clustering_Project.git
cd Unsupervised_Clustering_Project
```

### 2. Install Requirements
```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit App
```bash
streamlit run main.py
```

> 📂 Upload your `mall_customers.csv` file when prompted.

---

## 📈 Features

- Visualize customer clusters based on income & spending
- Generate WSS (elbow) and silhouette plots
- Understand optimal cluster count using metrics
- Fully interactive app with auto clustering

---

## 🧪 Techniques Used

- KMeans Clustering (`sklearn.cluster.KMeans`)
- Elbow Method (WSS)
- Silhouette Score
- Seaborn scatterplots and pairplots

---

## 📦 Requirements

```
pandas
numpy
matplotlib
seaborn
scikit-learn
streamlit
```

Install with:
```bash
pip install -r requirements.txt
```

---

## 🤝 Contributions

Pull requests and feedback are always welcome!

---

## 📜 License

This project is open source under the MIT License.

---

## 🙏 Acknowledgements

Inspired by classic mall customer datasets used for segmentation and behavioral clustering tutorials.


## Contact

For any questions or suggestions, feel free to contact the project maintainer at pand0106@algonquinlive.com
