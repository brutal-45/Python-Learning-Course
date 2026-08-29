# Deployment Guide

This repository is configured for seamless deployment on multiple platforms.

## 🚀 Vercel Deployment (Recommended)

### Quick Deploy

1. **Install Vercel CLI** (optional, for local testing):
   ```bash
   npm install -g vercel
   ```

2. **Deploy to Vercel**:
   ```bash
   # Login to Vercel
   vercel login
   
   # Deploy
   vercel
   ```

3. **Or use the Vercel Dashboard**:
   - Go to [vercel.com](https://vercel.com)
   - Import your GitHub repository
   - Vercel will automatically detect the `vercel.json` configuration
   - Click "Deploy"

### What Gets Deployed

- **Frontend**: `index.html` - Interactive dashboard
- **API Endpoints**: 
  - `GET /api/health` - Health check
  - `GET /api/status` - Repository status
  - `GET /api/lessons` - List all lessons
  - `GET /api/run?script=<name>` - Run Python scripts

### Local Testing

```bash
# Install Vercel CLI
npm install -g vercel

# Run locally
vercel dev
```

Visit `http://localhost:3000` to test.

---

## 🐙 GitHub Actions Workflow

The repository includes a CI/CD workflow that:

1. **Tests** on Python 3.9, 3.10, 3.11, 3.12
2. **Runs linting** with flake8
3. **Checks formatting** with black
4. **Executes tests** with pytest
5. **Verifies Vercel deployment** readiness

### Workflow Triggers

- Push to `main` or `master` branch
- Pull requests
- Manual trigger via GitHub Actions UI

---

## 🔧 Alternative Deployment Options

### Docker

Create a `Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000
CMD ["python", "-m", "http.server", "8000"]
```

### Netlify

1. Connect your GitHub repository
2. Set build command: `echo "No build needed"`
3. Set publish directory: `/`
4. Add serverless functions in `api/` directory

### Render

1. Create new Web Service
2. Connect GitHub repository
3. Build Command: `pip install -r requirements.txt`
4. Start Command: `python -m http.server $PORT`

---

## 📁 Project Structure

```
├── api/                    # Vercel serverless functions
│   └── __init__.py        # API endpoints
├── .github/workflows/     # GitHub Actions CI/CD
│   └── python-package.yml
├── 01-basics/            # Lesson modules
├── 02-data-types/
├── ...
├── projects/             # Example projects
├── index.html           # Frontend dashboard
├── vercel.json          # Vercel configuration
├── requirements.txt     # Python dependencies
└── README.md           # Documentation
```

---

## ✅ Pre-Deployment Checklist

- [ ] All Python scripts run without errors
- [ ] Tests pass (`pytest`)
- [ ] Code is formatted (`black .`)
- [ ] `vercel.json` is properly configured
- [ ] API endpoints are tested locally
- [ ] Environment variables are set (if needed)

---

## 🎯 Post-Deployment

After deploying to Vercel:

1. Visit your deployed URL
2. Test all API endpoints via the dashboard
3. Share your deployment link!

### Environment Variables (Optional)

Set these in Vercel dashboard if needed:

- `SECRET_KEY` - For API security
- `DATABASE_URI` - For database connections
- `JWT_SECRET_KEY` - For JWT authentication

---

## 📞 Support

For issues or questions:
- Check the [README.md](./README.md)
- Review [CONTRIBUTING.md](./CONTRIBUTING.md)
- Open an issue on GitHub
