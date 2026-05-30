# Server Health CLI

A simple Python command-line tool that checks the health status of a server and sends alerts to Slack when issues are detected.

## Project Overview

This project demonstrates basic DevOps and monitoring concepts by:

* Checking server availability
* Monitoring HTTP response status
* Sending Slack notifications
* Using environment variables for secure secret management
* Following GitHub security best practices

## Features

* Check if a website/server is reachable
* Display HTTP response status codes
* Send Slack alerts when a server is unavailable
* Store sensitive credentials using environment variables
* Prevent secrets from being committed to GitHub

## Technologies Used

* Python 3
* Requests Library
* Slack Incoming Webhooks
* Git & GitHub
* VS Code

## Project Structure

server-health-cli/

├── slack_alert.py

├── .env

├── .gitignore

└── README.md

## Setup Instructions

### Clone the Repository

```bash
git clone https://github.com/feranzeey/server-health.git
cd server-health
```

### Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

Git Bash:

```bash
source venv/Scripts/activate
```

Windows Command Prompt:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install requests python-dotenv
```

### Configure Environment Variables

Create a `.env` file:

```env
SLACK_WEBHOOK_URL=YOUR_SLACK_WEBHOOK_URL
```

### Run the Script

```bash
python slack_alert.py
```

## Security Best Practices

* Secrets are stored in environment variables.
* `.env` is excluded from Git tracking using `.gitignore`.
* No sensitive credentials are committed to GitHub.

## Learning Outcomes

Through this project, I practiced:

* Linux command-line operations
* Git and GitHub workflows
* Environment variable management
* Basic monitoring concepts
* Secure handling of application secrets
* Troubleshooting GitHub Push Protection errors

## Future Improvements

* Monitor multiple servers
* Add email notifications
* Generate health reports
* Schedule automatic checks using cron jobs
* Containerize the application using Docker

## Author

Oluwaferanmi Dada

DevOps Engineer | Linux | AWS | Python | GitHub
