import sys
import platform
import pyperclip
from google import genai

def readInput():
    text = ''
    for word in sys.argv[1:]:
        text += f' {word}'

    return text

def aiInit():

    client = genai.Client()
    current_os = platform.system()
    if current_os == "Linux":
        os_info = platform.freedesktop_os_release()
        os_name = os_info.get('NAME')
        current_os = f"{current_os} {os_name}"

    aiCall = f"""You are a Command Line Interface generator.
    Target Operating System: {current_os}
    Your task is to translate the user's natural language request into the correct command for this OS.

    Rules:
    1. Output ONLY the command.
    2. Do NOT use markdown formatting (no backticks).
    3. Do NOT include any explanations, notes, or extra text.
    4. If the user asks for a dangerous operation, output the command commented out with #.
    5. If the request is unrelated to terminal commands, ask the user to redefine his prompt and try again.
    User Request: {readInput()}
    """ 
    
    text = readInput()
    if text == '':
        return 
    final_prompt = aiCall.format(user_input=text)

    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=final_prompt
    )
    print(response.text)
    
    if response.text == "Please redefine your prompt and try again.":
        exit()

    while True:
        print("Copy this command? [y/n]",end='', flush=True)
        c = input()
        
        if c=='y':
            pyperclip.copy(response.text)
            break
        elif c=='n':
            break
        else:
            print("Select [y/N] \n" )


if __name__ == '__main__':
    aiInit()
