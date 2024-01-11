from pydub import AudioSegment, silence
import os

def segment_audio(file_path, output_dir, min_silence_len=1000, silence_thresh=-35):
    """
    Segments the audio file into individual strums and saves them as separate files.

    :param file_path: Path to the input WAV file.
    :param output_dir: Directory to save the segmented audio files.
    :param min_silence_len: Minimum length of silence between strums in milliseconds.
    :param silence_thresh: Silence threshold in dBFS.
    """
    # Load the audio file
    audio = AudioSegment.from_wav(file_path)

    # Split audio based on silence
    audio_chunks = silence.split_on_silence(
        audio,
        min_silence_len=min_silence_len,
        silence_thresh=silence_thresh
    )

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Save each chunk as a separate file
    for i, chunk in enumerate(audio_chunks):
        chunk_name = f"strum{i+1}.wav"
        chunk_path = os.path.join(output_dir, chunk_name)
        chunk.export(chunk_path, format="wav")
        print(f"Saved: {chunk_path}")

    print(f"Total strums segmented: {len(audio_chunks)}")

# Example usage
segment_audio("your_file_path_here", "your_output_directory_here")
# Note: Replace "path_to_your_file.wav" with the path to your audio file and "output_directory" with your desired output directory.
