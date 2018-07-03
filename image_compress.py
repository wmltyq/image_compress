from glob import glob
from PIL import Image
import os
import math

# 未压缩文件和压缩文件存放位置
uncompress_dir = 'uncompress'
compress_dir = 'compress'

# 图片压缩大小上限值
threshold = 2 * 1024 * 1024

# 设置压缩后的文件宽度
# compressed_width = 1024

# 获取未压缩文件夹下的所有文件
file_names = glob('{}/*'.format(uncompress_dir))


# 压缩图片
def compress_img():
    # 如果输出压缩文件的文件夹不存在则创建
    if not os.path.exists(compress_dir):
        os.makedirs(compress_dir)

    for file_name in file_names:
        with Image.open(file_name) as img:
            # 获取原始图片的文件大小
            file_size = os.path.getsize(file_name)
            # 找出文件大小大于等于压缩上限值的文件
            if file_size >= threshold:
                # 获取原始图片的宽、高
                width, height = img.size
                print(file_name)
                print('  >>>未压缩时：%d × %d，%.2f M' % (width, height, file_size / 1024 / 1024))

                # 调整图片大小并保存
                if width >= height:
                    compressed_width = int(math.sqrt(threshold / 2))
                    compressed_height = int(compressed_width * height / width)
                else:
                    compressed_height = int(math.sqrt(threshold / 2))
                    compressed_width = int(compressed_height * width / height)
                compressed_img = img.resize((compressed_width, compressed_height))
                compressed_dir = file_name.replace(uncompress_dir, compress_dir)
                # 只有文件不存在时才保存
                if not os.path.exists(compressed_dir):
                    compressed_img.save(compressed_dir)

                # 输出压缩后图片的相关信息
                compressed_file_size = os.path.getsize(compressed_dir)
                if compressed_file_size / 1024 < 1024:
                    print('  >>>压缩后：%d × %d，%.2f K' % (compressed_width, compressed_height, compressed_file_size / 1024))
                else:
                    print('  >>>压缩后：%d × %d，%.2f M' % (compressed_width, compressed_height, compressed_file_size / 1024 / 1024))


if __name__ == '__main__':
    compress_img()
