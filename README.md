# Optimizing Bank Marketing: Deposit Prediction
___
Welcome to the **Bank Deposit Predictor** project! This repository showcases an end-to-end data science project aimed at predicting whether a bank's client will subscribe to a term deposit based on historical marketing data. 🚀📈

## Overview

The project leverages various machine learning algorithms to build a predictive model that helps improve the effectiveness of marketing campaigns for a Portuguese banking institution. By accurately predicting client behavior, the bank can target potential clients more efficiently, reduce marketing costs, and increase the success rate of their campaigns.

**Link to the App**: [Deposit Predictor](https://huggingface.co/spaces/fadhiil23/Bank_Deposit_Predictor)

## Dataset Description

The dataset used in this project is sourced from Kaggle and is related to direct marketing campaigns of a Portuguese banking institution. The data includes information about clients, their interactions with the bank, and whether they subscribed to a term deposit.

- **Source**: [Kaggle | Bank Marketing Dataset](https://www.kaggle.com/datasets/janiobachmann/bank-marketing-dataset/data)

| # | Attribute  | Description | Type       | Values |
|---|------------|-------------|------------|--------|
| 1 | age        | Age of the client | Numeric    | |
| 2 | job        | Type of job | Categorical | "admin.", "technician", "services", "management", "retired", "blue-collar", "unemployed", "entrepreneur", "housemaid", `"unknown"`, "self-employed", "student" |
| 3 | marital    | Marital status | Categorical | "married", "single", "divorced" |
| 4 | education  | Education level | Categorical | "secondary", "tertiary", "primary", `"unknown"` |
| 5 | default    | Has credit in default? | Binary      | "no", "yes" |
| 6 | balance    | Average yearly balance (in euros) | Numeric    | |
| 7 | housing    | Has housing loan? | Binary      | "yes", "no" |
| 8 | loan       | Has personal loan? | Binary      | "no", "yes" |
| 9 | contact    | Contact communication type | Categorical | `"unknown"`, "cellular", "telephone" |
| 10 | day       | Last contact day of the month | Numeric    | |
| 11 | month     | Last contact month of the year | Categorical | "jan", "feb", "mar", ..., "nov", "dec" |
| 12 | duration  | Last contact duration (in seconds) | Numeric    | |
| 13 | campaign  | Number of contacts during this campaign | Numeric    | |
| 14 | pdays     | Number of days since last contacted from a previous campaign | Numeric    | `-1 if not contacted before` |
| 15 | previous  | Number of contacts before this campaign | Numeric    | |
| 16 | poutcome  | Outcome of the previous campaign | Categorical | `"unknown"`, "other", "failure", "success" |
| 17 | deposit (target) | Subscribed to a term deposit? | Binary  | "yes", "no" |

## Problem Statement

The main goal is to build a Machine Learning Classification model with over 70% precision to predict whether a client will subscribe to a term deposit within a week. Accurate predictions can enhance marketing campaign efficiency, target clients likely to respond positively, and ultimately increase the success rate of sales while reducing marketing costs.

## Exploratory Data Analysis (EDA)

### Key Findings

- **Age**: Average age is 39 years, with a majority of clients in the 30-50 age range.
- **Balance**: Average balance is 255 EUR. High deviation indicates a mix of debtors and elite clients.
- **Duration**: Average call duration is 255 seconds, with longer calls likely indicating interest.
- **Contacts**: Average number of contacts is 2 per client, with higher contacts for some up to 63 times.
- **Previous Campaigns**: Most clients are new, with 0 previous contacts and 0 days since last contact.

## Chi-Squared Test Insights

### Influential Factors

1. **Job**: 
    - Passive jobs (retired, student, unemployed) and management show higher deposit rates.
2. **Marital Status**:
    - Single clients are more likely to deposit due to fewer financial responsibilities.
3. **Education**:
    - Higher education (tertiary) correlates with higher deposit rates.
4. **Default, Housing, Loan**:
    - Financially stable clients (no credit default, no loan) are more likely to deposit.
5. **Contact Method**:
    - Mobile phone contacts are more effective.
6. **Previous Campaign Outcome**:
    - Successful previous deposits influence future deposits.
7. **Week**:
    - Higher deposits in the first week despite most contacts in the third week.

## Model Building

### Algorithms Tried

- **K-Nearest Neighbors (KNN)**
- **Support Vector Machine (SVM)**
- **Decision Tree**
- **Random Forest**
- **Gradient Boosting**

### Best Model: KNN

- **Baseline Precision**:
    - Train: 75%
    - Test: 74%
- **After Hypertuning**:
    - Train: 82%
    - Test: 79%

## Recommendations for Marketing Strategy

1. **Targeting Demographics**: Focus on productive age groups and specific jobs.
2. **Educational Campaigns**: Educate clients on the benefits of deposits.
3. **Stability Focus**: Prioritize financially stable clients.
4. **Effective Communication**: Use mobile phones for client contact.
5. **Leverage History**: Re-target clients with successful previous deposits.
6. **Optimal Timing**: Initiate contacts at the start of the month/week.
7. **Promotional Offers**: Provide special offers to encourage deposits.

## Conclusion

By implementing this predictive model, the bank can significantly enhance the efficiency of its marketing campaigns, ensuring targeted and effective client interactions. This project demonstrates the power of machine learning in transforming marketing strategies and achieving business goals.

Feel free to explore the repository and reach out if you have any questions or suggestions!

---

### Author

- **Name**: [Fadhiil Dzaki Mulyana](www.linkedin.com/in/fadhiildzaki)
- **GitHub**: [FadhiilDzaki](https://github.com/FadhiilDzaki)
