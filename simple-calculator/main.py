import streamlit as st

def main():
    # Custom CSS for styling
    st.markdown("""
    <style>
        .title {
            text-align: center;
            font-size: 40px;
            color: #4CAF50;
            font-weight: bold;
            margin-bottom: 20px;
        }
        .subheader {
            text-align: center;
            font-size: 18px;
            color: #555;
            margin-bottom: 40px;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 24px;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            margin-top: 20px;
            transition: 0.3s;
        }
        .stButton button:hover {
            background-color: #45a049;
        }
        
        .stSelectbox > div {
            display: flex;
            justify-content: center;
        }
        .stSelectbox div[data-baseweb="select"] {
            width: 100%; 
            margin: auto;
            text-align: center;
        }
        .stSelectbox div[data-baseweb="select"] > div {
            text-align: center !important;
        }
        .stNumberInput input {
            border-radius: 8px;
            padding: 8px;
        }
    </style>
""", unsafe_allow_html=True)

    # Title and Subtitle
    st.markdown('<div class="title">🧮 Simple Calculator</div>', unsafe_allow_html=True)
    st.markdown('<div class="subheader">Enter two numbers and select an operation to perform</div>', unsafe_allow_html=True)

    # Columns for input
    col1, col2 = st.columns(2)

    with col1:
        num1 = st.number_input("Enter first number", value=0.0)
    with col2:
        num2 = st.number_input("Enter second number", value=0.0)

    # Operation selector
    operation = st.selectbox(
        "Choose operation",
        ["Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)"]
    )

    # Calculate button
    if st.button("Calculate"):
        try:
            if operation == "Addition (+)":
                result = num1 + num2
                symbol = "+"
            elif operation == "Subtraction (-)":
                result = num1 - num2
                symbol = "-"
            elif operation == "Multiplication (×)":
                result = num1 * num2
                symbol = "×"
            else:  # Division
                if num2 == 0:
                    st.error("🚫 Error: Division by zero!")
                    return
                result = num1 / num2
                symbol = "÷"

            st.success(f"✅ **Result:** {num1} {symbol} {num2} = {round(result, 2)}")

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
