# BlogHub - Django Blog Application

A modern, responsive blogging platform built with Django and Bootstrap 5. Complete with user authentication, post creation, commenting system, and more.

## Features

### Core Features
✅ User Authentication (Sign Up, Login, Logout)
✅ Create & Publish Blog Posts
✅ View Blog Posts with Images
✅ Responsive Design (Mobile-Friendly)
✅ Bootstrap 5 Styling
✅ Font Awesome Icons
✅ Image Upload Support
✅ User-Specific Functionality

### Bonus Features (Ready for Implementation)
🔸 Edit/Delete Posts
🔸 Like System
🔸 Comment Section
🔸 Pagination
🔸 Dark Mode
🔸 Search Functionality

## Project Structure

```
blogproject/
├── blogproject/          # Main project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── blogapp/              # Django app
│   ├── templates/        # HTML templates
│   │   ├── base.html     # Base template with navbar & footer
│   │   └── blogapp/
│   │       ├── home.html
│   │       ├── signup.html
│   │       ├── login.html
│   │       ├── create_post.html
│   │       └── post_detail.html
│   ├── models.py         # Post model
│   ├── views.py          # View functions
│   ├── forms.py          # Django forms
│   └── urls.py           # App URLs
├── static/               # Static files (CSS, JS, images)
├── media/                # User-uploaded files
├── requirements.txt      # Python dependencies
├── Procfile              # Render deployment config
├── runtime.txt           # Python version
├── manage.py
└── db.sqlite3            # Database (local only)
```

## Installation & Setup

### Prerequisites
- Python 3.11+
- pip (Python package manager)
- Git

### Local Development Setup

1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/BlogHub.git
cd BlogHub
```

2. **Create Virtual Environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Create Superuser (Admin Account)**
```bash
python manage.py createsuperuser
```

5. **Run Migrations**
```bash
python manage.py migrate
```

6. **Collect Static Files**
```bash
python manage.py collectstatic --noinput
```

7. **Start Development Server**
```bash
python manage.py runserver
```

8. **Access the Application**
- Application: http://127.0.0.1:8000/
- Admin Panel: http://127.0.0.1:8000/admin/

## Database Models

### Post Model
```python
class Post(models.Model):
    title = CharField(max_length=200)
    content = TextField()
    author = ForeignKey(User, on_delete=CASCADE)
    created_at = DateTimeField(auto_now_add=True)
    image = ImageField(upload_to='post_images/', blank=True, null=True)
```

## URL Routes

| URL | Name | Description |
|-----|------|-------------|
| `/` | home | Home page with all posts |
| `/signup/` | signup | User registration page |
| `/login/` | login | User login page |
| `/logout/` | logout | User logout |
| `/create/` | create_post | Create new blog post |
| `/post/<id>/` | post_detail | View individual blog post |
| `/admin/` | admin | Django admin panel |

## Usage Guide

### For Users

1. **Create Account**
   - Click "Sign Up" button
   - Fill in username, email, and password
   - Click "Create Account"

2. **Login**
   - Click "Login" button
   - Enter credentials
   - Click "Login"

3. **Create Post**
   - After login, click "Create Post"
   - Fill in title and content
   - (Optional) Upload featured image
   - Click "Publish Post"

4. **View Posts**
   - Posts are displayed on home page
   - Click "Read More" to view full post details
   - See author and date information

### For Admin

1. Access Django admin: `/admin/`
2. Manage posts, users, and site content
3. Moderate comments and content

## Deployment to Render

### Step 1: Push to GitHub

```bash
# Initialize Git (if not already done)
git init
git add .
git commit -m "Initial commit: BlogHub Django application"
git branch -M main
git remote add origin https://github.com/yourusername/BlogHub.git
git push -u origin main
```

### Step 2: Set Up Render Account

1. Go to [Render.com](https://render.com)
2. Sign up with GitHub account
3. Click "Create +"
4. Select "Web Service"

### Step 3: Connect Repository

1. Select your BlogHub repository
2. Name: `bloghub` (or your preference)
3. Runtime: `Python 3`
4. Build Command: `pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput`
5. Start Command: `gunicorn blogproject.wsgi:application`

### Step 4: Set Environment Variables

1. In Render dashboard, go to Environment
2. Add these variables:
   ```
   DEBUG=False
   SECRET_KEY=your-secret-key-here
   ALLOWED_HOSTS=yourdomain.onrender.com
   ```

### Step 5: Deploy

1. Click "Create Web Service"
2. Wait for deployment (5-10 minutes)
3. Your site will be live at: `https://bloghub.onrender.com`

## Environment Variables

Create a `.env` file locally (not committed to git):

```
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=your-database-url
ALLOWED_HOSTS=localhost,127.0.0.1,yourdomain.onrender.com
```

## Technologies Used

- **Backend**: Django 5.2.12
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Database**: SQLite (local), PostgreSQL (production recommended)
- **Image Processing**: Pillow
- **Server**: Gunicorn
- **Deployment**: Render, Docker
- **Version Control**: Git, GitHub
- **Icons**: Font Awesome 6.4

## File Upload

- **Max File Size**: 5MB per image
- **Supported Formats**: JPG, PNG, GIF, WebP
- **Upload Directory**: `/media/post_images/`
- **Recommended Size**: 1200x630px for featured images

## Security Features

- CSRF Protection
- SQL Injection Prevention
- XSS Protection
- Password Hashing
- User Authentication
- Permission-Based Access Control

## Performance Optimization

- WhiteNoise for static file serving
- Gzip compression
- Database query optimization
- Caching ready

## Troubleshooting

### Issue: "No module named 'blogapp'"
**Solution**: Make sure `blogapp` is added to `INSTALLED_APPS` in settings.py

### Issue: Images not showing
**Solution**: Run `python manage.py collectstatic` and check MEDIA_URL/MEDIA_ROOT

### Issue: Database errors
**Solution**: Run `python manage.py migrate`

### Issue: Static files not loading
**Solution**: 
```bash
python manage.py collectstatic --noinput
```

## API Documentation

### View List
- **Endpoint**: `/`
- **Method**: GET
- **Description**: Display all blog posts

### Create Post
- **Endpoint**: `/create/`
- **Method**: POST
- **Authentication**: Required (Login)
- **Fields**: title, content, image (optional)

### View Post Detail
- **Endpoint**: `/post/<id>/`
- **Method**: GET
- **Description**: View full blog post with details

## Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## Future Enhancements

- [ ] Post categories/tags
- [ ] Search functionality
- [ ] User profiles with bio
- [ ] Follow system
- [ ] Notifications
- [ ] Email notifications
- [ ] RSS feed
- [ ] Social sharing
- [ ] Analytics dashboard
- [ ] Multi-language support

## License

This project is licensed under the MIT License - see LICENSE file for details.

## Support

For issues, questions, or suggestions:
- Create an issue on GitHub
- Contact: your-email@example.com

## Authors

- Your Name - BlogHub Developer

## Acknowledgments

- Django Documentation
- Bootstrap 5
- Font Awesome
- Render.com for hosting
- Contributors and community

---

**Last Updated**: April 2024
**Version**: 1.0.0
