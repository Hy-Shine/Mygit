## Data Type

### 1	六种标准数据类型

```python
数字 number(int,float)
字符串 str
列表 list #[],可变
元组 tuple #(),初始化后不可修改
字典 dict #{},
集合 set
不可变数据（3个）：Number（数字）、String（字符串）、tuple（元组）；
可变数据（3个）：List（列表）、Dictionary（字典）、Set（集合）。 
```

- 数字number

  ```python
  支持的数字类型:int,float,bool,complex
  bool(True,False)
  #数值运算
  加(+)减(-)乘(*)乘方(**)
  除(/)浮点数(//)取商(%)取余
  ```

  ```python
  #判断数据类型
  a = 123
  type(a)	type('123')
  isinstance(a,int)
  #type()与isinstance()的区别
  type()不会认为子类是一种父类类型。
  isinstance()会认为子类是一种父类类型。
  ```

- 字符串

  ```python
  \ 转义字符，+ 字符拼接
  r'ssdfd\sff' 原始字符串
  ```

  

- list

  ```python
  a = [123,'abc',True,'789']
  a.append('ABC')#尾部追加元素
  a.insert(i,x)#指定位置添加元素
  a.pop()#删除最后一个元素
  a.pop(i)#删除指定位置元素,i是索引位置
  a[i] = x #指定位置替换元素
  ```

- tuple

  ```python
  
  ```

- dict

  ```python
  d = {'abc':12,'ming':34}
  #
  1 'abc' in d
  2 d.get('abc'[,value])
  
  d.pop('abc')
  ```

  