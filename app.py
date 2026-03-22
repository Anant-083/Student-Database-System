import streamlit as st
from database import *

st.set_page_config(page_title="Student Database", page_icon="🎓", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        font-size: 16px;
        font-weight: bold;
    }
    .stTextInput>div>div>input {
        border-radius: 10px;
    }
    .title {
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        color: #4A90D9;
        margin-bottom: 0px;
    }
    .subtitle {
        text-align: center;
        font-size: 16px;
        color: #888;
        margin-bottom: 30px;
    }
    .card {
        background-color: white;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="title">🎓 Student Database System</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Manage your students easily</p>', unsafe_allow_html=True)
st.markdown("---")

with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/201/201818.png", width=100)
    st.title("📋 Navigation")
    menu = st.selectbox("", ["➕ Add Student", "👀 View Students", "🔍 Search Student", "✏️ Update Student", "🗑️ Delete Student"])
    st.markdown("---")
    st.markdown("**Total Students:**")
    students = get_all_students()
    st.markdown(f"### 👨‍🎓 {len(students)}")

st.markdown('<div class="card">', unsafe_allow_html=True)

if menu == "➕ Add Student":
    st.subheader("➕ Add New Student")
    st.markdown(" ")
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("👤 Student Name")
        age = st.number_input("🎂 Age", min_value=1, max_value=100)
    with col2:
        grade = st.text_input("📚 Grade")
        email = st.text_input("📧 Email")
    st.markdown(" ")
    if st.button("✅ Add Student"):
        if name and grade and email:
            add_student(name, age, grade, email)
            st.success(f"🎉 Student **{name}** added successfully!")
            st.balloons()
        else:
            st.error("⚠️ Please fill all fields!")

elif menu == "👀 View Students":
    st.subheader("👀 All Students")
    students = get_all_students()
    if students:
        st.markdown(f"**{len(students)} students found**")
        st.markdown(" ")
        import pandas as pd
        df = pd.DataFrame(students, columns=["ID", "Name", "Age", "Grade", "Email"])
        st.dataframe(df, use_container_width=True)
    else:
        st.info("📭 No students found! Add some students first.")

elif menu == "🔍 Search Student":
    st.subheader("🔍 Search Student")
    name = st.text_input("Enter name to search")
    if st.button("🔍 Search"):
        results = search_student(name)
        if results:
            import pandas as pd
            df = pd.DataFrame(results, columns=["ID", "Name", "Age", "Grade", "Email"])
            st.dataframe(df, use_container_width=True)
        else:
            st.warning("⚠️ No student found with that name!")

elif menu == "✏️ Update Student":
    st.subheader("✏️ Update Student")
    students = get_all_students()
    if students:
        import pandas as pd
        df = pd.DataFrame(students, columns=["ID", "Name", "Age", "Grade", "Email"])
        st.dataframe(df, use_container_width=True)
        st.markdown(" ")
        student_id = st.number_input("Enter Student ID to update", min_value=1)
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("New Name")
            age = st.number_input("New Age", min_value=1, max_value=100)
        with col2:
            grade = st.text_input("New Grade")
            email = st.text_input("New Email")
        if st.button("✅ Update Student"):
            if name and grade and email:
                update_student(student_id, name, age, grade, email)
                st.success("✅ Student updated successfully!")
            else:
                st.error("⚠️ Please fill all fields!")
    else:
        st.info("📭 No students found!")

elif menu == "🗑️ Delete Student":
    st.subheader("🗑️ Delete Student")
    students = get_all_students()
    if students:
        import pandas as pd
        df = pd.DataFrame(students, columns=["ID", "Name", "Age", "Grade", "Email"])
        st.dataframe(df, use_container_width=True)
        st.markdown(" ")
        student_id = st.number_input("Enter Student ID to delete", min_value=1)
        if st.button("🗑️ Delete Student"):
            delete_student(student_id)
            st.success("✅ Student deleted successfully!")
            st.rerun()
    else:
        st.info("📭 No students found!")

st.markdown('</div>', unsafe_allow_html=True)
st.markdown("---")
st.markdown('<p style="text-align:center; color:#888;">Built by Anant 🚀 | Student Database System</p>', unsafe_allow_html=True)