======================
Django研究之admin系统
======================

`Django`_ 的Admin系统是 `Django`_ 几大killer feature之一，
所以对它的一些研究对于熟悉 `Django`_ 及其应用都有重要价值(因为Admin系统
是一个完整的 `Django`_ 应用示例）.

.. image:: ../../images/django_logo.png


本次大致的研究过程如下：

1. 将 `Django`_ 的Admin系统拷贝出来，在一个新的 `Django`_ 项目中作为独立应用来运行
2. 对这个独立的应用进行一定的修改
3. 理解和分析Admin系统的设计和代码书写值得学习和注意的问题
4. 总结

相关的代码可在 `bitbuckt <https://bitbucket.org/icatclaw/blog>`_ 查看和检出

将Django的Admin系统作为独立应用来运行
=========================================

1. 使用django-admin.py startproject myadmin新建一个新项目
2. 将django的原文件拷贝到新项目myadmin目录下

  * 找到django的安装目录, 如果不知道，可在python的交互式prompt下输入:
  * import django
  * print django.__file__
  * 那么 `Django`_ 的Admin应用就在DJANGO/contrib/admin/
  * 将整个目录拷贝到myadmin目录下
  * 如果需要，则调整相关的文件权限

3. 修改myadmin项目中的settings.py和urls.py
4. 同步数据库(syncdb)和运行代码

这时我们的第一个目标得以实现，因为根据Python语言package的导入规则(或者叫module search规则），
相对引入(relative import)会覆盖系统的django module，所以myadmin项目中运行的是myadmin下的
admin项目，而不是系统安装的。

为了检验，我们不妨可做一个简单的修改来证明，我们使用的是myadmin下的admin,我们在myadmin/django/contrib/admin/sites.py
的248行加入一句: import logging; logging.debug("My Edit here")

使用浏览器请求http://127.0.0.1:8000/admin/， 则你可在输出的log中看到上面的log.

对Admin系统进行一定的修改
=============================

我们打算做以下几点修改：

1. 在一个具体的table的显示页面，增加导出csv的功能（也就是将当前查看表的数据导出为csv)
2. 在一个具体的table的显示页面，增加快捷的聚合操作的支持（如sum,average等）

修改1
----------

通过阅读代码，大致的修改步骤如下：
1. 找到显示页面对应的template(change_list.html),也可使用方便的debug_toolbar来查看
2. 添加导出为csv的链接
3. 增加相应的url映射（options.py第254行）
4. 增加相应的处理（options.py第773行）

相应的csv逻辑还是比较简单的，当然我只实现了将此表中所有记录导出的功能，部分数据导出的功能并未实现。

在实现的过程中，找到相应的url映射和及处理逻辑是比较重要，和相对较难的，大致的过程如下：
1. 入口是: admin.sites.urls,发现其是一个property
2. 继而找到get_urls方法，得到相应的url映射，发现对于特定model的url映射是对应各个model的urls属性
3. 继而找到options.py文件，同样发现其是一个property
4. 继而找到get_urls方法，及其相应的url映射，这里便是我们要添加我们的url映射的地方
5. 然后加入相应的url映射的处理逻辑即可

从上面的代码我们会发现django的逻辑很清楚，而且层次分割和明确。

修改2
----------

基本的步骤同修改1，只是在功能和界面上有所调整。

在修改2的完成中，我们使用了
1. `forms`_
2. `database aggregation`_

最终的结果可见下图：

.. image:: ../../images/django_admin_result.png

分析与总结
=============
请查看下篇文章。

.. _Django: http://djangoproject.com
.. _forms: http://docs.djangoproject.com/en/dev/topics/forms/
.. _database aggregation: http://docs.djangoproject.com/en/dev/topics/db/aggregation/


