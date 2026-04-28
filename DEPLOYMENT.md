# BlogHub Deployment Guide - Render.com

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Local Development](#local-development)
3. [GitHub Setup](#github-setup)
4. [Render.com Deployment](#rendercom-deployment)
5. [Post-Deployment](#post-deployment)
6. [Troubleshooting](#troubleshooting)

---

## Prerequisites

Before deploying, ensure you have:
- ✅ Python 3.11+ installed
- ✅ Git installed and configured
- ✅ GitHub account
- ✅ Render.com account (free tier available)
- ✅ PostgreSQL account (for production database)

---

## Local Development

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/BlogHub.git
cd BlogHub
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup Database
```bash
# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic --noinput
```

### 5. Run Development Server
```bash
python manage.py runserver
```

Visit: http://127.0.0.1:8000/

---

## GitHub Setup

### 1. Initialize Git Repository
```bash
# If not already initialized
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: BlogHub Django application"

# Create main branch
git branch -M main
```

### 2. Create GitHub Repository
1. Go to [GitHub.com](https://github.com)
2. Click "New Repository"
3. Name it: `BlogHub`
4. Don't initialize with README (we have one)
5. Click "Create Repository"

### 3. Push to GitHub
```bash
# Add remote
git remote add origin https://github.com/yourusername/BlogHub.git

# Push to main branch
git push -u origin main

# Verify
git remote -v
```

### 4. Key Files for Deployment
Ensure these files are in your repository:
- ✅ `Procfile` - Render configuration
- ✅ `runtime.txt` - Python version
- ✅ `requirements.txt` - Dependencies
- ✅ `.gitignore` - Files to ignore
- ✅ `manage.py` - Django management script

---

## Render.com Deployment

### Step 1: Connect GitHub to Render
1. Go to [Render.com](https://render.com)
2. Sign up or log in with GitHub
3. Authorize Render to access your repositories

### Step 2: Create New Web Service
1. Click "New +" button
2. Select "Web Service"
3. Search for and select your "BlogHub" repository
4. Click "Connect"

### Step 3: Configure Service

Fill in these settings:

**Basic Settings:**
- Name: `bloghub`
- Environment: `Python 3`
- Region: Choose your region
- Plan: Free (or upgrade as needed)

**Build & Deploy:**
- Build Command:
```
pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput
```

- Start Command:
```
gunicorn blogproject.wsgi:application
```

### Step 4: Environment Variables

Click "Advanced" → "Environment" and add:

```
DEBUG=False
SECRET_KEY=your-generated-secret-key-here
ALLOWED_HOSTS=bloghub.onrender.com
PYTHON_VERSION=3.11.8
```

**Generate SECRET_KEY:**
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Or use: [Secret Key Generator](https://djecrety.ir/)

### Step 5: Deploy
1. Click "Create Web Service"
2. Wait 5-10 minutes for deployment
3. Check logs for any errors
4. Your site will be live at: `https://bloghub.onrender.com`

---

## Quick Render Setup (Option 2)

### Step 1: Push to GitHub
```bash
git add .
git commit -m "Ready for Render deployment"
git push origin main
```

### Step 2: Create on Render
1. Go to [Render Dashboard](https://dashboard.render.com)
2. Click "New +" → "Web Service"
3. Select your repository
4. Fill in the configuration (same as above)
5. Deploy!

---

---



## Post-Deployment

### 1. Create Superuser on Production
```bash
# SSH into Render service
render shell

# Create superuser
python manage.py createsuperuser

# Exit
exit
```

### 2. Verify Deployment
- ✅ Check main site: https://yourdomain.onrender.com
- ✅ Check admin: https://yourdomain.onrender.com/admin
- ✅ Test user signup
- ✅ Test post creation
- ✅ Test image upload

### 3. Setup Custom Domain (Optional)
1. In Render dashboard, go to "Settings"
2. Find "Custom Domains"
3. Add your domain
4. Update DNS records at domain registrar

### 4. Enable HTTPS
- Render automatically provides SSL/TLS certificates
- Redirect HTTP to HTTPS in Django settings

### 5. Monitor Deployment
1. Check logs regularly: Dashboard → Logs
2. Monitor performance metrics
3. Set up error notifications

---

## Environment Variables

### Production Variables (Render)
```
DEBUG=False
SECRET_KEY=your-generated-secret-key
ALLOWED_HOSTS=yourdomain.onrender.com,www.yourdomain.com
CSRF_TRUSTED_ORIGINS=https://yourdomain.onrender.com
```

### Optional Variables
```
# Database (Render provides one automatically)
DATABASE_URL=postgresql://...

# Email (for notifications)
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

---

## Database Migration

### SQLite to PostgreSQL
For production, migrate from SQLite to PostgreSQL:

1. **Export data from SQLite:**
```bash
python manage.py dumpdata > db.json
```

2. **Update DATABASE_URL in Render**
3. **Load data:**
```bash
python manage.py loaddata db.json
```

---

## Performance Optimization

### Caching
```python
# Add to settings.py
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
```

### Database Optimization
```python
# Use select_related for foreign keys
posts = Post.objects.select_related('author').all()
```

### Static Files
- WhiteNoise configured for efficient serving
- CSS and JS are minified
- Images compressed

---

## Troubleshooting

### Issue: "Application Error"
**Solution:**
1. Check Render logs: Dashboard → Logs
2. Verify environment variables
3. Ensure Procfile exists
4. Check for syntax errors

```bash
# Local test
python manage.py check
```

### Issue: "Static Files Not Loading"
**Solution:**
```bash
# Rebuild
python manage.py collectstatic --noinput --clear

# Restart service in Render dashboard
```

### Issue: "Database Connection Error"
**Solution:**
1. Verify DATABASE_URL is set
2. Run migrations: `python manage.py migrate`
3. Check database credentials

### Issue: "Module Not Found"
**Solution:**
1. Verify requirements.txt has all packages
2. Check Python version matches runtime.txt
3. Reinstall dependencies: `pip install -r requirements.txt`

### Issue: "500 Internal Server Error"
**Solution:**
1. Check error logs in Render
2. Set DEBUG=True temporarily to see errors
3. Check for missing migrations: `python manage.py makemigrations && python manage.py migrate`

### Issue: "Images Not Uploading"
**Solution:**
1. Check file permissions
2. Verify media directory exists
3. Check file size limits
4. For Render, use external storage (S3, Cloudinary)

---

## External Storage (S3/Cloudinary)

### Using AWS S3
```bash
pip install django-storages boto3
```

### Using Cloudinary
```bash
pip install cloudinary django-cloudinary-storage
```

---

## Security Checklist

- ✅ DEBUG=False in production
- ✅ SECRET_KEY is secret and strong
- ✅ ALLOWED_HOSTS configured correctly
- ✅ HTTPS enforced
- ✅ CSRF protection enabled
- ✅ SQL injection prevention
- ✅ XSS protection enabled
- ✅ Regular security updates

---

## Continuous Deployment

### Auto-Deploy on Push
Render automatically deploys when you push to main branch.

### Manual Deploy
1. Push code to GitHub
2. Render detects change
3. Automatic deployment starts
4. Service restarts with new code

---

## Monitoring & Maintenance

### Log Monitoring
```bash
# SSH into service
render shell

# Check logs
tail -f /var/log/application.log
```

### Database Maintenance
```bash
# Backup database
python manage.py dumpdata > backup.json

# Clear cache
python manage.py shell
>>> from django.core.cache import cache
>>> cache.clear()
```

### Regular Updates
```bash
# Update dependencies
pip list --outdated
pip install --upgrade [package-name]
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Update dependencies"
git push
```

---

## Support & Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Render.com Docs](https://render.com/docs)
- [Bootstrap 5 Docs](https://getbootstrap.com/docs/5.0/)
- [PostgreSQL Docs](https://www.postgresql.org/docs/)

---

## Next Steps

1. ✅ Deploy to Render
2. ✅ Test all functionality
3. ✅ Set up custom domain
4. ✅ Configure external storage (optional)
5. ✅ Set up monitoring
6. ✅ Share deployment link

---

**Last Updated**: April 2024
**Version**: 1.0.0
