import streamlit as st
import pandas as pd
import joblib



model = joblib.load("mobile_price_model.pkl")
scaler = joblib.load("scaler.pkl")




st.set_page_config(
    page_title="Mobile Price Predictor",
    page_icon="📱",
    layout="wide"
)




st.markdown("""
<style>

.stApp {
    background-color: #FFFFFF;
}

.main-title {
    text-align: center;
    font-size: 48px;
    font-weight: 800;
    color: #6688B5;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #777777;
    margin-bottom: 35px;
}

.section-title {
    background-color: #DFF3FF;
    padding: 12px 18px;
    border-radius: 14px;
    color: #54749D;
    font-size: 23px;
    font-weight: 700;
    margin-top: 20px;
    margin-bottom: 20px;
}

.feature-label {
    font-size: 16px;
    font-weight: 650;
    color: #5F6F85;
    margin-bottom: 5px;
}

.stButton > button {
    width: 100%;
    background-color: #F6DCE8;
    color: #5B6472;
    border: none;
    border-radius: 14px;
    padding: 14px;
    font-size: 18px;
    font-weight: 700;
}

.stButton > button:hover {
    background-color: #DFF3FF;
}

.result-box {
    background-color: #F6DCE8;
    padding: 25px;
    border-radius: 18px;
    text-align: center;
    margin-top: 25px;
}

</style>
""", unsafe_allow_html=True)




st.markdown(
    '<div class="main-title">📱 Mobile Price Predictor</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Enter the specifications of your mobile phone and predict its price range'
    '</div>',
    unsafe_allow_html=True
)




st.markdown(
    '<div class="section-title">⚡ Performance & Battery</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="feature-label">Battery Power (mAh)</div>',
                unsafe_allow_html=True)
    battery_power = st.slider(
        "Battery Power",
        500, 2000, 1200,
        step=50,
        label_visibility="collapsed"
    )

with col2:
    st.markdown('<div class="feature-label">RAM (MB)</div>',
                unsafe_allow_html=True)
    ram = st.slider(
        "RAM",
        256, 4000, 2000,
        step=128,
        label_visibility="collapsed"
    )

with col3:
    st.markdown('<div class="feature-label">Clock Speed (GHz)</div>',
                unsafe_allow_html=True)
    clock_speed = st.slider(
        "Clock Speed",
        0.5, 3.0, 1.5,
        step=0.1,
        label_visibility="collapsed"
    )


col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="feature-label">CPU Cores</div>',
                unsafe_allow_html=True)
    n_cores = st.select_slider(
        "CPU Cores",
        options=[1, 2, 3, 4, 5, 6, 7, 8],
        value=4,
        label_visibility="collapsed"
    )

with col2:
    st.markdown('<div class="feature-label">Internal Memory (GB)</div>',
                unsafe_allow_html=True)
    int_memory = st.slider(
        "Internal Memory",
        2, 64, 32,
        step=2,
        label_visibility="collapsed"
    )

with col3:
    st.markdown('<div class="feature-label">Mobile Weight (g)</div>',
                unsafe_allow_html=True)
    mobile_wt = st.slider(
        "Mobile Weight",
        80, 200, 140,
        step=5,
        label_visibility="collapsed"
    )




st.markdown(
    '<div class="section-title">🖥️ Display</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="feature-label">Pixel Height</div>',
                unsafe_allow_html=True)
    px_height = st.slider(
        "Pixel Height",
        0, 2000, 1000,
        step=50,
        label_visibility="collapsed"
    )

with col2:

    st.markdown('<div class="feature-label">Pixel Width</div>',

                unsafe_allow_html=True)

    px_width = st.slider(

        "Pixel Width",

        0, 2000, 1000,

        step=50,

        label_visibility="collapsed"

    )

with col3:

    st.markdown('<div class="feature-label">Mobile Depth</div>',

                unsafe_allow_html=True)

    m_dep = st.slider(

        "Mobile Depth",

        0.1, 1.0, 0.5,

        step=0.05,

        label_visibility="collapsed"

    )

col1, col2 = st.columns(2)

with col1:

    st.markdown('<div class="feature-label">Screen Height</div>',

                unsafe_allow_html=True)

    sc_h = st.slider(

        "Screen Height",

        5, 20, 12,

        step=1,

        label_visibility="collapsed"

    )

