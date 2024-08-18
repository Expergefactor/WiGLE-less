import os
import sys
import subprocess


def menu():
    menu_script = f"python3 menu.py"
    subprocess.run(menu_script, shell=True)


def checkpermissions():
    try:
        if os.geteuid() != 0:
            print("\n\033[91;1m Secure erase function requires Super User privileges, elevating to sudo...\033[0m")
            args = ["sudo", sys.executable] + sys.argv
            os.execvp("sudo", args)
    except PermissionError:
        pass


def overwrite_file(file_path, overwrite_passes=1):
    try:
        with open(file_path, 'r+b') as f:
            length = os.path.getsize(file_path)
            for _ in range(overwrite_passes):
                f.seek(0)
                f.write(os.urandom(length))
                f.flush()
                os.fsync(f.fileno())
    except Exception as error_overwrite:
        print(f"\033[91;1m Error overwriting file {file_path}: {error_overwrite}\033[0m")
        return False

    try:
        os.remove(file_path)
    except Exception as error_delete:
        print(f"\033[91;1m Error removing file {file_path}: {error_delete}\033[0m")
        return False

    if os.path.exists(file_path):
        print(f"\033[91;1m File {file_path} was not successfully removed.\033[0m")
        return False

    print(f"\n\033[1;92m Success, \033[1;93m{file_path}\033[1;92m nuked!\033[0m\n")
    return True


def secure_erase_folder(folder_path, overwrite_passes=1, dry_run=False):

    if not os.path.exists(folder_path):
        print(f"\033[91;1m Error: {folder_path} does not exist.\033[0m")
        return

    files_found = False

    for name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, name)
        if os.path.isfile(file_path):
            files_found = True
            if dry_run:
                print(f"        {file_path}")
            else:
                if not overwrite_file(file_path, overwrite_passes):
                    print(f"\033[91;1m Failed to securely erase {file_path}\033[0m")

    if not files_found:
        input("\033[91;1m No files found. Press enter to return to the menu.\033[0m")
        menu()


if __name__ == '__main__':
    folder_to_erase = 'files/DB_files'
    overwrite_passes = 1
    dry_run = True

    checkpermissions()

    print("\n\033[1;97m Finding Original database files to clean up...\033[1;93m\n")
    secure_erase_folder(folder_to_erase, overwrite_passes=overwrite_passes, dry_run=True)

    confirm = input("\n\033[91;1m WARNING!\n\033[1;97m"
                    " This will erase the files listed above & cannot be undone, proceed?\n"
                    " Enter \033[1;93my\033[1;97m or \033[1;93mn\033[0m: ")
    if confirm.lower() == 'y':
        dry_run = False
        secure_erase_folder(folder_to_erase, overwrite_passes=overwrite_passes, dry_run=dry_run)
        input("\033[1;93m Press enter to return to the menu.\033[0m")
        menu()

    if confirm.lower() == 'n':
        print("\n\033[1;92m Aborted!\033[0m")
        input("\033[1;93m Press enter to return to the menu.\033[0m")
        menu()
