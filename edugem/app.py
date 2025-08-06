import streamlit as st
from gemma_interface import run_gemma
from pdf_utils import extract_pdf_text

st.set_page_config(page_title="EduGem", layout="wide")
st.title("📘 EduGem – Offline AI Tutor")

tab1, tab2 = st.tabs(["🎓 Learn by Topic", "📚 Upload Textbook"])

with tab1:
    st.header("Choose a Topic")
    grade = st.selectbox("Grade Level", ["Grade 5", "Grade 6", "Grade 7", "Grade 8"])
    subject = st.selectbox("Subject", ["Science", "Math", "History"])
    topic = st.text_input("Enter Topic", placeholder="e.g. Water Cycle")

    if st.button("📖 Teach Me"):
        with st.spinner("Thinking..."):
            prompt = f"Teach a {grade} student about the topic '{topic}' in simple terms. Include a quiz at the end."
            response = run_gemma(prompt)
            st.subheader("🧠 Explanation + Quiz")
            st.write(response)

with tab2:
    st.header("Turn Your Textbook Into a Lesson")
    uploaded_file = st.file_uploader("Upload a PDF textbook", type=['pdf'])

    if uploaded_file:
        text = extract_pdf_text(uploaded_file)
        st.success("✅ Text extracted!")
        with st.expander("🔍 View Extracted Text"):
            st.text_area("Extracted Text", text[:3000], height=300)

        if st.button("🪄 Summarize + Quiz"):
            with st.spinner("Summarizing..."):
                prompt = f"Summarize the following for a {grade} student. Give 5 key facts and a quiz:\n\n{text[:3000]}"
                result = run_gemma(prompt)
                st.subheader("📘 Lesson Summary + Quiz")
                st.write(result)
