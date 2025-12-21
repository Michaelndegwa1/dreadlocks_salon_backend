import os
import psycopg2

url = "postgresql://postgres:MkScLsEkkgbcmobQvagAEQKCunZUSEcy@postgres-production-6900.up.railway.app:5432/railway"

try:
    conn = psycopg2.connect(url)
    print("Connection successful!")
    cur = conn.cursor()
    cur.execute("SELECT 1")
    print("Query successful!")
    cur.close()
    conn.close()
except Exception as e:
    print(f"Connection failed: {e}")
