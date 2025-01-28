# YouTube Media Downloader

A Python script to download YouTube videos, playlists, or entire channels with customizable quality options.

## Features
- Download single videos, playlists, or entire channels.
- Choose from multiple quality options:
  - Best quality (video + audio)
  - 1080p
  - 720p
  - 480p
  - Audio only (best quality)
- Automatically merges video and audio streams (requires `ffmpeg`).
- Saves downloads in the `downloads` folder.

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
   Select the desired quality:
   1. Best quality (video + audio)
   2. 1080p
   3. 720p
   4. 480p
   5. Audio only (best quality)
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
