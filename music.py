import os
import shutil
import random
import json

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
sound_dir = os.path.join(script_dir, "Sound")
output_folder = os.path.join(script_dir, "OutputFolder")

# Get the path to the blacklist JSON file from the environment variable, default to 'blacklist.json'
blacklist_file_path = os.path('./music_blacklist.json')

# Load the blacklist from the JSON file
if os.path.exists(blacklist_file_path):
    with open(blacklist_file_path, 'r') as f:
        blacklist = json.load(f).get("blacklisted_files", [])
        # Convert blacklist to lowercase for case-insensitive comparison
        blacklist = [item.lower() for item in blacklist]
else:
    print(f"Blacklist file not found at {blacklist_file_path}. Exiting.")
    exit(1)

# Ensure sound_dir exists
if not os.path.isdir(sound_dir):
    print(f"Sound directory {sound_dir} does not exist. Exiting.")
    exit(1)

# Create the OutputFolder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

print(f"Working in directory: {sound_dir}")
print(f"Output will be stored in: {output_folder}")

# List all files in the sound_dir
all_files = os.listdir(sound_dir)
files_to_swap = []
blacklisted_files = []

# Collect files to swap and log blacklisted files
for f in all_files:
    file_path = os.path.join(sound_dir, f)
    if os.path.isfile(file_path):
        if f.lower() in blacklist:
            blacklisted_files.append(f)
            print(f"Copied {f} to {f}")
            try:
                shutil.copy2(file_path, os.path.join(output_folder, f))
            except Exception as e:
                print(f"Error during file operation for blacklisted file {f}: {e}")
        else:
            files_to_swap.append(f)

n = len(files_to_swap)

if n < 2:
    print("Not enough files to swap.")
else:
    # Shuffle the list of files
    shuffled_files = random.sample(files_to_swap, len(files_to_swap))

    # Copy files to the OutputFolder with swapped names
    for original, new_name in zip(files_to_swap, shuffled_files):
        src = os.path.join(sound_dir, original)
        dst = os.path.join(output_folder, new_name)

        try:
            shutil.copy2(src, dst)
            print(f"Copied {original} to {new_name}")
        except Exception as e:
            print(f"Error during file operation for {original}: {e}")

print("Finished processing.")
