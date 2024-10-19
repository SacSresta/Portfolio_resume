import os

# Define the structure of the project
project_structure = {
        "static": {
            "css": ["styles.css"],
            "images": []
        },
        "templates": ["base.html", "index.html", "project.html"],
        "": ["app.py", "projects.json","requirements.txt"]
}

def create_structure(base_path, structure):
    for folder, contents in structure.items():
        # Create the base folder
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        
        # If contents is a dictionary, it's a nested folder structure
        if isinstance(contents, dict):
            create_structure(folder_path, contents)
        else:
            # If contents is a list, these are files to create in the folder
            for file_name in contents:
                file_path = os.path.join(folder_path, file_name)
                open(file_path, 'a').close()  # Create an empty file

def main():
    # Set the base directory for your project
    base_dir = os.getcwd()  # Current working directory
    create_structure(base_dir, project_structure)
    print("Project structure created successfully!")

if __name__ == "__main__":
    main()
