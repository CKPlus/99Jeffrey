# 99傑弗瑞小工具使用說明

## 說明

讀取各式內容包含 phonenumber 的 csv file，並轉換 phonenumber 成特定格式輸出

## 安裝套件

	pip install -r requires.txt

## 執行命令範例

    python parser.py Telexpress_yp_data_0515-2.csv 1 TW 1

## 參數說明 (自 parser.py 後第一個算起)

    1. 檔案名稱 (要跟 parse.py放在同一層)
    2. 指定號碼在 csv 內的第幾個 column (從 0 算起)
    3. region name 縮寫 (如 "TW", "US", "KR"...有點不確定每個國家的縮寫要再查)
    4. 輸出格式
           1 = +886223681234
       	   2 = 0223681234
       	   3 = 23681234

## 輸出檔案名稱

	result.csv



