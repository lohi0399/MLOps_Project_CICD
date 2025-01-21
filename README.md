# MLOps Project: Continuous Integration and Continuous Deployment (CI/CD)

This README provides a structured guide for building an MLOps project using Python, Flask, and AWS Elastic Beanstalk with CI/CD pipelines. The project focuses on deploying a machine learning pipeline for a student performance indicator system.

---

## 1. **Setting up the GitHub Repository**

### a. Create a Virtual Environment
- Use the command: `python -m venv .venv` to create a virtual environment.
- Activate it using `\.venv\Scripts\activate` (Windows).
- Freeze dependencies into `requirements.txt` to manage project-specific libraries.
- Add a `.gitignore` file to exclude unnecessary files (e.g., `.venv`, `artifacts/`).

**Placeholder for Virtual Environment Image**

### b. Create `setup.py`
- `setup.py` allows you to package your project for reuse and deployment.
- To identify the project's packages, structure your code with a `src` folder containing an `__init__.py` file. Example:
  ```
  src/
    __init__.py
  ```
- Use the `find_packages()` function in `setup.py` to locate all `__init__.py` files.
- Link `setup.py` to `requirements.txt` by adding `-e .` in the latter. Install dependencies with:
  ```
  pip install -r requirements.txt
  ```
  
**Placeholder for Setup.py Example Image**

### c. Automate File Creation (Optional)
- Use a `template.py` script to automate boilerplate creation, but manually setting up files is recommended for beginners to understand their roles.

---

## 2. **Logging and Exception Handling**

### a. Create a `component` Folder
- This folder organizes key functionalities:
  - `data_ingestion.py`: Handles data extraction, splitting into train/test.
  - `data_transformation.py`: Manages data preprocessing like encoding and scaling.
  - `model_trainer.py`: Trains models and evaluates performance (e.g., R² score).
  - `model_pusher.py`: Pushes the trained `model.pkl` file to cloud storage.

**Placeholder for Component Folder Image**

### b. Create a `pipeline` Folder
- Defines the overall workflow:
  - `train_pipeline.py`: Integrates data ingestion, transformation, and model training.
  - `prediction_pipeline.py`: Handles inference for new data.

**Placeholder for Pipeline Folder Image**

### c. Add Utility Scripts
- **`exception.py`**: Centralized exception handling.
- **`logger.py`**: Logs errors and runtime information.
- **`utils.py`**: Helper functions for dependencies and reusable code.

---

## 3. **Defining the Problem Statement**

### Student Performance Indicator
- Use Jupyter Notebook for Exploratory Data Analysis (EDA).
- Install `ipykernel` to run Jupyter in your virtual environment.
- Analyze data to uncover insights and prepare observations for implementation.

**Placeholder for EDA Notebook Image**

---

## 4. **Data Ingestion Implementation**

### Goals:
- Extract data from local sources or databases (e.g., MongoDB).
- Split data into training and testing sets.
- Store processed data in an `artifacts/` folder. (Add `artifacts/` to `.gitignore` to avoid pushing it to GitHub.)

**Placeholder for Data Ingestion Image**

---

## 5. **Data Transformation Pipeline**

### Goals:
- Perform feature engineering and data cleaning.
- Use transformers for scaling, encoding, and preprocessing.
- Ensure consistency with the training dataset structure.

**Placeholder for Data Transformation Image**

---

## 6. **Model Training**

### Goals:
- Train a machine learning model.
- Save the trained model as a `model.pkl` file in the `artifacts/` folder.

**Placeholder for Model Training Image**

---

## 7. **Hyperparameter Tuning**
- Implement techniques like Grid Search or Random Search to optimize model performance.
- Use cross-validation for robust evaluation.

**Placeholder for Hyperparameter Tuning Image**

---

## 8. **Prediction Pipeline**

### Goals:
- Develop a Flask-based web application.
- Provide endpoints for:
  - Home: `http://127.0.0.1:5000/`
  - Predictions: `http://127.0.0.1:5000/predictions`
- Interact with the `model.pkl` file for inference.

![](images/web_output.png "Web Output from Flask")

---

## 9. **Project Deployment Using AWS Elastic Beanstalk**

### AWS Elastic Beanstalk Overview
- AWS Elastic Beanstalk orchestrates AWS services (e.g., EC2, S3, SNS, CloudWatch) for easy application deployment.
- Automates server configuration, scaling, and load balancing.
- AWS has a feature called codepipeline which gives a framework for **continous delivery**. Basically, using the python file we have a eb instance and we have our githun repo where all the code is. To connect both these we use this codepipeline provided by AWS.



### Configuration
1. **`.ebextensions` Folder**
   - Create a `python.config` file specifying the application's entry point:
     ```
     WSGIPath: application:application
     ```
   - Ensure the entry point (`application.py`) is correctly defined.

**Placeholder for .ebextensions Folder Image**

2. **AWS Elastic Beanstalk Setup**
   - Create an AWS account (requires a credit card).
   - Navigate to Elastic Beanstalk and create a new application (e.g., "Student Performance") under the Top Features option.
   - Select the Python platform and configure your environment.
![](images/1.png)
![](images/2.png)
![](images/3.png)
![](images/4.png)
![](images/5.png)

We select python as the environment for the eb instance (we can also have docker).

3. **CI/CD Pipeline with AWS CodePipeline**
   - Use AWS CodePipeline for continuous delivery.
   - Connect the GitHub repository to automate deployment to Elastic Beanstalk.
![](images/6.png)
![](images/7.png)
![](images/8.png)
![](images/9.png)
Here we give out github repo path and branch

![](images/10.png)
AWS Jenkins can be added for building tests.

![](images/11.png)
![](images/12.png)
---

## Notes
- **Docker and Python Virtual Environments**: A Docker container also needs Python installed to run a Python application. However, the key difference is that Python in Docker is bundled as part of the container image, independent of the host system. This ensures:
  - **Portability**: The container can run on any system with Docker installed, regardless of the host's Python version.
  - **Reproducibility**: The Python version and dependencies remain consistent across environments (e.g., development, testing, production).
  - **Isolation**: Each container is fully isolated, preventing conflicts with other projects or system-level dependencies. Therefore we don't have conflicts arising due to different OS, machines etc.
- Update this README with screenshots of deployed applications, pipelines, and results.
- Add detailed explanations for each implementation step in future updates.
- Can use python linter to avoid warning and manage test quality.
-- Logging and checkpointing system can be used as tests



