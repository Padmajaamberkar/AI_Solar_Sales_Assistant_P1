import streamlit as st
import pandas as pd
import plotly.express as px

from calculator import SolarCalculator
from ai_chat import ask_ai
from pdf_generator import generate_pdf
from database import save_customer


# Page Config
st.set_page_config(
    page_title="AI Solar Sales Assistant",
    page_icon="☀️",
    layout="wide"
)


# Load CSS
try:
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )
except:
    pass


calculator = SolarCalculator()


# Sidebar
st.sidebar.title("☀️ AI Solar Sales Assistant")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "☀️ Solar Calculator",
        "🤖 AI Assistant",
        "📊 Dashboard",
        "ℹ️ About"
    ]
)


# ---------------- HOME PAGE ----------------

if page == "🏠 Home":

    st.markdown("""
    # ☀️ SunSmart AI

    ### Intelligent Solar Recommendation Platform
    """)

    st.subheader(
        "Helping homeowners and businesses choose the right solar system using AI."
    )

    st.markdown("---")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Customers", "1500+")
    c2.metric("Projects", "820")
    c3.metric("Accuracy", "96%")
    c4.metric("ROI", "3.9 Years")

    st.markdown("---")

    st.header("Why Choose Solar?")

    st.success("💰 Reduce Electricity Bills")
    st.success("🌞 Government Subsidy Available")
    st.success("🌱 Eco-Friendly Energy")
    st.success("📈 Long-Term Savings")

    st.markdown("---")

    st.info(
        "Use the Solar Calculator from the sidebar to get your personalised recommendation."
    )


# ---------------- SOLAR CALCULATOR ----------------

elif page == "☀️ Solar Calculator":

    st.title("☀️ Solar Calculator")

    customer = st.text_input("Customer Name")
    mobile = st.text_input("Mobile Number")
    email = st.text_input("Email Address")
    city = st.text_input("City")

    property_type = st.selectbox(
        "Property Type",
        ["Residential", "Commercial"]
    )

    phase = st.selectbox(
        "Connection Type",
        ["Single Phase", "Three Phase"]
    )

    bill = st.number_input(
        "Monthly Electricity Bill (₹)",
        min_value=0,
        value=1500,
        step=100
    )

    roof = st.number_input(
        "Roof Area (sq.ft)",
        min_value=100,
        value=600,
        step=10
    )


    if st.button("Calculate Recommendation"):

        result = calculator.calculate(
            bill,
            roof
        )

        save_customer(
            customer,
            mobile,
            email,
            city,
            bill,
            roof,
            result
        )


        st.session_state["result"] = result
        st.session_state["customer"] = customer
        st.session_state["mobile"] = mobile
        st.session_state["city"] = city


        st.success(
            "✅ Recommendation Generated Successfully"
        )


        c1, c2, c3 = st.columns(3)

        c1.metric(
            "System Size",
            f"{result['system_kw']} kW"
        )

        c2.metric(
            "Panels",
            result["panels"]
        )

        c3.metric(
            "Payback",
            f"{result['payback']} Years"
        )


        st.markdown("---")

        st.subheader("Recommendation")

        st.write(
            f"Installation Cost : ₹{result['installation_cost']:,}"
        )

        st.write(
            f"Government Subsidy : ₹{result['subsidy']:,}"
        )

        st.write(
            f"Final Cost : ₹{result['final_cost']:,}"
        )

        st.write(
            f"Monthly Generation : {result['monthly_generation']} Units"
        )

        st.write(
            f"Monthly Savings : ₹{result['monthly_savings']:,}"
        )

        st.write(
            f"Yearly Savings : ₹{result['yearly_savings']:,}"
        )


        pdf_path = generate_pdf(
            customer,
            mobile,
            city,
            result
        )


        with open(pdf_path, "rb") as file:

            st.download_button(
                label="📄 Download Proposal PDF",
                data=file,
                file_name="Solar_Proposal.pdf",
                mime="application/pdf"
            )


        if roof >= result["roof_required"]:

            st.success(
                "✅ Roof Area is Sufficient"
            )

        else:

            st.error(
                f"❌ Minimum Roof Required: {result['roof_required']} sq.ft"
            )



# ---------------- AI ASSISTANT ----------------

elif page == "🤖 AI Assistant":

    st.title(
        "🤖 SunSmart AI Assistant"
    )

    st.write(
        "Ask anything about Solar Energy."
    )


    question = st.text_area(
        "Ask your question"
    )


    if st.button("Ask AI"):

        if question:

            with st.spinner("Thinking..."):

                answer = ask_ai(question)

            st.success(answer)

        else:

            st.warning(
                "Please enter a question."
            )



# ---------------- DASHBOARD ----------------

elif page == "📊 Dashboard":

    st.title(
        "📊 Solar Dashboard"
    )


    if "result" not in st.session_state:

        st.warning(
            "⚠️ Please calculate a recommendation first from Solar Calculator."
        )


    else:

        result = st.session_state["result"]


        col1, col2, col3 = st.columns(3)

        col1.metric(
            "System Size",
            f"{result['system_kw']} kW"
        )

        col2.metric(
            "Panels",
            result["panels"]
        )

        col3.metric(
            "Payback",
            f"{result['payback']} Years"
        )


        st.markdown("---")


        cost = pd.DataFrame(
            {
                "Category":
                [
                    "Installation Cost",
                    "Government Subsidy",
                    "Final Cost"
                ],

                "Amount":
                [
                    result["installation_cost"],
                    result["subsidy"],
                    result["final_cost"]
                ]
            }
        )


        fig = px.bar(
            cost,
            x="Category",
            y="Amount",
            text="Amount",
            title="Cost Analysis"
        )


        st.plotly_chart(
            fig,
            use_container_width=True
        )



# ---------------- ABOUT ----------------

else:

    st.title(
        "About"
    )

    st.subheader(
        "AI Solar Sales Assistant"
    )

    st.write(
        "Developed by Padmaja Amberkar"
    )

    st.write(
        "Built using Python, Streamlit, Plotly and ReportLab"
    )

    st.info(
        "Version 1.0"
    )
