# image_compress

该程序实现了图片压缩的功能，其原理是通过 PIL.Image.resize() 方法调整图片的宽高实现的。因为经过计算，图片大小和宽高并不成正比，所以无法准确压缩到指定大小，只能通过设定阀值（threshold）曲线救国。如果不通过 math.sqrt() 方法去计算压缩后的图片宽高而直接将 compressed_width 设置成固定值，就可以无视阀值的存在，将图片的宽设定得比原图片大就能实现图片”解压“的效果。

因为一方面考虑到一般情况压缩图片才是大众的需求，另一方面为了迎合项目的主题，所以只将功能设定成压缩。当然，有兴趣的朋友可以根据以上提示以及实际的代码做相应的修改就可以实现图片的放大和缩小。

![压缩前](https://github.com/wmltyq/image_compress/blob/master/uncompress/cat.png)

别看它可爱，实际上它有 2.72 M 那么大！

![压缩前](https://github.com/wmltyq/image_compress/blob/master/compress/cat.png)

给它重新“打扮”一下，一下子就到 816.24 K 了！