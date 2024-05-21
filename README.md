This is something I created to simplify the process of creating a dataset of guitarchords for my chord-recognition model. 
Instead of having to record each chord individually (which takes forever), with this script you can press play and 
strum as long as you like, and when running the script it will automatically crop out all the chords, therefor reducing
the time to collect chords significantly. 

Uses a volume threshold to determine where to slice. So optimally strum a chord and let it ring out to silence before strumming again. 
