import os
from youtube_transcript_api import YouTubeTranscriptApi
import requests

def get_youtube_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return transcript
    except Exception as e:
        print(f"An error occurred while fetching the transcript: {str(e)}")
        return None

def format_transcript(transcript):
    return ' '.join([entry['text'] for entry in transcript])

def summarize_with_ollama(text, model="llama3.1"):
    API_URL = "http://192.168.1.171:11434/api/generate"
    
    payload = {
        "model": model,
        "prompt": f"Please summarize the following text and create bullets of topics:\n\n{text}\n\nSummary:",
        "stream": False
    }
    
    try:
        response = requests.post(API_URL, json=payload)
        response.raise_for_status()
        return response.json()['response']
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while summarizing: {str(e)}")
        return None

def display_full_transcript(transcript):
    for entry in transcript:
        print(f"[{entry['start']:.2f}s] {entry['text']}")

def export_transcript_to_file(transcript, video_id):
    filename = f"{video_id}_transcript.txt"
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for entry in transcript:
                file.write(f"[{entry['start']:.2f}s] {entry['text']}\n")
        print(f"Transcript exported successfully to {filename}")
    except IOError as e:
        print(f"An error occurred while exporting the transcript: {str(e)}")

def main():
    video_url = input("Enter the YouTube video URL: ")
    video_id = video_url.split("v=")[1]
    
    transcript = get_youtube_transcript(video_id)
    if transcript:
        while True:
            choice = input("\nEnter 's' for summary, 'f' for full transcript, 'e' to export transcript, or 'q' to quit: ").lower()
            
            if choice == 's':
                formatted_transcript = format_transcript(transcript)
                summary = summarize_with_ollama(formatted_transcript)
                if summary:
                    print("\nSummary:")
                    print(summary)
                else:
                    print("Failed to generate summary.")
            elif choice == 'f':
                print("\nFull Transcript:")
                display_full_transcript(transcript)
            elif choice == 'e':
                export_transcript_to_file(transcript, video_id)
            elif choice == 'q':
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Failed to fetch transcript.")

if __name__ == "__main__":
    main()
