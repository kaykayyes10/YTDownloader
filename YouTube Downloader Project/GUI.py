import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from pytube import YouTube

def download_video():
    url = url_entry.get()
    try:
        youtube_video = YouTube(url)
        video_stream = youtube_video.streams.get_highest_resolution()
        video_stream.download()
        messagebox.showinfo("Download Successful", "Video downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the main application window
root = tk.Tk()
root.title("YouTube Downloader")

# URL Entry
url_label = ttk.Label(root, text="Enter YouTube URL:")
url_label.pack()
url_entry = ttk.Entry(root, width=100)
url_entry.pack()

# Download Button
download_button = ttk.Button(root, text="Download", command=download_video)
download_button.pack()

# Run the main event loop
root.mainloop()
