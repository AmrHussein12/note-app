client_loop: send disconnect: Connection resetnder_template_string
PS C:\Users\valem\downloads>
import os
from datetime import datetime

app = Flask(__name__)

# Database configuration (use environment variables for security)
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "notes_db")
DB_USER = os.getenv("DB_USER", "notes_user")
DB_PASS = os.getenv("DB_PASS", "STRONG_DB_PASSWORD")  # replace later
DB_PORT = int(os.getenv("DB_PORT", 3306))

def get_db_conn():
    return mysql.connector.connect(
        host=DB_HOST, user=DB_USER, password=DB_PASS, database=DB_NAME, port=DB_PORT
    )

HTML = """
<!doctype html>
<title>Notes</title>
<h2>Simple Note-Taking App</h2>
<form method="post">
  <textarea name="content" rows="4" cols="60" placeholder="Write your note here..."></textarea><br>
  <button type="submit">Save Note</button>
</form>
<hr>
{% for note in notes %}
  <div>
    <small>🕒 {{ note['created_at'] }}</small><br>
    <p>📌 {{ note['content']|e }}</p>
    <hr>
  </div>
{% else %}
  <p>No notes yet.</p>
{% endfor %}
"""

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        content = request.form.get("content","").strip()
        if content:
            conn = get_db_conn()
            cur = conn.cursor()
            cur.execute("INSERT INTO notes (content) VALUES (%s)", (content,))
            conn.commit()
            cur.close()
            conn.close()
