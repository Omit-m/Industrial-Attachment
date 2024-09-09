import os
import csv

content = os.listdir('F:/dataset')

def item_split(content):
    parts = content.split(".")
    return parts[-1]

def is_audio(content):
    ext = item_split(content)
    return ext in ["mp3", "mp4"]

def is_picture(content):
    ext = item_split(content)
    return ext in ["jpg", "png"]

audio_dir = 'F:/dataset/audio'
pictures_dir = 'F:/dataset/picture'

os.makedirs(audio_dir, exist_ok=True)
os.makedirs(pictures_dir, exist_ok=True)

audio_files = []
picture_files = []

for file in content:
    file_path = os.path.join('F:/dataset', file)
    if is_audio(file):
        new_path = os.path.join(audio_dir, file)
        os.rename(file_path, new_path)
        audio_files.append(new_path)
    elif is_picture(file):
        new_path = os.path.join(pictures_dir, file)
        os.rename(file_path, new_path)
        picture_files.append(new_path)

def rename_files(files, ext):
    renamed_files = []
    for idx, file_path in enumerate(sorted(files), start=1):
        new_name = f"{str(idx).zfill(2)}.{ext}"
        new_path = os.path.join(os.path.dirname(file_path), new_name)
        os.rename(file_path, new_path)
        renamed_files.append(new_path)
    return renamed_files

if audio_files:
    audio_ext = item_split(audio_files[0])
    audio_files = rename_files(audio_files, audio_ext)

if picture_files:
    picture_ext = item_split(picture_files[0])
    picture_files = rename_files(picture_files, picture_ext)


with open('F:/dataset/dataset.csv', mode='w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Type', 'File Path'])  # হেডার লেখা

    for file in audio_files:
        csv_writer.writerow(['Audio', file])

    for file in picture_files:
        csv_writer.writerow(['Picture', file])

print(f"CSV file created at {'F:/dataset/dataset.csv'}")
