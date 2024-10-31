//项目的入口 项目从这里开始执行

//react的两个核心包
import React from 'react';
import ReactDOM from 'react-dom/client';
//导入项目的根组件
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);

