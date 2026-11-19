from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from pathlib import Path

from database import create_database, add_record


app = FastAPI(
    title="DataHub Demo",
    description="A data integration and analytics platform",
    version="1.0.0"
)


# Create the database when DataHub starts
create_database()


# Display the main dashboard
@app.get("/", response_class=HTMLResponse)
def home():

    html_file = Path("templates/index.html")

    return html_file.read_text(encoding="utf-8")


# Display the Add Data page
@app.get("/add-data", response_class=HTMLResponse)
def add_data():

    html_file = Path("templates/add_data.html")

    return html_file.read_text(encoding="utf-8")


# Receive and save a new record
@app.post("/save-record")
def save_record(
    full_name: str = Form(...),
    email: str = Form(...),
    category: str = Form(...),
    description: str = Form("")
):

    add_record(
        full_name,
        email,
        category,
        description
    )

    return """
    <h1>Record Saved Successfully!</h1>
    <p>The record has been saved to the DataHub database.</p>
    <a href="/add-data">Add Another Record</a>
    <br><br>
    <a href="/">Return to Dashboard</a>
    """