# 🛒 Superstore Sales Analysis  

## 🎯 **Goal**  
Analyze sales data to identify:  
- Most profitable product categories  
- Regional sales trends  

## 🛠 **Tools**  
- Python (Pandas, Matplotlib)  
- Excel  

## 📂 **Dataset**  
[Superstore Sales Data] (https://www.kaggle.com/datasets/vivek468/superstore-dataset-final?resource=download)

## 📊 **Key Findings**  
1. **Technology** is the most profitable category
2. Highest order volume comes from **California**  


## 💻 **Setup & Execution**  
1. Place `superstore.csv` in the `data/` directory  
2. Open `sales_analysis.ipynb` in Jupyter Notebook  
3. Run all cells  

## 🔍 **Core Analysis Code**  
```python
profit_by_category = df.groupby('Category')['Profit'].sum().sort_values(ascending=False)