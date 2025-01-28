from yt_dlp import YoutubeDL

def download_media(url, quality):
    # Options for downloading
    ydl_opts = {
        'format': quality,  # Use the selected quality
        'outtmpl': 'downloads/%(title)s.%(ext)s',  # Save files in the 'downloads' folder
        'quiet': False,  # Show progress and logs
        'merge_output_format': 'mp4',  # Merge video and audio into mp4
        'ignoreerrors': True,  # Ignore errors and continue downloading
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',  # Ensure the final format is mp4
        }],
    }

    # Create a YoutubeDL object
    with YoutubeDL(ydl_opts) as ydl:
        try:
            print("Starting download...")
            ydl.download([url])  # Download the media (video, playlist, or channel)
            print("Download complete!")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Ask the user to input a video, playlist, or channel link
    user_input = input("Enter the YouTube video, playlist, or channel link: ").strip()

    # Validate the input
    if not user_input:
        print("No link provided. Exiting.")
    elif "youtube.com" not in user_input and "youtu.be" not in user_input:
        print("Invalid YouTube link. Please provide a valid YouTube link.")
    else:
        # Ask the user to select the quality
        print("Select the desired quality:")
        print("1. Best quality (video + audio)")
        print("2. 1080p")
        print("3. 720p")
        print("4. 480p")
        print("5. Audio only (best quality)")
        quality_choice = input("Enter your choice (1-5): ").strip()

        # Map the user's choice to the corresponding yt-dlp format
        quality_map = {
            '1': 'bestvideo+bestaudio/best',
            '2': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
            '3': 'bestvideo[height<=720]+bestaudio/best[height<=720]',
            '4': 'bestvideo[height<=480]+bestaudio/best[height<=480]',
            '5': 'bestaudio',
        }

        if quality_choice in quality_map:
            quality = quality_map[quality_choice]
            print(f"Selected quality: {quality}")
            # Start the download process
            download_media(user_input, quality)
        else:
            print("Invalid choice. Exiting.")
