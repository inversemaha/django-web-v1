# Django Web V1

A Django-based tutorial and category web application with Docker support, Materialize CSS, TinyMCE, and Prism.js integration.

## Features
- Category, series, and tutorial navigation
- User registration, login, and logout
- Rich text editing with TinyMCE
- Syntax highlighting with Prism.js
- Responsive UI with Materialize CSS
- Admin interface for managing content
- Dockerized development environment

## Project Structure
```
django-web-v1/
├── docker-compose.yml
├── Dockerfile
├── README.md
├── requirements.txt
├── main/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── templates/
│   │   └── main/
│   │       ├── categories.html
│   │       ├── category.html
│   │       ├── tutorial.html
│   │       ├── header.html
│   │       └── ...
│   ├── urls.py
│   ├── views.py
│   └── ...
└── ...
```

## Setup & Usage

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd django-web-v1
```

### 2. Build and run with Docker
```bash
docker-compose up --build
```
App will be available at `http://localhost:8000/`

### 3. Database migrations
If not using Docker, run:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create a superuser
```bash
python manage.py createsuperuser
```

### 5. Access the admin
Visit `http://localhost:8000/admin/` and log in with your superuser credentials.

## Navigation
- **Homepage:** Lists all categories.
- **Category page:** Lists all series in a category, each card links to the first tutorial in the series.
- **Tutorial page:** Shows tutorial content, sidebar lists all tutorials in the series.

## Models
- `TutorialCategory`: Holds category info and slug.
- `TutorialSeries`: Linked to category, holds series info and summary.
- `Tutorial`: Linked to series, holds tutorial content, slug, and creation date.

## Templates
- `categories.html`: Category cards, responsive with Materialize CSS.
- `category.html`: Series cards, each links to first tutorial.
- `tutorial.html`: Tutorial detail, sidebar for series navigation.
- `header.html`: Navigation bar and static includes.

## Static & Media
- Place custom CSS/JS in `main/static/main/`.
- TinyMCE and Prism.js are loaded via CDN in `header.html`.

## User Management
- Registration, login, and logout handled via forms and views.
- Messages and errors shown with Materialize toasts.

## Notes
- All tutorial and category slugs must be URL-safe (lowercase, hyphens, no spaces).
- The admin route is defined in the main `urls.py` and must come before slug routes.
- Use `{% url 'main:single_slug' tutorial.tutorial_slug %}` for tutorial links.

## License
MIT
