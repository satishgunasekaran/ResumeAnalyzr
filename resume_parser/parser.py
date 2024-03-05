from lyzr import QABot
from resume_parser.prompt import system_prompt, prompt
import uuid
import json
from resume_parser.utils import create_vector_store_params_local

class ResumeParser:
    def __init__(self, file_path):
        self.file_path = file_path
        uuid_string = "I" + str(uuid.uuid4()).replace("-", "")
        vector_store_params = create_vector_store_params_local("I" + uuid_string)
        self.qabot = QABot.(
            input_files=[self.file_path],
            vector_store_params=vector_store_params,
            system_prompt=system_prompt
        )

    def extract_resume_json(self):
        """
        Extract information from a resume PDF and return the response as JSON.

        Args:
        - prompt (str): Prompt for extracting resume information.

        Returns:
        - dict: JSON response containing extracted resume information.
        """
        # Query the QABot for information related to the resume
        response = self.qabot.query(prompt)

        # Extract JSON response
        json_response = response.response.replace("```json", "").replace("```", "")

        # Parse the JSON string
        parsed_json = json.loads(json_response)

        return parsed_json
