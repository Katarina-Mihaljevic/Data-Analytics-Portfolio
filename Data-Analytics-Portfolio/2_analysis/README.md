# 🔍 Data Analyst Job Market Research  

## 🎯 **Objective**  
Identify:  
- Most in-demand skills  
- Highest-paying locations  

## 🛠 **Tools**  
- SQL (PostgreSQL)  
- Python (Pandas)  

## 📂 **Dataset**  
[Data Analyst Jobs](https://www.kaggle.com/datasets/andrewmvd/data-analyst-jobs)  

## 📊 **Findings**  
1. Top demanded skills: **SQL, Python, Tableau**  
2. Highest-paying locations: **San Francisco, New York**  

```sql
-- Example query
SELECT skills, COUNT(*) AS demand 
FROM jobs 
GROUP BY skills 
ORDER BY demand DESC;