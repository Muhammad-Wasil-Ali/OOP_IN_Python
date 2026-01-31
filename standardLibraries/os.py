import os

print(os.getcwdb())
print("Listing directory")
print(os.listdir())

# os.mkdir("test-folder/hello.txt")
print(os.path.exists("test-folder"))
os.removedirs("test-folder/hello.txt")