=============
数据库相关
=============


更喜欢使用where而不是join
==========================
例如，两个表user, profile其结构分别为：

::

    user table

    id(主键)
    name
    sex


    profile table

    id
    uid(外键指向user table的id)
    website
    blog
    phone
    email

我想查询uid为[1,2,3,4]的用户的所有信息（包括user和profile表中的内容）时，我更喜欢：


::

    select * from user, profile where user.id=profile.uid and user.id in (1, 2, 3, 4);



而更加正确的是：

::

    select * from user 
        join profile on user.id=profile.uid
    where user.id in (1, 2, 3, 4)


参考：

1. http://stackoverflow.com/questions/1018822/inner-join-versus-where-clause-any-difference
2. http://stackoverflow.com/questions/128965/is-there-something-wrong-with-joins-that-dont-use-the-join-keyword-in-sql-or-mys


喜欢使用join
==============


常见的mysql best practice
===============================
http://net.tutsplus.com/tutorials/other/top-20-mysql-best-practices/


