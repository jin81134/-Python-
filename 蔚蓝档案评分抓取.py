# coding:utf-8
import csv
import json
import os.path
import time
from datetime import datetime
import requests

file_name = "蔚蓝档案评分抓取_B站.csv"  # 数据保存位置1
file_name2 = "蔚蓝档案评分抓取_Tap.csv"  # 数据保存位置2
file_error_name = "蔚蓝档案评分抓取-出错信息.txt"  # 错误信息位置

while True:
    try:

        # "Bilibili数据"
        url = 'https://line1-h5-pc-api.biligame.com/game/comment/summary?game_base_id=109864&ts=1680585215754&request_id=ZgNwydOaxhj62MXUz3L1FgYrnIsudEgC&appkey=h9Ejat5tFh81cq8V&sign=39b48ab6cd61acf044cda2493af9d15e'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'}

        response = requests.get(url, headers=headers)
        data_dict = json.loads(response.text)
        Bili_ba_api = data_dict['data']['grade']  # 当前分数
        Bili_ba_api1 = data_dict['data']['comment_number']  # 评价人数
        # Bili_ba_api2 = data_dict['data']['valid_comment_number']  # 未知人数
        Bili_ba_api3 = data_dict['data']['star_number_list']  # 分段评分人数
        stra_1, stra_2, stra_3, stra_4, stra_5 = Bili_ba_api3  # 每个星级赋予不同变量,1,2,3,4,5
        average = (stra_1 * 1 + stra_2 * 2 + stra_3 * 3 + stra_4 * 4 + stra_5 * 5) / (
                    stra_1 + stra_2 + stra_3 + stra_4 + stra_5)*2
        print("B站评价 " + str(Bili_ba_api) + "分  " "评价人数 " + str(Bili_ba_api1) + "  1星" + str(stra_1) + "  2星" + str(
            stra_2) + "  3星" + str(stra_3) + "  4星" + str(stra_4) + "  5星" + str(stra_5) + "  计算评分" + str(average))

        # 获取当前时间
        now = datetime.now()
        minute = now.strftime("%Y-%m-%d %H:%M")  # 格式化为精确到分钟的字符串
        print("当前时间 " + minute)

        # 定义CSV文件的字段名称
        field_names = ['时间', 'Bilibili评分', '评价人数', '1星', '2星', '3星', '4星', '5星', '计算评分']  # 表头
        file_write = [minute, Bili_ba_api, Bili_ba_api1, stra_1, stra_2, stra_3, stra_4, stra_5, average]  # 写入变量数据

        # 检查CSV文件是否存在
        if os.path.exists(file_name):
            # 如果文件存在，则检查表头是否存在
            with open(file_name, 'r') as csvfile:
                reader = csv.reader(csvfile)
                headers = next(reader, None)  # 读取表头
                if headers == field_names:
                    print("表头已存在")
                    with open(file_name, mode='a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow(file_write)  # 写入变量数据
                else:
                    print("错误!!!  " + file_name + "的表头与定义的字段名称不匹配,请检查")
                    with open(file_name, mode='a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow(field_names)  # 写入CSV文件的表头
                        writer.writerow(file_write)  # 写入变量数据
                        exit(1)
        else:
            print("CSV文件不存在，已创建文件 " + file_name)
            with open(file_name, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(field_names)  # 写入CSV文件的表头
                writer.writerow(file_write)  # 写入变量数据

    # Bilibili错误信息输出
    except Exception as e:

        # 获取当前时间
        now = datetime.now()
        minute = now.strftime("%Y-%m-%d %H:%M")  # 格式化为精确到分钟的字符串
        print("当前时间" + minute)

        # 输出出错信息到文件
        with open(file_error_name, mode='a', newline='') as f:
            f.write(minute + " Bilibili错误信息 " + str(e) + '\r\n')
        print("Error:", e)

    try:

        # "TapTap数据"
        url = 'https://www.taptap.cn/webapiv2/app/v2/detail-by-id/316964?X-UA=V%3D1%26PN%3DWebApp%26LANG%3Dzh_CN%26VN_CODE%3D100%26VN%3D0.1.0%26LOC%3DCN%26PLT%3DPC%26DS%3DAndroid%26UID%3D403e642a-90ca-42a4-9bef-faa806d58dc1%26VID%3D3126483%26DT%3DPC%26OS%3DWindows%26OSV%3D10'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'}

        response = requests.get(url, headers=headers)
        data_dict = json.loads(response.text)
        Tap_ba_api = data_dict['data']['stat']['rating']['score']  # 当前分数
        Tap_ba_api1 = data_dict['data']['stat']['review_count']  # 评价人数
        Tap_ba_api2 = data_dict['data']['stat']['vote_info']['1']  # 分段评价人数 1星
        Tap_ba_api3 = data_dict['data']['stat']['vote_info']['2']  # 分段评价人数 2星
        Tap_ba_api4 = data_dict['data']['stat']['vote_info']['3']  # 分段评价人数 3星
        Tap_ba_api5 = data_dict['data']['stat']['vote_info']['4']  # 分段评价人数 4星
        Tap_ba_api6 = data_dict['data']['stat']['vote_info']['5']  # 分段评价人数 5星
        print("Tap评价 " + str(Tap_ba_api) + "分  " "评价人数 " + str(Tap_ba_api1) + "  1星" + str(Tap_ba_api2) + "  2星" + str(
            Tap_ba_api3) + "  3星" + str(Tap_ba_api4) + "  4星" + str(Tap_ba_api5) + "  5星" + str(Tap_ba_api6))

        # 获取当前时间
        now = datetime.now()
        minute = now.strftime("%Y-%m-%d %H:%M")  # 格式化为精确到分钟的字符串
        print("当前时间 " + minute)

        # 定义CSV文件的字段名称
        field_names = ['时间', 'Tap评分', '评价人数', '1星', '2星', '3星', '4星', '5星']  # 表头
        file_write = [minute, Tap_ba_api, Tap_ba_api1, Tap_ba_api2, Tap_ba_api3, Tap_ba_api4, Tap_ba_api5,
                      Tap_ba_api6]  # 写入变量数据

        # 检查CSV文件是否存在
        if os.path.exists(file_name2):
            # 如果文件存在，则检查表头是否存在
            with open(file_name2, 'r') as csvfile:
                reader = csv.reader(csvfile)
                headers = next(reader, None)  # 读取表头
                if headers == field_names:
                    print("表头已存在")
                    with open(file_name2, mode='a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow(file_write)  # 写入变量数据
                else:
                    print("表头与定义的字段名称不匹配,请检查")
                    with open(file_name2, mode='a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow(field_names)  # 写入CSV文件的表头
                        writer.writerow(file_write)  # 写入变量数据
                        exit(1)
        else:
            print("CSV文件不存在，已创建文件 " + file_name2)
            with open(file_name2, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(field_names)  # 写入CSV文件的表头
                writer.writerow(file_write)  # 写入变量数据

    # Tap错误信息输出
    except Exception as e:

        # 获取当前时间
        now = datetime.now()
        minute = now.strftime("%Y-%m-%d %H:%M")  # 格式化为精确到分钟的字符串
        print("当前时间" + minute)

        # 输出出错信息到文件
        with open(file_error_name, mode='a', newline='') as f:
            f.write(minute + " Tap错误信息 " + str(e) + '\r\n')
        print("Error:", e)
    time.sleep(60)
