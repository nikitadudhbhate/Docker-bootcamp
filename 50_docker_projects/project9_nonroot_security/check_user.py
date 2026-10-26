import os
import pwd

uid = os.getuid()
username = pwd.getpwuid(uid).pw_name

print(f"🔒 Current Container User: {username}")
print(f"🆔 User ID (UID): {uid}")

if uid == 0:
    print("⚠️ WARNING: Running as ROOT! This is a security risk in production.")
else:
    print("✅ SUCCESS: Running securely as a non-root user!")
