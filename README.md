# Record-of-Controversial-Events
就是個拿來存放紀錄的小地方。<br>


使用說明：<br>
紀錄內容資料放在 data/events.csv<br>
CSV 格式為 date,company,tags,summary,links,screenshots<br>
date(日期): 無固定格式<br>
tags(標籤): 可以多個，請用逗號分隔<br>
summary(事件簡述): 如果需要分行請用 \<br\><br>
links(網址): 可以多個，請用分號分隔<br>
screenshots(紀錄截圖): 可以多個，請用分號分隔，只寫檔名，請於 images 底下依 company(名稱) 建目錄放置圖片檔案<br>

events.csv 範例：<br>
date,company,tags,summary,links,screenshots<br>
2025,OrgNameX,"TagX,TagYZ","OrgNameX XXX事件簡述\<br\>集團相關：X1, X2, X3","XXX1|https://x1/;XXX2|https://x2/","1.jpeg;2.jpeg"<br>

1.jpeg, 2.jpeg 檔案放在 images/OrgNameX/ 底下<br>

以上完成後於 repository 主目錄執行<br>
tools/build_events.py 以更新 partials/events.html
以瀏覽器開啟 index.html 檢視成果