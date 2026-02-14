#!/usr/bin/env python3
"""
Twitter Media Uploader
Upload images/videos to Twitter and get media IDs for posting
"""

import os
import sys
import json
import mimetypes
from requests_oauthlib import OAuth1Session

# Twitter API credentials
CONSUMER_KEY = "qnuZrAAsXcAvcpmTY3yMQQXGe"
CONSUMER_SECRET = "C4pzqaqfGu8Vz8FwVdWpIKyoKxcdWFAbvLMU9971KffwXcP4t1"
ACCESS_TOKEN = "2021426499317018624-4qUWIkj9GUybgL3nAhYYs0Im4Hjijq"
ACCESS_TOKEN_SECRET = "smrhgjhdfMKft3yB78aZPLBp6SIXNEUpvpxMVgpswbE2f"


class MediaUploader:
    def __init__(self):
        self.oauth = OAuth1Session(
            CONSUMER_KEY,
            client_secret=CONSUMER_SECRET,
            resource_owner_key=ACCESS_TOKEN,
            resource_owner_secret=ACCESS_TOKEN_SECRET,
        )
        self.upload_url = "https://upload.twitter.com/1.1/media/upload.json"

    def upload_media(self, file_path, alt_text=None):
        """Upload media file and return media_id"""
        if not os.path.exists(file_path):
            return {"success": False, "error": f"File not found: {file_path}"}
        
        # Detect media type
        mime_type, _ = mimetypes.guess_type(file_path)
        if not mime_type:
            mime_type = "application/octet-stream"
        
        # Read file
        with open(file_path, 'rb') as f:
            files = {"media": f}
            response = self.oauth.post(self.upload_url, files=files)
        
        if response.status_code in [200, 201]:
            data = response.json()
            media_id = data["media_id_string"]
            
            # Add alt text if provided
            if alt_text:
                self.add_alt_text(media_id, alt_text)
            
            return {
                "success": True,
                "media_id": media_id,
                "size": data.get("size"),
                "type": mime_type
            }
        else:
            return {
                "success": False,
                "error": response.text,
                "status_code": response.status_code
            }

    def add_alt_text(self, media_id, alt_text):
        """Add alt text to uploaded media (accessibility)"""
        endpoint = "https://upload.twitter.com/1.1/media/metadata/create.json"
        payload = {
            "media_id": media_id,
            "alt_text": {"text": alt_text}
        }
        
        response = self.oauth.post(endpoint, json=payload)
        return response.status_code == 200

    def upload_multiple(self, file_paths, alt_texts=None):
        """Upload multiple media files (max 4 for images, 1 for video)"""
        if not alt_texts:
            alt_texts = [None] * len(file_paths)
        
        media_ids = []
        results = []
        
        for file_path, alt_text in zip(file_paths, alt_texts):
            result = self.upload_media(file_path, alt_text)
            results.append(result)
            
            if result["success"]:
                media_ids.append(result["media_id"])
        
        return {
            "success": len(media_ids) > 0,
            "media_ids": media_ids,
            "results": results
        }


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Upload media to Twitter")
    parser.add_argument("files", nargs="+", help="Media files to upload")
    parser.add_argument("--alt-text", action="append", 
                        help="Alt text for accessibility (repeat for multiple files)")
    parser.add_argument("--json", action="store_true",
                        help="Output JSON response")
    
    args = parser.parse_args()
    
    uploader = MediaUploader()
    
    if len(args.files) == 1:
        # Single file
        alt_text = args.alt_text[0] if args.alt_text else None
        result = uploader.upload_media(args.files[0], alt_text)
        
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            if result["success"]:
                print(f"✓ Media uploaded successfully!")
                print(f"  Media ID: {result['media_id']}")
                print(f"  Type: {result['type']}")
                print(f"  Size: {result.get('size', 'unknown')} bytes")
                print(f"\nUse with twitter-poster.py:")
                print(f"  python3 twitter-poster.py post --text 'Your text' --media-id {result['media_id']}")
            else:
                print(f"✗ Upload failed: {result['error']}", file=sys.stderr)
                sys.exit(1)
    else:
        # Multiple files
        result = uploader.upload_multiple(args.files, args.alt_text)
        
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            if result["success"]:
                print(f"✓ Uploaded {len(result['media_ids'])} media files!")
                for i, media_id in enumerate(result['media_ids'], 1):
                    print(f"  {i}. {media_id}")
                print(f"\nUse with twitter-poster.py:")
                media_ids_str = ",".join(result['media_ids'])
                print(f"  python3 twitter-poster.py post --text 'Your text' --media-ids {media_ids_str}")
            else:
                print(f"✗ Upload failed", file=sys.stderr)
                for r in result["results"]:
                    if not r["success"]:
                        print(f"  Error: {r['error']}", file=sys.stderr)
                sys.exit(1)


if __name__ == "__main__":
    main()
