from dotenv import load_dotenv
load_dotenv()

import openai
import os
from colorama import Fore

openai.api_key = os.getenv('API_KEY')

def colored_print(text, color):
    print(color + text)

def generate_response(role, content, messages, model="gpt-4", max_tokens=1500, temperature=None, color=None):
    messages.append({"role": role, "content": content})
    response_content = ""
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            max_tokens=max_tokens,
            temperature=temperature,
            stream=True
        )
        for resp in response:
            chunk_content = resp.get('choices', [{}])[0].get('delta', {}).get('content', "")
            response_content += chunk_content
            if color is not None:
                print(color + chunk_content, end="")  # print each chunk as it arrives, without adding a newline
            else:
                print(chunk_content, end="")  # print each chunk as it arrives, without adding a newline
            if resp.get('choices', [{}])[0].get('finish_reason'):
                print(Fore.RESET + "\n")  # print a newline at the end of the response
                return response_content
    except openai.error.OpenAIError as e:
        print(Fore.RED + f"An error occurred: {e}" + Fore.RESET)
        return None

def chat_with_gpt():
    system_message = [{"role": "system", "content": "You are an open minded problem solver."}]
    temperatures = [0.7,0.8,0.9]

    while True:

        colored_print("Welcome to RMC", Fore.WHITE)
        colored_print("Feel free to ask for anything, and Ill do my best to complete the task step by step.", Fore.WHITE)
        colored_print("(Keep in mind, I will not retain information across multiple user inputs.)", Fore.WHITE)
        question = input("Input: ")
        if question.lower() == "quit":
            break

        user_message = f"{question} Answer: Let's work this out in a step by step way to be sure we have the right answer."
        messages = [system_message[0].copy(), {"role": "user", "content": user_message}]

        answers = []
        for i, temperature in enumerate(temperatures):
            colored_print("Response " + str(i+1) + ": \n", Fore.CYAN)
            answer = generate_response("user", user_message, messages, temperature=temperature, color=Fore.YELLOW)
            if answer:
                answers.append({"role": "assistant", "content": answer})
        
        num_answers = len(answers)       

        colored_print("Reflection: \n", Fore.CYAN)
        # Pass the list of messages to the researcher
        researcher_messages = answers.copy()
        if num_answers > 1:
            researcher_message = "You are a researcher tasked with investigating the response options provided. List the flaws and faulty logic of each answer option. Let's work this out in a step by step way to be sure we have all the errors."
        else:
            researcher_message = "You are a researcher tasked with investigating the response provided. List any flaws and faulty logic. Let's work this out in a step by step way to be sure we have found all potential errors."
        researcher_response = generate_response("user", researcher_message, researcher_messages, temperature=1.0, color=Fore.MAGENTA)
        if researcher_response:
            researcher_messages.append({"role": "assistant", "content": researcher_response})

        colored_print("Final Answer: \n", Fore.CYAN)
        # Pass the list of messages from the researcher to the resolver
        resolver_messages = researcher_messages.copy()
        if num_answers > 1:
            resolver_message = "You are a resolver tasked with 1) finding which of the answer options the researcher thought was best, 2) improving that answer, and 3) Printing the improved answer in full. Let's work this out in a step by step way to be sure we have the right answer."
        else:
            resolver_message = "You are a resolver tasked with 1) analyzing the researcher's investigation, 2) improving the answer if needed, and 3) Printing the improved answer in full. Let's work this out in a step by step way to ensure we have the right answer."
        resolver_response = generate_response("user", resolver_message, resolver_messages, temperature=1.0, color=Fore.GREEN)
        if resolver_response:
            resolver_messages.append({"role": "assistant", "content": resolver_response})

if __name__ == "__main__":
    chat_with_gpt()
