import csv
import re
import time
from pathlib import Path
from urllib.parse import urljoin

import requests
from lxml import etree


BASE_URL = 'https://c.gongkong.com/'
OUTPUT_FILE = Path(__file__).with_name('中国工控网.csv')
HEAD = ['公司名称', '详情页url', '邮箱', '网址', '电话', '地址', '邮编/联系人', '传真']
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}


def clean_text(value):
    """把网页排版使用的空白统一为一个普通空格。"""
    value = value.replace('&nbsp;', ' ').replace('&emsp;', ' ')
    return re.sub(r'\s+', ' ', value).strip()


def node_text(node):
    """取一个 HTML 节点中的全部文字，并统一清洗。"""
    return clean_text(' '.join(node.xpath('.//text()')))


def first_text(tree, xpath):
    values = tree.xpath(xpath)
    return clean_text(values[0]) if values else ''


def labeled_fields(paragraphs):
    """把形如“标签：值”的 p 标签整理成字典。"""
    fields = {}
    for paragraph in paragraphs:
        text = node_text(paragraph)
        if '：' not in text:
            continue
        label, value = text.split('：', 1)
        fields[re.sub(r'\s+', '', label)] = clean_text(value)
    return fields


def parse_detail(tree, company_name):
    """兼容工控网目前两种详情页结构，并始终返回 6 个详情字段。"""
    contact_blocks = tree.xpath('//div[contains(@class, "y_Contact_text")]')
    if contact_blocks:
        all_fields = [labeled_fields(block.xpath('./p')) for block in contact_blocks]
        fields = all_fields[0]
        for candidate in all_fields:
            detail_name = candidate.get('名称', '')
            if detail_name and (detail_name in company_name or company_name in detail_name):
                fields = candidate
                break
        return [
            fields.get('Email', ''),
            fields.get('网址', ''),
            fields.get('电话', ''),
            fields.get('地址', ''),
            fields.get('邮编', ''),
            fields.get('传真', ''),
        ]

    fields = labeled_fields(tree.xpath('//p[./b]'))
    contact = first_text(tree, '//h1[@id="Rtitle_D"]/text()')
    return [
        fields.get('邮箱', ''),
        fields.get('网址', ''),
        fields.get('电话', ''),
        fields.get('地址', ''),
        contact,
        '',
    ]


def get_tree(session, url):
    response = session.get(url, timeout=15)
    response.raise_for_status()
    return etree.HTML(response.content)


def main():
    rows = []
    with requests.Session() as session:
        session.headers.update(HEADERS)
        home_tree = get_tree(session, BASE_URL)
        links = home_tree.xpath('//div[contains(@class, "main_bot_l_text")]//ul/li/a')

        for index, link in enumerate(links, 1):
            company_name = node_text(link)
            detail_url = urljoin(BASE_URL, link.get('href'))
            print(f'[{index}/{len(links)}] {company_name} {detail_url}')

            try:
                detail_fields = parse_detail(get_tree(session, detail_url), company_name)
            except requests.RequestException as error:
                print(f'  请求失败：{error}')
                detail_fields = ['', '', '', '', '', '']

            rows.append([company_name, detail_url, *detail_fields])
            time.sleep(0.2)

    with OUTPUT_FILE.open('w', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(HEAD)
        writer.writerows(rows)


if __name__ == '__main__':
    main()
