# SpectrunX
A modern blog platform built with Django and TailwindCSS that covers topics in technology, travel, lifestyle, food, art, and science.

![SpectrunX Blog Homepage](static/img/home.jpeg)

## Features
- 🎨 Modern responsive design with TailwindCSS
- 🔍 Live search functionality 
- 📱 Mobile-friendly navigation
- 📧 Newsletter subscription
- 🏷️ Category-based content organization
- 🎯 SEO-optimized structure
- ✅ Responsive admin dashboard
- 📊 User analytics integration
- 🌙 Light/dark mode toggle

## Color Scheme
```js
colors: {
    primary: '#6366f1',    // Indigo
    'primary-dark': '#4f46e5',
    secondary: '#f59e0b',  // Amber
    'secondary-dark': '#d97706',
    dark: '#111827',
    'gray-dark': '#374151',
    'gray-medium': '#6b7280',
    'gray-light': '#e5e7eb',
    tech: '#3b82f6',      // Blue
    travel: '#10b981',    // Emerald
    lifestyle: '#ec4899',  // Pink
    food: '#f59e0b',      // Amber
    art: '#8b5cf6',       // Violet
    science: '#6366f1'    // Indigo
}
```

## Project Structure
```
specturnx/           # Django project folder
├── blog/            # Blog app
├── media/           # User uploaded content
├── static/         
│   ├── favicon/
│   └── img/
└── templates/       # HTML templates
    ├── base.html    # Base template
    └── blog/        # Blog templates
```

## Setup
1. Create a virtual environment:
```bash
python -m venv .env
```
2. Activate the virtual environment:
```bash
# Windows
.env\Scripts\activate
# Linux/MacOS
source .env/bin/activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Run migrations:
```bash
python manage.py migrate
```
5. Start development server:
```bash
python manage.py runserver
```

## Usage

### Admin Panel

After running the server, navigate to http://127.0.0.1:8000/admin/ and log in with your superuser credentials to:

- Create, edit, and delete blog posts
- Manage categories
- Moderate comments
- Configure site settings

### Creating a Superuser

```bash
python manage.py createsuperuser
```

### Adding Content

1. Log in to the admin panel
2. Navigate to "Posts" and click "Add Post"
3. Fill in the title, content, select a category, add featured image
4. Save the post as "Published" to make it visible on the site

## Technologies Used
- Django 5.1.7
- TailwindCSS
- Font Awesome
- Swiper.js

## Customization

### Adding New Categories

1. Log in to the admin panel
2. Navigate to "Categories" and click "Add Category"
3. Fill in the name, slug, and description
4. Save the category

### Modifying the Theme

The Tailwind configuration can be adjusted in the `tailwind.config.js` file to match your branding preferences.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Contact
Connect with me on [LinkedIn](https://pk.linkedin.com/in/sulman-majeed-7409442a9)

## License
[MIT](https://choosealicense.com/licenses/mit/)
