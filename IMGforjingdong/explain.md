主要技术点

1. 多线程

2. 使用python第三方库实现avif转jpeg



代码为出初始版本，未优化。

如何实现avif转jpeg

> 使用第三方库pillow 和 pillow库关于处理avif的插件 pillow-avif-plugin
>
> 开发中出现的问题
>
> 在没导入import pillow_avif 读取avif文件报错
>
> 导入之后就正常了
>
> 处理步骤
>
> ```python
> image = Image.open('imgSrc')
> # 转换为rgb
> image = image.convert("RGB")
> output_path = 'img/01.jpg'
> image.save(output_path, "JPEG")
> ```

