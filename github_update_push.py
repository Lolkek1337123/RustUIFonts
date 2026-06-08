import subprocess
import os

token_path = r"c:\AI_Antigravity\github.txt"
with open(token_path, "r", encoding="utf-8") as f:
    token = f.read().strip()

owner = "Lolkek1337123"
repo_name = "RustUIFonts"
repo_url = f"https://{owner}:{token}@github.com/{owner}/{repo_name}.git"
cwd_dir = r"c:\AI_Antigravity\RustFonts"

# Git add and commit
subprocess.run(["git", "add", "."], check=True, cwd=cwd_dir)
subprocess.run(["git", "commit", "-m", "Rename files to remove spaces and update README to embed image previews"], check=True, cwd=cwd_dir)

# Update remote URL with token
subprocess.run(["git", "remote", "set-url", "origin", repo_url], check=True, cwd=cwd_dir)

# Push
print("Pushing updates to GitHub...")
result = subprocess.run(["git", "push", "origin", "main", "--force"], cwd=cwd_dir, capture_output=True, text=True)
if result.returncode == 0:
    print("PUSH_SUCCESS")
else:
    err = result.stderr.replace(token, "********")
    print(f"PUSH_FAILED: {err}")

# Restore clean remote URL in local config
subprocess.run(["git", "remote", "set-url", "origin", f"https://github.com/{owner}/{repo_name}.git"], cwd=cwd_dir)
print("Cleaned up token from local git config.")
