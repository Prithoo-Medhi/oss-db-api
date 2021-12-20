import os
import pwd


# print(os.geteuid())
print(pwd.getpwuid(os.getuid())[0])