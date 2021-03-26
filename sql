INSERT INTO MyApp_stendent(`id`, `name`, `age`, `qq`, `sex`, `add`, `email`) VALUES (1, 'test11', 21, 1231, '男', '北京市', '1231@qq.com'),
(2, 'test12', 22, 1232, '男', '北京市', '1232@qq.com'),
(3, 'test12', 22, 1232, '男', '北京市', '1232@qq.com'),
(4, 'test13', 23, 1233, '女', '北京市', '1233@qq.com'),
(5, 'test14', 24, 1234, '女', '北京市', '1234@qq.com'),
(6, 'test15', 25, 1235, '女', '北京市', '1235@qq.com'),
(7, 'test16', 26, 1236, '男', '北京市', '1236@qq.com'),
(8, 'test17', 27, 1237, '男', '北京市', '1237@qq.com'),
(9, 'test18', 28, 1238, '女', '北京市', '1238@qq.com'),
(10, 'test11', 21, 1231, '男', '北京市', '1231@qq.com'),
(11, 'test19', 29, 1239, '女', '北京市', '123@qq.com');

select * from MyApp_stendent;


INSERT INTO `my_django1`.`MyApp_testtimer`(`id`, `creattime`, `updatetime`, `date`, `time`) VALUES (1, '2021-03-26 11:35:04.000000', '2021-03-26 11:35:16.000000', '2021-03-26', '11:35:28.000000');



ALTER TABLE `task` CHANGE COLUMN `created_at` `created_at` datetime NOT NULL;



