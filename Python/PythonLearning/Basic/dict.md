## 1	dict 字典

```python
格式：dict_name = {key1:value1,key1:value2,...}
每个key必须在一个字典中唯一,value不必
删除字典	del dict_name
删除key	del dict_name(key)
修改字典值	dict_name[key] = value_new
```

### 1.1 循环

```python
##只打印key
for dict_key in dict_name:
    print(dict_key)
等价于
for dict_element in dict_name.keys():
    print(dict_key)
##以下可以打印key与value
for dict_key,dict_value in dict_name.item():
    print(dict_key,dict_value)
    
```

