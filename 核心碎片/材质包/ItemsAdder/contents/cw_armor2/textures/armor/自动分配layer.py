import os
import shutil

def organize_armor_files():
    # 获取当前目录
    current_dir = os.getcwd()
    
    # 遍历当前目录下的所有文件
    for filename in os.listdir(current_dir):
        if not filename.endswith('.png'):
            continue
        
        # 检查文件名格式
        if '_layer_1.png' in filename or '_layer_2.png' in filename:
            try:
                # 提取前缀（xxxxx部分）
                prefix = filename.split('_layer_')[0]
                
                # 创建目标文件夹（如果不存在）
                target_dir = os.path.join(current_dir, prefix)
                os.makedirs(target_dir, exist_ok=True)
                
                # 确定新文件名
                layer_num = filename.split('_layer_')[1]
                new_filename = f"layer_{layer_num}"
                
                # 源文件和目标文件路径
                src_path = os.path.join(current_dir, filename)
                dst_path = os.path.join(target_dir, new_filename)
                
                # 移动并重命名文件
                shutil.move(src_path, dst_path)
                print(f"已移动并重命名: {filename} -> {prefix}/{new_filename}")
                
            except Exception as e:
                print(f"处理 {filename} 时出错: {str(e)}")
                continue

if __name__ == "__main__":
    print("开始整理盔甲纹理文件...")
    organize_armor_files()
    print("整理完成!")