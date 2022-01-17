import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
voiceFemales = filter(lambda v: v.gender == 'VoiceGenderFemale', voices)
for v in voices:
    engine.setProperty('voice', v.id)
    print(v.id)
    engine.say('Hello world from ' + v.name)
    engine.runAndWait()
