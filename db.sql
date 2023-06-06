

-- 标签表
CREATE TABLE `tag` (
  `id` varchar(255) NOT NULL COMMENT 'id',
  `title` varchar(255) NOT NULL COMMENT '标题',
  `createtime` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updatetime` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;


CREATE TABLE `album` (
  `id` varchar(255) NOT NULL COMMENT 'id',
  `title` varchar(255) NOT NULL COMMENT '标题',
  `tagid` varchar(255) NOT NULL COMMENT '标签id',
  `introduction` longtext NOT NULL COMMENT '简介',
  `polt` longtext COMMENT '标图',
  `author` varchar(255) NOT NULL COMMENT '作者',
  `commentcount` varchar(255) NOT NULL COMMENT '评论数',
  `musics` longtext NOT NULL COMMENT '音乐id',
  `createtime` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updatetime` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间',
  `playvolume` int DEFAULT '0' COMMENT '点击',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--  音乐表


CREATE TABLE `music` (
  `id` varchar(255) NOT NULL COMMENT 'id',
  `title` varchar(255) NOT NULL COMMENT '标题',
  `playtime` int NOT NULL COMMENT '时长 bMusic',
  `singer` varchar(255) NOT NULL COMMENT '歌手',
  `Vip` int DEFAULT NULL COMMENT '是否为VIP歌曲（0：No，1：Yes）',
  `audiorul` varchar(255) NOT NULL COMMENT '音频地址',
  `mv` varchar(255) NOT NULL COMMENT 'mv地址',
  `composer` varchar(255) DEFAULT NULL COMMENT '作曲者',
  `song_type` varchar(255) NOT NULL COMMENT '歌曲类型',
  `tagid` varchar(255) NOT NULL COMMENT '标签id',
  `commentvolume` int DEFAULT NULL COMMENT '评论量',
  `plot` varchar(255) DEFAULT NULL COMMENT '图像',
  `createtime` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updatetime` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
