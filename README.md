# Flask 

[flask官网](https://palletsprojects.com/p/flask/)

## 一、项目结构

- `manager.py`

    项目管理文件
    
- app

    - `__init__.py`
    
        - 初始化文件
        
    - `settings.py`
        
        - config配置
        - 全局项目配置
        
    - `extensions.py`
    
        - extension扩展库
        
        - 除了和路由相关的
        
    - `views.py`
    
        - apis
        
        - 路由，视图函数
        
    - `models.py`
    
        - 定制模型     

## 二、使用的插件

- [flask-script](https://flask-script.readthedocs.io/en/latest/)
    
  ```shell script
  python manager.py runserver -p 8000 -r -d --threade
  ```

- [flask-blueprint](https://flask.palletsprojects.com/en/1.0.x/blueprints/)

- [flask-sqlalchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)

- [flask-migrate](https://flask-migrate.readthedocs.io/en/latest/)

- [flask-debugtoolbar](https://flask-debugtoolbar.readthedocs.io/en/latest/)


## 三、开发环境

- 开发环境

    开发人员使用

- 测试环境

    测试人员使用

- 演示环境

    - 给产品看的
    
    - 做演习，彩排
    
 - 生产环境
 
    - 真实环境
    
    - 给用户看


