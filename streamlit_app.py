import streamlit as st

def main():
    st.title("Water Treatment Recommendation Tool")

    # Input Fields
    source = st.selectbox("Water Source", ["City", "Well"])
    people = st.number_input("Number of People in Household", min_value=1, max_value=10, value=4)
    hardness = st.number_input("Hardness (gpg)", min_value=0, max_value=100, value=10)
    iron = st.number_input("Iron (ppm)", min_value=0.0, max_value=20.0, value=1.0)
    pH = st.number_input("pH Level", min_value=0.0, max_value=14.0, value=7.0)
    staining = st.selectbox("Staining (Blue/Green)", ["None", "Blue", "Green"])
    discoloration = st.selectbox("Water Discoloration (Red/Orange)", ["None", "Red", "Orange"])
    sulfur_smell = st.selectbox("Sulfur Smell (Strong/Constant)", ["None", "Strong", "Very Strong"])
    bathrooms = st.number_input("Number of Bathrooms", min_value=1, max_value=10, value=2)
    bacteria = st.selectbox("Bacteria Present", ["No", "Yes"])

    # Call for recommendations check
    def call_for_recommendation():
        if pH < 5.5 or iron > 10 or (source == "City" and 5.5 <= pH <= 6.9) or bathrooms > 4 or sulfur_smell in ["Strong", "Very Strong"]:
            return True
        return False

    # Recommendation Logic
    if call_for_recommendation():
        st.write("**CALL FOR RECOMMENDATION**: Please contact a professional due to the following reasons:")
        if pH < 5.5:
            st.write("- pH is below 5.5")
        if iron > 10:
            st.write("- Iron exceeds 10 ppm")
        if source == "City" and 5.5 <= pH <= 6.9:
            st.write("- City water with pH between 5.5–6.9")
        if bathrooms > 4:
            st.write("- More than 4 bathrooms")
        if sulfur_smell in ["Strong", "Very Strong"]:
            st.write("- Sulfur smell is strong or constant")
    else:
        # Citysoft System
        if source == "City" and iron == 0 and pH == 7.0:
            gpw = people * 60 * hardness * 7
            if gpw < 17000:
                st.write("**Citysoft System Recommendation:** 7-LXDCS-75B")
            elif gpw <= 23000:
                st.write("**Citysoft System Recommendation:** 7-LXDCS-100B (most common)")
            elif gpw <= 35000:
                st.write("**Citysoft System Recommendation:** 7-LXDCS-150B")
            elif gpw <= 48000:
                st.write("**Citysoft System Recommendation:** 7-LXDCS-200B")
            else:
                st.write("**CALL FOR RECOMMENDATION**: GPW exceeds 48,000")

        # Acid Neutralizer
        if source == "Well" and pH < 7.0:
            if iron < 2:
                if people <= 2:
                    st.write("**Acid Neutralizer Recommendation:** 7-LXDAN-1.5B (with pump capable of 6.5 GPM)")
                else:
                    st.write("**Acid Neutralizer Recommendation:** 7-LETDAN-2B (with pump capable of 10 GPM)")
            else:
                st.write("**CALL FOR RECOMMENDATION**: Iron > 2 ppm, install after softener.")

        # Iron Soft System
        if source == "Well" and 1 <= iron <= 10 and (discoloration != "None" or staining != "None"):
            gpr = people * 60 * (hardness + (iron * 4)) * 4
            if gpr < 23000:
                st.write("**Iron Soft System Recommendation:** 7-FESLX-24B + Res-up Feeder")
            elif gpr <= 31000:
                st.write("**Iron Soft System Recommendation:** 7-FESLX-32B + Res-up Feeder (most common)")
            elif gpr <= 47000:
                st.write("**Iron Soft System Recommendation:** 7-FESLX-45B + Res-up Feeder")
            elif gpr <= 64000:
                st.write("**Iron Soft System Recommendation:** 7-FESLX-60B + Res-up Feeder")
            else:
                st.write("**CALL FOR RECOMMENDATION**: GPR exceeds 64,000")

        # Softener
        if source == "Well" and iron < 1:
            gpw = people * 60 * hardness * 7
            if gpw < 17000:
                st.write("**Water Softener Recommendation:** 7-LX-75B / 7-LER-75B")
            elif gpw <= 23000:
                st.write("**Water Softener Recommendation:** 7-LX-100B / 7-LER-100B (most common)")
            elif gpw <= 35000:
                st.write("**Water Softener Recommendation:** 7-LX-150B / 7-LER-150B")
            elif gpw <= 48000:
                st.write("**Water Softener Recommendation:** 7-LX-200B / 7-LER-200B")
            else:
                st.write("**CALL FOR RECOMMENDATION**: GPW exceeds 48,000")

        # UV Light System
        if source == "Well" and bacteria == "Yes":
            st.write("**UV Light System Recommendation:** 7-LWTUV-009 (up to 9 GPM)")

if __name__ == "__main__":
    main()
