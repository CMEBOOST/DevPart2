# DevPart2

Django project for a small web app with user authentication, profile editing, avatar upload, and a showcase page comparing vanilla JavaScript and Alpine.js examples.

## Project Overview

This project includes:

- Django authentication and user registration
- User profile model with avatar upload
- Home page that shows the logged-in user and profile image
- Tailwind CSS integration
- PostgreSQL database configured through Docker
- Showcase examples for frontend JavaScript patterns

## Tech Stack

- Python 3.x
- Django 5.x
- PostgreSQL 16
- Tailwind CSS
- Docker Compose

## Project Structure

```text
WebDev69/
├── docker-compose.yaml
├── requirement.txt
├── manage.py
├── postgres_data/
├── part2/
│   ├── accounts/
│   ├── part2/
│   ├── showcase/
│   ├── templates/
│   ├── theme/
│   └── manage.py
├── templates/
└── README.md
```

## Requirements

Install Python dependencies:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirement.txt
```

If you are using PowerShell on Windows:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1
```

## Database Setup

Start PostgreSQL with Docker:

```bash
docker-compose up -d
```

Then apply migrations:

```bash
python manage.py migrate
```

## Run the Project

From the project root:

```bash
cd part2
python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```

## Tailwind Setup

If Tailwind styles are not generated yet:

```bash
cd part2
python manage.py tailwind install
python manage.py tailwind start
```

## Creating a Superuser

```bash
cd part2
python manage.py createsuperuser
```

## Useful Commands

Run Django checks:

```bash
python manage.py check
```

Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Notes

- Media files are stored in the project media folder.
- The avatar upload path is configured in the profile model.
- For local development, Django settings enable debug mode and allow all hosts.

## License

This project is for learning and development purposes.
