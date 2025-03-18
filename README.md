### 📖 中文版 README  

# 📚 ref-bib-harvester  

**ref-bib-harvester** 是一个自动化工具，能够从 Google Scholar 批量抓取学术论文的 **BibTeX** 和 **摘要**，帮助你快速整理参考文献，提高学术写作效率。  

---

## 🚀 使用方法  

### 1️⃣ 安装依赖  
请确保你的环境已安装 Python，然后运行以下命令安装必要的依赖库：  

```bash
pip install selenium webdriver-manager beautifulsoup4
```

### 2️⃣ 运行脚本  
执行以下命令启动抓取过程：  

```bash
python fetch_bibs.py
```

在运行过程中，Google Scholar 可能会要求你**手动完成验证码**。遇到验证码时，请按照页面提示操作，并在完成后**按 Enter 继续**。  

---

## 📄 输出文件  

执行脚本后，将生成以下两个文件（如果文件已存在，将自动追加内容，而不会覆盖）：  

📌 **bibtex.txt**：包含所有论文的 BibTeX 数据，可直接粘贴到 LaTeX 项目中。  
📌 **summary.txt**：包含论文标题、BibTeX 信息和摘要，可用于整理参考文献或提供给 LLM 生成 Related Works 部分。  

---

## 📝 自定义文章列表  

要更改要抓取的论文列表，请直接编辑 **fetch_bibs.py** 文件，在其中添加或修改论文标题。  

---

## 🎯 应用场景  

✅ **论文写作**：快速整理参考文献，直接获取 BibTeX。  
✅ **LLM 辅助**：将 summary.txt 提供给大语言模型（LLM），自动生成 Related Works 部分。  
✅ **高效文献管理**：无需手动查找和复制 BibTeX，提高科研效率。  

---

### 📖 English Version  

# 📚 ref-bib-harvester  

**ref-bib-harvester** is an automation tool that **batch-fetches** academic papers' **BibTeX** and **abstracts** from Google Scholar, making it easier to manage references and streamline academic writing.  

---

## 🚀 Usage  

### 1️⃣ Install Dependencies  
Ensure you have Python installed, then install the required libraries:  

```bash
pip install selenium webdriver-manager beautifulsoup4
```

### 2️⃣ Run the Script  
Start the fetching process by running:  

```bash
python fetch_bibs.py
```

During execution, Google Scholar may require **manual CAPTCHA verification**. If prompted, complete the CAPTCHA and press **Enter to continue**.  

---

## 📄 Output Files  

After running the script, two output files will be generated (if they already exist, new content will be appended instead of overwritten):  

📌 **bibtex.txt** – Contains BibTeX entries for all retrieved papers, ready to be pasted into LaTeX.  
📌 **summary.txt** – Includes paper titles, BibTeX entries, and abstracts, which can be used for literature review or fed into LLMs for **automated Related Works generation**.  

---

## 📝 Customizing the Paper List  

To modify the list of papers to fetch, simply edit the **fetch_bibs.py** file and add or update paper titles.  

---

## 🎯 Use Cases  

✅ **Academic Writing** – Quickly gather references and retrieve BibTeX data.  
✅ **LLM Assistance** – Use summary.txt as input for an LLM to generate a **Related Works** section.  
✅ **Efficient Literature Management** – No need to manually search for and copy BibTeX, saving time.  

---

## 🔗 Contributions & Feedback  

Feel free to submit issues or contribute to this project! 🚀  