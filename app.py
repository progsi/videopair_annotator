import streamlit as st
import pandas as pd


# Read in the CSV file with the YouTube video IDs
df = pd.read_csv("video_pairs.csv")


# Create a button to cycle through the video pairs
if "index" not in st.session_state:
    st.session_state.index = 0
if st.button("Next Pair"):
    st.session_state.index += 1
    if st.session_state.index >= len(df):
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
classification = st.selectbox("Classification", classification_options)

df.at[st.session_state.index, "Classification"] = classification


if st.button("Save Classification"):
    # Write the video classification to the CSV file
    df.to_csv("video_pairs.csv", index=False)
    st.success("Classification saved!")

