# 🌍 全球时间查询工具

这是一个基于Python和Streamlit开发的全球时间查询工具，使用聚合数据API获取全球各地的实时时间信息，并提供友好的可视化界面。

## 功能特点

- 🔍 支持查询世界各地主要城市的当前时间
- 🌐 显示详细的时间信息，包括日期、时区、星期等
- 🗺️ 提供世界时区地图可视化
- 📱 响应式设计，适配不同设备屏幕
- 🔄 实时数据更新，确保时间信息准确性

## 安装与使用

### 前置条件

- Python 3.8或更高版本
- 聚合数据API密钥（注册获取：[聚合数据](https://www.juhe.cn/)）

### 安装步骤

1. 克隆本仓库到本地：
2. 安装所需依赖：

```bash
pip install -r requirements.txt
```

3. 创建`.env`文件并添加API密钥：

```
API_KEY=你的聚合数据API密钥
```

4. 运行应用：

```bash
streamlit run global_time_inquiry.py
```

5. 在浏览器中访问应用（默认地址为 http://localhost:8501）

## 使用说明

1. 在应用左侧选择输入方式：可以直接输入城市名称或从预设列表中选择
2. 点击"查询时间"按钮获取该城市的实时时间信息
3. 右侧界面将显示详细的时间信息和时区地图

## 数据来源

本工具使用[聚合数据](https://www.juhe.cn/)提供的世界时间API服务。

## 许可证

本项目采用MIT许可证 - 详情请查看 [LICENSE](LICENSE) 文件。

## 贡献

欢迎提交问题报告和功能建议！如果您想为项目做出贡献，请：

1. Fork本仓库
2. 创建您的功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建一个Pull Request 