# Complete Stroke Dataset Analysis - Educational Guide

## Overview
This notebook demonstrates a complete machine learning pipeline using a healthcare stroke prediction dataset. The analysis is divided into two main parts:
1. **Data Analysis & Cleaning** (Pandas/NumPy focus)
2. **Machine Learning Implementation** (Scikit-learn focus)

---

## Part 1: Data Analysis and Cleaning

### 1.1 Initial Setup and Data Loading

```python
import warnings 
warnings.filterwarnings('ignore')
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv("healthcare-dataset-stroke-data.csv")
```

**Key Learning Points:**
- **Warning suppression**: `warnings.filterwarnings('ignore')` prevents cluttering output with non-critical warnings
- **Library imports**: Essential data science stack - pandas for data manipulation, matplotlib/seaborn for visualization
- **Data loading**: `pd.read_csv()` is the most common way to load structured data

### 1.2 Initial Data Exploration

```python
data
```

**What we observe:**
- Dataset has **5,110 rows** and **12 columns**
- Features include: `id`, `gender`, `age`, `hypertension`, `heart_disease`, `ever_married`, `work_type`, `Residence_type`, `avg_glucose_level`, `bmi`, `smoking_status`, `stroke`
- Target variable: `stroke` (binary: 0 = no stroke, 1 = stroke)
- Mix of numerical and categorical features
- Some missing values visible (NaN in BMI column)

### 1.3 Data Structure Analysis

```python
data.info()
```

**Key Insights:**
- **Data types**: 3 float64, 4 int64, 5 object (string) columns
- **Missing values**: BMI column has only 4,909 non-null values (201 missing)
- **Memory usage**: 479.2+ KB - manageable dataset size
- **Index**: RangeIndex from 0 to 5109

**Teaching Points:**
- `.info()` provides crucial overview of dataset structure
- Data types matter for analysis and model performance
- Missing values need to be addressed before modeling

### 1.4 Missing Values Analysis

```python
data.isnull().sum()
```

**Results:**
- Only BMI column has missing values (201 out of 5,110 = ~3.9%)
- All other columns are complete

**Strategy Discussion:**
- 3.9% missing is relatively low
- BMI is important for health analysis
- Options: drop rows, impute with mean/median, or use advanced imputation

---

## Part 2: Exploratory Data Analysis (EDA)

### 2.1 Categorical Variables Analysis

```python
data['gender'].value_counts()
data['hypertension'].value_counts()
data['heart_disease'].value_counts()
# ... and so on
```

**Key Findings:**

1. **Gender Distribution:**
   - Female: 2,994 (58.6%)
   - Male: 2,115 (41.4%)
   - Other: 1 (0.02%) - outlier to consider

2. **Medical Conditions:**
   - Hypertension: 498/5,110 (9.7%)
   - Heart Disease: 276/5,110 (5.4%)

3. **Lifestyle Factors:**
   - Ever Married: 3,353/5,110 (65.6%)
   - Work Types: Private sector dominates (2,925), followed by self-employed (819)
   - Residence: Nearly equal urban (2,596) vs rural (2,514)

4. **Target Variable (Stroke):**
   - No stroke: 4,861 (95.1%)
   - Stroke: 249 (4.9%)
   - **Critical observation**: Highly imbalanced dataset!

**Teaching Points:**
- `.value_counts()` is essential for understanding categorical distributions
- Class imbalance is a major concern in ML (95.1% vs 4.9%)
- Domain knowledge helps interpret these distributions

### 2.2 Data Cleaning Decisions

#### Handling Gender Categories
```python
data = data[data['gender'].isin(['Female', 'Male'])]
```

**Rationale:**
- Only 1 record with "Other" gender
- Too few samples to be statistically meaningful
- Removal improves model consistency

#### Handling Missing BMI Values
```python
bmi_mean = data['bmi'].mean()
data['bmi'] = data['bmi'].apply(lambda x: bmi_mean if pd.isnull(x) else x)
```

**Teaching Points:**
- **Mean imputation**: Simple but effective for small amounts of missing data
- **Lambda functions**: Concise way to apply conditional logic
- **Alternative shown**: Could use `data['bmi'].fillna(bmi_mean)` 
- **When to use**: Mean imputation works when data is Missing Completely At Random (MCAR)

### 2.3 Data Visualization

#### Numerical Features Analysis
```python
histogram_columns = ['age', 'avg_glucose_level', 'bmi']
data[histogram_columns].hist(figsize=(15,8))
```

**Observations:**
- **Age**: Normal-like distribution, slight right skew
- **Glucose Level**: Right-skewed, many people with normal levels
- **BMI**: Normal distribution centered around 25-30

