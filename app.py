# Author: Vikas Kumar
# Date: 15 Oct 2025

from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.request, re, json, html, socket

HOST, PORT = "0.0.0.0", 8080
URL = "https://time.com"
LIMIT = 6           # We can increase as per our requirement. 

def get_html(site):
    req = urllib.request.Request(site, headers={"User-Agent": "Mozilla/5.0 (VikasKumar)"})
    with urllib.request.urlopen(req, timeout=10) as r:
        charset = r.headers.get_content_charset() or "utf-8"
        return r.read().decode(charset, "ignore")

def clean(txt):
    txt = re.sub(r"<[^>]*>", "", txt)
    return " ".join(html.unescape(txt).split())

def extract(html_text):
    pattern = re.compile(r'<a[^>]*href=["\'](https?://time\.com/[^"\']+)["\'][^>]*>(.*?)</a>', re.I | re.S)
    stories, seen = [], set()
    for m in pattern.finditer(html_text):
        link, title = m.group(1).rstrip("/"), clean(m.group(2))
        if len(title) < 15 or link in seen: continue
        seen.add(link)
        stories.append({"title": title, "link": link})
        if len(stories) >= LIMIT: break
    return stories

class Handler(BaseHTTPRequestHandler):
    def send_json(self, data, code=200):
        out = json.dumps(data, indent=2, ensure_ascii=False)
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.end_headers()
        self.wfile.write(out.encode("utf-8"))

    def do_GET(self):
        if self.path == "/":
            try:
                with open("index.html", "rb") as f: page = f.read()
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.end_headers()
                self.wfile.write(page)
            except:
                self.send_json({"error": "index.html not found"}, 404)
            return

        if self.path == "/getTimeStories":
            try:
                page = get_html(URL)
                data = extract(page)
                print(f"[{self.client_address[0]}] Stories fetched.")
                self.send_json(data if data else {"msg": "No stories found"})
            except socket.timeout:
                self.send_json({"error": "Timeout"}, 504)
            except Exception as e:
                self.send_json({"error": str(e)}, 500)
            return

        if self.path == "/status":
            self.send_json({"developer": "Vikas Kumar", "status": "Running", "port": PORT})
            return

        self.send_json({"error": "Invalid endpoint"}, 404)

print(f" Server started by Vikas Kumar at http://localhost:{PORT}") # fetch the port of local machine 
with HTTPServer((HOST, PORT), Handler) as server:
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped by user.")
        server.server_close()
