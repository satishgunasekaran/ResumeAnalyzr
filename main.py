from resume_parser.parser import ResumeParser

from resume_parser import utils
import json
import os

# add openai key
os.environ["OPENAI_API_KEY"] = "sk-............................."


resume_files = utils.get_resume_files("Resumes")

for resume_file in resume_files:
    resume = ResumeParser(resume_file).extract_resume_json()

    # store as json file 
    with open(resume_file.split(".")[0] + ".json", "w") as f:
        json.dump(resume, f)