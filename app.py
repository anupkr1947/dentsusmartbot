"""
Dentsu Smart Buddy — v5.1 (Production)
=========================================
Features:

Enter your name
Write quick notes/tasks
Save notes during the session
View all saved notes
Clear notes
Simple clean UI
Purpose 
Streamlit basics
Session state
Forms and buttons
Lists and simple UI
Python + frontend interaction
"""

import streamlit as st
from datetime import datetime

# Page setup
st.set_page_config(
    page_title="Simple Notes App",
    page_icon="📝",
    layout="centered"
)

# Title
st.title("📝 Simple Notes App")
st.write("A beginner-friendly Streamlit application.")

# Initialize session state
if "notes" not in st.session_state:
    st.session_state.notes = []

# User input
name = st.text_input("Enter your name")

# Note input
note = st.text_area("Write your note")

# Save button
if st.button("Save Note"):

    if name and note:
        current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        st.session_state.notes.append({
            "name": name,
            "note": note,
            "time": current_time
        })

        st.success("Note saved successfully!")

    else:
        st.warning("Please enter both name and note.")

# Display notes
st.subheader("Saved Notes")

if st.session_state.notes:

    for item in reversed(st.session_state.notes):

        st.markdown("---")

        st.write(f"👤 Name: {item['name']}")
        st.write(f"📝 Note: {item['note']}")
        st.write(f"⏰ Time: {item['time']}")

else:
    st.info("No notes saved yet.")

# Clear notes button
if st.button("Clear All Notes"):
    st.session_state.notes = []
    st.success("All notes cleared!")
