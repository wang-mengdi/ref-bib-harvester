from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 打开 Chrome 浏览器（手动模式，不使用无头模式）
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

def is_captcha_page():
    """检查当前页面是否为验证码页面"""
    try:
        # 检查页面中是否存在验证码相关的元素（例如，'I'm not a robot' checkbox）
        captcha_element = driver.find_element(By.XPATH, "//div[contains(@class, 'g-recaptcha')]")
        return True
    except:
        return False

def get_bibtex_and_abstract(title):
    """在 Google Scholar 手动搜索后，自动获取 BibTeX 和 Abstract"""
    driver.get("https://scholar.google.com")
    time.sleep(2)

    # 在搜索框输入论文标题
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(title)
    search_box.submit()
    time.sleep(2)

    # **检查是否遇到验证码**
    if is_captcha_page():
        input("⚠️ 请手动完成验证码，然后按 Enter 继续...")

    # 找到第一个论文的 "Cite" 按钮（通过 class 定位）
    cite_button = driver.find_element(By.XPATH, "//a[contains(@class, 'gs_or_cit')]")
    cite_button.click()
    time.sleep(1)

    # **检查是否遇到验证码**
    if is_captcha_page():
        input("⚠️ 请手动完成验证码，然后按 Enter 继续...")

    # 点击 BibTeX 选项
    bibtex_button = driver.find_element(By.LINK_TEXT, "BibTeX")
    bibtex_button.click()
    time.sleep(2)

    # **检查是否遇到验证码**
    if is_captcha_page():
        input("⚠️ 请手动完成验证码，然后按 Enter 继续...")

    # 获取 BibTeX 代码
    bibtex_text = driver.find_element(By.TAG_NAME, "pre").text

    # 返回并获取摘要
    driver.back()  # 返回到论文列表页面
    time.sleep(1)
    driver.back()  # 返回到论文列表页面
    time.sleep(1)

    # 获取摘要
    try:
        # 直接从页面加载的摘要部分提取摘要
        abstract_element = driver.find_element(By.CLASS_NAME, "gs_fma_abs")
        abstract_text = abstract_element.text
    except:
        abstract_text = "Abstract not available."

    # 打印结果并将其追加到 summary.txt 文件中
    result = f"Title: {title}\nBibTeX:\n{bibtex_text}\nAbstract:\n{abstract_text}\n\n"
    print(result)

    # 将结果追加到文件
    with open("summary.txt", "a", encoding="utf-8") as file:
        file.write(result)
    with open("bibtex.txt", "a", encoding="utf-8") as file:
        file.write(f'{bibtex_text}\n\n')

    return bibtex_text, abstract_text

# 示例论文
titles = [
    "Simulating Water and Smoke with an Octree Data Structure",
    "Hybrid multigrid methods for high-order discontinuous Galerkin discretizations"
]

print(len(titles))

for title in titles:
    get_bibtex_and_abstract(title)
    time.sleep(10)  # 避免被封 IP

driver.quit()
