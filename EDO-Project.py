import os

def add_gitkeep_files(directory):
    for root, dirs, files in os.walk(directory):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            if not os.listdir(dir_path):  # Check if the directory is empty
                gitkeep_path = os.path.join(dir_path, '.gitkeep')
                with open(gitkeep_path, 'w') as gitkeep_file:
                    gitkeep_file.write('')  # Create an empty .gitkeep file
                print(f"Added .gitkeep to {dir_path}")

if __name__ == "__main__":
    directory_path = 'D:\\Escuela\\EDO Rugen-Kutta'
    add_gitkeep_files(directory_path)
