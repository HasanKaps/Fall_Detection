import os


Fall_Folder = "Datasets/Fall Sequences"
ADL_Folder = "Datasets/ADL Sequences"

# Function to rename multiple files
def main():
   
    for count, filename in enumerate(os.listdir(ADL_Folder)):
        dst = f"{filename}.mp4"
        src =f"{ADL_Folder}/{filename}"  # foldername/filename, if .py file is outside folder
        dst =f"{ADL_Folder}/{dst}"
         
        # rename() function will
        # rename all the files
        os.rename(src, dst)
        print(f"Renamed {filename} to {dst}")
 
# Driver Code
if __name__ == '__main__':
     
    # Calling main() function
    main()