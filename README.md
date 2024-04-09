# Website Generation with Prompt2HTML

## Project Overview

The "Prompt2HTML" project aims to streamline the process of website development by utilizing natural language prompts to generate HTML, CSS, and JavaScript code. The application leverages the capabilities of the GPT-3.5 language model to interpret user inputs and generate corresponding website source code.

## Project Goal

The primary objective is to empower users, especially web developers, to quickly generate professional-grade website layouts and functionalities by simply providing textual prompts. By automating the initial stages of website development, the project aims to enhance productivity and reduce the time required for manual coding.

## Approach

### Prompt-Based Generation:
The core of the application lies in its ability to interpret user prompts and generate HTML code accordingly. The provided prompt template prompts the user to specify the desired functionalities, design elements, and layout preferences for the website. The GPT-3.5 language model processes these prompts and generates HTML code snippets that align with the user's requirements.

### Implementation Framework:
The project is built using Streamlit, a popular Python library for building web applications. Streamlit provides a user-friendly interface for users to input their prompts and view the generated website code in real-time. The application architecture consists of backend logic written in Python and frontend interface rendered using Streamlit components.

## Project Components

### Prompt Template:
The project utilizes a custom prompt template designed to capture user requirements for website development. The template instructs users to specify design elements, functionalities, color schemes, fonts, and other preferences for the website.

### Model Integration:
The GPT-3.5 language model, specifically tuned for prompt-based generation, is integrated into the application using the ChatOpenAI class from the langchain library. This allows the application to generate HTML code based on the user's prompt.

### Streamlit Interface:
The user interface is developed using Streamlit, with input fields for users to enter their prompts and display areas to showcase the generated HTML code. Streamlit's interactive components enable users to dynamically interact with the application and view instant updates.

## Usage

### Input Prompt:
Users are prompted to enter their website requirements, including design preferences, layout specifications, and desired functionalities. The prompt should provide sufficient details for the GPT-3.5 model to generate accurate HTML code.

### Generation Process:
Upon receiving the user's prompt, the application processes the input using the GPT-3.5 model and generates HTML code snippets in real-time. Users can interact with the application to refine their prompts and customize the generated code.

### Output Display:
The generated HTML code is displayed to the user in a code block within the Streamlit interface. Users can review the code, make additional requests, or download the code for further use.

## Conclusion

The "Prompt2HTML" project offers a user-friendly solution for rapid website development by leveraging natural language prompts and AI-powered code generation. By simplifying the website creation process, the application empowers users to focus on design and functionality aspects while eliminating the need for manual coding.
## Libraries & Tools used

1. Python
2. OpenAI
3. Streamlit for user interface
4. Visual Studio Code as IDE

![Screenshot (32)](https://github.com/Prathamesh282001/PromptToHTML_LLM_Project/assets/122107260/b3171657-ffdd-4890-a7b9-3b317a183887)

![Screenshot (33)](https://github.com/Prathamesh282001/PromptToHTML_LLM_Project/assets/122107260/879e171a-db00-43f7-bc3c-a2f60b370e96)

![Screenshot (34)](https://github.com/Prathamesh282001/PromptToHTML_LLM_Project/assets/122107260/73187bcc-257e-4f0a-a85c-7c0835a978c0)
