# File handling

File handling in Python is an essential skill for managing data storage, retrieval, and manipulation.

## Opening a file

To open a file in python we can use 'open()' function.

the open function takes two parameter the file name and the mode.
Here are the common modes.

- **'r'** : Read Mode (default). Opens the file for reading.

- **'w'** : writing Mode. Opens the file for writing(create a new file if file not exists if the file exists it truncates the file to zero length (means empty the file) and the write new contents within it)

- **'a'** : append mode . opens the file for appending content (creates new file if file not exists)

- **'b'** : binary mode. opens the file in binary mode.

- **'+'** : update mode. opens the file for reading and writing

## Reading from a file

- **read()** : Reads entire file

- **readline()** : Reads single line from a file

- **readlines()** : Reads multiple lines from a file and return them as an list

### Note

- file.read(): Reads the entire content of the file. After this operation, the file pointer is at the end of the file.

- file.readline(): Reads one line from the file. However, since the file pointer is already at the end of the file (due to the previous read() operation), this will return an empty string.

- file.readlines(): Reads all remaining lines from the file and returns them as a list of strings. Again, because the file pointer is at the end of the file, this will return an empty list.

## Writing to a file

- **write(str)** : writes a string to a file.

- **writelines(list)** : writes a list of strings to a file.

## Closing file

Always close the file after completing the operations to free up system resources:

    ```python
    file.close()
    ```

## Using with statement

The with statement provides a cleaner and more concise way to work with file objects, ensuring that the file is properly closed after its suite finishes:

```python
with open("example.txt","r") as file:
    content = file.read()
    print(content)
```

## Working with Binary Files

To read and write binary files, open the file in binary mode ('b'):

```python
with open("example.jpg", "rb") as file:
    content = file.read()

with open("example_copy.jpg", "wb") as file:
    file.write(content)

```

## File methods

- **file.seek(offset, whence)** :

  The seek() method allows you to change the current file position. This is useful for reading or writing at a specific location within the file.

- offset: This is the number of bytes to move the file pointer.

- whence: This is the reference point from where the bytes are to be moved. It can take three values:

  - 0: Beginning of the file (default)
  - 1: Current position
  - 2: End of the file

- **file.tell()**

  The tell() method returns the current position of the file pointer. This is helpful for understanding where you are in the file.

- **file.flush()**

The flush() method flushes the internal buffer. When you write data to a file, it may be held in a buffer before being written to the disk. flush() ensures that the buffer is cleared and the data is written to the disk immediately.
