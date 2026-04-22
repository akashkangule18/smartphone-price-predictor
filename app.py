import streamlit as st
import pickle
import pandas as pd

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Smartphone Price Predictor",
    layout="wide"
)

# =========================
# LOAD MODEL
# =========================
with open('final_pipeline.pkl', 'rb') as f:
    model, columns = pickle.load(f)

# =========================
# TITLE
# =========================
st.markdown("<h1 style='text-align: center;'>Smartphone Price Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Enter specifications to estimate price</p>", unsafe_allow_html=True)

st.divider()

# =========================
# LAYOUT
# =========================
col1, col2 = st.columns(2)

# =========================
# LEFT COLUMN
# =========================
with col1:
    st.subheader(" Performance")

    brand = st.selectbox(
        "Brand",
        ['vivo','motorola','oneplus','poco','xiaomi','samsung','realme','oppo','apple','other']
    )

    # PROCESSOR LOGIC
    if brand == "apple":
        processor_options = ['bionic']
        st.info(" Apple devices use Bionic chips")
    else:
        processor_options = ['snapdragon','dimensity','exynos','helio','tensor','unisoc','other']

    processor = st.selectbox("Processor Type", processor_options)

    gigahertz = st.number_input("Processor Speed (GHz)", value=2.5)
    ram = st.selectbox("RAM (GB)", [2,4,6,8,12,16])
    rom = st.selectbox("Storage (GB)", [32,64,128,256,512])
    battery = st.number_input("Battery Capacity (mAh)", value=5000)
    charging = st.number_input("Charging Speed (Watt)", value=33)

# =========================
# RIGHT COLUMN
# =========================
with col2:
    st.subheader(" Display & Camera")

    size = st.number_input("Screen Size (inch)", value=6.5)
    refresh = st.selectbox("Refresh Rate (Hz)", [60,90,120,144])

    has_5g = st.selectbox("5G Support", ["Yes", "No"])

    front_cam = st.number_input("Front Camera (MP)", value=16)
    rear_cam = st.number_input("Rear Camera Count", value=2)

    # FOLDABLE LOGIC
    if brand == "apple":
        st.warning(" Apple does not manufacture foldable phones")
        is_folded = "No"
    else:
        is_folded = st.selectbox("Foldable Phone", ["Yes", "No"])

# =========================
# CONVERSIONS
# =========================
has_5g_val = 1 if has_5g == "Yes" else 0
is_folded_val = 1 if is_folded == "Yes" else 0

# =========================
# FEATURE ENGINEERING
# =========================
performance_score = ram * gigahertz
camera_score = front_cam + rear_cam

def processor_tier(p):
    if p in ['snapdragon','tensor','bionic']:
        return 'high'
    elif p in ['dimensity','exynos']:
        return 'mid'
    else:
        return 'low'

processor_tier_val = processor_tier(processor)

# =========================
# DATAFRAME
# =========================
input_data = pd.DataFrame([{
    'brand': brand,
    'mobile_processor': processor,
    'gigahertz': gigahertz,
    'RAM': ram,
    'ROM': rom,
    'battery_in_mAh': battery,
    'charging_support_in_watt': charging,
    'size_in_inch': size,
    'refresh_rate': refresh,
    'has_5G': has_5g_val,
    'front_camera_in_megapixel': front_cam,
    'rear_camera': rear_cam,
    'is_folded': is_folded_val,
    'performance_score': performance_score,
    'camera_score': camera_score,
    'processor_tier': processor_tier_val
}])

st.divider()

# =========================
# PREDICT BUTTON
# =========================
if st.button(" Predict Price", use_container_width=True):

    prediction = model.predict(input_data)[0]

    # =========================
    # RESULT BOX (STYLED)
    # =========================
    st.markdown(
        f"""
        <div style="
            background: linear-gradient(90deg, #00c853, #64dd17);
            padding: 25px;
            border-radius: 12px;
            text-align: center;
            font-size: 28px;
            font-weight: bold;
            color: black;
            box-shadow: 0px 4px 20px rgba(0,0,0,0.3);
        ">
             Estimated Price: ₹{int(prediction):,}
        </div>
        """,
        unsafe_allow_html=True
    )