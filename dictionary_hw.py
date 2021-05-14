
pairs={'태연':'what do i call you', 'sokomodo': '지구멸망', '휘인':'water color'}

#1
print(pairs)
pairs['선미'] = '꼬리'
print(pairs)

#2
del pairs['태연'] 
print(pairs)

#3
print(pairs.get('휘인'))