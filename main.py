import streamlit as st
import json

# Load the data from data.json
with open('data.json', 'r') as file:
    data = json.load(file)

# Function to set dark mode
def set_dark_mode():
    dark_mode = st.sidebar.checkbox("Toggle Dark Mode", value=False)
    if dark_mode:
        st.markdown(
            """
            <style>
            body {
                background-color: #121212;
                color: white;
            }
            h1, h2, h3, h4, h5, h6 {
                color: white;
            }
            </style>
            """, unsafe_allow_html=True)
    else:
        st.markdown(
            """
            <style>
            body {
                background-color: white;
                color: black;
            }
            h1, h2, h3, h4, h5, h6 {
                color: black;
            }
            </style>
            """, unsafe_allow_html=True)

# Dark mode toggle
set_dark_mode()

# Display documentation data
st.title("AI-Powered WordPress Chat Bot Documentation")

st.header("1. Introduction")
st.write(data["introduction"])

st.header("2. Installation Instructions")
for step in data["installation_instructions"][0]["steps"]:
    st.subheader(step["title"])
    for instruction in step["instructions"]:
        if isinstance(instruction, str):
            st.write(f"- {instruction}")
        elif isinstance(instruction, dict) and "code_snippet" in instruction:
            st.code(instruction["code_snippet"], language='python')
        if "example" in instruction:
            st.write("Example:")
            st.code(instruction["example"], language='python')

st.header("3. Customizing Your Chat Bot")
for step in data["customizing_your_chat_bot"][0]["steps"]:
    st.subheader(step["title"])
    for instruction in step["instructions"]:
        if isinstance(instruction, str):
            st.write(f"- {instruction}")
        elif isinstance(instruction, dict) and "code_snippet" in instruction:
            st.code(instruction["code_snippet"], language='python')

st.header("4. Testing and Verification")
for step in data["testing_and_verification"][0]["steps"]:
    st.write(f"- {step}")

st.header("5. Troubleshooting")
for issue in data["troubleshooting"][0]["steps"]:
    st.subheader(issue["title"])
    for detail in issue["issues"]:
        st.write(f"- {detail}")

    if "links" in issue:
        st.write("Resources:")
        for link in issue["links"]:
            st.markdown(f"[{link['label']}]({link['url']})")

st.header("6. Support")
for support in data["support"][0]["steps"]:
    st.write(support["step"])
    for detail in support["details"]:
        st.write(f"- {detail['contact_method']}: {detail['value']}")

st.write(data["closing"])
st.write(data["signature"])