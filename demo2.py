from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/generate_blog', methods=['POST'])
def generate_blog():
    data = request.get_json()

    # Ensure query parameter is provided
    query = data.get('query')
    if not query:
        return jsonify({'error': 'query parameter is required'}), 400

    # Set filename: If not provided, use query as filename
    filename = data.get('filename', f"{query.lower().replace(' ', '_')}.md")

    # Ensure filename ends with ".md"
    if not filename.endswith('.md'):
        filename += ".md"

    # Save the blog file (For demonstration purposes)
    os.makedirs('output', exist_ok=True)
    file_path = os.path.join('output', filename)
    with open(file_path, 'w') as f:
        f.write(f"Blog content for: {query}")

    return jsonify({'message': 'Blog created successfully', 'filename': filename})

if __name__ == '__main__':
    app.run(debug=True,port=8000)
