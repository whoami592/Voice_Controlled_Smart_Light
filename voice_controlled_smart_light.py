import speech_recognition as sr
import pyfiglet
import sys

# Function to display stylish banner
def display_banner():
    banner = pyfiglet.figlet_format("Smart Light Control", font="slant")
    credit = pyfiglet.figlet_format("By Mr. Sabaz Ali Khan", font="small")
    print(banner)
    print(credit)
    print("Pakistani Ethical Hacker | Email: Sabazali236@gmail.com\n")

# Simulated function to control smart light
def control_light(command):
    if "turn on the light" in command.lower():
        print("Smart Light: Turning ON")
        # Replace with actual smart light API call, e.g., Philips Hue
        # Example: hue_api.turn_on()
        return "Light turned on"
    elif "turn off the light" in command.lower():
        print("Smart Light: Turning OFF")
        # Replace with actual smart light API call
        # Example: hue_api.turn_off()
        return "Light turned off"
    else:
        print("Command not recognized. Say 'turn on the light' or 'turn off the light'.")
        return "Unrecognized command"

# Initialize speech recognizer
recognizer = sr.Recognizer()

# Main function to process voice commands
def voice_control():
    display_banner()
    print("Starting Voice-Controlled Smart Light System...")
    print("Say 'turn on the light' or 'turn off the light'. Say 'exit' to quit.\n")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for command...")
                recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                
                # Convert speech to text
                command = recognizer.recognize_google(audio)
                print(f"You said: {command}")

                # Check for exit command
                if "exit" in command.lower():
                    print("Exiting Smart Light Control System.")
                    break

                # Process light control command
                result = control_light(command)
                print(f"Result: {result}\n")

        except sr.WaitTimeoutError:
            print("No speech detected. Please try again.\n")
        except sr.UnknownValueError:
            print("Could not understand audio. Please try again.\n")
        except sr.RequestError as e:
            print(f"Error with speech recognition service: {e}\n")
        except KeyboardInterrupt:
            print("\nProgram interrupted. Exiting.")
            break
        except Exception as e:
            print(f"An error occurred: {e}\n")

if __name__ == "__main__":
    try:
        voice_control()
    except Exception as e:
        print(f"Fatal error: {e}")
        sys.exit(1)