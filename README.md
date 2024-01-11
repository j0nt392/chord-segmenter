README: 

This audio-segmentation tool helps to create a dataset for a chord-recognition model, or to simply slice audio-files. 
Adjust min_silence_len and min_silence_threshold for a desired effect. 

Example usage: 
Record yourself playing guitar-strums. Let each strum ring out before strumming again. The script checks for volume threshold 
in the audiofile, so once each chord fades out the script will extract that chord and export it into your destination folder. 
