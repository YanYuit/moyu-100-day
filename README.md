# Moyu-100-Day 挑战项目

这是一个使用 Next.js 和 Supabase 构建的 100 天挑战记录应用。用户可以上传每天的照片，记录自己的 100 天挑战过程，并与其他用户互动。

## 功能特点

- 用户认证（注册、登录、个人资料管理）
- 照片上传和管理
- 按天数记录挑战进度
- 社交互动（点赞、评论）
- 数据分析和统计
- 响应式设计，支持移动端和桌面端

## 技术栈

- **前端**：Next.js, React, Tailwind CSS
- **后端**：Supabase (PostgreSQL 数据库, 认证, 存储)
- **部署**：Vercel

## 本地开发

1. 克隆仓库
2. git clone [https://github.com/yourusername/moyu-100-day.git](https://github.com/yourusername/moyu-100-day.git)
cd moyu-100-day
2. 安装依赖
3. 设置环境变量
创建 `.env.local` 文件并添加：
NEXT_PUBLIC_SUPABASE_URL=your_supabase_url
NEXT_PUBLIC_SUPABASE_ANON_KEY=your_supabase_anon_key

4. 启动开发服务器
5. npm run dev
6. 
5. 在浏览器中访问 http://localhost:3000

## 数据库设置

项目使用 Supabase 作为后端服务。需要创建以下数据表：

- profiles：用户资料
- photos：照片记录
- comments：评论
- likes：点赞
- interactions：用户互动记录

详细的数据库设置说明请参考 [数据库设置文档](docs/database-setup.md)。

## 部署

本项目可以轻松部署到 Vercel：

1. 在 Vercel 上导入 GitHub 仓库
2. 设置环境变量
3. 部署

## 贡献指南

欢迎提交 Pull Request 或创建 Issue 来改进这个项目。

## 许可证

[MIT](LICENSE)
