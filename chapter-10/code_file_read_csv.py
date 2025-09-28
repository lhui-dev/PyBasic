import csv

# 打开csv文件
with open(file="test_csv_read.csv", mode="r", encoding="utf-8") as f:
        # 获取文件句柄
        cf = csv.reader(f)
        # 获取表头信息
        header = next(cf)
        scores = []
        for row in cf:
            # 处理信息
            scores.append(int(row[2]))
        print(sum(scores) / len(scores))