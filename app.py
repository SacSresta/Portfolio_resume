from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# Load projects from JSON file
def load_projects():
    with open('projects.json') as f:
        print(f)
        return json.load(f)

@app.route('/')
def index():
    projects = load_projects()
    return render_template('index.html', projects=projects)

@app.route('/project/<int:project_id>')
def project(project_id):
    projects = load_projects()
    project = next((p for p in projects if p['id'] == project_id), None)
    if project:
        return render_template('project.html', project=project)
    else:
        return "Project not found", 404

if __name__ == '__main__':
    app.run(debug=True)
