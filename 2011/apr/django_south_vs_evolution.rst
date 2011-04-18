===================================================
Django的Schema Migration工具介绍及South工具推荐
===================================================

摘要
======
本文主要说明在 `django`_ 中 *schema migration* 的两种最常用工具 `south`_ 和 `evolution`_,
并且说明二者的差异和为什么要使用 `south`_ 作为最主要的 *migration* 工具。

正文
======

.. image:: ../../images/db_migration.png

关于schema migration
----------------------
无论我们使用何种语言进行web开发，快速开发随之相伴的是需求的不断变动，也就意味着我们要不断
增加或者调整已有的数据库模式（database schema），譬如一个很常见的变动是，我们需要在用户表中
增加一个状态位来标记当前用户是否已经删除，而不是直接从数据库中删除（虽然我不支持这样的保留用户
数据的行为，可是如今大多数的应用即使你要删除自己的账号，其实也不会永久删除的，所以，只要是网上的
信息，大致你可以认为是不会消失的），那么除了应用逻辑的改动外，你需要在数据库上增加一个状态位的
字段。

上面就是一个很常见的应用场景，当然诸如字段的属性更改，增加或者减少字段等等，也都属于这个范畴。

很可惜， `django`_ 本身并不支持 *schema migration* （也就是当你执行 *syncdb* 时并不会产生任何作用，
增加和删除字段会有效，不过复杂的则不支持，如更改一个字段的属性等）,这也就是 `evolution`_ 和
`south`_ 所要解决的问题。

关于evolution
---------------

相比于下面要说明的 `south`_ ， `evolution`_ 出现的比较早，它的主要思路是：在项目初始时会对所有的数据库schema
进行记录（也会存在一个数据库表中），当某个表的schema有更改时，当你执行 *syncdb* 时， `evolution`_ 也会与当前记录的
schema进行比较，如果 `evolution`_ 认为有更改，则它会进行比较进而生成一个最新schema与上次schema所要做更改的sql，用户可选择执行来进行
*schema migration*. 

相对而言， `evolution`_ 很容易集成到自己的项目中，并且也很容易使用，并且 *通常* 也能很好工作。所以，在我最初的
项目中我基本都是使用 `evolution`_ ，但是相比于 `south`_ ， `evolution`_ 的不足有：

1. 开发并不活跃（写本文时，看到的最近一次更新是2010/11/19)
2. 没有得到 `django`_ 项目核心开发人员的推荐和认可（而 `south`_ 是推荐的选项）
3. 不支持1.2的多数据库
4. 不支持数据的迁移（只支持表结构本身的迁移）
5. 不支持rollback到某个schema
6. 通常需要从项目上线起就开始使用（也就是没有数据时），对于已经有数据的项目则不支持
7. 跨app的迁移并不支持
8. migration的code并不能纳入到版本控制工具中（因为 `evolution`_ 使用数据库表，而数据库本身是没有状态的）

当然它也有诸如简单易用，学习曲线低，配置较少等优点，当然 `south`_ 也并不复杂，并且有更多的优点，请参考下面的说明。

关于south
-----------

`south`_ 正是因为 `evolution`_ 有这么多的问题，作者才开始了这个项目，上面提到的8个问题， `south`_ 已经很好
地进行了解决，并且在未来可能加入到 `django`_ 的代码库中（其实1.2也差点合并进去，因为 `south`_ 作者不建议现在合并
才最终没有成形）。

如果你之前没有使用过 `south`_ ，那么从现在起开始用 `south`_ 会对你受益匪浅；
如果你之前使用的是 `evolution`_ ，你会发现 `south`_ 更加友好和强大。

那么，不妨从今天起在你的项目中开始使用 `south`_ 吧，如何开始，具体可以参考 `south的tutorial`_ 。

另外，你也可以看看 `south alternatives`_ 和 `south's design`_ 两篇文章来了解更多。


总结
------

`django`_ 在不断发展，相应的周边的工具也是层出不穷，选择合适高效的工具，对于开发者而言是有很重要的意义的,
而让人头疼的 *schema migration* 则会因为 `south`_ 的出现而得到很好的解决。

下载原文
===========
可从 `此处 <https://github.com/topman/blog/tree/master/2011/apr/django_south_vs_evolution.rst>`_ 查看或者下载。 

参考资料
===========

1. `evolution`_ 
2. `south的tutorial`_ 
3. `south alternatives`_ 
4. `django`_ 
5. `south`_ 
6. `south's design`_ 

.. _evolution: http://code.google.com/p/django-evolution/
.. _south的tutorial: http://south.aeracode.org/docs/tutorial/index.html
.. _south alternatives: http://south.aeracode.org/wiki/Alternatives
.. _south's design: http://www.aeracode.org/2009/5/9/souths-design/
.. _south: http://south.aeracode.org/
.. _django: http://djangoproject.com
