# Aba-ml-journey
# Aba Farm Data ML 🌾🌴🍫
> Production ML for Abia State agriculture: Palm Oil, Cocoa, Cassava, Plantain, Maize, Garden Egg, Pepper, Yam.

**TL;DR:** Building FastAPI to predict yield for 8 major Abia crops. Helping 10k+ farmers with data.  
**Status:** Maize v1.0 Shipping Tonight | Palm Oil + Cocoa v1.0 Week 2 | Others in pipeline  
**Impact:** Reduce post-harvest loss. Increase farmer income. Built from Android in Aba on 30 B/s network.

**Tech:** `Python` `scikit-learn` `joblib` `FastAPI` `Pandas` `Colab` `GitHub Actions`

**Recruiters:** ThriveAgric, Releaf, AFEX, Olam, IITA — This is SE Nigeria AgTech. Let’s talk.

---

### **Day 1: Learning ML Engineering from Android in Aba**
Goal: Build production ML for African agriculture. No laptop. No PhD. Just grit.

### **Day 2-3: Train + Save First Model**
Trained LinearRegression for **Aba maize yield prediction**  
Used `joblib.dump()` to save model + features to `.pkl`  
**Features:** rainfall_mm, soil_ph, farm_size_hectares, fertilizer_kg  
**Next:** Load model and predict via API

### **Day 4/100: ML Web App with Gradio ✅**
**Project:** Aba Maize Yield Predictor UI  
**Tech Stack:** Python, scikit-learn, Gradio, Colab, joblib  
**Deployed:** gradio.live share link

**What it does:**  
Takes farmer input → rainfall, soil pH, farm size → predicts maize yield in kg/hectare real-time

**Example Prediction:**  
Input: 1200mm rainfall, 6.5 pH, 2 hectares  
Output: 2,400 kg estimated yield

### **Day 5/100: From Debug Hell to Deployment**
**Challenges I Killed:**
1. `FileNotFoundError` - model.pkl missing after Colab reset
2. `LocalTunnel 502/503` - Aba 30 B/s network vs Gradio tunneling  
3. Colab runtime disconnections at 4 AM
4. Stress-deleting files instead of debugging

**Lesson learned:** Never delete files from stress. Debug first, delete last.  

**What I Proved in 24hrs ✅**
1. **Train:** Built LinearRegression model for Aba crops from scratch
2. **Save:** Used joblib to freeze model so Colab crashes can't stop me
3. **Load:** Load trained model instantly without retraining  
4. **Deploy:** Launched public Gradio interface for farmers to use

### **Day 6/100: Aba Farm Data API 🌾🚀
Pivoted from generic tutorials to real impact.
Now Building: FastAPI with 8 endpoints: /predict/palm_oil, /predict/maize, /predict/yam...
Goal: One API call helps an Aba farmer plan harvest.

**Tech Stack v2.0**  
`Python` `scikit-learn` `joblib` `FastAPI` `Pandas` `Uvicorn`

**How to Run**
```bash
pip install scikit-learn joblib fastapi uvicorn pandas
uvicorn api.main:app --reload
