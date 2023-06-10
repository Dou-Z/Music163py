

-- 标签表
CREATE TABLE `tag_info` (
  `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT 'id',
  `tag` varchar(255) NOT NULL COMMENT '类型',
  `title` varchar(255) DEFAULT NULL COMMENT '标题',
  `url` varchar(255) DEFAULT NULL COMMENT '链接',
  `playtimes` varchar(255) DEFAULT NULL COMMENT '播放次数',
  `tag_author` varchar(255) DEFAULT NULL COMMENT 'data-res-author作者',
  `createtime` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updatetime` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;


CREATE TABLE `playlist_info` (
  `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT 'id',
  `title` varchar(255) NOT NULL COMMENT '标题',
  `musics` longtext NOT NULL COMMENT '音乐id',
  `introduction` longtext NOT NULL COMMENT '歌单介绍',
  `author` varchar(255) NOT NULL COMMENT '作者',
  `commentcount` varchar(255) NOT NULL COMMENT '评论数',
  `playvolume` int DEFAULT '0' COMMENT '点击',
  `createtime` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updatetime` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间'

) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--  音乐表


CREATE TABLE `music` (
  `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT 'id',
  `title` varchar(255) NOT NULL COMMENT '标题',
  `music_id` varchar(255) DEFAULT NULL COMMENT '音乐ID',
  `playtime` varchar(255) DEFAULT NULL COMMENT '时长 bMusic',
  `singer` varchar(255) DEFAULT NULL COMMENT '歌手',
  `Vip` int DEFAULT NULL COMMENT '是否为VIP歌曲（0：No，1：Yes）',
  `commentvolume` int DEFAULT 0 COMMENT '评论量',
  `createtime` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updatetime` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
