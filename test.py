import pyaudio
import wave

WAVE_OUTPUT_FILENAME = "sample.wav" #音声を保存するファイル名
iDeviceIndex = 0 #録音デバイスのインデックス番号

def MakeWavFile(FileName = "sample.wav", Record_Seconds = 2):
    chunk = 1024
    FORMAT = pyaudio.paInt16

    CHANNELS = 1 #モノラル
    RATE = 44100 #サンプルレート（録音の音質）

    p = pyaudio.PyAudio()

    stream = p.open(format = FORMAT,
                    channels = CHANNELS,
                    rate = RATE,
                    input = True,
                    frames_per_buffer = chunk)

    #レコード開始
    print("Now Recording...")
    all = []
    for i in range(0, int(RATE / chunk * Record_Seconds)):
        data = stream.read(chunk) #音声を読み取って、
        all.append(data) #データを追加

    #レコード終了
    print("Finished Recording.")

    stream.close()
    p.terminate()
    wavFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wavFile.setnchannels(CHANNELS)
    wavFile.setsampwidth(p.get_sample_size(FORMAT))
    wavFile.setframerate(RATE)
    # wavFile.writeframes(b''.join(all)) #Python2 用
    wavFile.writeframes(b"".join(all)) #Python3用

    wavFile.close()


# if __name__ is "__main__":
#     #WAVファイル作成, 引数は（ファイル名, 録音する秒数）
#     MakeWavFile("sample.wav", Record_Seconds = 2)


# MakeWavFile("sample.wav", Record_Seconds = 5)
