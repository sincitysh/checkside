
# Cosmos Address to Excel Exporter

## 简介  
这是一个简单的 Python 脚本，用于从文件中读取 Cosmos 地址，通过查询 API 检测是否有空投资格，并将结果导出到 Excel 文件中。导出的 Excel 文件包含地址及其对应的代币数量。

---

## 功能  
1. **读取地址**：从本地文件加载 Cosmos 地址列表（每行一个地址）。  
2. **查询空投信息**：通过调用 API 获取每个地址的空投资格和代币数量。  
3. **导出结果**：将地址及其空投数量保存到 Excel 文件，格式为：  
   ```
   地址       数量
   cosmos1...  100
   cosmos1...  0
   ```

---

## 使用方法

### 1. 安装依赖  
确保你的环境安装了 Python，并使用以下命令安装依赖：  
```bash
pip install requests openpyxl
```

### 2. 准备输入文件  
创建一个文本文件，例如 `addresses.txt`，文件内容格式如下：  
```
cosmos1w6exhwqnts6jn3jrcv0zuazdenvt3dffr7zug8
cosmos1abc...
cosmos1xyz...
```

### 3. 运行脚本  
运行脚本
```bash
python CheckSide.py 
```

---

## 输出说明  
脚本运行后，将生成一个名为 `output.xlsx` 的 Excel 文件，包含以下两列：  
- **地址**：从输入文件读取的 Cosmos 地址。  
- **数量**：对应地址的空投代币数量。  

---

## 开发环境  
- **Python 版本**：3.8 或以上  
- **依赖库**：  
  - `requests`：用于 API 调用。  
  - `openpyxl`：用于生成 Excel 文件。  

---

## 贡献  
欢迎提交 Pull Request 或建议。任何问题可以通过 Issue 反馈。

---

## 许可  
该项目基于 [MIT License](https://opensource.org/licenses/MIT) 开源。  
