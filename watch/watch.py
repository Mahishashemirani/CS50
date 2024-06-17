import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    match = re.search(r'^.*iframe src=\"(?:https?://)?(?:w{3}\.)?youtube\.com/(?:embed/)?([a-zA-Z0-9_-]{11})\".*$', s, re.IGNORECASE)
    if match:
        return f"https://youtu.be/{match.group(1)}"
    else:
        return None

if __name__ == "__main__":
    main()
