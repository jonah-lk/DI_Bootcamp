# api.py
import os
from flask import Flask, request, jsonify, abort
from dotenv import load_dotenv
from db import init_db
from blog import Blog

load_dotenv()

app = Flask(__name__)

init_db()

def _validate_blog_payload(data):
    if not data:
        abort(400, description="Missing JSON payload.")
    title = data.get("title")
    content = data.get("content")
    if not title or not isinstance(title, str):
        abort(400, description="Field 'title' is required and must be a string.")
    if not content or not isinstance(content, str):
        abort(400, description="Field 'content' is required and must be a string.")
    return title, content

@app.route("/blogs", methods=["POST"])
def create_blog():
    data = request.get_json()
    title, content = _validate_blog_payload(data)
    blog = Blog(title=title, content=content)
    try:
        blog.save()
    except Exception as e:
        abort(500, description=str(e))
    return jsonify(blog.to_dict()), 201

@app.route("/blogs", methods=["GET"])
def list_blogs():
    blogs = Blog.get_all()
    filtered = list(filter(lambda b: bool(b.content and b.content.strip()), blogs))
    blogs_json = list(map(lambda b: b.to_dict(), filtered))
    for bj in blogs_json:
        bj["summary"] = (bj["content"][:120] + "...") if len(bj["content"]) > 120 else bj["content"]
    return jsonify(blogs_json), 200

@app.route("/blogs/<int:blog_id>", methods=["GET"])
def get_blog(blog_id):
    blog = Blog.get_by_id(blog_id)
    if not blog:
        abort(404, description="Blog not found.")
    return jsonify(blog.to_dict()), 200

@app.route("/blogs/<int:blog_id>", methods=["PUT"])
def update_blog(blog_id):
    blog = Blog.get_by_id(blog_id)
    if not blog:
        abort(404, description="Blog not found.")
    data = request.get_json()
    title, content = _validate_blog_payload(data)
    blog.title = title
    blog.content = content
    try:
        blog.update()
    except Exception as e:
        abort(500, description=str(e))
    return jsonify(blog.to_dict()), 200

@app.route("/blogs/<int:blog_id>", methods=["DELETE"])
def delete_blog(blog_id):
    blog = Blog.get_by_id(blog_id)
    if not blog:
        abort(404, description="Blog not found.")
    try:
        blog.delete()
    except Exception as e:
        abort(500, description=str(e))
    return jsonify({"message": "Deleted"}), 200

# Trans/TTS
@app.route("/blogs/<int:blog_id>/translate", methods=["GET"])
def translate_blog(blog_id):
    source = request.args.get("source")
    target = request.args.get("target")
    if not source or not target:
        abort(400, description="Query parameters 'source' and 'target' required: ?source=fr&target=en")
    blog = Blog.get_by_id(blog_id)
    if not blog:
        abort(404, description="Blog not found.")

    try:
        result = blog.translate_and_speak(source, target)
    except Exception as e:
        abort(500, description=str(e))

    return jsonify({
        "id": blog.id,
        "original_title": blog.title,
        "original_content": blog.content,
        "translated_content": result["translated"],
        "audio_file": result["audio_file"]
    }), 200

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(port=5000)