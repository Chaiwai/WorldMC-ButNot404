import os
import shutil

def process_folders():
    # 获取当前目录
    current_dir = os.getcwd()
    
    # 检查文件夹1是否存在
    source_folder = os.path.join(current_dir, "1")
    if not os.path.exists(source_folder) or not os.path.isdir(source_folder):
        print("错误: 文件夹 '1' 不存在或不是一个目录!")
        return
    
    # 获取文件夹1中的所有文件
    source_files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]
    if not source_files:
        print("警告: 文件夹 '1' 中没有文件可复制")
        return
    
    # 遍历当前目录下的所有文件夹
    for folder in os.listdir(current_dir):
        folder_path = os.path.join(current_dir, folder)
        
        # 跳过非目录、文件夹1和当前目录
        if not os.path.isdir(folder_path) or folder == "1" or folder == ".":
            continue
        
        print(f"正在处理文件夹: {folder}")
        
        # 清空目标文件夹
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"删除 {file_path} 时出错: {e}")
        
        # 复制文件夹1中的文件到目标文件夹
        for filename in source_files:
            src_path = os.path.join(source_folder, filename)
            dst_path = os.path.join(folder_path, filename)
            try:
                shutil.copy2(src_path, dst_path)
                print(f"已复制: {filename} -> {folder}/{filename}")
            except Exception as e:
                print(f"复制 {filename} 到 {folder} 时出错: {e}")
    
    print("处理完成!")

if __name__ == "__main__":
    process_folders()