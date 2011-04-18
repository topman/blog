===============
Django相关
===============

1. 获得一条记录的查询：

::

    a = Model.objects.filter(xxx=yyy)
    if a:
        a[0].xxx = "zzz"
        a[0].save() #不能工作
    else:
        pass

对于上面的查询,对于已知期待一条记录的查询，使用get可以增加limit=1的限制，
而当db查询到一条记录后，则不再继续查询，也能够提高性能。

正确的应该是：

 ::
    
    try:
        a = Model.objects.get(xxx=yyy)
        a.xxx = "zzz"
        a.save()
    except:
        pass
        
