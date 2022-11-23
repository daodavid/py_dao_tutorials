from namespaces  import intro


print(intro.x)
print(intro.__y)

intro.x = "Change from another modol"
print(intro.x)

intro.foo()
intro.myfunc()


