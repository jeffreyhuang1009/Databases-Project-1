'''
All information about Project from project entity
Join button for joining project
Link to calendar page
Post wall (This a wall of all posts, comments and likes in a specific project). This information will be ordered by datetime
'''

from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy import create_engine, text

engine = create_engine('postgresql://wf2322:St278-Ahobo$#cGHh@w4111.cisxo09blonu.us-east-1.rds.amazonaws.com/w4111')
conn = engine.connect()

app = Flask(__name__)

def set_schema():
    conn.execute(text("SET search_path TO wf2322;"))

@app.route('/project/<int:project_id>')
def show_project(project_id):
    set_schema()
    project_query = text("SELECT * FROM CreateProject WHERE ProjectID = :project_id")
    project_data = conn.execute(project_query, {"project_id": project_id}).fetchone()
    
    if project_data:
        return render_template('project.html', project=project_data)
    else:
        flash("Project not found!")
        return redirect(url_for('home'))

@app.route('/project/<int:project_id>/join', methods=['POST'])
def join_project(project_id):
    set_schema()
    flash("You have joined the project!")
    return redirect(url_for('show_project', project_id=project_id))

if __name__ == "__main__":
    app.secret_key = "supersecretkey"
    app.run(debug=True, host="0.0.0.0", port=4000)
