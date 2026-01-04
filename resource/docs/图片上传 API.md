普通上传是指通过 `put_object` 方法上传单个对象(Object)，支持上传字符串（字符流）、上传Bytes（Bytes流）、上传网络流和上传本地文件四种形式。
<span id="注意事项"></span>
## **注意事项**

* 上传对象前，您必须具有 `tos:PutObject` 权限，具体操作，请参见[权限配置指南](/docs/6349/102120)。
* 上传对象时，对象名必须满足一定规范，详细信息，请参见[对象命名规范](/docs/6349/74822)。
* TOS 是面向海量存储设计的分布式对象存储产品，内部分区存储了对象索引数据。为横向扩展您上传对象和下载对象时的最大吞吐量和减小热点分区的概率，请您避免使用字典序递增的对象命名方式，详细信息，请参见[性能优化](/docs/6349/155630)。
* 如果桶中已经存在同名对象，则新对象会覆盖已有的对象。如果您的桶开启了版本控制，则会保留原有对象，并生成一个新版本号用于标识新上传的对象。

<span id="示例代码"></span>
## 示例代码
<span id="上传字符流"></span>
### **上传字符流**
以下代码用户将字符流上传到目标桶 `bucket-test` 中的 `object-test` 对象。
```python
from io import StringIO

import os
import tos


# 从环境变量获取 AK 和 SK 信息。
ak = os.getenv('TOS_ACCESS_KEY')
sk = os.getenv('TOS_SECRET_KEY')
# your endpoint 和 your region 填写Bucket 所在区域对应的Endpoint。# 以华北2(北京)为例，your endpoint 填写 tos-cn-beijing.volces.com，your region 填写 cn-beijing。
endpoint = "your endpoint"
region = "your region"
bucket_name = "bucket-test"
# 对象名称，例如 example_dir 下的 example_object.txt 文件，则填写为 example_dir/example_object.txt
object_key = "object-test"
content = StringIO('Hello TOS')

try:
    client = tos.TosClientV2(ak, sk, endpoint, region)
    # 若在上传对象时设置文件存储类型（x-tos-storage-class）和访问权限 (x-tos-acl), 请在 put_object中设置相关参数
    # 用户在上传对象时，可以自定义元数据，以便对对象进行自定义管理
    # result = client.put_object(bucket_name, object_key, content=content, acl=tos.ACLType.ACL_Private, storage_class=tos.StorageClassType.Storage_Class_Standard, meta={'name': '张三', 'age': '20'})
    result = client.put_object(bucket_name, object_key, content=content)
    # HTTP状态码
    print('http status code:{}'.format(result.status_code))
    # 请求ID。请求ID是本次请求的唯一标识，建议在日志中添加此参数
    print('request_id: {}'.format(result.request_id))
    # hash_crc64_ecma 表示该对象的64位CRC值, 可用于验证上传对象的完整性
    print('crc64: {}'.format(result.hash_crc64_ecma))
except tos.exceptions.TosClientError as e:
    # 操作失败，捕获客户端异常，一般情况为非法请求参数或网络异常
    print('fail with client error, message:{}, cause: {}'.format(e.message, e.cause))
except tos.exceptions.TosServerError as e:
    # 操作失败，捕获服务端异常，可从返回信息中获取详细错误信息
    print('fail with server error, code: {}'.format(e.code))
    # request id 可定位具体问题，强烈建议日志中保存
    print('error with request id: {}'.format(e.request_id))
    print('error with message: {}'.format(e.message))
    print('error with http code: {}'.format(e.status_code))
    print('error with ec: {}'.format(e.ec))
    print('error with request url: {}'.format(e.request_url))
except Exception as e:
    print('fail with unknown error: {}'.format(e))
```

