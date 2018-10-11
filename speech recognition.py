from pocketsphinx import LiveSpeech
#print live speech (heard from microphone) on console
for phrase in LiveSpeech(): 
	print(phrase)
