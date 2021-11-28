import pandas as pd
import librosa as ros



def load_wav(filename: str):
    clip,sr = ros.load(filename,sr=None)
    for i in (clip[:132300]):
        print(i)



if __name__ == "__main__":

    load_wav("data/nsynth-test/audio/guitar_acoustic_014-046-075.wav")

