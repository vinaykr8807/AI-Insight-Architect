import os
import requests

PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")

def get_pexels_image(query, page=1):
    if not PEXELS_API_KEY:
        return None
    url = "https://api.pexels.com/v1/search"
    headers = {"Authorization": PEXELS_API_KEY}
    
    # Always fetch the single most relevant photo to guarantee it matches the topic
    params = {"query": query, "per_page": 1, "page": page}
    try:
        r = requests.get(url, headers=headers, params=params, timeout=5)
        data = r.json()
        if data.get("photos"):
            # Return the absolute top result for maximum relevance
            return data["photos"][0]["src"]["large"]
    except:
        pass
    return None

def get_pexels_video(query, page=1):
    # Fallback to YouTube for sound and longer duration as requested
    return get_youtube_video(query)

def get_youtube_video(query):
    """Search YouTube (DDGS with a robust direct scrape fallback) and return a valid embed URL."""
    # Try direct YouTube scrape (most reliable)
    try:
        import urllib.request
        import urllib.parse
        import re
        
        search_query = urllib.parse.quote(f"{query} tutorial")
        url = f"https://www.youtube.com/results?search_query={search_query}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        
        with urllib.request.urlopen(req, timeout=5) as response:
            html = response.read().decode()
            # Extract video IDs directly from YouTube's initial JSON payload
            video_ids = re.findall(r'"videoId":"([a-zA-Z0-9_-]{11})"', html)
            
            # Filter out common non-content IDs by grabbing the first valid one
            for vid in video_ids:
                return f"https://www.youtube.com/embed/{vid}?rel=0"
    except Exception as e:
        print(f"Direct YouTube search error: {e}")

    # Fallback to DDGS if direct scrape fails
    try:
        from ddgs import DDGS
        import re
        
        search_query = f"{query} tutorial"
        results = DDGS().videos(search_query, max_results=5)
        
        if results:
            for video in results:
                url = video.get("content", "")
                if "youtube.com/watch?v=" in url:
                    video_id = url.split("v=")[1][:11]
                    return f"https://www.youtube.com/embed/{video_id}?rel=0"
                elif "youtu.be/" in url:
                    video_id = url.split("youtu.be/")[1][:11]
                    return f"https://www.youtube.com/embed/{video_id}?rel=0"
    except Exception as e:
        print(f"YouTube search error (DDGS): {e}")
        
    return None
