# RMC-ReflectiveMultiChat

RMC (Reflective Multi-Chat) is an innovative Python-based AI bot designed for optimal AI decision making. It generates multiple responses to a single user query, reflects on the quality and relevance of each, and refines its output to deliver the most accurate and contextually fitting response.

## Getting Started

### Prerequisites

- Python 3.7 or later
- [OpenAI API Key](https://beta.openai.com/signup/)
- [Python-dotenv](https://pypi.org/project/python-dotenv/)
- [Colorama](https://pypi.org/project/colorama/)

### Installation

1. Clone the repo: `git clone https://github.com/yourusername/RMC-ReflectiveMultiChat.git`
2. Install the required packages: `pip install -r requirements.txt`
3. Create a `.env` file in your project root and set your OpenAI API key: `API_KEY=yourapikey`

## Usage

This script allows you to interact with OpenAI's GPT-4 model to generate responses to user inputs. It provides a chat interface where you can ask questions and receive answers from the model. The script also includes a feature to generate multiple responses and analyze them for potential errors.

Setting the Number of Responses
The number of responses generated for each user input is determined by the length of the temperatures list. Each temperature in the list corresponds to one response. To change the number of responses, modify the temperatures list in the chat_with_gpt function. For example, to generate 4 responses, you could set temperatures = [0.6, 0.7, 0.8, 0.9].

Changing the Temperature
The temperature parameter controls the randomness of the model's output. A higher temperature results in more random outputs, while a lower temperature results in more deterministic outputs. You can adjust the temperature for each response by modifying the values in the temperatures list in the chat_with_gpt function.

Changing the Model
The model used for generating responses is set in the generate_response function. By default, it uses the "gpt-4" model. To use a different model, change the model parameter in the generate_response function. For example, to use GPT-3, you would set model="text-davinci-003".

Running the Script
Before running the script, make sure you have set your OpenAI API key as an environment variable. You can do this by creating a .env file in the same directory as the script and adding the line API_KEY=your_api_key_here, replacing your_api_key_here with your actual OpenAI API key.

To run the script, navigate to the directory containing the script in your terminal and run the command python script_name.py, replacing script_name.py with the name of your script.

During execution, you can interact with the chat interface by typing your inputs at the prompt. To exit the chat, type "quit".

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Don Cuddihee - [@DonCudd3](https://twitter.com/DonCudd3) - doncudd3@gmail.com
