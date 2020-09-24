from tkinter import messagebox
from PIL import Image, ImageTk
import random

def buttonTrainFuntion():
    messagebox.showinfo(message="Modelo entrenado", title="Estado")


def buttonTestFuntion():
    accuracy = "90" #TODO:REEMPLAZAR POR ACCURACY DEL MODELO
    messagebox.showinfo(message="Modelo testeado\nAccuracy: " + accuracy+"%", title="Estado")

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


def buttonPredictFunction(labelResultadoEmocion, labelEmotionImage):
    labelResultadoEmocion.place(x = 270, y = 70 , width=180, height=40)
    labelEmotionImage.place(x = 271, y = 121, width=178, height=208)
    
    #TODO: OBTENER LA PREDICCIÓN:'neutral','calm','happy','sad','angry','fearful','disgust','surprised'
    prediction = random.choice(['sad','angry','happy','fearful','disgust','calm','surprised','neutral'])

    labelResultadoEmocion.configure(text=prediction)
    emotionImage = ImageTk.PhotoImage(Image.open("resources/emotions/" + prediction + ".png").resize((170, 200), Image.ANTIALIAS))
    labelEmotionImage.configure(image=emotionImage)
    labelEmotionImage.image = emotionImage

def buttonPlayFunction():
    pass

def buttonPauseFunction():
    pass



