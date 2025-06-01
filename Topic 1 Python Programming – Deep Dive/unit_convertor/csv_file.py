import os
import shutil

def copy_txt_csv_files(source_dir, target_dir):
    try:
        
        if not os.path.isdir(source_dir):
            print(f"Source directory '{source_dir}' does not exist.")
            return
        
        os.makedirs(target_dir, exist_ok=True)
        
        files = [f for f in os.listdir(source_dir)
                 if os.path.isfile(os.path.join(source_dir, f)) and
                    (f.lower().endswith('.txt') or f.lower().endswith('.csv'))]

        if not files:
            print("No .txt or .csv files found.")
            return
        
        for f in files:
            src_path = os.path.join(source_dir, f)
            dst_path = os.path.join(target_dir, f)
            shutil.copy2(src_path, dst_path)
            print(f"Copied: {f}")

        print(f"\nCopied {len(files)} files to '{target_dir}'.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    source = input("Enter source directory path: ").strip()
    target = input("Enter target directory path: ").strip()
    copy_txt_csv_files(source, target)
