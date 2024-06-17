def print_media_type(file_name):
    # Define a dictionary mapping file extensions to media types
    media_types = {
        '.gif': 'image/gif',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.png': 'image/png',
        '.pdf': 'application/pdf',
        '.txt': 'text/plain',
        '.zip': 'application/zip'
    }

    # Convert the file name to lowercase for case-insensitive comparison
    file_name = file_name.lower()
    file_name = file_name.strip()
    # Check the file extension
    var = False
    for ext, media_type in media_types.items():
        if file_name.endswith(ext):
            print(media_type)
            var = True

    if var == False:
        print('application/octet-stream')

def main():
    # Prompt the user for the name of a file
    file_name = input("Enter the name of the file: ")

    # Print the media type for the file
    print_media_type(file_name)

if __name__ == "__main__":
    main()




