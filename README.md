# Time.com Story Fetcher

This is a small Python Flask project that shows the latest 6 stories from [Time.com](https://time.com).  
Instead of showing the data in JSON format, it displays the results on a simple HTML and CSS page.

---

## Live Project
You can check the live version here:  
🔗 [https://timecom-story-fetcher.onrender.com/](https://timecom-story-fetcher.onrender.com/)

---

## About the Project
- The app fetches the latest 6 stories from Time.com.
- Each story has a title and a clickable link.
- It uses basic HTML parsing (no external libraries like BeautifulSoup).
- The frontend is made with plain HTML and CSS.
- The project is deployed on Render.

---

## How It Works
1. Flask fetches the main page of Time.com.
2. The backend extracts the titles and URLs of the latest stories.
3. The results are sent to an HTML template and shown in a simple webpage.

---

## Tech Used
- **Python** (Flask)
- **HTML & CSS**
- **Gunicorn** for deployment on Render

---

## Run Locally
If you want to run this project on your system:
```bash
git clone https://github.com/Vikaskumar63-devops/timecom-story-fetcher.git
cd Timecom-Story-Fetcher
pip install -r requirements.txt
python app.py
