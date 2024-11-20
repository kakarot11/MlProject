# END TO END MACHINE LEARNING PROJECT

## PROJECT OVERVIEW.
This project is an end-to-end machine learning implementation, focusing on the "Student Performance Indicator" dataset. The goal is to predict student test scores based on factors such as gender, ehtnicity, parental education level, lunch type and test preparation course.

## DATASET AND PROBLEM STATEMENT
1. **Dataset**: "Student Performance Indicator" ---(https://www.kaggle.com/datasets/spscientist/students-performance-in-exams?datasetId=74977)
2. **Objective**: Predict student performance using features like gender, ethnicity, parental education, lunch type and test preparation course.
3. **Size**: 1,000 rows and 8 columns.

## EXPLORATORY DATA ANALYSIS (EDA)
1. Conducted using Jupyter Notebook.
2. Key tasks include checking for missing values, duplicates and data types.
3. EDA insights guiding decision making process and stakeholder communication.

## MODEL TRAINING
1. Focus on regression techniques to predict continuous values (test scores).
2. Categorical features are handled through one-hot encoding, and numerical features through standard scaling.
3. **Performance metrics**: Mean Absolute Error, R-Squared and Root Mean Squared Error.

## COMPONENTS
1. **Data Ingestion**: Reads datasets from various sources. The dataset is split into training and testing sets. Data frames for training, testing and raw data are saved in specified artifact paths.
2. **Data Transformation**: Essential for feature engineering and data cleaning. Converts categorical features into numerical features using pipelines.
3. **Model Trainer**: Trains the model and evalutes metrics.

## PIPELINE IMPLEMENTATION
1. Training and prediction pipelines with seperate Python files.
2. **__init__.py** in the pipeline folder for module importing.

## COMMON FUNCTIONALITIES
1. **logger.py**: Logs execution details and errors.
2. **exception.py**: Handles exceptions with custom messages.
3. **utils.py**: Contains shared functionalities.

**MODEL TRAINING, HYPERPARAMETER TUNING AND CREATION OF TWO PICKLE FILES: model.pkl and preprocessor.pkl**

## CREATING PROJECT PIPELINE USING **FLASK WEB APP**
1. Flask Application setup.
2. Prediction Pipeline
3. Input Handling and Prediction.
4. Testing and Validation.