<span id="上传bytes流"></span>
### **上传Bytes流**
以下代码用于将 Bytes 流上传到目标桶 `bucket-test` 中的 `object-test` 对象。
```python
from io import BytesIO

import os
import tos

# 从环境变量获取 AK 和 SK 信息。
ak = os.getenv('TOS_ACCESS_KEY')
sk = os.getenv('TOS_SECRET_KEY')
# your endpoint 和 your region 填写Bucket 所在区域对应的Endpoint。# 以华北2(北京)为例，your endpoint 填写 tos-cn-beijing.volces.com，your region 填写 cn-beijing。
endpoint = "your endpoint"
region = "your region"
bucket_name = "bucket-test"
# 对象名称，例如 example_dir 下的 example_object.txt 文件，则填写为 example_dir/example_object.txt
object_key = "object-test"
content = BytesIO(b'Hello TOS')

try:
    client = tos.TosClientV2(ak, sk, endpoint, region)
    result = client.put_object(bucket_name, object_key, content=content)
    # HTTP状态码
    print('http status code:{}'.format(result.status_code))
    # 请求ID。请求ID是本次请求的唯一标识，建议在日志中添加此参数
    print('request_id: {}'.format(result.request_id))
    # hash_crc64_ecma 表示该对象的64位CRC值, 可用于验证上传对象的完整性
    print('crc64: {}'.format(result.hash_crc64_ecma))
except tos.exceptions.TosClientError as e:
    # 操作失败，捕获客户端异常，一般情况为非法请求参数或网络异常
    print('fail with client error, message:{}, cause: {}'.format(e.message, e.cause))
except tos.exceptions.TosServerError as e:
    # 操作失败，捕获服务端异常，可从返回信息中获取详细错误信息
    print('fail with server error, code: {}'.format(e.code))
    # request id 可定位具体问题，强烈建议日志中保存
    print('error with request id: {}'.format(e.request_id))
    print('error with message: {}'.format(e.message))
    print('error with http code: {}'.format(e.status_code))
    print('error with ec: {}'.format(e.ec))
    print('error with request url: {}'.format(e.request_url))
except Exception as e:
    print('fail with unknown error: {}'.format(e))
```

<span id="上传网络流"></span>
### **上传网络流**
以下代码用于将网络流上传到目标桶 `bucket-test` 中的 `object-test` 对象。TOS 将网络流视为可迭代对象（Iterable），并以 Chunked Encoding 的方式上传。
```python
from io import BytesIO

import requests
import os
import tos


# 从环境变量获取 AK 和 SK 信息。
ak = os.getenv('TOS_ACCESS_KEY')
sk = os.getenv('TOS_SECRET_KEY')
# your endpoint 和 your region 填写Bucket 所在区域对应的Endpoint。# 以华北2(北京)为例，your endpoint 填写 tos-cn-beijing.volces.com，your region 填写 cn-beijing。
endpoint = "your endpoint"
region = "your region"
bucket_name = "bucket-test"
# 对象名称，例如 example_dir 下的 example_object.txt 文件，则填写为 example_dir/example_object.txt
object_key = "object-test"

try:
    # 创建 TosClientV2 对象，对桶和对象的操作都通过 TosClientV2 实现
    client = tos.TosClientV2(ak, sk, endpoint, region)
    # requests.get 获取网络流， python sdk 支持上传网络流
    # requests 返回的是一个可迭代对象（Iterable），此时Python SDK会通过Chunked Encoding方式上传。
    content = requests.get('https://www.volcengine.com')
    result = client.put_object(bucket_name, object_key, content=content)
    content.close()
    # HTTP状态码
    print('http status code:{}'.format(result.status_code))
    # 请求ID。请求ID是本次请求的唯一标识，建议在日志中添加此参数
    print('request_id: {}'.format(result.request_id))
    # hash_crc64_ecma 表示该对象的64位CRC值, 可用于验证上传对象的完整性
    print('crc64: {}'.format(result.hash_crc64_ecma))
except tos.exceptions.TosClientError as e:
    # 操作失败，捕获客户端异常，一般情况为非法请求参数或网络异常
    print('fail with client error, message:{}, cause: {}'.format(e.message, e.cause))
except tos.exceptions.TosServerError as e:
    # 操作失败，捕获服务端异常，可从返回信息中获取详细错误信息
    print('fail with server error, code: {}'.format(e.code))
    # request id 可定位具体问题，强烈建议日志中保存
    print('error with request id: {}'.format(e.request_id))
    print('error with message: {}'.format(e.message))
    print('error with http code: {}'.format(e.status_code))
    print('error with ec: {}'.format(e.ec))
    print('error with request url: {}'.format(e.request_url))
except Exception as e:
    print('fail with unknown error: {}'.format(e))
```

