====================
Gvim的字体设置
====================

.. image:: ../../images/vim.png

在各个系统下都习惯了 `vim`_ 这个编辑器，但是基于win下的gvim的默认字体是
fixedsys，显示中文时实在是磕碜的不行，而直接在vimrc中写入中文名的
字体配置又不行（如新宋体），经过确认要么将encoding设置为cp936，要么
使用中文字体的英文名称，还好有一篇博文有详细的记录，参考：
`常见系统中文字体的英文名`_, 简单摘录如下：

Mac OS的一些：
==================

::

    华文细黑：STHeiti Light [STXihei]
    华文黑体：STHeiti
    华文楷体：STKaiti
    华文宋体：STSong
    华文仿宋：STFangsong
    儷黑 Pro：LiHei Pro Medium
    儷宋 Pro：LiSong Pro Light
    標楷體：BiauKai
    蘋果儷中黑：Apple LiGothic Medium
    蘋果儷細宋：Apple LiSung Light

Windows的一些：
=================

::

    新細明體：PMingLiU
    細明體：MingLiU
    標楷體：DFKai-SB
    黑体：SimHei
    宋体：SimSun
    新宋体：NSimSun
    仿宋：FangSong
    楷体：KaiTi
    仿宋_GB2312：FangSong_GB2312
    楷体_GB2312：KaiTi_GB2312
    微軟正黑體：Microsoft JhengHei
    微软雅黑体：Microsoft YaHei

装Office会生出来的一些
==========================

::

    隶书：LiSu
    幼圆：YouYuan
    华文细黑：STXihei
    华文楷体：STKaiti
    华文宋体：STSong
    华文中宋：STZhongsong
    华文仿宋：STFangsong
    方正舒体：FZShuTi
    方正姚体：FZYaoti
    华文彩云：STCaiyun
    华文琥珀：STHupo
    华文隶书：STLiti
    华文行楷：STXingkai
    华文新魏：STXinwei


所以我在vimrc中将guifont配置为"NSimSun"即可（新宋体）。

.. _常见系统中文字体的英文名: http://blog.163.com/logotools@126/blog/static/44362656200971302246860/
.. _vim: http://www.vim.org
