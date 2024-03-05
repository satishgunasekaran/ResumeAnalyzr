system_prompt = "Extract resume information:"

# Add prompts for extracting resume information
prompt = f"""

Please provide the following details extracted from the resume and return as a json format of below
- Name: [str]
- Education: [List of dictionaries with 'degree' and 'institution' keys]
- Work Experiences: [List of dictionaries with 'position', 'company', and 'duration' keys]
- Location: [str]
- Phone: [str]
- Email: [str]
- Skills: [List of strings]
- Certifications: [List of strings]
- Languages: [List of strings]
- Projects: [List of dictionaries with 'name', 'description', and 'duration' keys]
"""