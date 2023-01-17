file = input("File name: ")
file_arr = file.split(".")
if len(file_arr) == 1:
    print("application/octet-stream")
else:
    match file_arr[-1].lower().strip():
        case 'jpg':
            print("image/jpeg")
        case 'gif':
            print("image/" + file_arr[-1].lower())
        case 'jpeg':
            print("image/" + file_arr[-1].lower())
        case 'png':
            print("image/" + file_arr[-1].lower())
        case 'pdf':
            print("application/" + file_arr[-1].lower())
        case 'txt':
            print("text/plain")
        case 'zip':
            print("application/" + file_arr[-1].lower())
        case other:
            print("application/octet-stream")
