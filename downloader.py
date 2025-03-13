from yt_dlp import YoutubeDL
import os

def download_media(url, quality, output_format):
    # Fetch metadata to determine if it's a playlist or single video
    metadata = get_metadata(url)
    if not metadata:
        print("Failed to fetch metadata. Exiting.")
        return

    # Determine the folder name
    if 'entries' in metadata:  # It's a playlist
        folder_name = metadata.get('title', 'Unknown_Playlist')
    else:  # It's a single video
        folder_name = metadata.get('uploader', 'Unknown_Channel')

    # Create the folder if it doesn't exist
    folder_path = os.path.join('downloads', folder_name)
    os.makedirs(folder_path, exist_ok=True)

    # Options for downloading
    ydl_opts = {
        'format': quality,  # Use the selected quality
        'outtmpl': os.path.join(folder_path, '%(playlist_index)s - %(title)s.%(ext)s'),  # Save files with numbering
        'quiet': False,  # Show progress and logs
        'merge_output_format': output_format,  # Merge video and audio into the desired format
        'ignoreerrors': True,  # Ignore errors and continue downloading
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',  # Convert to MP3 if output format is audio-only
            'preferredquality': '192',  # Set MP3 quality (192 kbps)
        }] if output_format == 'mp3' else []
    }

    # Create a YoutubeDL object
    with YoutubeDL(ydl_opts) as ydl:
        try:
            print("Starting download...")
            ydl.download([url])  # Download the media (video, playlist, or channel)
            print("Download complete!")
        except Exception as e:
            print(f"An error occurred: {e}")

def get_metadata(url):
    # Options for extracting metadata
    ydl_opts = {
        'quiet': True,  # Suppress output
        'extract_flat': True,  # Extract metadata without downloading
    }

    # Create a YoutubeDL object
    with YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(url, download=False)
            return info
        except Exception as e:
            print(f"An error occurred while fetching metadata: {e}")
            return None

if __name__ == "__main__":
    # Ask the user to input a video, playlist, or channel link
    user_input = input("Enter the YouTube video, playlist, or channel link: ").strip()
    
    # Validate the input
    if not user_input:
        print("No link provided. Exiting.")
    elif "youtube.com" not in user_input and "youtu.be" not in user_input:
        print("Invalid YouTube link. Please provide a valid YouTube link.")
    else:
        # Ask the user to select the quality and format
        print("Select the desired quality:")
        print("1. Best quality (video + audio)")
        print("2. 1080p")
        print("3. 720p")
        print("4. 480p")
        print("5. Audio only (best quality)")
        print("6. Audio only (MP3 format)")
        
        quality_choice = input("Enter your choice (1-6): ").strip()

        # Map the user's choice to the corresponding yt-dlp format and output format
        quality_map = {
            '1': ('bestvideo+bestaudio/best', 'mp4'),
            '2': ('bestvideo[height<=1080]+bestaudio/best[height<=1080]', 'mp4'),
            '3': ('bestvideo[height<=720]+bestaudio/best[height<=720]', 'mp4'),
            '4': ('bestvideo[height<=480]+bestaudio/best[height<=480]', 'mp4'),
            '5': ('bestaudio', 'mp4'),
            '6': ('bestaudio', 'mp3'),
        }

        if quality_choice in quality_map:
            quality, output_format = quality_map[quality_choice]
            print(f"Selected quality: {quality}, Output format: {output_format}")
            
            # Start the download process
            download_media(user_input, quality, output_format)
        else:
            print("Invalid choice. Exiting.")
