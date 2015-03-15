from JSB2 import song

## create a new song with default settings
song1 = song()

## create a new song with one or more user-defined parameters
# song1 = song(rand_seed=1000, tempo=90, divs_per_beat=8, beats_per_bar=3, key='C', structure=['verse','chorus'])

## NOTE:
## the rand_seed is in the name of all files,
## if you want to save the audio of a song you listened to but didn't save, you can regenerate the song using that rand_seed

## HERE ARE 5 THINGS YOU CAN DO WITH THE song INSTANCE
## 1) save the midi file
# song1.write_midi()
## 2) save the FluidSynth script
# song1.write_fs_script() 
## 3) save the audio in .raw format (also saves the midi file and FluidSynth script)
# song1.write_raw_audio()
## 4) convert the .raw audio file to .wav format. Need SoX installed for this
# song1.convert_raw_to_wav()
## 5) play the audio with FluidSynth (also saves the midi file and FluidSynth script)
song1.play_audio_fs()

