import os
import shutil
import pathlib


# Pastas exemplo, substituir com os diretórios do próprio PC
source_dir = r'C:/Users/file_organizer' # Pasta onde o projeto fica

archive_dir = r'C:/Users/Archives' # Pasta para arquivos .zip ou .rar

doc_dir = r'C:/Users/Documents' # Pasta para arquivos .docx, .txt, etc

exe_dir = r'C:/Users/Executables' # Pasta para arquivos .exe

image_dir = r'C:/Users/Images' # Pasta para arquivos .jpeg, .png, etc

music_dir = r'C:/Users/Music' # Pasta para arquivos .wav, .mp3, etc

pdf_dir = r'C:/Users/PDFs' # Pasta para arquivos .pdf

video_dir = r'C:/Users/Videos' # Pasta para arquivos .mp4, .avi, etc

file_names = os.listdir(source_dir)

for file_name in file_names:
    extension = pathlib.Path(file_name).suffix # Determina qual a extensão de cada arquivo sendo escaneado
    
    if extension == '.zip' or extension == '.rar':
        shutil.move(os.path.join(source_dir, file_name), archive_dir)
    
    elif extension == '.txt' or extension == '.doc' or extension == '.docx':
        shutil.move(os.path.join(source_dir, file_name), doc_dir)
    
    elif extension == '.exe':
        shutil.move(os.path.join(source_dir, file_name), exe_dir)
    
    elif extension == '.png' or extension == '.jpg' or extension == '.jpeg':
        shutil.move(os.path.join(source_dir, file_name), image_dir)
    
    elif extension == '.mp3' or extension == '.wav':
        shutil.move(os.path.join(source_dir, file_name), music_dir)
    
    elif extension == '.pdf':
        shutil.move(os.path.join(source_dir, file_name), pdf_dir)
    
    elif extension == '.mp4' or extension == '.avi':
        shutil.move(os.path.join(source_dir, file_name), video_dir)
    
