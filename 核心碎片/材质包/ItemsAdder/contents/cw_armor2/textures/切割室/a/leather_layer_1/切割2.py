import os
from PIL import Image

def crop_and_resize_images():
    # 获取当前目录
    current_dir = os.getcwd()
    
    # 设置目标尺寸
    target_width = 64
    target_height = 32
    
    # 遍历当前目录下的所有PNG文件
    for filename in os.listdir(current_dir):
        if not filename.lower().endswith('.png'):
            continue
            
        filepath = os.path.join(current_dir, filename)
        
        try:
            with Image.open(filepath) as img:
                # 获取原始尺寸
                width, height = img.size
                
                print(f"处理 {filename} ({width}x{height}) -> {target_width}x{target_height}")
                
                # 计算需要裁剪的区域（最上方的32像素）
                if height < target_height:
                    print(f"警告: {filename} 高度小于{target_height}像素，将拉伸处理")
                    crop_area = (0, 0, width, height)
                else:
                    crop_area = (0, 0, width, target_height)
                
                # 先裁剪最上方32像素
                cropped_img = img.crop(crop_area)
                
                # 然后调整到目标尺寸
                resized_img = cropped_img.resize((target_width, target_height), Image.LANCZOS)
                
                # 保存文件（覆盖原文件）
                resized_img.save(filepath)
                print(f"已保存: {filename}")
                
        except Exception as e:
            print(f"处理 {filename} 时出错: {str(e)}")
            continue

if __name__ == "__main__":
    print("开始图片处理...")
    crop_and_resize_images()
    print("处理完成!")