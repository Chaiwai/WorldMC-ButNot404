@echo OFF
chcp 65001 > nul
@set a=0
:Menu
title 生存1 WorldMC-1.21.4 重启次数[%a%]
echo        现在时间为%time%   今天是%date%
echo ============================================================
echo        生存1 WorldMC-1.21.4 正在启动... [重启次数: %a%]
echo ============================================================

"C:\Program Files\Java\jdk-21.0.10\bin\java" -Xms3000M -Xmx4000M -jar purpur-1.21.4-2416.jar --nogui
@echo OFF
@echo 服务器已关闭，将于20秒后重启
@ping -n 10 127.0.0.1>nul
@set /a a=%a%+1
@goto Menu