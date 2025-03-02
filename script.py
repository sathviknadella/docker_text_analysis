import os
import collections
import socket

# File paths
input_files = ["/home/data/IF-1.txt", "/home/data/AlwaysRememberUsThisWay-1.txt"]
output_file = "/home/data/output/result.txt"

# Dictionary to store word counts
word_counts = {}

# Process each file
for file_path in input_files:
    with open(file_path, "r", encoding="utf-8") as f:
        words = f.read().lower().split()
        words = [word.strip(".,!?()[]") for word in words]
        word_counts[file_path] = collections.Counter(words)

# Get container IP
container_ip = socket.gethostbyname(socket.gethostname())

# Write results to output file
with open(output_file, "w") as f:
    for file_path, counter in word_counts.items():
        total_words = sum(counter.values())
        f.write(f"Word count in {os.path.basename(file_path)}: {total_words}\n")
    
    grand_total = sum(sum(counter.values()) for counter in word_counts.values())
    f.write(f"Grand total word count: {grand_total}\n\n")

    # Find top 3 words in each file
    for file_path, counter in word_counts.items():
        f.write(f"Top 3 most frequent words in {os.path.basename(file_path)}:\n")
        for word, count in counter.most_common(3):
            f.write(f"{word}: {count}\n")
        f.write("\n")

    f.write(f"Container IP Address: {container_ip}\n")

# Print to console
with open(output_file, "r") as f:
    print(f.read())

print("result.txt successfully written!")

