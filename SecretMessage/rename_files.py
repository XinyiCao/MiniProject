import os

def rename_files():
    # (1) get file names from a folder
    file_list = os.listdir(r"/Users/CAO/Pythonia/Udacity/SecretMessage/prank")
    #print(file_list)
    saved_path = os.getcwd()
    print("Current Working Directroy is" + saved_path)
    os.chdir(r"/Users/CAO/Pythonia/Udacity/SecretMessage/prank")

    # (2) for each file, rename filename
    for file_name in file_list:
        to_remove = "0123456789"
        table = str.maketrans("", "", to_remove)
        os.rename(file_name, file_name.translate(table))
        # os.rename(file_name, file_name.translate(None, "0123456789"))
        print("Old Name - "+file_name)
        print("New Name - "+file_name.translate(table))
    os.chdir(saved_path)

rename_files()