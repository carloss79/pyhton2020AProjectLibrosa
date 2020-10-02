import librosa
import soundfile
import os, glob, pickle
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from tkinter import messagebox
from PIL import Image, ImageTk
import random

def prepareFile(ruta):
    x,y=[],[]
    for file in glob.glob(ruta):
        print(file)
        file_name=os.path.basename(file)
        emotion=emotions[file_name.split("-")[2]]
        feature=extract_feature(file, mfcc=True, chroma=True, mel=True)
        x.append(feature)
        y.append(emotion)
    return x,y

def load_data(test_size=0.2):
    x,y=[],[]
    for file in glob.glob("C:\\Users\\carlos\\gitKraken\\pyhton2020AProjectLibrosa\\resources\\data\\Actor_*\\*.wav"):
        file_name=os.path.basename(file)
        emotion=emotions[file_name.split("-")[2]]
        if emotion not in observed_emotions:
            continue
        feature=extract_feature(file, mfcc=True, chroma=True, mel=True)
        x.append(feature)
        y.append(emotion)
    
    return train_test_split(np.array(x), y, test_size=test_size, random_state=9)

#funcion para extraer data de un audio
def extract_feature(file_name, mfcc, chroma, mel):
    with soundfile.SoundFile(file_name) as sound_file:
        X = sound_file.read(dtype="float32")
        sample_rate=sound_file.samplerate
        if chroma:
            stft=np.abs(librosa.stft(X))
        result=np.array([])
        if mfcc:
            mfccs=np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T, axis=0)
            result=np.hstack((result, mfccs))
        if chroma:
            chroma=np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T,axis=0)
            result=np.hstack((result, chroma))
        if mel:
            mel=np.mean(librosa.feature.melspectrogram(X, sr=sample_rate).T,axis=0)
            result=np.hstack((result, mel))
        return result

emotions={
  '01':'neutral',
  '02':'calm',
  '03':'happy',
  '04':'sad',
  '05':'angry',
  '06':'fearful',
  '07':'disgust',
  '08':'surprised'
}
#DataFlair - Emotions to observe
#observed_emotions=['calm', 'happy', 'fearful', 'disgust','neutral','sad','angry','surprised']
observed_emotions=['calm', 'happy', 'fearful', 'disgust','neutral']

model=MLPClassifier(alpha=0.01, batch_size=256, epsilon=1e-08, hidden_layer_sizes=(300,), 
                        learning_rate='adaptive', max_iter=500)
x_train,x_test,y_train,y_test=load_data(test_size=0.25)


def buttonTrainFuntion():
    
    print((x_train.shape[0], x_test.shape[0]))
    print(f'Features extracted: {x_train.shape[1]}')
    global model
    model.fit(x_train,y_train)
    messagebox.showinfo(message="""Atributos del dataset: {}
    Tamaño del dataset de Entrenamiento: {}
    Tamaño del dataset de Prueba: {}                                
                        """.format(x_train.shape[1],x_train.shape[0], x_test.shape[0]),
                        title="Entrenamiento Finalizado")

def buttonTestFuntion():
    y_pred=model.predict(x_test)
    #DataFlair - Calculate the accuracy of our model
    accuracy=accuracy_score(y_true=y_test, y_pred=y_pred)
    #DataFlair - Print the accuracy
    print("Accuracy: {:.2f}%".format(accuracy*100))
    messagebox.showinfo(message="Modelo testeado\nSe obtuvo la siguiente precision\nAccuracy: {:.2f}%".format(accuracy*100), title="Testeo Finalizado")

def buttonRecordFunction(labelAudioIcon, labelAudioText, labelRecordingText, labelResultadoEmocion, labelEmotionImage):
    messagebox.showinfo(message="Presione ACEPTAR cuando esté listo para grabar", title="Grabación")
    labelResultadoEmocion.place_forget()
    labelEmotionImage.place_forget()
    labelAudioIcon.place_forget()
    labelAudioText.place_forget()
    labelRecordingText.place(x = 30, y = 50 , width=180, height=60)
    
    #TODO: INICIAR GRABACIÓN 

def buttonStopFunction(labelAudioIcon, labelAudioText, labelRecordingText):
    messagebox.showinfo(message="Presione ACEPTAR para finalizar la grabación", title="Grabación")
    labelRecordingText.place_forget()

    #TODO:FINALIZAR GRABACIÓN

    labelAudioIcon.place(x = 30, y = 50 , width=60, height=60)
    labelAudioText.place(x = 100, y = 50 , width=110, height=60)


def buttonPredictFunction(labelResultadoEmocion, labelEmotionImage,ruta):
    print(ruta)
    caracteristicas,emocionCorrecta=prepareFile(ruta)
    print(caracteristicas)
    print(emocionCorrecta)
    pred=model.predict(caracteristicas)
    print(pred)

    labelResultadoEmocion.place(x = 270, y = 70 , width=180, height=40)
    labelEmotionImage.place(x = 271, y = 121, width=178, height=208)
    
    #TODO: OBTENER LA PREDICCIÓN:'neutral','calm','happy','sad','angry','fearful','disgust','surprised'
    #prediction = random.choice(['sad','angry','happy','fearful','disgust','calm','surprised','neutral'])
    prediction = pred[0]

    labelResultadoEmocion.configure(text=prediction)
    emotionImage = ImageTk.PhotoImage(Image.open("../resources/emotions/" + prediction + ".png").resize((170, 200), Image.ANTIALIAS))
    labelEmotionImage.configure(image=emotionImage)
    labelEmotionImage.image = emotionImage
    
def buttonPlayFunction():
    pass

def buttonPauseFunction():
    pass
