
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Nigeria Malaria Intelligence System",
    page_icon="🦟",
    layout="wide"
)

# Load datasets
historical = pd.read_csv(r"C:\Users\HP\malaria_historical_data.csv")
forecast = pd.read_csv(r"C:\Users\HP\nigeria_malaria_forecast.csv")

# Dashboard title
st.title("🦟 Nigeria Malaria Intelligence System")
st.subheader("Historical Analysis and Malaria Forecasting")

st.write(
    "An interactive data science project exploring "
    "Nigeria's historical malaria trends and future projections."
)

# Navigation
st.sidebar.title("Navigation")

page = st.sidebar.selectbox(
    "Choose a section",
    [
        "Overview",
        "Historical Analysis",
        "Forecasting",
        "Model Evaluation",
        "Insights"
    ]
)

# Overview
if page == "Overview":

    st.header("Project Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric("Historical Period", "2000–2024")
    col2.metric("Forecast Period", "2025–2030")
    col3.metric("Forecasting Models", "4")

    st.info(
        "Explore historical malaria data and compare "
        "four forecasting approaches."
    )

# Historical Analysis
elif page == "Historical Analysis":

    st.header("Historical Malaria Analysis")

    st.write("Nigeria malaria incidence data from 2000 to 2024.")

    st.metric(
        "Number of Historical Observations",
        len(historical)
    )

    st.line_chart(
        historical.set_index("Year")["Incidence"]
    )

    st.subheader("Historical Data")

    st.dataframe(historical, use_container_width=True)

# Forecasting
elif page == "Forecasting":

    st.header("Malaria Forecasting")

    st.write("Four forecasting approaches for 2025–2030.")

    st.dataframe(forecast, use_container_width=True)

elif page == "Model Evaluation":

    st.header("Model Evaluation")

    st.write(
        "Comparing the performance of four forecasting "
        "models using Mean Absolute Error (MAE) and "
        "Root Mean Squared Error (RMSE)."
    )

    evaluation_data = pd.DataFrame({

        "Evaluation Period": [
            "2020–2024",
            "2020–2024",
            "2020–2024",
            "2020–2024",
            "2015–2019",
            "2015–2019",
            "2015–2019",
            "2015–2019"
        ],

        "Model": [
            "Holt's Linear Trend",
            "Naive Forecast",
            "Simple Exponential Smoothing",
            "Linear Regression",
            "Naive Forecast",
            "Simple Exponential Smoothing",
            "Holt's Linear Trend",
            "Linear Regression"
        ],

        "MAE": [
            4.43, 6.18, 6.18, 43.66,
            2.62, 2.62, 3.30, 14.78
        ],

        "RMSE": [
            5.80, 6.96, 6.96, 44.35,
            2.88, 2.88, 3.92, 17.48
        ]
    })

    st.subheader("Model Performance Results")

    st.dataframe(
        evaluation_data,
        use_container_width=True,
        hide_index=True
    )

    st.subheader("Understanding the Metrics")

    col1, col2 = st.columns(2)

    with col1:
        st.info(
            "**MAE:** Mean Absolute Error. "
            "It measures the average size of prediction errors. "
            "Lower values indicate better performance."
        )

    with col2:
        st.info(
            "**RMSE:** Root Mean Squared Error. "
            "It gives more weight to larger prediction errors. "
            "Lower values indicate better performance."
        )

    st.success(
        "Holt's Linear Trend performed best in the "
        "2020–2024 test period, while Naive Forecast "
        "and Simple Exponential Smoothing performed "
        "best in the 2015–2019 validation period."
    )
elif page == "Insights":

    st.header("Key Research Insights")

    # Historical statistics
    first_value = historical.iloc[0]["Incidence"]
    last_value = historical.iloc[-1]["Incidence"]

    highest = historical.loc[historical["Incidence"].idxmax()]
    lowest = historical.loc[historical["Incidence"].idxmin()]

    percentage_change = (
        (last_value - first_value) / first_value
    ) * 100

    st.subheader("Historical Findings (2000–2024)")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Starting Incidence (2000)",
        round(first_value, 2)
    )

    col2.metric(
        "Latest Incidence (2024)",
        round(last_value, 2)
    )

    col3.metric(
        "Overall Change",
        f"{percentage_change:.2f}%"
    )

    st.write(
        f"**Highest incidence:** {highest['Incidence']:.2f} "
        f"in {int(highest['Year'])}."
    )

    st.write(
        f"**Lowest incidence:** {lowest['Incidence']:.2f} "
        f"in {int(lowest['Year'])}."
    )

    st.subheader("Future Forecast Insights")

    st.write(
        "The four forecasting models produce different "
        "projections for 2025–2030."
    )

    st.dataframe(forecast, use_container_width=True)

    st.subheader("Research Limitations")

    st.warning(
        "This analysis uses only 25 annual observations "
        "from 2000 to 2024. Forecasts are estimates, not "
        "guaranteed future outcomes. They should not be "
        "treated as confirmed malaria case counts."
    )

    st.success(
        "The project demonstrates how historical health "
        "data can support trend analysis and forecasting."
    )