#!/usr/bin/env python
# coding: utf-8

# Import modules
import sys
import os
import re
import copy
from os import listdir
from os.path import isfile, join

# Setting paths
notebooks_path = "./notebooks/"
content_path = "./content/"
filename_in = [f for f in listdir(notebooks_path) if isfile(join(notebooks_path, f))][0]

# Import notebook file
with open(notebooks_path + filename_in, 'r') as file:
    doc = file.read()
    file.close()

# Fix paths for imgs
doc = doc.replace('![png](', '![png](/')

# Define regexes
chapter_regex = re.compile('\n# {#Kapitel}.*?(?=\n# {#Kapitel}|\n# {#END})', re.DOTALL)
chapter_title_regex = re.compile('(?<=# {#Kapitel}).*?(?=\n)')
chapter_text_regex = re.compile('(?<=\n# {#Kapitel}).*?(?=\n# {#Afsnit}|\n# {#Kapitel}|\n# {#END})', re.DOTALL)

section_regex = re.compile('\n# {#Afsnit}.*?(?=\n# \{#Afsnit|#Kapitel|#END|\n$)', re.DOTALL)
section_title_regex = re.compile('(?<=\n# {#Afsnit}).*?(?=\n)')
section_text_regex = re.compile('(?<=\n# {#Afsnit}).*$', re.DOTALL)

# Define functions
def get_chapters(doc):
    chapters = re.findall(chapter_regex, doc)
    return(chapters)

def get_chapter_titles(doc):
    chapter_titles = re.findall(chapter_title_regex, doc)
    return(chapter_titles)

def get_chapter_text(chapter):
    chapter_title = get_chapter_titles(chapter)[0]
    chapter_text = re.findall(chapter_text_regex, chapter)[0]
    
    chapter_text = chapter_text.replace(chapter_title, "")

    while re.match("\W", chapter_text[0]):
        chapter_text = re.sub("^\W", "", chapter_text)
    
    return(chapter_text)

def create_chapter_front(title, weight):
    front_matter = '---\ntitle: {title}\ntype: chapter\nweight: {weight}\npre: "<b>{weight}. </b>"\n---\n'.format(title = title, weight = weight)
    return(front_matter)

def create_foldername(title):
    first_word = re.findall(r'^.*?(?=\s)', title)[0].lower()
    return(first_word)

def get_sections(chapter):
    sections = re.findall(section_regex, chapter)
    return(sections)

def get_section_title(section):
    section_title = re.findall(section_title_regex, section)[0]
    return(section_title)

def get_section_text(section):
    section_title = get_section_title(section)
    section_text = re.findall(section_text_regex, section)[0]
    
    section_text = section_text.replace(section_title, "")
    
    while re.match("\W", section_text[0]):
        section_text = re.sub("^\W", "", section_text)
    
    return(section_text)

def create_section_filename(title):
    first_word = re.findall(r'^.*?(?=\s)', title)[0].lower()
    filename = first_word + '.md'
    
    return(filename)

def section_front_matter(title, weight):
    front_matter = '---\ntitle: {title}\nweight: {weight}\n---\n'.format(title = title, weight = weight)
    return(front_matter)

# Extract chapters
chapters = get_chapters(doc)
chapter_titles = get_chapter_titles(doc)


# Create chapters dictionary
weight = 1

chapters_dict = dict()
for chapter in chapters:
    chapter_title = re.findall(chapter_title_regex, chapter)[0]
    chapter_front = create_chapter_front(chapter_title, weight)
    chapter_text = get_chapter_text(chapter)
    chapter_sections = get_sections(chapter)
    chapter_foldername = create_foldername(chapter_title)
    
    sections_dict = dict()
    sect_weight = 1
    for section in chapter_sections:
        section_dict = dict()
        section_dict['title'] = get_section_title(section)
        section_dict['front'] = section_front_matter(section_dict['title'], sect_weight)
        section_dict['text'] = get_section_text(section)
        
        sections_dict[section_dict['title']] = section_dict
        
        sect_weight = sect_weight + 1 
        
    chapter_dict = dict()
    
    chapter_dict['title'] = chapter_title
    chapter_dict['front'] = chapter_front
    chapter_dict['text'] = chapter_text
    chapter_dict['folder'] = chapter_foldername
    chapter_dict['sections'] = copy.deepcopy(sections_dict)
    
    chapters_dict[chapter_title] = chapter_dict
    
    weight = weight + 1

# Export files to folders
for chaptkey,chapter in chapters_dict.items():
    
    folder = content_path + chapter['folder']
    chapter_out = chapter['front'] + chapter['text']
    
    if not os.path.isdir(folder):
        os.mkdir(folder)
    with open(folder + '/_index.md', 'w') as outfile:
        outfile.write(chapter_out)
        outfile.close()
    
    for sectkey,section in chapter['sections'].items():
        filename = '/' + create_section_filename(section['title'])
        section_out = section['front'] + section['text']
        
        with open(folder + filename, 'w') as outfile:
            outfile.write(section_out)
            outfile.close()
        
    

