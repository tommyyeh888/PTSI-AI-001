import psycopg2

try:
    # 這裡請完全複製 `test_neon.py` 內的正確連線方式
    conn = psycopg2.connect(
        dbname="neondb",
        user="neondb_owner",
        password="npg_siz7Iqc0ZPRD",  # 這裡請替換成你的正確密碼
        host="ep-broad-thunder-a13ihwuu-pooler.ap-southeast-1.aws.neon.tech",
        port=5432,  # port 必須是數字
        sslmode="require"
    )
    cursor = conn.cursor()
    print("✅ 成功連接到 Neon 資料庫！")

    # **建立工程師表**
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS engineers (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            phone TEXT NOT NULL UNIQUE,
            line_id TEXT UNIQUE
        );
    """)

    # **建立客戶表**
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            address TEXT NOT NULL,
            contact TEXT
        );
    """)

    # **建立完工回報表**
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS work_reports (
            id SERIAL PRIMARY KEY,
            engineer_id INTEGER REFERENCES engineers(id),
            customer_id INTEGER REFERENCES customers(id),
            description TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    # **建立照片表**
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS photos (
            id SERIAL PRIMARY KEY,
            work_report_id INTEGER REFERENCES work_reports(id) ON DELETE CASCADE,
            photo_url TEXT NOT NULL
        );
    """)

    conn.commit()
    print("✅ 資料表已成功建立！")

    cursor.close()
    conn.close()
except Exception as e:
    print("❌ 連接失敗：", e)
