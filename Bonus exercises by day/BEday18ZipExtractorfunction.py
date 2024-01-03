import zipfile


def extract_archive(ziparchive_path, dest_dir):
    # getting the zipfile path in read mode
    with zipfile.ZipFile(ziparchive_path, 'r') as zipfileobject:
        zipfileobject.extractall(dest_dir)


# testing the function by calling it and providing zip file path and destination dir path

if __name__ == "__main__":
    extract_archive("compressed.zip",
                    dest_dir="C:/Users/saikr/Documents/pycharm projects/Bonus exercises by day/destination day18 "
                             "bonus zip extractor")
