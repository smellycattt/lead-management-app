# Lead Management Application

## Requirements

- Python 3.8+
- FastAPI
- Uvicorn
- SQLAlchemy
- SMTP server for email (e.g., local Postfix)

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/smellycattt/lead-management-app.git
    cd lead-management-app
    ```

2. Set up a virtual environment and install dependencies:
    ```bash
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. Run the application:
    ```bash
    uvicorn main:app --reload
    ```

4. Access the application:
    - API: `http://127.0.0.1:8000/docs`
    - Internal UI: Authentication needed

## Design Document

- **Database**: SQLite for simplicity, storing leads with fields: first name, last name, email, resume, and state.
- **APIs**: Implemented using FastAPI with endpoints to create, get, and update leads.
- **Email**: SMTP for sending emails to prospects and attorneys upon lead creation.
- **Authentication**: Basic auth for internal UI.

## Submission

- Code and documentation are available in this repository.