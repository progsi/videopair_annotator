import streamlit as st
import pandas as pd
import base64

# Read in the CSV file with the YouTube video IDs
df = pd.read_csv("video_pairs.csv")

# Create a button to cycle through the video pairs
if "index" not in st.session_state:
    st.session_state.index = 0

# Display the current video pair
video_pair = df.iloc[st.session_state.index]
url1 = "https://www.youtube.com/watch?v=" + video_pair[1]
url2 = "https://www.youtube.com/watch?v=" + video_pair[2]

col1, col2 = st.columns(2)

with col1:
    st.subheader("Reference Video")
    st.video(url1)

with col2:
    st.subheader("Candidate Video")
    st.video(url2)

# Create a single choice selection for the video classification
classification_options = ["Match", "Cover", "Other", "No Music"]
classification = st.radio("Classification", classification_options)

if st.button("Next Pair"):

    df.loc[(df.reference_id == video_pair[1]) & (df.candidate_id == video_pair[2]), "classification"] = classification
    # df.to_csv("video_pairs.csv", index=False)
    st.session_state.index += 1
    if st.session_state.index >= len(df):
        st.session_state.index = 0


# Add a download button to download the DataFrame as a CSV file
def download_csv(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="data.csv">Download CSV</a>'
    return href


st.markdown(download_csv(df), unsafe_allow_html=True)


