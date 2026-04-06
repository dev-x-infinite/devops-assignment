from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>DevOps Demo App</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 600px; margin: 80px auto; text-align: center; }
        h1 { color: #2c3e50; }
        p { color: #7f8c8d; font-size: 1.2em; }
        .status { background: #27ae60; color: white; padding: 10px 20px; border-radius: 8px; display: inline-block; }
    </style>
</head>
<body>
    <h1>DevOps Demo App</h1>
    <p>A simple web app with CI/CD pipeline</p>
    <div class="status">Running</div>
</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML_TEMPLATE)


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


@app.route("/api/info")
def info():
    return jsonify({"app": "devops-demo", "version": "1.0.0"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