<span id="上传本地文件"></span>
### **上传本地文件**
以下代码用于将本地文件上传到目标桶 `bucket-test` 中的 `object-test` 对象。
```python
import os
import tos


# 从环境变量获取 AK 和 SK 信息。
ak = os.getenv('TOS_ACCESS_KEY')
sk = os.getenv('TOS_SECRET_KEY')
# your endpoint 和 your region 填写Bucket 所在区域对应的Endpoint。# 以华北2(北京)为例，your endpoint 填写 tos-cn-beijing.volces.com，your region 填写 cn-beijing。
endpoint = "your endpoint"
region = "your region"
bucket_name = "bucket-test"
# 对象名称，例如 example_dir 下的 example_object.txt 文件，则填写为 example_dir/example_object.txt
object_key = "object-test"
# 本地文件路径
file_name = "/usr/local/test.txt"
try:
    # 创建 TosClientV2 对象，对桶和对象的操作都通过 TosClientV2 实现
    client = tos.TosClientV2(ak, sk, endpoint, region)
    # 将本地文件上传到目标桶中
    # file_name为本地文件的完整路径。
    client.put_object_from_file(bucket_name, object_key, file_name)
except tos.exceptions.TosClientError as e:
    # 操作失败，捕获客户端异常，一般情况为非法请求参数或网络异常
    print('fail with client error, message:{}, cause: {}'.format(e.message, e.cause))
except tos.exceptions.TosServerError as e:
    # 操作失败，捕获服务端异常，可从返回信息中获取详细错误信息
    print('fail with server error, code: {}'.format(e.code))
    # request id 可定位具体问题，强烈建议日志中保存
    print('error with request id: {}'.format(e.request_id))
    print('error with message: {}'.format(e.message))
    print('error with http code: {}'.format(e.status_code))
    print('error with ec: {}'.format(e.ec))
    print('error with request url: {}'.format(e.request_url))
except Exception as e:
    print('fail with unknown error: {}'.format(e))
```

<span id="上传本地文件夹"></span>
### **上传本地文件夹**
以下代码用于将本地文件夹 `test/` 上传到目标桶 `bucket-test` 中。
```python
import os
import tos

# 从环境变量获取 AK 和 SK 信息。
ak = os.getenv('TOS_ACCESS_KEY')
sk = os.getenv('TOS_SECRET_KEY')
# your endpoint 和 your region 填写Bucket 所在区域对应的Endpoint。# 以华北2(北京)为例，your endpoint 填写 tos-cn-beijing.volces.com，your region 填写 cn-beijing。
endpoint = "your endpoint"
region = "your region"
bucket_name = "bucket-test"
# 本地文件的当前路径
file_dir = 'test/'
try:
    # 创建 TosClientV2 对象，对桶和对象的操作都通过 TosClientV2 实现
    client = tos.TosClientV2(ak, sk, endpoint, region)


    def upload_dir(root_dir):
        list = os.listdir(root_dir)
        for i in list:
            path = os.path.join(root_dir, i)
            if os.path.isdir(path):
                upload_dir(path)

            if os.path.isfile(path):
                client.put_object_from_file(bucket_name, path, path)


    upload_dir(file_dir)

except tos.exceptions.TosClientError as e:
    # 操作失败，捕获客户端异常，一般情况为非法请求参数或网络异常
    print('fail with client error, message:{}, cause: {}'.format(e.message, e.cause))
except tos.exceptions.TosServerError as e:
    # 操作失败，捕获服务端异常，可从返回信息中获取详细错误信息
    print('fail with server error, code: {}'.format(e.code))
    # request id 可定位具体问题，强烈建议日志中保存
    print('error with request id: {}'.format(e.request_id))
    print('error with message: {}'.format(e.message))
    print('error with http code: {}'.format(e.status_code))
    print('error with ec: {}'.format(e.ec))
    print('error with request url: {}'.format(e.request_url))
except Exception as e:
    print('fail with unknown error: {}'.format(e))
```

