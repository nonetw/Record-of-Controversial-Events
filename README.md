# Record-of-Controversial-Events
There is just records. To buy or not to buy is your choice.

使用說明：
表格內容資料放在 data/events.csv
格式為 date,company,tags,summary,links,screenshots
date(日期): 無固定格式
tags(標籤): 可以多個，請用逗號分隔
summary(事件簡述): 如果需要分行請用 <br>
links(網址): 可以多個，請用分號分隔
screenshots(紀錄截圖): 可以多個，請用分號分隔，只寫檔名，請於 images 底下依 company(名稱) 放置圖片檔案

範例：
date,company,tags,summary,links,screenshots
2021,Philips,"中國品牌,家電","飛利浦將家電部門出售給中國高瓴資本<br>PS. 飛利浦健康生活(Philips Personal Health)應仍為荷蘭廠商","台灣飛利浦|https://www.store-philips.tw/page/0701?lang=zh-TW;Reuters|https://www.reuters.com/world/china/chinas-hillhouse-capital-buy-philips-appliances-arm-37-bln-euros-2021-03-25/","20210701_store-philips.tw.jpeg;20210325_reuters.jpeg"

20210701_store-philips.tw.jpeg, 20210325_reuters.jpeg 檔案放在 images/Philips/ 底下

以上完成後於 repository 主目錄執行
tools/build_events.py 以更新 partials/events.html