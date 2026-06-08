# Aba-ml-journey-
Day 1: Learning ML Engineering from Android in Aba 

Learning ML Engineering from scratch, using only Android.

## Day 1: Setup 
- Created GitHub account + repo
- Goal: Learn ML → ML Engineering step by step

## Day 2: Train + Save Model
- Trained Linear Regression for house price prediction  
- Used joblib.dump() to save model + features to .pkl
- Next: Learn how to load model and predict

## How to run
1. Open notebook.ipynb in Google Colab Run all cell
- Used joblib.load() to load saved model
- Made predictions on new house data
- Goal- nextrap this in a simsimple API's next

## Day 3: Save & Load Model
- Trained Linear Regression on house data
- Saved model with joblib: model.pkl, features.pkl  
- Loaded model to predict: 1600 sqft, 3 bed, 7yr old = $234,687.20- 

## Day 4/100: ML Web App with Gradio ✅

**Project**: House Price Predictor UI  
**Tech Stack**: Python, scikit-learn, Gradio, Colab, pickle  
**Deployed**: gradio.live share link

### What it does
Takes user input → sqft, bedrooms, bathrooms → predicts house price in real-time

**Example Prediction:**  
Input: 1600 sqft, 3 bedrooms, 2 bathrooms  
Output: `$138,650.31`

### Challenges I killed
1. `FileNotFoundError` - model.pkl missing after Colab reset
2. `LocalTunnel 502/503` - Aba 30 B/s network vs Gradio tunneling 
3. Colab runtime disconnections
4. Stress-deleting files at 4 AM

**Lesson learned**: Never delete files from stress. Debug first, delete last.

### Screenshots

   **Gradio UI:**
   ![Gradio Interface](Screenshots/day4-ui.png)

   **Prediction $138,650.31:**
   ![Prediction Result](Screenshots/day4-prediction.png)

### Links
**Live Demo**: [gradio.live/xxxxx] - expires in 72hrs  
**Code**: [Colab Notebook link]
![UI Interface](screenshots/day4-ui.png)  
![Prediction Result $138,650.31](screenshots/day4-prediction.png)
**Prediction Proof**: 
Input: 1600 sqft, 3bd, 2ba
Output: $138,650.31
Timestamp: April 8, 2026 1:37 AM WAT
![Gradio UI](Screenshots/Screenshot_day4-ui.png)
![Prediction Result](Screenshots/Screenshot_day4-prediction.png)

### Day 4 Screenshots

**1. Training Complete:**
![Model Saved](Screenshots/day4-ui.png)

**2. Prediction Live:**
![House Price Predictor UI](Screenshots/day4-prediction.png)

## Day 4 Proof - House Price Predictor

**Gradio UI with inputs:**
![Gradio UI](Screenshots/day4-ui.png)

**Prediction Result:**
![Prediction $138,650.31](Screenshots/day4-prediction.png)

**Repo**: https://github.com/Johnzecus-ml-dev/aba-ml-journey-
