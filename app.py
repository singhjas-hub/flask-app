from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
  <title>MSOE Flask App</title>
  <style>
    body {
      background: #111;
      color: #fff;
      font-family: sans-serif;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      height: 100vh;
      margin: 0;
    }
    h1 { font-size: 3rem; margin-bottom: 1rem; }
    button {
      padding: 10px 20px;
      font-size: 1rem;
      border-radius: 8px;
      border: none;
      background: #e63946;
      color: white;
      cursor: pointer;
      font-weight: bold;
    }
    button:hover { background: #c52233; }
  </style>
</head>
<body>
  <h1 id="text">Hello MSOE</h1>
  <button onclick="changeText()">Click Me</button>

  <script>
    function changeText() {
      const el = document.getElementById('text');
      el.textContent = el.textContent === 'Hello MSOE' ? '🚀 Flask is Live!' : 'Hello MSOE';
    }
  </script>
</body>
</html>
"""

@app.route('/')
def hello_world():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)