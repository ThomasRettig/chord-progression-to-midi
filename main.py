import os
import pretty_midi
from pychord import ChordProgression
from showinfm import show_in_file_manager

HORIZONTAL_DIVIDER = "---------------------------"

def create_midi(chords):
    file_name = "chords.mid"
    midi_data = pretty_midi.PrettyMIDI()
    piano_program = pretty_midi.instrument_name_to_program("Acoustic Grand Piano")
    piano = pretty_midi.Instrument(program=piano_program)
    length = 1
    
    for n, chord in enumerate(chords):
        for note_name in chord.components_with_pitch(root_pitch=4):
            note_number = pretty_midi.note_name_to_number(note_name)
            note = pretty_midi.Note(velocity=100, pitch=note_number, start=n * length, end=(n + 1) * length)
            piano.notes.append(note)
    midi_data.instruments.append(piano)
    midi_data.write(file_name)
    print(f"\033[1;32;40mSuccesfully generated {file_name} \U0001F389 \033[00m\n\33[90m{HORIZONTAL_DIVIDER}")
    open_prompt = input("\33[97mShow output in file explorer? (y/n) \033[00m")
    while open_prompt != "y" and open_prompt != "n":
        open_prompt = input("\33[91mInvalid input. Please enter \"y\" or \"n\": \033[00m")
    if open_prompt == "y":
        show_in_file_manager(f"{os.path.abspath(os.curdir)}/{file_name}")

def main():
    cp = ChordProgression(input("\33[97mEnter chord progression: \033[93m").split())
    print(f"\33[90m{HORIZONTAL_DIVIDER}")
    for chord in cp:
        print(f"\033[93m{chord}\33[97m — {chord.components()}\033[00m")
    create_midi(cp)

if __name__ == '__main__':
    main()
