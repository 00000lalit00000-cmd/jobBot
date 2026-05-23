import instaloader
import hashlib


def _make_id(username, shortcode):
    return hashlib.sha1(f'{username}|{shortcode}'.encode('utf-8')).hexdigest()


def fetch_latest_posts(username, max_count=5):
    loader = instaloader.Instaloader(
        download_pictures=False,
        download_video_thumbnails=False,
        save_metadata=False,
        compress_json=False,
        download_comments=False,
        post_metadata_txt_pattern=''
    )
    posts = []
    try:
        profile = instaloader.Profile.from_username(loader.context, username)
        for post in profile.get_posts():
            posts.append({
                'id': _make_id(username, post.shortcode),
                'title': f'Instagram post from {username}',
                'company': username,
                'location': '',
                'url': f'https://www.instagram.com/p/{post.shortcode}/',
                'posted_at': post.date_utc.isoformat(),
                'source': f'instagram:{username}',
                'text': post.caption or ''
            })
            if len(posts) >= max_count:
                break
    except Exception:
        return []
    return posts
