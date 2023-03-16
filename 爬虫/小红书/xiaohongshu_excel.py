from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import xlsxwriter


def crawler_3():
    # 设置excel
    # 设置表格名称
    workbook = xlsxwriter.Workbook('小红书成都、杭州、上海美食探店.xlsx')
    # 增加一个sheet
    worksheet = workbook.add_worksheet()
    # 设置表头
    headings = ['小红书链接', '城市', '标题', '内容']
    # 整行写入
    worksheet.write_row('A1', headings)

    options = Options()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
    browser = webdriver.Chrome(options=options)

    url_list = []
    filename = './url.txt'
    file = open(filename, 'r', encoding='utf-8')
    for line in file.readlines():
        url_list.append('http' + line.split('http')[1].split('，')[0])
    # 行数
    column = 1
    for url in url_list:
        column = column + 1
        print(url)
        browser.get(url)
        time.sleep(0.5)
        # 输出：标题
        title = browser.find_elements(by=By.CLASS_NAME, value='title')
        if(len(title) < 1):
            continue
        # print('标题：' + title[0].text)
        # 输出：内容
        desc = browser.find_elements(by=By.CLASS_NAME, value='desc')

        videoFlag = browser.find_elements(by=By.ID,value='videoPlayer')
        if(len(videoFlag) > 0):
            continue
        file_title = title[0].text
        if(file_title.__contains__('|')):
            file_title = file_title.replace('|','｜')
        # 整行写入
        if(column < 52):
            data_xhs = [url, '上海', title[0].text, desc[0].text]
        elif(column < 82):
            data_xhs = [url, '杭州', title[0].text, desc[0].text]
        else:
            data_xhs = [url, '成都', title[0].text, desc[0].text]
        worksheet.write_row('A' + str(column),data_xhs)

    workbook.close()

if __name__ == '__main__':
    crawler_3()