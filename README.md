\# Industrial Machine Failure Prediction



\## Project Overview



This project predicts whether an industrial machine is likely to fail based on its operating and sensor measurements.



The project uses machine learning to support predictive maintenance by identifying machines that may have a higher risk of failure before an actual failure occurs.



The final solution includes:



\- Exploratory Data Analysis (EDA)

\- Data preprocessing

\- Multiple machine learning models

\- Model evaluation

\- Random Forest model selection

\- Saved trained model

\- Streamlit web application



\## Problem Statement



Industrial machines can fail because of operating conditions, excessive tool wear, temperature changes, torque, rotational speed, and other factors.



The objective of this project is to build a binary classification model that predicts:



\- `0` → No machine failure

\- `1` → Machine failure



The prediction is based on machine type and operating measurements.



\## Dataset



The dataset contains 10,000 machine records and 10 columns.



\### Features Used



| Feature | Description |

|---|---|

| `Type` | Machine/product type |

| `Air temperature \[K]` | Air temperature in Kelvin |

| `Process temperature \[K]` | Process temperature in Kelvin |

| `Rotational speed \[rpm]` | Machine rotational speed |

| `Torque \[Nm]` | Machine torque |

| `Tool wear \[min]` | Tool wear time |



\### Target



`Target`



\- `0` → No Failure

\- `1` → Failure



\### Features Not Used



`UDI` and `Product ID` were excluded because they are identifiers.



`Failure Type` was excluded because it describes the failure outcome and should not be used as an input feature for predicting the target.



\## Dataset Analysis



The dataset contains:



\- 10,000 rows

\- 10 columns

\- No missing values

\- No duplicate rows



The target is imbalanced:



\- No Failure: 96.61%

\- Failure: 3.39%



Because failure cases are much less frequent than normal cases, class imbalance was considered during model training.



\## Data Preprocessing



The dataset was divided into training and testing sets using an 80:20 split with stratification.



\### Numerical Features



The numerical features were standardized using `StandardScaler`.



\### Categorical Feature



The `Type` feature was converted into numerical form using `OneHotEncoder`.



\### Class Imbalance



`class\_weight="balanced"` was used for the classification models to give more importance to the minority failure class.



\## Machine Learning Models



Three classification models were tested:



1\. Logistic Regression

2\. Decision Tree

3\. Random Forest



\### Model Comparison



| Model | Accuracy | Precision | Recall | F1 Score | ROC-AUC |

|---|---:|---:|---:|---:|---:|

| Logistic Regression | 82.45% | 14.18% | 82.35% | 24.19% | 90.70% |

| Decision Tree | 93.65% | 33.14% | 85.29% | 47.74% | 87.61% |

| Random Forest | 95.35% | 41.01% | 83.82% | 55.07% | 96.44% |



\## Final Model



The Random Forest model was selected as the final model based on its overall evaluation results, particularly its F1 score and ROC-AUC.



The model configuration used:



\- 100 trees

\- Maximum depth: 8

\- Balanced class weights

\- Random state: 42



The trained model is saved as:



`Model/machine\_failure\_model.pkl`



\## Model Evaluation



The final Random Forest model achieved:



\- Accuracy: \*\*95.35%\*\*

\- Precision: \*\*41.01%\*\*

\- Recall: \*\*83.82%\*\*

\- F1 Score: \*\*55.07%\*\*

\- ROC-AUC: \*\*96.44%\*\*



The recall of 83.82% means the model detected a large proportion of the actual machine failure cases in the test data.



The precision is lower because the dataset is highly imbalanced and the model identifies additional cases as potential failures in order to detect more actual failures.



\## Streamlit Application



A Streamlit application was created to allow users to enter machine operating conditions and receive a failure-risk prediction.



The application accepts:



\- Machine Type

\- Air Temperature

\- Process Temperature

\- Rotational Speed

\- Torque

\- Tool Wear



It then displays:



\- Predicted machine status

\- Estimated failure probability



\### Example



Input:



\- Machine Type: `M`

\- Air Temperature: `300 K`

\- Process Temperature: `310 K`

\- Rotational Speed: `1500 rpm`

\- Torque: `50 Nm`

\- Tool Wear: `100 min`



Output:



\- Machine Status: \*\*Normal\*\*

\- Estimated Failure Probability: \*\*5.16%\*\*



\## Project Structure



```text

industrial-machine-failure-prediction/

│

├── Model/

│   └── machine\_failure\_model.pkl

│

├── archive/

│   ├── machine\_failure\_prediction.ipynb

│   └── predictive\_maintenance.csv

│

├── app.py

├── requirements.txt

├── .gitignore

└── README.md

