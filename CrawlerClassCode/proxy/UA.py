from fake_useragent import UserAgent

ua = UserAgent(path='C:\\Users\\Oringals\\Desktop\\python\\crawler\\proxy\\user-agent.json')
# ie浏览器的user agent
print(ua.ie)
 
# opera浏览器
print(ua.opera)
 
# chrome浏览器
print(ua.chrome)

#随机生成UA
print(ua.random)
