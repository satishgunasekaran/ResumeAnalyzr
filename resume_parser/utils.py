import os

# To have a local Embedded Weaviate vector store
def create_vector_store_params_local(IndexName):
  vector_store_params = {
      "vector_store_type": "WeaviateVectorStore",
      "index_name": IndexName # first letter should be capital
  }
  return vector_store_params

def get_resume_files(resume_directory):

    resume_files = []
    for filename in os.listdir(resume_directory):
        if filename.endswith(".docx"):
            file_path = os.path.join(resume_directory, filename)
            resume_files.append(file_path)
    return resume_files






