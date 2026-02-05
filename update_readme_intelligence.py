#!/usr/bin/env python3
"""
Update README with latest tech intelligence from Tech-Pulse.
Used by GitHub Actions daily workflow.
"""

import re
import sys
import json
import urllib.request
from datetime import datetime, timezone

HACKERNEWS_API = "https://hacker-news.firebaseio.com/v0"

def fetch_top_stories(limit: int = 5):
    """Fetch top stories from HackerNews."""
    try:
        with urllib.request.urlopen(f"{HACKERNEWS_API}/topstories.json", timeout=5) as response:
            story_ids = json.loads(response.read().decode('utf-8'))[:limit]
        
        stories = []
        for idx, story_id in enumerate(story_ids, 1):
            try:
                with urllib.request.urlopen(f"{HACKERNEWS_API}/item/{story_id}.json", timeout=5) as response:
                    story = json.loads(response.read().decode('utf-8'))
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
                pass
        
        return stories
    except Exception as e:
        print(f"Error fetching stories: {e}", file=sys.stderr)
        return []

def format_stories(stories):
    """Format stories for README."""
    if not stories:
        return "⚠️ Unable to fetch tech stories at this time."
    
    formatted = "### 📊 Top 5 Trending Tech Stories\n\n"
    for story in stories:
        formatted += f"**#{story['rank']}. {story['title']}**\n"
        formatted += f"- 🔗 [Read on HackerNews]({story['url']})\n"
        formatted += f"- 👤 By {story['author']} | 📈 {story['score']} points | 💬 {story['comments']} comments\n\n"
    
    return formatted

def update_readme():
    """Update README with latest tech intelligence."""
    try:
        # Fetch stories
        stories = fetch_top_stories(limit=5)
        formatted_stories = format_stories(stories)
        
        # Read README
        with open('README.md', 'r', encoding='utf-8') as f:
            readme = f.read()
        
        # Create updated section
        today = datetime.now(timezone.utc).strftime('%B %d, %Y')
        new_section = f"""## 🚀 Today's Agent Intelligence

> **Last Updated:** {today}

{formatted_stories}

> *This section is auto-updated daily with trending tech intelligence.*
"""
        
        # Replace the section (handles different formats)
        pattern = r'## 🚀 Today\'s Agent Intelligence\n\n>.*?\n\n.*?\n\n> \*This section is auto-updated daily.*?\*\n'
        
        if re.search(pattern, readme, re.DOTALL):
            updated_readme = re.sub(pattern, new_section + '\n', readme, flags=re.DOTALL)
        else:
            # Section doesn't exist in expected format, just append/replace by finding the section
            pattern = r'## 🚀 Today\'s Agent Intelligence.*?(?=\n## |\Z)'
            updated_readme = re.sub(pattern, new_section.rstrip(), readme, flags=re.DOTALL)
        
        # Write back
        with open('README.md', 'w', encoding='utf-8') as f:
            f.write(updated_readme)
        
        print(f"✅ README updated successfully at {today}")
        return 0
    
    except Exception as e:
        print(f"❌ Error updating README: {e}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(update_readme())
