## Data Types

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
### 2	data types
###  2.1	数字number

  ```python
支持的数字类型:int,float,bool,complex
bool(True,False)
complex:1+2j
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

### 2.2	字符串str

  ```python
  \ 转义字符，+ 字符拼接
  r'ssdfd\sff' 原始字符串
  ```

### 2.3	 列表list

  ```python
  a = [123,'abc',True,'789']
  a.append('ABC')#尾部追加元素
  a.insert(i,x)#指定位置添加元素
  a.pop()#删除最后一个元素
  a.pop(i)#删除指定位置元素,i是索引位置
  a[i] = x #指定位置替换元素
  ```

### 2.4	元组tuple

  ```python
  #元组
  #定义一个空元组
  tuple1 = ()
  #只包含一个元素
  tuple2 = (1,)
  #元组索引、截取
  tuple1[0]	#0位置元素
  tuple1[:]	#整个元组
  tuple1[1:]	#从1至末尾
  tuple1[:3]	#从0至2位置元素
  #内置的元组函数
  del tuple1	#删除整个元组
  len(tuple1)	#元组元素数
  max(tuple1)	#求元组中最大值
  min(tuple1)	#求元组中最小值
  tuple(list1) #将列表转换为元组
  ```

### 2.5	字典dict

  ```python
格式:dict1 = {key1:value1...}
键必须是唯一的，但值则不必,值可以取任何数据类型，但键必须是不可变的，用数字，字符串或元组充当。
dict = {'Alice':'2341','Beth':'9102','Cecil':'3258'}
del dict['Alice'] # 删除键'Alice'
dict.clear()     # 清空字典
del dict         # 删除字典
dict.item()
dict.keys()
  ```

### 2.6	集合set

  ```python
集合（set）是一个无序的不重复元素序列。
#集合运算
并集(a|b),交集(a&b),差集(a-b),不同时包含于ab,二者的并集去掉二者交集的元素(a^b)
  ```

  