import os

def create_file(path):
    with open(path, 'w'):
        pass

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

project_directories = [
    "src",
    "src/components",
    "src/pipelines",
    "data",
    "notebooks",
]

for directory in project_directories:
    create_directory(os.path.join("ml_project", directory))

# Create the required files
files = [
    "__init__.py",
    "logger.py",
    "exception.py",
    "utils.py",
    os.path.join("components", "__init__.py"),
    os.path.join("components", "data_ingestion.py"),
    os.path.join("components", "data_transformation.py"),
    os.path.join("components", "model_trainer.py"),
    os.path.join("pipelines", "__init__.py"),
    os.path.join("pipelines", "predict_pipeline.py"),
    os.path.join("pipelines", "train_pipeline.py"),
    "import_data.py",
    "setup.py",
    "requirements.txt",
]

for file in files:
    create_file(os.path.join("ml_project", "src", file))

print("Project structure and files created successfully!")
