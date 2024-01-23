import streamlit as st
from pytube import YouTube
from pathvalidate import sanitize_filename
import os

def download_video(video_url):
    try:
        # Download the video
        yt = YouTube(video_url)
        video_stream = yt.streams.get_highest_resolution()

        # Sanitize the filename
        sanitized_title = sanitize_filename(yt.title + ".mp4")
        video_path = f"{sanitized_title}"

        video_stream.download(output_path=".", filename=sanitized_title)

        return video_path
    except Exception as e:
        st.error(f'Error: {e}')

def main():
    st.title("YouTube Video Downloader")

    # Input for the YouTube video URL
    video_url = st.text_input("Enter YouTube Video URL:")

    # Button to download the video
    if st.button("Download Video"):
        # Download the video and get the path
        downloaded_video_path = download_video(video_url)

        if downloaded_video_path:
            # Display a link to download the video
            st.video(downloaded_video_path)

if __name__ == "__main__":
    main()
