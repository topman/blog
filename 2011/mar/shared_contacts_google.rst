=======================
Google Contact导入脚本
=======================

Google Contact是大家最常用的一种通信录之一，就像我所有的通信录都
是使用Google来管理的，并且使用于Gmail, 手机等等。

.. image:: ../../images/google_contact.png

那么经常会遇到下面的需求，就是将其它格式的通信录导入到Google Contact中，
当然Google Contact已经提供了常见的导入界面，很方便操作，但是对于程序控制
下的导入，则需要相关的脚本来完成，而我写的这个脚本就是为了这个目的。

相关的代码可以在 https://github.com/towerjoo/shared_contact 下载或者checkout,
目前的主要功能包括：

#. 支持导入
#. 支持导出
#. 支持删除

注意：

1. 只支持Google的Domain用户
2. 24小时后才能在通信录和发邮件时的自动补齐中出现
3. 具体说明参考代码库的文档（可使用 `sphinx`_ 来生成文档）


实现方面
==============
主要是基于已有的 http://code.google.com/p/google-shared-contacts-client/ ，使用
fields mapping(映射）的思路来完成。

To Do
==============

1. 增加对Gmail的支付（非Domain）
2. 增加常用Contact的映射模板，如outlook等


.. _sphinx: http://sphinx.pocoo.org/
