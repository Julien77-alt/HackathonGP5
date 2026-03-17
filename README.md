# HackathonGP5
# G5HackatonAI
Repository for the Explainability/AI hackathon

# HR Guardian AI: Explainable & Ethical Turnover Prediction

## Project Overview
**Our AI** is an intelligent, transparent, and fair predictive solution designed to help Human Resources departments better understand the causes of employee turnover and preserve talent. 

This project was developed for the Capgemini x ESILV Trusted AI Hackathon. It specifically tackles two major pillars of Responsible AI:
* **Explainable AI (XAI):** Ensuring our model is not a "black box" by providing transparent, justifiable results for HR managers using SHAP.
* **Ethical AI:** Actively mitigating algorithmic bias and discrimination to ensure fair treatment across all demographic groups.

## Objectives
* **Predict:** Identify which employees are at risk of leaving the company.
* **Explain:** Deconstruct the prediction to highlight the specific factors driving an employee's potential departure (e.g., salary, satisfaction, absences).
* **Audit:** Verify that the predictive model does not discriminate based on sensitive attributes like Gender or Ethnicity.
* **Recommend:** Provide actionable, preventative recommendations to HR to retain key talent.

## Scope
* **Data:** The project utilizes an anonymized HR dataset containing information on approximately 300 employees (age, position, salary, performance, termination status, etc.).
* **Security & Compliance:** GDPR compliance is maintained through strict data anonymization (removal/masking of sensitive identifiers).
* **Deliverables:** A complete machine learning pipeline, a demonstration dashboard (Streamlit), a Data Card, a Model Card, and a comprehensive Responsible AI framework.

##Personas
This solution is designed with a dual perspective:
* **The Client (HR Manager / CHRO):** *"I need a reliable and understandable solution to retain my employees and reduce turnover costs."* * **The Provider (HR-AI Company):** *"We bring cutting-edge, responsible, and ethical AI solutions to empower HR departments."* ---

## Repository Structure
* `app.py`: The main Streamlit application (Interactive Dashboard).
* `attrition_model.pkl`: The trained XGBoost machine learning model.
* `cleaned_dataset.csv`: The GDPR-compliant, anonymized dataset used for predictions.

## Technologies Used
* **Machine Learning:** Python, Scikit-Learn, XGBoost
* **Explainability & NLP:** SHAP (SHapley Additive exPlanations), VaderSentiment
* **Frontend/Dashboard:** Streamlit, Pandas, Matplotlib

---

## Instructions: How to Run the Dashboard Locally

Follow these steps to test the HR Guardian AI dashboard on your local machine:

**1. Clone the repository and navigate to the folder:**
```bash
git clone <your-repo-link>
cd <repository-folder-name>


## ARCHITECHTURE

Here is the high-level architecture of the HR Guardian AI solution:

```mermaid
graph TD
    A[(Raw HR Dataset)] -->|GDPR Anonymization| B(Data Preprocessing)
    
    B -->|Review Notes| C[VaderSentiment NLP]
    B -->|Tabular Data| D[Feature Engineering]
    
    C --> E((XGBoost Classifier))
    D --> E
    
    E -->|Risk Probabilities| F[Streamlit Dashboard]
    E -->|Model Weights| G[SHAP Explainer]
    
    G -->|Waterfall Plots| F
    
    F -->|Actionable Recommendations| H{HR Manager}
    
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style E fill:#bbf,stroke:#333,stroke-width:4px
    style F fill:#bfb,stroke:#333,stroke-width:2px
    style H fill:#fdb,stroke:#333,stroke-width:2px
