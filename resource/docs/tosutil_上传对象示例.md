本文以 macOS 系统为例，介绍使用 tosutil 工具上传对象的常见示例命令。
<span id="示例文件夹说明"></span>
## 示例文件夹说明
本地示例文件夹的格式说明如下：
```Plain Text
└── folder1
    ├── folder2
        ├── file1.txt
        └── file2.txt
    └── file3.txt
    ├── folder3
    ├── folder4
        ├── file4.txt
        └── file5.txt
        └── pic1.png
        └── pic2.png
        └── pic3.jpg
        └── pic4.jpg
```

<span id="常见示例"></span>
## 常见示例
基于示例文件夹的说明，不同上传场景的示例命令如下。
<span id="c42b7b88"></span>
### 上传本地指定文件
上传本地 **folder1** 文件夹下的 **file3.txt** 文件至 **bucketname** 桶的根目录：
```Plain Text
./tosutil cp /folder1/file3.txt tos://bucketname
```

上传成功后，桶内生成对象为：
```Plain Text
tos://bucketname/file3.txt
```

<span id="ea0d7fda"></span>
### 上传本地指定文件并重命名
上传本地 **folder1** 文件夹下的 **file3.txt** 文件至 **bucketname** 桶的根目录，并且重命名为 **aaa.txt**：
```Plain Text
./tosutil cp /folder1/file3.txt tos://bucketname/aaa.txt
```

上传成功后，桶内生成对象为：
```Plain Text
tos://bucketname/aaa.txt
```

<span id="e3fa5b2c"></span>
### 上传本地指定文件至存储桶指定目录
上传本地 **folder1** 文件夹下的 **file3.txt** 文件至 **bucketname** 桶的 **folder** 文件夹中：
```Plain Text
./tosutil cp /folder1/file3.txt tos://bucketname/folder/
```

上传成功后，桶内生成对象为：
```Plain Text
tos://bucketname/folder/file3.txt
```

<span id="145bddc0"></span>
### 上传本地文件夹（包括文件夹本身）
上传本地 **folder2** 文件夹中的所有文件（**包括 folder2 文件夹本身**）至 **bucketname** 桶的根目录：
```Plain Text
./tosutil cp /folder1/folder2 tos://bucketname -r
```

上传成功后，桶内生成对象为：
```Plain Text
tos://bucketname/folder2/
tos://bucketname/folder2/file1.txt
tos://bucketname/folder2/file2.txt
```

<span id="2c7111d3"></span>
### 上传本地文件夹至存储桶指定目录（包括文件夹本身）
上传本地 **folder1** 文件夹中的所有文件和文件夹（**包括 folder1 文件夹本身**）至 **bucketname** 桶的 **folder0** 文件夹下：
```Plain Text
./tosutil cp /folder1 tos://bucketname/folder0 -r
```

成功上传后，桶内生成对象为：
```Plain Text
tos://bucketname/folder0/folder1/
tos://bucketname/folder0/folder1/folder2/
tos://bucketname/folder0/folder1/folder2/file1.txt
tos://bucketname/folder0/folder1/folder2/file2.txt
tos://bucketname/folder0/folder1/folder3/
tos://bucketname/folder0/folder1/file3.txt
tos://bucketname/folder0/folder1/folder4/file4.txt
tos://bucketname/folder0/folder1/folder4/file5.txt
tos://bucketname/folder0/folder1/folder4/pic1.png
tos://bucketname/folder0/folder1/folder4/pic2.png
tos://bucketname/folder0/folder1/folder4/pic3.jpg
tos://bucketname/folder0/folder1/folder4/pic4.jpg
```

<span id="2ea18b14"></span>
### 上传本地文件夹至存储桶指定目录（不包括文件夹本身）
上传本地 **folder1** 文件夹中的所有文件和文件夹（**不包括 folder1 文件夹本身**）至 **bucketname** 桶的 **folder0** 文件夹下：
```Plain Text
./tosutil cp /folder1 tos://bucketname/folder0 -r -flat
```

成功上传后，桶内生成对象为：
```Plain Text
tos://bucketname/folder0/
tos://bucketname/folder0/folder2/
tos://bucketname/folder0/folder2/file1.txt
tos://bucketname/folder0/folder2/file2.txt
tos://bucketname/folder0/folder3/
tos://bucketname/folder0/file3.txt
tos://bucketname/folder0/folder4/file4.txt
tos://bucketname/folder0/folder4/file5.txt
tos://bucketname/folder0/folder4/pic1.png
tos://bucketname/folder0/folder4/pic2.png
tos://bucketname/folder0/folder4/pic3.jpg
tos://bucketname/folder0/folder4/pic4.jpg
```

<span id="116781bf"></span>
### 上传本地文件夹中指定名称的文件
上传本地 **folder4** 文件夹中的所有 **.txt** 和 **pi?1.png** 文件至 **bucketname** 桶：
```Plain Text
./tosutil cp /folder4 tos://bucketname -r -include=*.txt#*pi?1.png
```

成功上传后，桶内生成对象为：
```Plain Text
tos://bucketname/file4.txt
tos://bucketname/file5.txt
tos://bucketname/pic1.png
```

<span id="ad772c79"></span>
### 上传本地文件夹中符合条件的文件
上传本地 **folder4** 文件夹中的除了 **.png** 之外的所有文件至 **bucketname** 桶：
```Plain Text
./tosutil cp /folder4 tos://bucketname -r -exclude=*.png 
```

成功上传后，桶内生成对象为：
```Plain Text
tos://bucketname/file4.txt
tos://bucketname/file5.txt
tos://bucketname/pic3.jpg
tos://bucketname/pic4.jpg
```

<span id="3dd95f9f"></span>
### 
