import time
import random
import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By

# 配置 Chrome WebDriver
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

def random_sleep(min_t=5, max_t=15):
    """在给定时间范围内随机休眠，避免被封"""
    sleep_time = random.uniform(min_t, max_t)
    print(f"⏳ 休眠 {sleep_time:.2f} 秒...")
    time.sleep(sleep_time)

def is_captcha_page():
    """检查当前页面是否为验证码页面"""
    try:
        captcha_element = driver.find_element(By.XPATH, "//div[contains(@class, 'g-recaptcha')]")
        return True
    except:
        return False

def get_bibtex_and_abstract(title):
    """在 Google Scholar 手动搜索后，自动获取 BibTeX 和摘要"""
    driver.get("https://scholar.google.com")
    random_sleep(1, 3)

    # 输入搜索内容并提交
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(title)
    search_box.submit()
    random_sleep(2, 4)

    # 检查验证码
    if is_captcha_page():
        input("⚠️ 请手动完成验证码，然后按 Enter 继续...")

    # 找到第一个论文的 "Cite" 按钮
    cite_button = driver.find_element(By.XPATH, "//a[contains(@class, 'gs_or_cit')]")
    cite_button.click()
    random_sleep(1, 3)

    # 检查验证码
    if is_captcha_page():
        input("⚠️ 请手动完成验证码，然后按 Enter 继续...")

    # 点击 BibTeX 选项
    bibtex_button = driver.find_element(By.LINK_TEXT, "BibTeX")
    bibtex_button.click()
    random_sleep(2, 4)

    # 检查验证码
    if is_captcha_page():
        input("⚠️ 请手动完成验证码，然后按 Enter 继续...")

    # 获取 BibTeX 代码
    bibtex_text = driver.find_element(By.TAG_NAME, "pre").text

    # 返回到论文列表
    driver.back()
    random_sleep(1, 2)
    driver.back()
    random_sleep(1, 2)

    # 尝试获取摘要
    try:
        abstract_element = driver.find_element(By.CLASS_NAME, "gs_fma_abs")
        abstract_text = abstract_element.text
    except:
        abstract_text = "Abstract not available."

    # 结果写入文件
    result = f"Title: {title}\nBibTeX:\n{bibtex_text}\nAbstract:\n{abstract_text}\n\n"
    print(result)

    with open("summary.txt", "a", encoding="utf-8") as file:
        file.write(result)
    with open("bibtex.txt", "a", encoding="utf-8") as file:
        file.write(f"{bibtex_text}\n\n")

    return bibtex_text, abstract_text

def load_titles(file_path):
    """从给定的文件路径读取论文标题列表"""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            titles = [line.strip() for line in file.readlines() if line.strip()]
        return titles
    except FileNotFoundError:
        print(f"❌ 文件 {file_path} 未找到，请检查路径！")
        return []

if __name__ == "__main__":
    # 解析命令行参数
    parser = argparse.ArgumentParser(description="从 Google Scholar 抓取 BibTeX 和摘要")
    parser.add_argument("titles_file", nargs="?", default="titles.txt", help="包含论文标题的文本文件路径（默认：titles.txt）")
    args = parser.parse_args()

    # 读取论文标题
    titles = load_titles(args.titles_file)

    if not titles:
        print("❌ 没有找到论文标题，程序终止。")
    else:
        print(f"📄 读取到 {len(titles)} 篇论文")

        for title in titles:
            get_bibtex_and_abstract(title)
            random_sleep(5, 15)  # 避免 IP 被封

    driver.quit()
