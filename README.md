# YouTube Media Downloader

A Python script to download full YouTube channels, playlists, or single videos effortlessly.

## Features
- **Download videos, playlists, or entire channels** from YouTube.
- **Supports multiple quality options**:
  - Best quality (video + audio)
  - 1080p
  - 720p
  - 480p
  - Audio-only (MP3 format available).
- **Automatically organizes downloaded files** into folders based on the uploader or playlist title.
- **Error handling** to ensure smooth downloading even for problematic links.

## Table of Contents
1. [General Information](#general-information)
2. [Technologies Used](#technologies-used)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Contribution Guidelines](#contribution-guidelines)
6. [License](#license)
7. [Support](#support)

## General Information
This project leverages the powerful **yt-dlp** library to provide a seamless experience for downloading YouTube content. Whether you need videos for offline viewing or audio files for your playlist, this tool simplifies the process with an intuitive interface.

### Project Status
**Active**: The project is actively maintained, and new features are being added periodically.

## Technologies Used
- **Python**: Version 3.7+
- **yt-dlp**: A command-line program to download videos from YouTube and other platforms.
- **FFmpeg**: For audio conversion and video processing.

## Prerequisites
Before using this script, ensure you have the following installed:
1. **Python 3.x**: Download and install Python from [python.org](https://www.python.org/downloads/).
2. **ffmpeg**: Required for merging video and audio streams.
   - On Windows: Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add it to your system's PATH.
   - On macOS: Install via Homebrew: `brew install ffmpeg`.
   - On Linux: Install via your package manager, e.g., `sudo apt install ffmpeg`.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/youtube-media-downloader.git
   cd youtube-media-downloader
   ```
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the script:
   ```bash
   python downloader.py
   ```
2. Enter the YouTube video, playlist, or channel link when prompted.
3. Select the desired quality option:
   ```
   1. Best quality (video + audio)
2. 1080p
3. 720p
4. 480p
5. Audio only (MP3 format)
Enter your choice (1-5): 5
Starting download...
Download complete!
   ```
4. The downloaded files will be saved in the `downloads` folder.

## Example
```bash
$ python downloader.py
Enter the YouTube video, playlist, or channel link: https://www.youtube.com/watch?v=example
Select the desired quality:
1. Best quality (video + audio)
2. 1080p
3. 720p
4. 480p
5. Audio only (best quality)
Enter your choice (1-5): 1
Starting download...
Download complete!
```

## Folder Structure
```
youtube-media-downloader/
├── downloads/                  # Downloaded files are saved here
├── downloader.py               # Main script
├── README.md                   # This file
└── requirements.txt            # List of dependencies
```

## Dependencies
- [yt-dlp](https://github.com/yt-dlp/yt-dlp): A feature-rich command-line program to download videos from YouTube and other sites.
- [ffmpeg](https://ffmpeg.org/): For merging video and audio streams.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