<span id="进度条处理"></span>
### **进度条处理**
:::tip
对于字符串、Bytes 和本地文件四种形式的数据，支持进度条功能。网络流等类型数据无法获取上传内容的大小，因此回调时不会返回对象总体大小。
:::
以下的代码以上传字符串为例，介绍如何使用进度条。
```python
import os
import tos

from tos import DataTransferType

# 从环境变量获取 AK 和 SK 信息。
ak = os.getenv('TOS_ACCESS_KEY')
sk = os.getenv('TOS_SECRET_KEY')
# your endpoint 和 your region 填写Bucket 所在区域对应的Endpoint。# 以华北2(北京)为例，your endpoint 填写 tos-cn-beijing.volces.com，your region 填写 cn-beijing。
endpoint = "your endpoint"
region = "your region"
bucket_name = "bucket-test"
# 对象名称，例如 example_dir 下的 example_object.txt 文件，则填写为 example_dir/example_object.txt
object_key = "object-test"
try:
    def percentage(consumed_bytes: int, total_bytes: int, rw_once_bytes: int,
                   type: DataTransferType):
        if total_bytes:
            rate = int(100 * float(consumed_bytes) / float(total_bytes))
            print("rate:{}, consumed_bytes:{},total_bytes{}, rw_once_bytes:{}, type:{}".format(rate, consumed_bytes, total_bytes, rw_once_bytes, type))
    # 创建 TosClientV2 对象，对桶和对象的操作都通过 TosClientV2 实现。
    client = tos.TosClientV2(ak, sk, endpoint, region)
    # data_transfer_listener 为可选参数， 用于实现进度条功能。
    client.put_object(bucket_name, object_key, content='a' * 1024 * 1024, data_transfer_listener=percentage)
except tos.exceptions.TosClientError as e:
    # 操作失败，捕获客户端异常，一般情况为非法请求参数或网络异常
    print('fail with client error, message:{}, cause: {}'.format(e.message, e.cause))
except tos.exceptions.TosServerError as e:
    # 操作失败，捕获服务端异常，可从返回信息中获取详细错误信息
    print('fail with server error, code: {}'.format(e.code))
    # request id 可定位具体问题，强烈建议日志中保存
    print('error with request id: {}'.format(e.request_id))
    print('error with message: {}'.format(e.message))
    print('error with http code: {}'.format(e.status_code))
    print('error with ec: {}'.format(e.ec))
    print('error with request url: {}'.format(e.request_url))
except Exception as e:
    print('fail with unknown error: {}'.format(e))
```

<span id="配置客户端限速"></span>
### **配置客户端限速**
以下代码用于普通上传时客户端限速。
```python
import os
import tos

from tos import RateLimiter

# 从环境变量获取 AK 和 SK 信息。
ak = os.getenv('TOS_ACCESS_KEY')
sk = os.getenv('TOS_SECRET_KEY')
# your endpoint 和 your region 填写Bucket 所在区域对应的Endpoint。# 以华北2(北京)为例，your endpoint 填写 tos-cn-beijing.volces.com，your region 填写 cn-beijing。
endpoint = "your endpoint"
region = "your region"
bucket_name = "bucket-test"
# 对象名称，例如 example_dir 下的 example_object.txt 文件，则填写为 example_dir/example_object.txt
object_key = "object-test"
try:
    client = tos.TosClientV2(ak, sk, endpoint, region)

    # TOS Python SDK 通过最基本的令牌桶算法实现了客户端限速，其中rate为发送令牌的速率，capacity为总容量
    # 以下配置的意义为5mb/s的平均上传速率，最高支持 10 + 5 mb/s的下载速率
    rate_limiter = RateLimiter(rate=5 * 1024 * 1024, capacity=10 * 1024 * 1024)
    client.put_object(bucket_name, object_key, content='a' * 1024 * 1024, rate_limiter=rate_limiter)
except tos.exceptions.TosClientError as e:
    # 操作失败，捕获客户端异常，一般情况为非法请求参数或网络异常
    print('fail with client error, message:{}, cause: {}'.format(e.message, e.cause))
except tos.exceptions.TosServerError as e:
    # 操作失败，捕获服务端异常，可从返回信息中获取详细错误信息
    print('fail with server error, code: {}'.format(e.code))
    # request id 可定位具体问题，强烈建议日志中保存
    print('error with request id: {}'.format(e.request_id))
    print('error with message: {}'.format(e.message))
    print('error with http code: {}'.format(e.status_code))
    print('error with ec: {}'.format(e.ec))
    print('error with request url: {}'.format(e.request_url))
except Exception as e:
    print('fail with unknown error: {}'.format(e))
```

<span id="相关文档"></span>
## **相关文档**
关于上传对象的 API 文档，请参见 [PutObject](/docs/6349/74860)。

