#!/usr/bin/python3
from settings import Settings

writer = Settings()

str1 = writer.getSetting("window/winX","500")
print(str1)

str2 = writer.getSetting("window/winUU", "hello!")
print(str2)

str3 = writer.getAttributeSetting("window","css","Failed")
print(str3)

str4 = writer.getAttributeSetting("window","css1","Failed")
print(str4)

print("Performing write test...")

writer.writeSetting("toolbar/cut","true")
writer.writeAttributeSetting("window","css","hello")

print("Done")
