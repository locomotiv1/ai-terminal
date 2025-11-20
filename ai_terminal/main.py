import sys
import pyperclip
from google import genai

def readInput():
    text = ''
    for word in sys.argv[1:]:
        text += f' {word}'

    return text

def aiInit():

    client = genai.Client()
    
    aiCall = "You are a Linux command generator. Your only task is to translate the user's natural language request into the correct Linux command.\n" \
             "Rules:\n" \
             "1. Output ONLY the command.\n" \
             "2. Do NOT use markdown formatting (no backticks).\n" \
             "3. Do NOT include any explanations, notes, or extra text.\n" \
             "4. If the user asks for a dangerous operation, output the command commented out with #.\n" \
             "5. If the user types in a prompt that is unrelated to your scope of the project ask the user to redefine his prompt and try again \n" \
             "User Request: {user_input} \n" \
    
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
    print("Copy this command? [y/N]",end='', flush=True)
    c = input()

    if c=='y':
        pyperclip.copy(response.text)
    elif c=='n':
        exit()
    else:
        print("Select [y/N]")
        #TODO: Give choice once again without braking the program


if __name__ == '__main__':
    aiInit()
