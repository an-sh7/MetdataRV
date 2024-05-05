# MetaDataRV

This is a Python program designed to remove or view metadata from a file using exiftool. This tool is useful for users who want to protect their privacy by removing sensitive information embedded in files such as photos, documents, or audio files.

## How to Use

1. **Download exiftool**: If you don't want to use the exiftool provided in repository, download exiftool from the [official website](https://exiftool.org/). Extract the ZIP file and rename the executable to `exiftool.exe`.

2. **Setup**: Ensure that all files, including the Python script, the `exiftool.exe` are placed in the same folder.

3. **Run the Program**: To Start the program use `RunApp.bat`.

4. **Options**:
   - Select a button for reading data or removing data

5. **Output**: Depending on your choice, the program will either remove metadata from the specified file(s) or display the metadata information.

## Additional Information

- **Privacy**: Removing metadata can help protect your privacy by eliminating sensitive information such as location data, camera details, and timestamps from files.
  
- **Supported Files**: The program supports various file formats including JPEG, PNG, PDF, MP3, MP4, and more. Exiftool is capable of handling a wide range of file types.

- **Customization**: You can customize the program further by modifying the Python script according to your requirements. For example, you can add additional options or functionality.

- **Dependencies**: This program relies on the exiftool executable. Ensure that it is correctly installed and accessible from the same directory as the Python script.

  ## License
  [MIT License](LICENSE)
