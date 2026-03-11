#  Valorant Player Performance Predictor

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Data Collection](https://img.shields.io/badge/data-100%20players-brightgreen)]()
[![ML Model](https://img.shields.io/badge/ML-Random%20Forest-orange)]()
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

An open-source machine learning project that predicts and compares Valorant player performance , stratergizes there team gameplay , predicts the match outcomes
and helps teams create stratergies. 

## **Project Overview**

This project collects comprehensive Valorant player statistics and uses them to build ML models that can:
- Predict player performance metrics
- Compare players across different ranks and time periods
- Identify key factors that contribute to winning matches
- Find best winning case stratergies in each map 
- analyzes gameplays and predicts outcome

### **Current Progress: collected training set and test set from [!vlr.gg] using [![vlrdevapi](https://github.com/Vanshbordia/vlrdevapi?tab=readme-ov-file)]
                        applied linear regression on the data to predict player rating (81% accuracy)

The dataset contains the following features for each player:

 **CSV FILE**: [Google Sheets Link-https://docs.google.com/spreadsheets/d/1T0Y2eui4J85Jni2GwScZMxOJ7anHT6I69gyyIVYPvFk/edit?usp=shari]



## To-DO - 
- Add multithreading to data collection code to extract faster 
- figure out mathematical relation between the different factors affecting rating 
