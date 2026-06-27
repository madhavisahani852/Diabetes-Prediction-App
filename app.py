import numpy as np
import pickle
import streamlit as st
import time

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Diabetes Prediction",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.markdown("""
<style>

.main{
    background-color:#f4f7fb;
}

h1{
    color:#0E76A8;
    text-align:center;
}

.stButton>button{
    width:100%;
    height:55px;
    border-radius:10px;
    font-size:20px;
    font-weight:bold;
    background-color:#0E76A8;
    color:white;
}

.stButton>button:hover{
    background-color:#055d87;
    color:white;
}

div[data-testid="stMetric"]{
    border-radius:12px;
    padding:15px;
    background:#eef7ff;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Load Trained Model
# -----------------------------
loaded_model = pickle.load(
    open("trained_model.sav", "rb")
)

# -----------------------------
# Prediction Function
# -----------------------------
def diabetes_prediction(input_data):

    input_array = np.asarray(input_data, dtype=float)

    input_reshaped = input_array.reshape(1, -1)

    prediction = loaded_model.predict(input_reshaped)

    if prediction[0] == 0:
        return "The person is not diabetic."
    else:
        return "The person is diabetic."

# -----------------------------
# Main Function
# -----------------------------
def main():

    # Sidebar
    st.sidebar.title("🩺 Diabetes Prediction")

    st.sidebar.info(
        """
        Enter the patient's medical details and click **Predict Diabetes**.
        """
    )

    st.sidebar.success("Machine Learning Model")

    # Main Title
    st.title("🩺 Diabetes Prediction System")

    st.write(
        """
        This application predicts whether a person is likely to have
        diabetes based on several medical parameters.
        """
    )

    st.markdown("---")

    # Two Columns
    col1, col2 = st.columns(2)

    with col1:

        Pregnancies = st.number_input(
            "🤰 Number of Pregnancies",
            min_value=0,
            step=1
        )

        Glucose = st.number_input(
            "🩸 Glucose Level",
            min_value=0.0
        )

        BloodPressure = st.number_input(
            "❤️ Blood Pressure",
            min_value=0.0
        )

        SkinThickness = st.number_input(
            "📏 Skin Thickness",
            min_value=0.0
        )

    with col2:

        Insulin = st.number_input(
            "💉 Insulin Level",
            min_value=0.0
        )

        BMI = st.number_input(
            "⚖️ BMI",
            min_value=0.0
        )

        DiabetesPedigreeFunction = st.number_input(
            "🧬 Diabetes Pedigree Function",
            min_value=0.0,
            format="%.3f"
        )

        Age = st.number_input(
            "🎂 Age",
            min_value=1,
            step=1
        )

    st.markdown("---")

    # Prediction Button
    if st.button("🔍 Predict Diabetes"):

        with st.spinner("Analyzing medical data..."):

            time.sleep(1)

            diagnosis = diabetes_prediction([
                Pregnancies,
                Glucose,
                BloodPressure,
                SkinThickness,
                Insulin,
                BMI,
                DiabetesPedigreeFunction,
                Age
            ])

        st.subheader("Prediction Result")

        if diagnosis == "The person is diabetic.":

            st.error("⚠️ High Risk of Diabetes")

            st.write(
                "The model predicts that the person is **likely to have diabetes**."
            )

        else:

            st.success("✅ Low Risk of Diabetes")

            st.write(
                "The model predicts that the person is **unlikely to have diabetes**."
            )

    st.markdown("---")

    # About Section
    with st.expander("ℹ️ About this Project"):

        st.write("""
        **Algorithm Used:** Support Vector Machine (SVM)

        **Dataset:** Pima Indians Diabetes Dataset
        
        **Accuracy:** 80%

        **Purpose:** Predict whether a person is diabetic based on
        medical measurements.

        **Developed using:** Python, Scikit-learn, Streamlit
        """)

    st.markdown("---")
    st.caption("Made with ❤️ using Streamlit and Machine Learning")

# -----------------------------
# Run App
# -----------------------------
if __name__ == "__main__":
    main()