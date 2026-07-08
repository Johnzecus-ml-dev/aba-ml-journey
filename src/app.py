import gradio as gr
import joblib
import os

# Try to load model. If not found yet, we use dummy function
MODEL_PATH = "../models/maize_model.pkl"

def predict_yield(rainfall_mm, soil_ph, farm_size_hectares, fertilizer_kg):
    """
    Predict maize yield in kg/hectare
    Replace this with real model loading once we have it
    """
    if os.path.exists(MODEL_PATH):
        model = joblib.load(MODEL_PATH)
        features = [[rainfall_mm, soil_ph, farm_size_hectares, fertilizer_kg]]
        prediction = model.predict(features)[0]
    else:
        # Dummy formula for demo until model is ready
        prediction = (rainfall_mm * 2) + (soil_ph * 100) + (farm_size_hectares * 500) + (fertilizer_kg * 3)
    
    return f"Estimated Maize Yield: {prediction:.0f} kg/hectare"

# Gradio UI
iface = gr.Interface(
    fn=predict_yield,
    inputs=[
        gr.Number(label="Rainfall (mm)", value=1200),
        gr.Number(label="Soil pH", value=6.5),
        gr.Number(label="Farm Size (hectares)", value=2),
        gr.Number(label="Fertilizer (kg)", value=50)
    ],
    outputs=gr.Textbox(label="Prediction"),
    title="Aba Maize Yield Predictor v1.0",
    description="Predict maize yield for Abia farmers. Built on Android in Aba 🌽",
    examples=[
        [1200, 6.5, 2, 50],
        [900, 5.8, 1, 30],
        [1500, 7.0, 5, 100]
    ]
)

if __name__ == "__main__":
    iface.launch(share=True)