#### Stroke vs Features Analysis
```python
fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1, figsize=(10, 15))
sns.histplot(x='age', hue='stroke', data=data, kde=True, ax=ax1, bins=30)
# Similar for glucose and BMI
```

**Key Insights from Visualizations:**
- **Age**: Clear pattern - stroke incidence increases dramatically with age (especially 50+)
- **Glucose Level**: Higher glucose levels associated with increased stroke risk
- **BMI**: Less clear relationship, but some elevation in higher BMI groups

**Teaching Points:**
- `plt.subplots()` creates multiple plots in organized layout
- `hue` parameter in seaborn separates data by target variable
- KDE (Kernel Density Estimation) smooths histograms for trend visibility

#### Categorical Analysis - Heart Disease vs Stroke
```python
stroke_heart_disease_counts = pd.crosstab(data['heart_disease'], data['stroke'])
stroke_heart_disease_counts.div(stroke_heart_disease_counts.sum(axis=1), axis=0).plot(kind='bar', stacked=True)
```

**Critical Finding:**
- People with heart disease have ~17% stroke rate
- People without heart disease have ~4% stroke rate
- **4x higher risk** - strong predictive feature!

---

## Part 3: Feature Engineering

### 3.1 Creating Categorical Bins

```python
data['bmi_cat'] = pd.cut(data['bmi'], bins=[0, 19, 25, 30, 10000], 
                        labels=['Underweight', 'Ideal', 'Overweight', 'Obesity'])
data['age_cat'] = pd.cut(data['age'], bins=[0, 13, 18, 45, 60, 200], 
                        labels=['Children', 'Teens', 'Adults', 'Mid Adults', 'Elderly'])
data['glucose_cat'] = pd.cut(data['avg_glucose_level'], bins=[0, 90, 160, 230, 500], 
                            labels=['Low', 'Normal', 'High', 'Very High'])
```

**Feature Engineering Rationale:**
- **BMI Categories**: Medical standard classifications
- **Age Groups**: Life stage categories relevant to health
- **Glucose Levels**: Clinical thresholds for diabetes/prediabetes

**Teaching Points:**
- `pd.cut()` creates categorical bins from continuous variables
- Domain expertise drives bin selection
- Categorical features can capture non-linear relationships

---

## Part 4: Machine Learning Preprocessing

### 4.1 Data Preprocessing Pipeline

```python
from sklearn.preprocessing import StandardScaler, LabelEncoder
ss = StandardScaler()
le = LabelEncoder()

# Feature and target separation
X = data.drop(['stroke', 'id'], axis=1)
y = data['stroke']
```

**Key Decisions:**
- Remove `id` column (not predictive)
- Separate features (X) from target (y)
- Prepare for different encoding strategies

### 4.2 Feature Type Classification

```python
ordinal = ['age_cat', 'glucose_cat', 'bmi_cat', 'hypertension', 'heart_disease']
nominal = ['gender', 'ever_married', 'work_type', 'Residence_type', 'smoking_status']  
numerical = ['age', 'bmi', 'avg_glucose_level']
```

**Teaching Points:**
- **Ordinal variables**: Have natural order/ranking
- **Nominal variables**: Categories without inherent order
- **Numerical variables**: Continuous values requiring scaling
- Different encoding strategies needed for each type

### 4.3 Encoding Strategies

#### Label Encoding for Ordinal Variables
```python
for col in ordinal:
    X[col] = le.fit_transform(X[col])
```

#### Standard Scaling for Numerical Variables
```python
X[numerical] = ss.fit_transform(X[numerical])
```

#### One-Hot Encoding for Nominal Variables
```python
temp = X.drop(columns=nominal)
dummies = pd.get_dummies(X[nominal])
X = pd.concat([temp, dummies], axis=1)
```

**Final Feature Count**: 23 features (from original 11)

**Teaching Points:**
- Label encoding preserves ordinal relationships
- Standard scaling ensures all numerical features have similar magnitude
- One-hot encoding creates binary columns for each category
- Feature expansion is common in preprocessing

---

## Part 5: Machine Learning Implementation

### 5.1 Train-Test Split and Class Imbalance Handling

```python
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.25, 
                                                    shuffle=True, random_state=2021)

# SMOTE for handling class imbalance
smote = SMOTE()
x_resample, y_resample = smote.fit_resample(x_train, y_train)
```

**Key Concepts:**
- **75/25 split**: Standard practice for train/test division
- **Random state**: Ensures reproducible results
- **SMOTE**: Synthetic Minority Oversampling Technique creates synthetic examples of minority class
- **Result**: Balanced dataset (3,641 samples each class)

### 5.2 Outlier Detection and Removal

```python
from sklearn.ensemble import IsolationForest
outlier_detector = IsolationForest(contamination=0.01)
outlier_detector.fit(x_train)
no_outliers = outlier_detector.predict(x_train)
x_train, y_train = x_train[no_outliers == 1], y_train[no_outliers == 1]
```

