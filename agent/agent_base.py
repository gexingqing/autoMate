import openai
import yaml


class AgentBase:
    def __init__(self, role):
        """
        Initialize an Agent object.

        Args:
            role (str): The role of the agent.

        Returns:
            None
        """
        self.role = role
        

    def set_role(self, new_role):
        """
        Set the role of the agent.

        Args:
            new_role (str): The new role of the agent.

        Returns:
            None
        """
        self.role = new_role

    

    def call_gpt(self, input_text):
        """
        Make a call to the OpenAI chat API.

        Args:
            input_text (str): The input text for the chat API.

        Returns:
            str: The generated text from the chat API.
        """
        # Load API configuration from YAML file
        with open("config.yaml", "r") as file:
            config = yaml.safe_load(file).get("openai")

        openai.api_key = config.get("api_key")
        openai.base_url = config.get("api_url")

        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",  # GPT-3.5 model
            messages=[
                {"role": "system", "content": self.role},
                {"role": "user", "content": input_text}
            ],
            temperature=0.2
        )

        generated_text = response.choices[0].message.content

        return generated_text