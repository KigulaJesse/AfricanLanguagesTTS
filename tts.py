import pyttsx3

# Initialize the engine
engine = pyttsx3.init()

# Adjust speaking rate
rate = engine.getProperty('rate')
print(f'Current speaking rate: {rate}')
engine.setProperty('rate', 125)

# Adjust volume
volume = engine.getProperty('volume')
print(f'Current volume level: {volume}')
engine.setProperty('volume', 1.0)

# Change voice
voices = engine.getProperty('voices')
print(f'Current volume level: {voices}')
engine.setProperty('voice', voices[1].id)  # Selecting a female voice

# Make the engine speak
engine.say("Hello World!")
# engine.say(f'My current speaking rate is {rate}')
engine.runAndWait()

# Save to a file
engine.save_to_file('Hello World', 'test.mp3')
engine.runAndWait()

# Stop the engine
engine.stop()