## Task
当前 skill `SeeDream Image Generator` 只支持基于提示词生成单图或多图，增加支持传入输入参考图生成单图或多图，以覆盖Seedream 4.0-4.5 教程.md 中“基础使用”章节中包含的多种模式。

## 参考文档
@resource/docs/Seedream 4.0-4.5 教程.md  

## 更新 Workflow Decision Tree
更新节点“Single image or multiple images?” 为“Output Single image or multiple images?”

增加检查输入参考图的节点：
if input reference images mentioned as urls in query:
    pass the input image urls to the new argument "--input-images" of  generate_image.py 

## 实现建议
* generate_image.py 增加输入参考图的argument "--input-images"

## 约束
* 更新skill的py和skill.md 体现对输入参考图的支持
* 只使用OpenAI API协议
