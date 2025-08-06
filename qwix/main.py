from webapp import app
import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Render provides PORT env variable
    app.run(debug=True, host='0.0.0.0', port=port)
