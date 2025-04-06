# 🎥 Simple YouTube Video Downloader

A simple GUI-based YouTube video downloader built with Python, Tkinter, and `yt_dlp`. It allows users to download videos by pasting a link directly into the interface.

## 🛠 Features
- Download YouTube videos in MP4 format.
- Basic GUI built using Tkinter.
- Status messages for success or common errors (like age-restricted videos).
- Optional checkboxes for resolution selection (placeholders for future implementation).

### Prerequisites

Make sure you have the following installed:
- Python 3.13
- [`yt-dlp`](https://github.com/yt-dlp/yt-dlp)
To install `yt-dlp`, run:
pip install yt-dlp

#### ⚙️ Current Limitations

Resolution checkboxes (360p, 720p, 1080p) are not yet functional.

The output path is hardcoded to my system so you may want to change this path in the script (ydl_opts['outtmpl']) to match your system.

No error logging or advanced settings (like audio-only, playlists, or cookies for age-restricted content).

📌 TODO
- Make resolution selection functional.
- Add support for custom download paths.
- Improve error handling and display.

🤖 Author

Developed by Fatih Efe Ünal
