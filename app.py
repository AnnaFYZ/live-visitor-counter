from flask import Flask, jsonify, render_template_string

app = Flask(__name__)
visitor_count = 0

HTML_TEMPLATE = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Live Visitor Counter</title>
    <style>
      body { font-family: Arial, sans-serif; margin: 3rem; text-align: center; }
      .counter { font-size: 4rem; margin: 1rem 0; }
      .card { display: inline-block; padding: 2rem; border: 1px solid #ddd; border-radius: 1rem; box-shadow: 0 0 20px rgba(0,0,0,.05); }
    </style>
  </head>
  <body>
    <div class="card">
      <h1>Live Visitor Counter</h1>
      <div class="counter">{{ count }}</div>
      <p>Refresh the page to increase the visitor count.</p>
      <p><a href="/count">View JSON counter</a></p>
    </div>
  </body>
</html>
"""

@app.route("/")
def index():
    global visitor_count
    visitor_count += 1
    return render_template_string(HTML_TEMPLATE, count=visitor_count)

@app.route("/count")
def count():
    return jsonify(count=visitor_count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
