import os


# config

config_formats = {'Archives':    ['.rar', '.7z', '.zip'],
                  'Torrents':    ['.torrent'],
                  'Videos':      ['.mp4', '.mkv', 'avi'],
                  'Pictures':    ['.jpeg', '.jpg', '.png'],
                  'Documents':   ['.doc', '.docx', '.txt', '.pkpass', '.isc', '.pdf', '.xlsx'],
                  'Executables': ['.exe', '.html'],
                  'Trash':       ['.pub', '.key', '.crdownload']
                  }
config_dirs = [config_formats.keys()]


def sorting_Algo(dirpath,
                  config_dirs,
                  config_formats,
                  files):
    for j in config_dirs:
        folder = str(j)
        for k in config_formats.get(folder):
            for i in files:
                if os.path.splitext(i)[1] == k:
                    print(os.path.join(dirpath, folder, i))
                    os.replace(os.path.join(dirpath, i), os.path.join(dirpath, folder, i))


def ab_sort(dir_entities, dirpath):
    dirs = []
    file = []
    for entity in dir_entities:
        if os.path.isdir(os.path.join(dirpath, entity)): dirs.append(entity)
        if os.path.isfile(os.path.join(dirpath, entity)): file.append(entity)
    return file


def folder_create(path, config_dirs):
    for dir in config_dirs:
        if not os.path.isdir(os.path.join(dirpath, str(dir))):
            os.mkdir(os.path.join(path, dir))


while True:
    dirpath = input('Please paste the dir path to sort: ')
    dirpath = dirpath.replace('"', '')
    if os.path.exists(dirpath) == 1:
        # start
        dir_entities = os.listdir(dirpath)
        folder_create(dirpath, config_formats.keys())

        files = ab_sort(dir_entities, dirpath)

        sorting_Algo(dirpath, config_formats.keys(), config_formats, files)
        ending = input('program finished successfully, press any key to exit ')

        break
    else:
        print('Please enter the correct path')
