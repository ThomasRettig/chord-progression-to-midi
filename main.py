import os
import pretty_midi
from pychord import ChordProgression
from showinfm import show_in_file_manager

HORIZONTAL_DIVIDER = "---------------------------"

def show_file():
    open_prompt = input("\33[97mShow output in file explorer? (y/n) \033[00m")
    while open_prompt != "y" and open_prompt != "n":
        open_prompt = input("\33[91mInvalid input. Please enter \"y\" or \"n\": \033[00m")
    if open_prompt == "y":
        show_in_file_manager(f"{os.path.abspath(os.curdir)}/{file_name}")

def create_midi(chords):
    file_name = "chords.mid"
    midi_data = pretty_midi.PrettyMIDI()
    
    # ask user to choose instrument
    instrument_names = pretty_midi.program_to_instrument_name.values()
    print("\n".join([f"{i + 1}. {name}" for i, name in enumerate(instrument_names)]))
    instr_num = int(input("\n\33[97mChoose an instrument by number (default 1): \033[00m") or "1") - 1
    instr_name = instrument_names[instr_num]
    instr_program = pretty_midi.instrument_name_to_program(instr_name)
    
    # create instrument object
    instr = pretty_midi.Instrument(program=instr_program)
    length = 1
    
    for n, chord in enumerate(chords):
        for note_name in chord.components_with_pitch(root_pitch=4):
            note_number = pretty_midi.note_name_to_number(note_name)
            note = pretty_midi.Note(velocity=100, pitch=note_number, start=n * length, end=(n + 1) * length)
            instr.notes.append(note)
    midi_data.instruments.append(instr)
    midi_data.write(file_name)
    print(f"\033[1;32;40mSuccesfully generated {file_name} \U0001F389 \033[00m\n\33[90m{HORIZONTAL_DIVIDER}")
    show_file()

def main():
    cp = ChordProgression(input("\33[97mEnter chord progression: \033[93m").split())
    print(f"\33[90m{HORIZONTAL_DIVIDER}")
    for chord in cp:
        print(f"\033[93m{chord}\33[97m — {chord.components()}\033[00m")
    create_midi(cp)

if __name__ == "__main__":
    main()
