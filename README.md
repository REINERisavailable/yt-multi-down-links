# YouTube Playlist Downloader

A simple Python script using Tkinter and Pytube to download YouTube playlists. Given a playlist link, the script generates folders, text files, and downloads videos in the highest resolution.




## Prerequisites

Make sure you have the following dependencies installed:

- `tkinter`
- `os`
- `requests`
- `filedialog`
- `pytube`

Install the dependencies using:

```bash
pip install tk pytube
```

## How to Use

1. Run the script.
2. Browse and select the destination folder.
3. Enter the YouTube playlist link.
4. Click the "Generate" button.
5. Wait for the script to create folders, text files, and download videos.
6. Check the status label for completion.

## Important Note

Ensure you have a valid YouTube Data API key to extract playlist information. Replace the placeholder key in the script with your own.

```python
"key": "YOUR_API_KEY_HERE"
```

## Credits

- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [Pytube](https://python-pytube.readthedocs.io/en/latest/)
