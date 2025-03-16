import sys
from textblob import TextBlob

def analyze_commit(commit_msg):
    blob = TextBlob(commit_msg)
    
    # Example: Block commits with negative sentiment or short messages
    if len(commit_msg) < 10 or blob.sentiment.polarity < -0.25:
        return "BLOCK: Commit message is too short or negative"
        sys.exit(1)
    return "PASS: Commit message is good"

if __name__ == "__main__":
    commit_message = sys.argv[1]
    print(analyze_commit(commit_message))
