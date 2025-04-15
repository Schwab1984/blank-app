import streamlit as st

st.set_page_config(page_title="Water Treatment Recommendation Tool")
st.title("💧 Water Treatment Recommendation Tool")

# --- User Inputs ---
st.header("Step 1: Water Test Results")
source = st.selectbox("Water Source", ["Well", "City"])
ph = st.number_input("pH", min_value=0.0, max_value=14.0, step=0.1)
hardness = st.number_input("Hardness (gpg)", min_value=0.0)
iron = st.number_input("Iron (ppm)", min_value=0.0)
tds = st.number_input("TDS", min_value=0.0)
chlorine = st.selectbox("Chlorine", ["Present", "Absent"])
bacteria = st.selectbox("Bacteria Test Result", ["Positive", "Negative"])
staining = st.selectbox("Any staining?", ["None", "Red/Orange", "Blue/Green"])
sulfur_smell = st.selectbox("Sulfur Smell", ["None", "Mild", "Strong/Constant", "Very Strong"])

st.header("Step 2: Household Info")
people = st.number_input("# of People in Home", min_value=1, step=1)
bathrooms = st.number_input("# of Bathrooms", min_value=1, step=1)

# --- Call Recommendation Checks ---
call_needed = False
call_reasons = []

if ph < 5.5:
    call_needed = True
    call_reasons.append("pH < 5.5")
if iron > 10:
    call_needed = True
    call_reasons.append("Iron > 10 ppm")
if source == "City" and 5.5 <= ph < 7.0:
    call_needed = True
    call_reasons.append("City Water with pH 5.5–6.9")
if bathrooms > 4:
    call_needed = True
    call_reasons.append("More than 4 bathrooms")
if sulfur_smell in ["Strong/Constant", "Very Strong"]:
    call_needed = True
    call_reasons.append("Strong/Constant or Very Strong Sulfur Smell")

# --- Disclaimers ---
def show_disclaimers():
    st.info("**Disclaimers:**\n\n- All water should be tested for bacteria at a state-approved lab.\n- Blue/green staining can also be caused by electrolysis or dissolved gases.\n- For residential estimating use only.")

# --- Output Recommendation ---
st.header("Recommendations")
if call_needed:
    st.error("⚠️ CALL FOR RECOMMENDATION REQUIRED")
    for reason in call_reasons:
        st.write(f"- {reason}")
    show_disclaimers()
else:
    st.success("✅ Recommendations Ready – Next steps coming soon...")
    st.write("(Logic for specific equipment recommendations will be added here.)")
    show_disclaimers()
