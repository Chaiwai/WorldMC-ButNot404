import os
import shutil

def organize_and_rename_files():
    # 获取当前目录
    current_dir = os.getcwd()
    
    # 遍历当前目录下的所有文件
    for filename in os.listdir(current_dir):
        if filename.endswith('.png') and '_' in filename:
            # 分割文件名
            parts = filename.split('_')
            if len(parts) == 2:  # 确保格式是a_b.png
                folder_name = parts[0]
                new_filename = parts[1]  # 已经是b.png，因为split('.')[0]会去掉.png
                
                # 创建目标文件夹（如果不存在）
                folder_path = os.path.join(current_dir, folder_name)
                os.makedirs(folder_path, exist_ok=True)
                
                # 源文件路径和目标文件路径
                src_path = os.path.join(current_dir, filename)
                dst_path = os.path.join(folder_path, new_filename)
                
                # 移动并重命名文件
                shutil.move(src_path, dst_path)
                print(f"已移动并重命名: {filename} -> {folder_name}/{new_filename}")

if __name__ == "__main__":
    organize_and_rename_files()
    print("文件整理完成！")