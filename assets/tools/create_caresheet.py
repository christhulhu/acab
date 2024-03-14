import os
import yaml

images = "images"
data = "data"
about = ''''''
hero = '''---
src: images/-hero.jpg
alt: 
attr: 
---
'''
index = '''---
title: 
description: 
type: page
layout: caresheet
bookhidden: true
author:
- 
---
'''

def create_caresheet_files(target):
    dest_folder = os.path.join('../../content/caresheets', target)
    print(f'working dir: {dest_folder}')
    create_caresheet_folder(dest_folder)
    create_images_dir(dest_folder)
    create_data_dir(dest_folder)
    create_data_file(dest_folder, 'about.yml')
    create_data_file(dest_folder, 'caresheet.yml')
    create_data_file(dest_folder, 'galleries.yml')
    create_data_file(dest_folder, 'references.yml')
    create_md_file(dest_folder, 'index.md', index)
    create_md_file(dest_folder, 'about.md')
    create_md_file(dest_folder, 'hero.md', hero)

def create_md_file(dest_folder, file, content = None):
    out = os.path.join(dest_folder, file)
    with open(out, 'w') as file:
        if (content):
            file.write(content)
        else:
            file.write('')

def create_data_file(dest_folder, file):
    out = os.path.join(dest_folder, data, file)
    with open(out, 'w') as file:
        file.write('')

def create_folder(parent, folder):
    if folder:
        target = os.path.join(parent, folder)
    else:
        target = parent
    if not os.path.exists(target):
        print(f'creating DIR {target}')
        os.mkdir(target)
    else:
        print(f'DIR {target} exists!')

def create_images_dir(dest_folder):
    create_folder(dest_folder, images)

def create_data_dir(dest_folder):
    create_folder(dest_folder, data)

def create_caresheet_folder(dest_folder):
    create_folder(dest_folder, '')

create_caresheet_files("scolopendra/alternans_red_giant")