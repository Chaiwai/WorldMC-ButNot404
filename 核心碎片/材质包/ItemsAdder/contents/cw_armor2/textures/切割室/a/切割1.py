import os
from PIL import Image

def split_images_into_slices():
    # 获取当前目录
    current_dir = os.getcwd()
    
    # 设置切片宽度
    slice_width = 64
    
    # 遍历当前目录下的所有文件
    for filename in os.listdir(current_dir):
        filepath = os.path.join(current_dir, filename)
        
        # 只处理文件（跳过目录）
        if not os.path.isfile(filepath):
            continue
            
        try:
            # 尝试打开图片文件
            with Image.open(filepath) as img:
                # 获取图片尺寸
                width, height = img.size
                
                # 计算可以切多少片
                num_slices = width // slice_width
                if num_slices == 0:
                    print(f"跳过 {filename} - 宽度小于 {slice_width} 像素")
                    continue
                
                # 创建目标文件夹
                basename = os.path.splitext(filename)[0]
                output_dir = os.path.join(current_dir, basename)
                os.makedirs(output_dir, exist_ok=True)
                
                print(f"正在处理 {filename} ({width}x{height}) -> 切成 {num_slices} 片")
                
                # 切割图片
                for i in range(num_slices):
                    left = i * slice_width
                    right = left + slice_width
                    
                    # 确保不会超出图片边界
                    if right > width:
                        right = width
                    
                    # 切割并保存
                    slice_img = img.crop((left, 0, right, height))
                    slice_filename = f"{basename}_{i+1}.png"
                    slice_path = os.path.join(output_dir, slice_filename)
                    slice_img.save(slice_path)
                    
                    print(f"  保存切片: {slice_filename}")
                    
        except Exception as e:
            print(f"处理 {filename} 时出错: {str(e)}")
            continue

if __name__ == "__main__":
    print("开始图片切割处理...")
    split_images_into_slices()
    print("处理完成!")