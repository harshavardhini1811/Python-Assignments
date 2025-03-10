# Open the file in read mode
with open("example.txt", "r") as file:
    # Read and process the file in chunks
    chunk_size = 1024  # Read 1KB at a time
    while True:
        chunk = file.read(chunk_size)
        if not chunk:
            break
        print(chunk, end="")  # Print without extra newlines