本文介绍对 TOS 中公有访问的图片进行处理的过程。

# 前言

目前，TOS 支持处理其存储的图片文件，您可以通过 GetObject 接口，在请求中携带图片处理的相关参数。TOS 支持的图片处理功能包括图片缩放、图片裁剪、图片水印、格式转换等。

# 关于实验
- 预计部署时间：30分钟
- 级别：初级
- 相关产品：TOS
- 受众： 通用

# 实验说明
- 点击此[链接](https://console.volcengine.com/tos/bucket)登录控制台。

- 如果您还没有账户，请点击此[链接](https://console.volcengine.com/auth/signup/?redirectURI=%2Ftos%2Fbucket)注册账户。

# 实验步骤

总体步骤如下：
* 新建 TOS 存储桶
* 将图片上传至 TOS 存储桶
* 使用 URL 携带特定参数进行图片处理

具体操作步骤：
## 一、新建存储桶

您可以通过控制台、API、SDK、第三方工具新建存储桶。

本示例使用 TOS 命令行工具 tosutil 新建存储桶，您也可以使用其他方式新建存储桶。

关于 tosutil 使用方法，您可以参考此[链接](https://www.volcengine.com/docs/6349/148775)。

命令执行如下：

```bash
[root@iv-ybtg5t0rk12xxxmidr7t tosutil]# ./tosutil mb tos://imageprocessing
Start at 2022-10-23 03:00:48.260776431 +0000 UTC

Create bucket [imageprocessing] successfully, request id [6668487d8ce35a4cxxxxxce3-ac1f46b7-1oxg0J-CB-cb-tos-bj-3]
```

然后使用 tosutil 进行检查桶是否创建成功，如下：
```bash
[root@iv-ybtg5t0rk1xxxxmidr7t tosutil]# ./tosutil ls
Start at 2022-10-23 03:02:41.0927131 +0000 UTC

Bucket                   CreationDate                  Location
tos://imageprocessing    2022-10-23T03:00:51Z          cn-beijing
```

可以看到已经成功创建存储桶 imageprocessing。

## 二、上传图片文件到 imageprocessing 存储桶

如下：
```bash
[root@iv-ybtg5t0rk1xxxxmidr7t tosutil]# ./tosutil cp test.png tos://imageprocessing/test.png
Start at 2022-10-23 03:09:21.158079953 +0000 UTC


Parallel:      1                   Jobs:          5
Threshold:     100.00MB            PartSize:      auto
VerifyChecksum: false
CheckpointDir: /root/.tosutil_checkpoint

[----------------------------------] 100.00% 597.68KB/s 427.94KB/427.94KB 918ms

Upload successfully, 427.94KB, n/a, /root/tosutil/test.png --> tos://imageprocessing/test.png, cost [918], status [200], request id [2a03487d8ee20aa06xxxxxe2-ac161f1c-1oxg8Y-PuO-cb-tos-bj-3]
```

查看 test.png 属性，如下：
```bash
[root@iv-ybtg5t0rk1xxxxmidr7t tosutil]# ./tosutil stat tos://imageprocessing/test.png
Start at 2022-10-23 03:11:41.472731633 +0000 UTC

Key:
  tos://imageprocessing/test.png
LastModified:
  2022-10-23 03:09:22 +0000 UTC
Size:
  438212
StorageClass:
  STANDARD
HashCrc64ecma:
  15722218774810241166
ETag:
  9e7b47a510aceb061024c8c41ce01c2a
ContentType:
  image/png
Type:
  file
```

可以看到图片已经成功上传至存储桶。

## 三、使用 url 方式进行图片处理

url 图片处理的方式为在对象url后加“?x-tos-process=image/” 请求参数，然后“/”后加具体的处理方式，如：resize（图片缩放）、watermark（图片水印）、crop（自定义剪裁）等，然后处理方式后逗号“，”分隔，填写各种处理方式的具体参数。

所有可用处理方式及参数，您可以参考此[文档](https://www.volcengine.com/docs/6349/153623)。

一个完整的图片处理 url 如下（以图片缩放为例）：

https://tos-tools.tos-cn-beijing.volces.com/misc/sample.png?x-tos-process=image/resize,w_100

在浏览器查看效果：

原图：
![alt](https://portal.volccdn.com/obj/volcfe/cloud-universal-doc/upload_212f0f3212bccd1a731247a888c386f2.png)

处理后的图片：

![alt](https://portal.volccdn.com/obj/volcfe/cloud-universal-doc/upload_2eb060c2cfc3918217a3615222f94cda.png)

**如果您有其他问题，欢迎您联系火山引擎[技术支持服务](https://console.volcengine.com/ticket/createTicketV2/)**