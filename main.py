import time
from replit import audio 

def play_note(note, duration, volume=1):
    note_to_freq = {
        "C": 262, "D": 294, "E": 330, "F": 349, "G": 392, "A": 440
    }
    audio.play_tone(duration, note_to_freq[note], 0, volume=volume)
    time.sleep(duration)


notes = ["C", "C", "G", "G", "A", "A", "G", "F", "F", "E", "E", "D", "D", "C"]
durations = [2, 2, 2, 2, 2, 2, 4, 2, 2, 2, 2, 2, 2, 4]

volume = 1
for i in range(len(notes)):
    volume -= 0.05
    play_note(notes[i], durations[i], volume=volume)


