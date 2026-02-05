#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tech-Pulse Skill: Fetch top 5 trending tech stories from HackerNews API.
No API key required - uses free, public endpoint.
Keeps AI Agents contextually aware of today's tech landscape.
"""

import sys
import io
import urllib.request
import json
from datetime import datetime
from typing import List, Dict

# Set UTF-8 encoding on Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

HACKERNEWS_API = "https://hacker-news.firebaseio.com/v0"

def fetch_top_stories(limit: int = 5) -> List[Dict]:
    """
    Fetch top stories from HackerNews.
    
    Args:
        limit: Number of stories to fetch (default: 5)
    
    Returns:
        List of story dictionaries with title, url, score, etc.
    """
    print(f"📰 Fetching top {limit} tech stories from HackerNews...\n")
    
    try:
        # Get list of top story IDs
        with urllib.request.urlopen(f"{HACKERNEWS_API}/topstories.json", timeout=5) as response:
            story_ids = json.loads(response.read().decode('utf-8'))[:limit]
        
        stories = []
        for idx, story_id in enumerate(story_ids, 1):
            try:
                with urllib.request.urlopen(f"{HACKERNEWS_API}/item/{story_id}.json", timeout=5) as response:
                    story = json.loads(response.read().decode('utf-8'))
                    
                    # Filter for tech-relevant stories
                    if story.get('type') == 'story' and story.get('url'):
                        stories.append({
                            'rank': idx,
                            'title': story.get('title', 'N/A'),
                            'url': story.get('url', ''),
                            'score': story.get('score', 0),
                            'author': story.get('by', 'Anonymous'),
                            'comments': story.get('descendants', 0),
                        })
            except Exception as e:
                print(f"⚠️  Warning: Failed to fetch story {story_id}: {e}")
        
        return stories
    
    except urllib.error.URLError as e:
        raise Exception(f"Failed to fetch HackerNews data: {e}")

def format_story(story: Dict) -> str:
    """Format a single story for display."""
    return f"""
**#{story['rank']}. {story['title']}**
- 🔗 URL: {story['url']}
- 👤 Author: {story['author']}
- 📈 Score: {story['score']} | 💬 Comments: {story['comments']}"""

def main():
    """Main execution function."""
    print("🔥 Tech-Pulse: Today's Top Tech Stories\n")
    print(f"⏰ Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}\n")
    print("-" * 80 + "\n")
    
    stories = fetch_top_stories(limit=5)
    
    print("📊 Top 5 Trending Stories:\n")
    for story in stories:
        print(format_story(story))
    
    print("\n" + "-" * 80)
    print("\n✅ Context loaded! AI agents can now stay aware of tech trends.\n")

if __name__ == "__main__":
    main()