**Teaching Points:**
- **Isolation Forest**: Unsupervised outlier detection
- **1% contamination**: Conservative approach, removes only extreme outliers
- **Applied only to training set**: Prevents data leakage

### 5.3 Model Comparison Framework

```python
def predictions(x_set, y_set):
    # Initialize metric storage
    accuracy, precision, recall, f1, auc, conf_mat = [], [], [], [], [], []
    
    # Define classifiers
    classifiers = [
        SVC(random_state=random_state, probability=True),
        DecisionTreeClassifier(random_state=random_state),
        AdaBoostClassifier(DecisionTreeClassifier(random_state=random_state)),
        RandomForestClassifier(random_state=random_state),
        GradientBoostingClassifier(random_state=random_state),
        KNeighborsClassifier(),
        LogisticRegression(random_state=random_state),
        XGBClassifier(random_state=random_state),
        LGBMClassifier(random_state=random_state)
    ]
```

**Algorithm Selection Rationale:**
- **SVC**: Effective for high-dimensional data
- **Decision Tree**: Interpretable, handles non-linear relationships
- **AdaBoost**: Ensemble method, improves weak learners
- **Random Forest**: Robust ensemble, reduces overfitting
- **Gradient Boosting**: Sequential learning, often high performance
- **K-Neighbors**: Instance-based learning
- **Logistic Regression**: Linear baseline, interpretable
- **XGBoost/LightGBM**: State-of-the-art gradient boosting

---

## Part 6: Results Analysis

### 6.1 Performance Comparison

#### Original Data Results (Imbalanced):
- **High Accuracy** (95%): Misleading due to class imbalance
- **Low Recall** (0-25%): Models fail to detect stroke cases
- **Poor F1 Scores** (0-22%): Harmonic mean of precision/recall shows poor performance

#### SMOTE Resampled Results (Balanced):
- **Lower Accuracy** (85-93%): More realistic assessment
- **Better Recall** (8-41%): Improved stroke detection
- **Balanced F1 Scores** (9-21%): Better overall performance
- **Best Performers**: LightGBM (93% accuracy), Gradient Boosting (41% recall)

### 6.2 Key Insights

1. **Class Imbalance Impact**: Original high accuracy was misleading
2. **Recall Importance**: In medical diagnosis, missing positive cases (strokes) is costly
3. **Trade-offs**: SMOTE improves recall but reduces overall accuracy
4. **Model Selection**: Depends on business requirements (precision vs recall)

### 6.3 Visualization Analysis

The bar charts reveal:
- **Gradient Boosting**: Best recall (41%) - detects most stroke cases
- **LightGBM**: Best overall balance (93% accuracy, 15% recall)
- **Random Forest/XGBoost**: Consistent performers across metrics

---

## Teaching Applications

### For Pandas/NumPy Lesson:
1. **Data Loading**: `pd.read_csv()`, initial exploration
2. **Data Cleaning**: Handling missing values, filtering data
3. **EDA**: `.value_counts()`, `.info()`, `.describe()`
4. **Feature Engineering**: `pd.cut()`, categorical encoding
5. **Visualization**: Integration with matplotlib/seaborn

### For Scikit-learn Lesson:
1. **Preprocessing**: StandardScaler, LabelEncoder, train_test_split
2. **Class Imbalance**: SMOTE, understanding evaluation metrics
3. **Model Comparison**: Multiple algorithms, systematic evaluation
4. **Metrics**: Accuracy vs precision vs recall in context
5. **Real-world Considerations**: Medical diagnosis priorities

---

## Extension Ideas

1. **Advanced Feature Engineering**: Interaction terms, polynomial features
2. **Hyperparameter Tuning**: GridSearchCV, RandomizedSearchCV
3. **Cross-Validation**: More robust model evaluation
4. **Feature Selection**: Recursive feature elimination, feature importance
5. **Cost-Sensitive Learning**: Alternative to SMOTE for imbalanced data
6. **Model Interpretation**: SHAP values, feature importance analysis

---

## Conclusion

This notebook demonstrates a complete ML pipeline from raw data to model evaluation. Key learning outcomes:

1. **Data Understanding**: EDA reveals class imbalance and feature relationships
2. **Preprocessing Importance**: Proper encoding and scaling critical for model performance
3. **Class Imbalance**: Major consideration in real-world problems
4. **Metric Selection**: Context matters - accuracy isn't always the best metric
5. **Model Comparison**: Systematic evaluation reveals trade-offs between algorithms

The healthcare context makes this analysis particularly meaningful, as the cost of missing a stroke (false negative) is much higher than a false alarm (false positive), making recall a critical metric.