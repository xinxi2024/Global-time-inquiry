import requests
import os
import streamlit as st
from datetime import datetime
import pytz
import pandas as pd
# 引入env配置文件
import dotenv
dotenv.load_dotenv()
apiKey = os.getenv('API_KEY')

# 基本参数配置
apiUrl = 'http://apis.juhe.cn/fapigx/worldtime/query'  # 接口请求URL

# 预设一些常用城市
common_cities = ["北京", "上海", "东京", "首尔", "新加坡", "悉尼", "伦敦", "巴黎", "柏林", "莫斯科", "纽约", "洛杉矶", "多伦多", "开罗", "迪拜"]

# 创建Streamlit应用
st.set_page_config(page_title="全球时间查询工具", page_icon="🌍", layout="wide")
st.title("🌍 全球时间查询工具")
st.markdown("查询世界各地的当前时间，实时了解全球时区")

# 创建页面布局
col1, col2 = st.columns([1, 2])

with col1:
    # 允许用户输入城市名称或从预设城市中选择
    input_method = st.radio("选择输入方式", ["输入城市名称", "选择常用城市"])
    
    if input_method == "输入城市名称":
        city = st.text_input("输入城市名称", value="北京")
    else:
        city = st.selectbox("选择城市", common_cities)
    
    if st.button("查询时间", key="query"):
        with st.spinner("正在查询..."):
            # 接口请求入参配置
            requestParams = {
                'key': apiKey,
                'city': city,
            }
            
            # 发起接口网络请求
            response = requests.get(apiUrl, params=requestParams)
            
            # 解析响应结果
            if response.status_code == 200:
                responseResult = response.json()
                if responseResult.get('error_code') == 0:
                    result = responseResult.get('result')
                    st.session_state['result'] = result
                    st.success(f"成功获取 {result['city']} 的时间信息!")
                else:
                    st.error(f"查询失败: {responseResult.get('reason')}")
            else:
                st.error(f"请求异常: {response.status_code}")

with col2:
    if 'result' in st.session_state:
        result = st.session_state['result']
        
        # 创建信息卡片
        st.markdown("### 时间信息")
        
        # 使用容器和列创建漂亮的卡片布局
        card = st.container()
        with card:
            cols = st.columns(2)
            with cols[0]:
                st.metric("城市", f"{result['city']} ({result['encity']})")
                st.metric("国家", f"{result['country']} ({result['encountry']})")
                st.metric("时区", result['timeZone'])
                st.metric("夏令时", "是" if result['cursummertime'] == 1 else "否")
            
            with cols[1]:
                current_time = result['strtime']
                st.metric("当前日期时间", current_time)
                st.metric("星期", f"{result['week']} ({result['enweek']})")
                st.metric("月份", f"{result['nowmonth']}月 ({result['ennowmonth']})")
                st.metric("时段", f"{result['noon']} ({result['ennoon']})")
        
        # 添加世界地图可视化（简化版）
        st.markdown("### 世界各地时区")
        st.info("下图显示了世界各地的主要时区。您查询的城市所在的时区为 " + result['timeZone'])
        
        # 显示世界时区图（这里只是一个placeholder）
        timezone_img = "https://upload.wikimedia.org/wikipedia/commons/8/88/World_Time_Zones_Map.png"
        st.image(timezone_img, caption="世界时区图", use_column_width=True)

# 添加页脚
st.markdown("---")
st.markdown("### 数据来源")
st.markdown("本工具使用聚合数据提供的API服务，实时查询全球各地时间信息。")
st.markdown("### 使用说明")
st.markdown("1. 输入您想查询的城市名称或从常用城市列表中选择")
st.markdown("2. 点击\"查询时间\"按钮获取实时信息")
st.markdown("3. 查看右侧详细的时间信息和时区图")