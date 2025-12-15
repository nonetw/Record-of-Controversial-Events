import os, csv, sys

# 專案根目錄（以本檔案為基準）
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT = os.path.join(BASE_DIR, "data", "events.csv")
OUTPUT = os.path.join(BASE_DIR, "partials", "events.html")
IMG_DIR = os.path.join(BASE_DIR, "images")

REQUIRED_HEADERS = ["date", "company", "tags", "summary", "links", "screenshots"]

def escape_html(s):
    return (s or "").replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")\
                    .replace('"',"&quot;").replace("'","&#39;")

def parse_links(raw):
    raw = (raw or "").strip()
    if not raw:
        return ""
    items = [x.strip() for x in raw.split(";") if x.strip()]
    html = []
    for item in items:
        if "|" in item:
            label, url = item.split("|", 1)
        else:
            label, url = item, item
        html.append(f'<a href="{escape_html(url)}" target="_blank">{escape_html(label)}</a>')
    return "<br>".join(html)

def parse_screenshots(raw, company):
    raw = (raw or "").strip()
    if not raw:
        return ""
    items = [x.strip() for x in raw.split(";") if x.strip()]
    html = []
    company_dir = os.path.join(IMG_DIR, company)
    if not os.path.isdir(company_dir):
        os.makedirs(company_dir, exist_ok=True)  # 自動建立公司目錄
    for name in items:
        path = os.path.join(company_dir, name)
        if os.path.exists(path):
            html.append(f'<a href="images/{escape_html(company)}/{escape_html(name)}" target="_blank">查看截圖</a>')
        else:
            html.append(f'<span style="color:red">缺檔: {escape_html(name)}</span>')
    return "<br>".join(html)

def main():
    if not os.path.exists(INPUT):
        raise FileNotFoundError(f"找不到 CSV 檔案: {INPUT}")
    if not os.path.isdir(os.path.dirname(OUTPUT)):
        os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)

    with open(INPUT, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or []
        missing = [h for h in REQUIRED_HEADERS if h not in headers]
        if missing:
            raise ValueError(f"CSV 欄位缺失: {missing}。必須包含: {REQUIRED_HEADERS}")

        rows = []
        for row in reader:
            date = escape_html(row.get("date",""))
            company = escape_html(row.get("company",""))
            tags_raw = row.get("tags","") or ""
            tags_list = [t.strip() for t in tags_raw.split(",") if t.strip()]
            tags_html = " ".join(f'<span class="tag">{escape_html(t)}</span>' for t in tags_list)
            summary_raw = row.get("summary","") or ""
            summary = escape_html(summary_raw).replace("&lt;br&gt;", "<br>")
            links_html = parse_links(row.get("links","") or "")
            screenshots_html = parse_screenshots(row.get("screenshots","") or "", row.get("company",""))

            tr = f"<tr><td>{date}</td><td>{company}</td><td>{tags_html}</td><td>{summary}</td><td>{links_html}</td><td>{screenshots_html}</td></tr>"
            rows.append(tr)

    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write("\n".join(rows))

    print(f"✅ 已生成: {OUTPUT}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"❌ 錯誤: {e}")
        sys.exit(1)