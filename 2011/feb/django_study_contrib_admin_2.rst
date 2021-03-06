=================================
Django研究之admin系统(二）
=================================

接着 `上文`_ 的内容，本文将基于自己的理解尝试回答 `上文`_ 中研究列表中的3和4，即：

3. 理解和分析Admin系统的设计和代码书写值得学习和注意的问题
4. 总结


理解和分析Admin系统的设计和代码书写
=====================================

Admin系统具有多种特征，首先它是一个普通的 `Django`_ 应用，其次它又承担
作为各个其它Djago应用的基础应用而存在，所以我们可以从上面两个方面
来加以分析。

作为一个普通的应用
-------------------

`Django`_ 本身是一个基于MVC的web框架，各个层次非常清楚，当然在 `Django`_ 中，更多地被
称为MTV，即Model, Template, View，对应于MVC的Model, View, Controller。
其中Template和View的衔接是通过url映射完成，而url映射也是 `Django`_ 架构中最为巧妙的
地方。

.. image:: http://towerjoo.blog.techweb.com.cn/wp-content/blogs.dir/14215/files/blog/django_layers.png

对于一个 `Django`_ 的应用，我们通常可以从url映射入手，找到url处理的函数，和渲染出的页面，
从而理清整个的应用逻辑。

 `Django`_ 的Admin应用的url映射大致如下：

::

    # sites.py
    urlpatterns = patterns('',
        url(r'^$',
            wrap(self.index),
            name='index'),
        url(r'^logout/$',
            wrap(self.logout),
            name='logout'),
        url(r'^password_change/$',
            wrap(self.password_change, cacheable=True),
            name='password_change'),
        url(r'^password_change/done/$',
            wrap(self.password_change_done, cacheable=True),
            name='password_change_done'),
        url(r'^jsi18n/$',
            wrap(self.i18n_javascript, cacheable=True),
            name='jsi18n'),
        url(r'^r/(?P<content_type_id>\d+)/(?P<object_id>.+)/$',
            'django.views.defaults.shortcut'),
        url(r'^(?P<app_label>\w+)/$',
            wrap(self.app_index),
            name='app_list')
        )   

    # Add in each model's views.
    for model, model_admin in self._registry.iteritems():
        urlpatterns += patterns('',
            url(r'^%s/%s/' % (model._meta.app_label, model._meta.module_name),
                    include(model_admin.urls))
        )


从上面的代码，我们可以看到，Admin应用的landing page，登出，密码修改等相应的逻辑，
重点查看最后几行代码，将已经注册的应用的model(数据库的表)相应url映射指向了其自身的方法。

我们来看model_admin.urls这个逻辑：

::

    urlpatterns = patterns('',
        url(r'^$',
            wrap(self.changelist_view),
            name='%s_%s_changelist' % info),
        url(r'^add/$',
            wrap(self.add_view),
            name='%s_%s_add' % info),

        # added by Tower Joo At 2011/2/27
        # have to be ahead of change_view unless it will be overrided
        url(r'^export/$',
            wrap(self.export),
            name='%s_%s_export' % info),
        url(r'^aggregate/$',
            wrap(self.aggregate),
            name='%s_%s_aggregate' % info),

        url(r'^(.+)/history/$',
            wrap(self.history_view),
            name='%s_%s_history' % info),
        url(r'^(.+)/delete/$',
            wrap(self.delete_view),
            name='%s_%s_delete' % info),
        url(r'^(.+)/$',
                wrap(self.change_view),
                name='%s_%s_change' % info),
        )    


从上面的url映射来看，已经包含了增加记录，删除记录，修改记录等操作，当然上面也包含了
在 `上文`_ 中我做的一些url映射的修改。

看过上面的url映射后，心里就会有数，知道整个Admin系统大致有多少个页面，各个页面的作用是什么。

然后，我们可以通过url映射知道处理这个url的函数，例如，处理/add/的self.add_view函数。
通过阅读self.add_view函数的代码，除了相比于我们通常的逻辑更多的边界和条件处理外，其它的
也是相同的，例如数据库的操作，页面渲染所需要的数据准备等。

最后，我们看到的是页面渲染所需要的Template, change_form.html，查看对应的代码，则与通常的
 `Django`_ 的Template并无二异。

其它的逻辑也相同。相比于我们自己的 `Django`_ 应用，这个逻辑中有更多的边界条件的处理和异常的处理
等，你可能会说它过于复杂，这也就引入了我们接下来要说明的第二个问题。



作为其它应用的通用基础应用
-----------------------------

作为一个基础的应用，它就需要适应所有基于其上的其它应用的需要。
通用性通常意味着更多的复杂性，我们来看 `Django`_ 是如何有效且优美地处理这个问题的。

1. 充分使用Python的内省，也即model的元数据，如app_label, module_name等，使得动态地构造url映射
   和合适的显示成为可能
2. admin = AdminSite()是一个全局的变量，来维护所有的注册应用的列表
3. 两级的处理结构：admin site级和table级，分别由两个类来处理，并完成相应的url映射
4. 可配置性：对于其上层的应用，都提供了完善的可override的属性，如list_display,list_filter等等
5. 使用类而非 `Django`_ 默认推荐的函数作为view的处理，这样就提供了用户基于Admin系统建立自己的Admin系统的可能

总结
============

Admin系统可谓是 `Django`_ 最强大的功能了,它也大大方便了数据库驱动的应用的开发难度,为应用的数据输入,管理等
提供了一个稳定,可靠,方便的管理界面.

从 `上文`_ 和本文的介绍中,我们可以从中学习到一些 `Django`_ 常用的开发技巧:

1. 基于类的view实现(当然在 `Django`_ 1.3中已经完全支持class view了, 参考 `Class-based generic views`_ )
2. 分级的数据处理
3. 可配置性
4. 灵活性

会使用 `Django`_ 的Admin系统那可以让你的工作时间节省30%以上(基于数据库的应用),如果能够弄清楚 `Django`_ Admin
的实现原理并从中学习到可用于自己实际开发的经验与方法,则可运筹帷幄,谈笑风生地写代码了.

.. image:: ../../images/yunchou.jpg


.. _上文: http://towerjoo.blog.techweb.com.cn/archives/99.html
.. _Django: http://djangoproject.com
.. _Class-based generic views: http://docs.djangoproject.com/en/dev/topics/class-based-views/
