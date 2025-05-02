import streamlit as st
import re
import math
import random
import string

def generate_strong_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(12))

def calculate_password_strength(password):
    length_score = min(len(password) / 12, 1) * 30  # 30% weight
    digit_score = min(len(re.findall(r'\d', password)) / 2, 1) * 20  # 20% weight
    upper_score = min(len(re.findall(r'[A-Z]', password)) / 2, 1) * 20  # 20% weight
    special_score = min(len(re.findall(r'[!@#$%^&*(),.?":{}|<>]', password)) / 2, 1) * 20  # 20% weight
    
    total_score = length_score + digit_score + upper_score + special_score
    return math.ceil(total_score)  # Round up for better readability

def evaluate_strength(score):
    if score >= 80:
        return "Strong", "#4CAF50"
    elif score >= 50:
        return "Moderate", "#FFC107"
    else:
        return "Weak", "#F44336"

# Streamlit UI
st.set_page_config(page_title="Password Strength Checker", page_icon="🔐", layout="centered")
st.title("🔐 Password Strength Checker...")
st.markdown("**Create a secure password and check its strength in real-time!**")

password = st.text_input("Enter your password:", type="password")
if password:
    score = calculate_password_strength(password)
    strength, color = evaluate_strength(score)
    
    st.markdown(f"""
        <div style="text-align: center; padding: 10px; background-color: {color}; color: white; border-radius: 10px;">
            <h3>{strength} Password</h3>
            <h4>Strength Score: {score}%</h4>
        </div>
    """, unsafe_allow_html=True)
    
    if score < 80:
        st.warning("🔹 Tips to strengthen your password:")
        st.markdown("✔ Use at least 12 characters")
        st.markdown("✔ Include uppercase & lowercase letters")
        st.markdown("✔ Add numbers and special symbols")

# Offer to generate a strong password
response = st.radio("Need a strong password?", ("Yes", "No"), index=None)
if response == "Yes":
    strong_password = generate_strong_password()
    st.success(f"Here is a strong password: `{strong_password}`")
elif response == "No":
    st.info("As you wish, dear! 😊")
    
st.markdown("---")
st.markdown("Made with ❤️ by Mrs Asif")