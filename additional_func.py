#функция, чтобы разделить путь до файла на название файла без расширений
def get_name_out_of_path(files):
    out=[0]*(len(files))
    for i in range(len(files)):
        out[i]=files[i].split('\\')[-1]
    return out