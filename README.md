Transcript and Summary Generator from YouTube Video
======================================================

A Python script that retrieves the transcript of a YouTube video, formats it into plain text, and uses an Ollama model to summarize the content.

Features
--------

* Fetches the transcript of a YouTube video using the `youtube_transcript_api`
* Formats the transcript into plain text for easier reading
* Uses an Ollama model to summarize the content
* Exports the full transcript to a file (optionally)
* Provides options to view the summary, full transcript, or export the transcript

Requirements
------------

* Python 3.8+
* `youtube_transcript_api` library (`pip install youtube-transcript-api`)
* `requests` library (`pip install requests`)
* Ollama model API running on `http://localhost:11434/api/generate`

Usage
-----

1. Clone this repository to your local machine.
2. Install the required libraries using pip.
3. Run the script by executing `python main.py`.
4. Enter the YouTube video URL when prompted.
5. Choose from the following options:
	* `s`: View summary and bullets of topics
	* `f`: View full transcript
	* `e`: Export full transcript to a file
	* `q`: Quit

Note: Make sure you have the Ollama model API running on your machine for this script to work.

API Documentation
-----------------

If you're interested in integrating this script with another application, here's a brief overview of the APIs used:

### YouTube Transcript API

The `youtube_transcript_api` library is used to fetch the transcript of a YouTube video. This API requires no authentication and provides a simple way to retrieve transcripts.

### Ollama Model API

The Ollama model API is used to summarize the content of the transcript. This API runs on your local machine (or can be deployed elsewhere) and expects a JSON payload with a prompt, model, and other parameters.

License
-------

This script is released under the MIT License. See LICENSE for details.

Contributing
------------

If you'd like to contribute to this project or suggest improvements, please feel free to open an issue or submit a pull request!