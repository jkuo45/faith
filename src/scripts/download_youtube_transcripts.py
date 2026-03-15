from youtube_transcript_api import YouTubeTranscriptApi
import re

def get_yt_id(url):
    if not url:
        return None
    match = re.search(r'(?:v=|youtu\.be/|embed/|v/|shorts/|live/)([a-zA-Z0-9_-]{11})', url)
    return match.group(1) if match else None

def main():
    url = input("Enter Youtube url: ")
    video_id = get_yt_id(url)
    output_file_dir = f".output/transcript_{video_id}.txt"

    if video_id:
        try:
            yttapi = YouTubeTranscriptApi()
            transcript_list = yttapi.fetch(video_id, languages=["en"])
            transcript_text = " ".join([entry.text for entry in transcript_list])
            print(transcript_text[:100])
            with open(output_file_dir, "w") as f:
                f.write(transcript_text)
                print("Successfully downloaded transcript")
        except Exception as e:
            print(f"Error fetching transcript: {e}")

if __name__ == "__main__":
    main()