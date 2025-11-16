# blog.py
import os
import platform
import subprocess
from typing import List, Optional
from datetime import datetime
from googletrans import Translator
from gtts import gTTS
from db import get_conn

# Ensure audio folder exists
AUDIO_DIR = "audio"
os.makedirs(AUDIO_DIR, exist_ok=True)

class Blog:
    def __init__(self, title: str, content: str, id: Optional[int]=None,
                 created_at: Optional[str]=None, updated_at: Optional[str]=None):
        self.id = id
        self.title = title
        self.content = content
        self.created_at = created_at
        self.updated_at = updated_at

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

    def save(self):
        sql = """
        INSERT INTO blogs (title, content)
        VALUES (%s, %s)
        RETURNING id, created_at, updated_at;
        """
        with get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (self.title, self.content))
                row = cur.fetchone()
                conn.commit()
        if row:
            self.id = row["id"]
            self.created_at = row["created_at"].isoformat()
            self.updated_at = row["updated_at"].isoformat()
        return self

    def update(self):
        if not self.id:
            raise ValueError("Cannot update blog without id.")
        sql = """
        UPDATE blogs
        SET title = %s, content = %s, updated_at = NOW()
        WHERE id = %s
        RETURNING updated_at;
        """
        with get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (self.title, self.content, self.id))
                row = cur.fetchone()
                conn.commit()
        if row:
            self.updated_at = row["updated_at"].isoformat()
        return self

    def delete(self):
        if not self.id:
            raise ValueError("Blog must have id to delete.")
        sql = "DELETE FROM blogs WHERE id = %s;"
        with get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (self.id,))
                conn.commit()
        return True
    
    @staticmethod
    def get_all() -> List['Blog']:
        sql = "SELECT id, title, content, created_at, updated_at FROM blogs ORDER BY id;"
        with get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                rows = cur.fetchall()
        blogs = list(map(lambda r: Blog(r["title"], r["content"],
                                        id=r["id"],
                                        created_at=r["created_at"].isoformat(),
                                        updated_at=r["updated_at"].isoformat()), rows))
        return blogs

    @staticmethod
    def get_by_id(blog_id: int) -> Optional['Blog']:
        sql = "SELECT id, title, content, created_at, updated_at FROM blogs WHERE id = %s;"
        with get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (blog_id,))
                row = cur.fetchone()
        if not row:
            return None
        return Blog(row["title"], row["content"],
                    id=row["id"],
                    created_at=row["created_at"].isoformat(),
                    updated_at=row["updated_at"].isoformat())

    def translate_text(self, source_lang: str, target_lang: str) -> str:
        try:
            translator = Translator()
            result = translator.translate(self.content, src=source_lang, dest=target_lang)
            return result.text
        except Exception as e:
            raise RuntimeError(f"Translation failed: {e}")

    def translate_and_speak(self, source_lang: str, target_lang: str, play_audio: bool=False) -> dict:
        if not self.id:
            raise ValueError("Blog must have id to generate audio filename.")
        translated = self.translate_text(source_lang, target_lang)

        filename = os.path.join(AUDIO_DIR, f"blog_{self.id}_audio.mp3")
        try:
            tts = gTTS(text=translated, lang=target_lang)
            tts.save(filename)
        except Exception as e:
            raise RuntimeError(f"TTS generation failed: {e}")

        return {"translated": translated, "audio_file": filename}