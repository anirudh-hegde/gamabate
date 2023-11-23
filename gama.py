import speech_recognition as sr
import pywhatkit as pw


def speech_2_text():
    while True:
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            print("Say something:")
            recognizer.adjust_for_ambient_noise(source)

            audio = recognizer.listen(source)
            print("audio record successful")
            try:
                print("transcribing..")

                text = recognizer.recognize_google(audio)

                # print(text)
                if text.lower() == "exit":
                    break
                text_save_type = input("enter the destination you want write(txt/gmail): ")
                if text_save_type == "txt":
                    with open("freshie.txt", "a") as f:
                        f.write(text + "\n")
                elif text_save_type == "gmail":
                    pw.send_mail("sender-email", "sender-pswd",
                                 "message", text, "receiver-email")

            except sr.UnknownValueError:
                print("unable to understand the audio")


if __name__ == "__main__":
    speech_2_text()
