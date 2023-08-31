import tkinter as tk
import os
import requests
from tkinter import filedialog
from pytube import YouTube
#
def browse_directory():
    selected_directory = filedialog.askdirectory()
    dir_var.set(selected_directory)
def extract_video_links(playlist_id):
    api_url = f"https://www.googleapis.com/youtube/v3/playlistItems"
    response = requests.get(api_url, params={"part": "snippet", "maxResults": 50, "playlistId": playlist_id, "key": "AIzaSyCXycF_7TTthSaIl2ZEojtMYMEicxestv4"})
    data = response.json()
    return [item['snippet']['resourceId']['videoId'] for item in data.get("items", [])]

def extract_downloadable_links(video_ids):
    downloadable_links = []
    for video_id in video_ids:
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        video = YouTube(video_url)
        stream = video.streams.get_highest_resolution()
        downloadable_links.append(stream.url)
    return downloadable_links

def generate_folders_and_file():
    playlist_id = playlist_link_entry.get().split("&list=")[1].split("&")[0]
    playlist_name = playlist_link_entry.get().split("&list=")[1].split("&", 1)[1].split("=")[1].replace("%", "_")

    selected_directory = dir_var.get()
    playlist_folder_path = os.path.join(selected_directory, playlist_name)
    os.makedirs(playlist_folder_path, exist_ok=True)

    video_ids = extract_video_links(playlist_id)
    downloadable_links = extract_downloadable_links(video_ids)

    text_file_path = os.path.join(playlist_folder_path, f"{playlist_name}.txt")
    with open(text_file_path, "w") as text_file:
        for link in downloadable_links:
            text_file.write(link + "\n")

    status_label.config(text="Done!")

#
app = tk.Tk()
app.title("YouTube Playlist App")
app.geometry("468x160")
app.resizable(False, False)

dir_var = tk.StringVar(value=os.path.expanduser("~/Desktop"))
directory_label = tk.Label(app, text="Select Folder:")
directory_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
dir_entry = tk.Entry(app, textvariable=dir_var, width=40)
dir_entry.grid(row=0, column=1, padx=10, pady=10)
dir_entry.configure(state='readonly')

browse_button = tk.Button(app, text="Browse", command=browse_directory)
browse_button.grid(row=0, column=2, padx=10, pady=10)

playlist_label = tk.Label(app, text="Enter Playlist Link:")
playlist_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
playlist_link_entry = tk.Entry(app, width=40)
playlist_link_entry.grid(row=1, column=1, padx=10, pady=10)

generate_button = tk.Button(app, text="Generate", command=generate_folders_and_file)
generate_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

status_label = tk.Label(app, text="", fg="green")
status_label.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

icon_path = "ic.ico"
app.iconbitmap(icon_path)
app.mainloop()

