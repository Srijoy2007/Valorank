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

### **Current Progress: collected 100 agent stats from [![vlr.gg](https://www.vlr.gg/)] using [![vlrdevapi](https://github.com/Vanshbordia/vlrdevapi?tab=readme-ov-file)]

The dataset contains the following features for each player:

 **CSV FILE**: [Google Sheets Link-https://docs.google.com/spreadsheets/d/1T0Y2eui4J85Jni2GwScZMxOJ7anHT6I69gyyIVYPvFk/edit?usp=shari]

## To-DO - 
- fit this data into a linear regression model
- optimize it with sgd and bgd
- use one non linear model and compare the output 
- increase dataset to 10000+ data points 
- setup website 
- setup a redis backend for fast and smooth functioning
- setup a fast api to get user data and show output on the website 


