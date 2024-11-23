import requests
import openpyxl

# 文件名定义
input_file = "addresses.txt"  # 输入文件，包含地址
output_file = "output.xlsx"   # 输出文件

# 初始化 Excel 工作簿
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Airdrop Results"
ws.append(["Address", "Total Amount"])  # 添加表头

# URL 和 Headers
url = "https://insider.side.one/airdrop/login/checkEligibility"

# 从文件中读取地址
with open(input_file, "r") as file:
    addresses = file.read().splitlines()

# 遍历地址并获取数据
for address in addresses:
    try:
        # 请求数据
        response = requests.get(url, params={"address": address})
        response.raise_for_status()  # 检查请求是否成功
        
        # 解析 JSON 响应
        data = response.json()
        total_amount = data.get("totalAmount", 0)  # 获取 totalAmount

        # 将结果写入 Excel
        ws.append([address, total_amount])
        print(f"Processed address: {address}, Total Amount: {total_amount}")
    
    except Exception as e:
        print(f"Error processing address {address}: {e}")

# 保存结果到 Excel 文件
wb.save(output_file)
print(f"Results saved to {output_file}")