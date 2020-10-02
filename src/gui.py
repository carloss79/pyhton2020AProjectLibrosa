from tkinter import Frame, Label, Tk, Button, Toplevel, Entry, filedialog, messagebox
from PIL import Image, ImageTk
from funcionalidad import *

ruta="ruta"
def browsecsv():    
    file = filedialog.askopenfile(parent=root,mode='rb',title='Choose a file')
    print(file)
    global ruta
    ruta = file.name

root = Tk() 
root.title("EMOGNITION") 
root.resizable(False, False)
root.geometry("490x380") 

font = ("Comic Sans")

labelMuestraText = Label(text ="MUESTRA", font=("Times New Roman", 15)) 
labelMuestraText.place(x = 20, y = 10 , width=200, height=20)

labelMuestraBackground = Label(text ="",  bg="lightgrey", borderwidth=2, relief="solid") 
labelMuestraBackground.place(x = 20, y = 30 , width=200, height=100)

bbutton= Button(root, text="File Browser",command=browsecsv)
bbutton.place(x = 30, y = 40 , width=180, height=20)

audioIcon = ImageTk.PhotoImage(Image.open("../resources/audio.png").resize((60, 60), Image.ANTIALIAS))
labelAudioIcon = Label(image = audioIcon,  bg="lightgrey") 
#labelAudioIcon.place(x = 30, y = 50 , width=60, height=60)

labelAudioText = Label(text ="Audio recorder", bg="lightgrey", font=("Times New Roman", 12)) 
#labelAudioText.place(x = 100, y = 50 , width=110, height=60)

labelRecordingText = Label(text ="Recording...", bg="lightgrey", font=("Times New Roman", 15)) 
#labelRecordingText.place(x = 30, y = 50 , width=180, height=60)




stopIcon = ImageTk.PhotoImage(Image.open("../resources/stop.png").resize((30, 30), Image.ANTIALIAS))
buttonStop = Button(image = stopIcon, bg="lightgrey",
                    command=lambda:buttonStopFunction(labelAudioIcon,labelAudioText,labelRecordingText))
buttonStop.place(x = 73, y = 150 , width=40, height=40)

playIcon = ImageTk.PhotoImage(Image.open("../resources/play.png").resize((30, 30), Image.ANTIALIAS))
buttonPlay = Button(image = playIcon, bg="lightgrey",
                    command=lambda:buttonPlayFunction(ruta))
buttonPlay.place(x = 126, y = 150 , width=40, height=40)

pauseIcon = ImageTk.PhotoImage(Image.open("../resources/pause.png").resize((30, 30), Image.ANTIALIAS))
buttonPause = Button(image = pauseIcon, bg="lightgrey",
                    command=lambda:buttonPauseFunction())
buttonPause.place(x = 180, y = 150 , width=40, height=40)

buttonTrain = Button(text="Train", bg="#207863", font = ("Times New Roman", 15, "bold"),
                    command=lambda:buttonTrainFuntion())
buttonTrain.place(x = 20, y = 220 , width=200, height=30)

buttonTest = Button(text="Test", bg="#207863", font = ("Times New Roman", 15, "bold"),
                    command=lambda:buttonTestFuntion())
buttonTest.place(x = 20, y = 270 , width=200, height=30)



labelResultadoText = Label(text ="RESULT", font=("Times New Roman", 15)) 
labelResultadoText.place(x = 250, y = 10 , width=220, height=20)

labelResultadoBackground = Label(text ="",  bg="lightgrey", borderwidth=2, relief="solid") 
labelResultadoBackground.place(x = 250, y = 30 , width=220, height=320)

labelEmocionText = Label(text ="Emotion", bg="lightgrey", font=("Times New Roman", 10)) 
labelEmocionText.place(x = 270, y = 50 , width=180, height=20)

labelResultadoEmocion = Label(bg="lightgrey", font=("Times New Roman", 12), borderwidth=1, relief="solid") 
labelResultadoEmocion.place(x = 270, y = 70 , width=180, height=40)

labelImageResultBackground = Label(bg="lightgrey", borderwidth=1, relief="solid") 
labelImageResultBackground.place(x = 270, y = 120 , width=180, height=210)

emotionImage = ImageTk.PhotoImage(Image.open("../resources/emotions/sad.png").resize((170, 200), Image.ANTIALIAS))
labelEmotionImage = Label(bg="lightgrey") 
labelEmotionImage.place(x = 271, y = 121, width=178, height=208)

buttonPredict = Button(text="Predict", bg="#207863", font = ("Times New Roman", 15, "bold"),
                        command=lambda:buttonPredictFunction(labelResultadoEmocion, labelEmotionImage,ruta))
buttonPredict.place(x = 20, y = 320 , width=200, height=30)

recordIcon = ImageTk.PhotoImage(Image.open("../resources/record.png").resize((30, 30), Image.ANTIALIAS))
buttonRecord = Button(image = recordIcon, bg="lightgrey",
                    command=lambda:buttonRecordFunction(labelAudioIcon,labelAudioText,labelRecordingText, labelResultadoEmocion, labelEmotionImage))
buttonRecord.place(x = 20, y = 150 , width=40, height=40)

root.mainloop() 