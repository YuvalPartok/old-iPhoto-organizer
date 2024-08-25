import os
import shutil

# Insert the path of the main directory that contains all of the smaller direcrories with the photos and the destination path
origin_path = r"C:\Users\yuval\OneDrive - post.bgu.ac.il\שולחן העבודה\תמונות\אחר\תמונות iPhoto"
dest_path = r"C:\Users\yuval\OneDrive - post.bgu.ac.il\שולחן העבודה\תמונות\אחר\iPhoto pics organized"

def organize_folders(origin_path, dict=None, dest_path=None):
    
    main_folder = os.fsencode(origin_path)
    for dir in os.listdir(main_folder):
        dir_name = os.fsdecode(dir)

        dir_list = dir_name.split()
        day = dir_list[0]
        month = dict[dir_list[1]]
        year = dir_list[2]

        year_dir = os.path.join(dest_path, year)
        if os.path.isdir(year_dir):
            pass
        else:
            os.mkdir(year_dir)

        source_dir = os.path.join(origin_path, dir_name)
        month_dir = os.path.join(year_dir, month)

        if os.path.isdir(month_dir):
            pass
        else:
            os.mkdir(month_dir)

        copy_all_files(source_dir=source_dir, destination_folder=month_dir)


def copy_all_files(source_dir, destination_folder):
    for file in os.listdir(source_dir):
        source_file = os.path.join(source_dir, file)
        destination_file = os.path.join(destination_folder, file)
        if os.path.isfile(source_file):  # Ensure it's a file, not a subdirectory
            shutil.copy2(source_file, destination_file)

month_dict = {"בינו׳": "January",
              "בפבר׳": "February",
              "במרץ": "March",
              "באפר׳": "April",
              "במאי": "May",
              "ביוני": "June",
              "ביולי": "July",
              "באוג׳": "August",
              "בספט׳": "September",
              "באוק׳": "October",
              "בנוב׳": "November",
              "בדצמ׳": "December"}


organize_folders(origin_path=origin_path, dict=month_dict, dest_path=dest_path)