with col2:

    st.markdown('<div class="feature-label">Screen Width</div>',

                unsafe_allow_html=True)

    sc_w = st.slider(

        "Screen Width",

        2, 20, 7,

        step=1,

        label_visibility="collapsed"

    )



st.markdown(

    '<div class="section-title">📷 Camera</div>',

    unsafe_allow_html=True

)

col1, col2 = st.columns(2)

with col1:

    st.markdown('<div class="feature-label">Primary Camera (MP)</div>',

                unsafe_allow_html=True)

    pc = st.slider(

        "Primary Camera",

        0, 20, 10,

        step=1,

        label_visibility="collapsed"

    )

with col2:

    st.markdown('<div class="feature-label">Front Camera (MP)</div>',

                unsafe_allow_html=True)

    fc = st.slider(

        "Front Camera",

        0, 20, 5,

        step=1,

        label_visibility="collapsed"

    )



st.markdown(

    '<div class="section-title">📡 Connectivity</div>',

    unsafe_allow_html=True

)

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.markdown('<div class="feature-label">Bluetooth</div>',

                unsafe_allow_html=True)

    blue = st.selectbox(

        "Bluetooth",

        [0, 1],

        format_func=lambda x: "Yes" if x == 1 else "No",

        label_visibility="collapsed"

    )

with col2:

    st.markdown('<div class="feature-label">Dual SIM</div>',

                unsafe_allow_html=True)

    dual_sim = st.selectbox(

        "Dual SIM",

        [0, 1],

        format_func=lambda x: "Yes" if x == 1 else "No",

        label_visibility="collapsed"

    )

with col3:

    st.markdown('<div class="feature-label">4G</div>',

                unsafe_allow_html=True)

    four_g = st.selectbox(

        "4G",

        [0, 1],

        format_func=lambda x: "Yes" if x == 1 else "No",

        label_visibility="collapsed"

    )

with col4:

    st.markdown('<div class="feature-label">3G</div>',

                unsafe_allow_html=True)

    three_g = st.selectbox(

        "3G",

        [0, 1],

        format_func=lambda x: "Yes" if x == 1 else "No",

        label_visibility="collapsed"

    )

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown('<div class="feature-label">WiFi</div>',

                unsafe_allow_html=True)

    wifi = st.selectbox(

        "WiFi",

        [0, 1],

        format_func=lambda x: "Yes" if x == 1 else "No",

        label_visibility="collapsed"

    )

with col2:

    st.markdown('<div class="feature-label">Touch Screen</div>',

                unsafe_allow_html=True)

    touch_screen = st.selectbox(

        "Touch Screen",

        [0, 1],

        format_func=lambda x: "Yes" if x == 1 else "No",

        label_visibility="collapsed"

    )

with col3:

    st.markdown('<div class="feature-label">Talk Time (hours)</div>',

                unsafe_allow_html=True)

    talk_time = st.slider(

        "Talk Time",

        1, 20, 10,

        step=1,

        label_visibility="collapsed"

    )



st.markdown("---")

if st.button("🔮 Predict Mobile Price Range"):

    input_data = pd.DataFrame([{

        "battery_power": battery_power,

        "blue": blue,

        "clock_speed": clock_speed,

        "dual_sim": dual_sim,

        "fc": fc,

        "four_g": four_g,

        "int_memory": int_memory,

        "m_dep": m_dep,

        "mobile_wt": mobile_wt,

        "n_cores": n_cores,

        "pc": pc,

        "px_height": px_height,

        "px_width": px_width,

        "ram": ram,

        "sc_h": sc_h,

        "sc_w": sc_w,

        "talk_time": talk_time,

        "three_g": three_g,

        "touch_screen": touch_screen,

        "wifi": wifi

    }])

    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)[0]

    price_ranges = {

        0: "Low Cost",

        1: "Medium Cost",

        2: "High Cost",

        3: "Very High Cost"

    }

    st.markdown(

        f"""

        <div class="result-box">

            <h2>Predicted Price Range</h2>

            <h1>{price_ranges[prediction]}</h1>

        </div>

        """,

        unsafe_allow_html=True

    )
