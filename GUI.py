from tkinter import *
from pydub.silence import split_on_silence
from pydub import AudioSegment
from tkinter import filedialog

# define the function that is called when the submit button is pressed


def process_audio():
    # get the input file path from the entry widget
    input_file_path = input_entry.get()

    # load audio file
    audio_file = AudioSegment.from_wav(input_file_path)

    # split audio on silence
    chunks = split_on_silence(
        audio_file, min_silence_len=500, silence_thresh=-40)

    # combine non-silent chunks
    combined_audio = AudioSegment.empty()
    for chunk in chunks:
        combined_audio = combined_audio.append(chunk, crossfade=0)

    # export output file
    combined_audio.export("output.wav", format="wav")


# create the main window of the GUI
window = Tk()
window.geometry("400x100")
window.title("My Application")
window.configure(bg='black')
window.title("Remove Silence from Audio")

# create a label and entry widget for the input file path
input_label = Label(window, text="Input File Path: ", fg='white', bg='black')
input_label.place(relx=0.5, rely=0.2, anchor='center')
input_entry = Entry(window, bg='grey')
input_entry.place(relx=0.5, rely=0.5, anchor='center')
input_button = Button(window, text="Browse", bg='black', fg='white', command=lambda: input_entry.insert(
    0, filedialog.askopenfilename()), highlightthickness=0, relief="flat")
input_button.place(relx=0.75, rely=0.5, anchor='center')

# create a button to submit the input file
submit_button = Button(window, text="Submit", bg='black',
                    fg='white', command=process_audio, highlightthickness=0, relief="flat")
submit_button.place(relx=0.5, rely=0.8, anchor='center')

# run the main loop of the GUI
window.mainloop()
