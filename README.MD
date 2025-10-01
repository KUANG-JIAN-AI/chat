创建虚拟环境  
py -3 -m venv .venv

进入虚拟环境  
.venv\Scripts\activate

安装依赖  
pip install flask flask-socketio eventlet  

安装 mysql  
pip install Flask Flask-SQLAlchemy pymysql  


表结构  
CREATE TABLE `chat_users` (  
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,  
  `nickname` varchar(255) NOT NULL DEFAULT '' COMMENT '昵称',  
  `password` varchar(255) NOT NULL DEFAULT '' COMMENT '密码',  
  `created_at` int(10) unsigned NOT NULL DEFAULT 0,  
  `updated_at` int(10) unsigned NOT NULL DEFAULT 0,  
  `deleted_at` int(10) unsigned DEFAULT NULL,  
  PRIMARY KEY (`id`)  
  UNIQUE KEY `uk_nickname` (`nickname`)  
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `chat_msgs` (  
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,  
  `sender_id` int(10) unsigned NOT NULL DEFAULT 0 COMMENT '发送用户id',  
  `receiver_id` int(10) unsigned NOT NULL DEFAULT 0 COMMENT '接收用户id',  
  `message` varchar(255) NOT NULL DEFAULT '',  
  `created_at` int(10) unsigned DEFAULT 0,  
  PRIMARY KEY (`id`)  
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT   CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;