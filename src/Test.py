from gtts import gTTS
import os
import json
import requests
from requests.exceptions import RequestException
import time
from datetime import datetime
import pygame
import random

Bible = {
        0: {'name': 'GEN', 'chapters': 50},
        1: {'name': 'EXO', 'chapters': 40},
        2: {'name': 'LEV', 'chapters': 27},
        3: {'name': 'NUM', 'chapters': 36},
        4: {'name': 'DEU', 'chapters': 34},
        5: {'name': 'JOS', 'chapters': 24},
        6: {'name': 'JDG', 'chapters': 21},
        7: {'name': 'RUT', 'chapters': 4},
        8: {'name': '1SA', 'chapters': 31},
        9: {'name': '2SA', 'chapters': 24},
        10: {'name': '1KI', 'chapters': 22},
        11: {'name': '2KI', 'chapters': 25},
        12: {'name': '1CH', 'chapters': 29},
        13: {'name': '2CH', 'chapters': 36},
        14: {'name': 'EZR', 'chapters': 10},
        15: {'name': 'NEH', 'chapters': 13},
        16: {'name': 'EST', 'chapters': 10},
        17: {'name': 'JOB', 'chapters': 42},
        18: {'name': 'PSA', 'chapters': 150},
        19: {'name': 'PRO', 'chapters': 31},
        20: {'name': 'ECC', 'chapters': 12},
        21: {'name': 'SNG', 'chapters': 8},
        22: {'name': 'ISA', 'chapters': 66},
        23: {'name': 'JER', 'chapters': 52},
        24: {'name': 'LAM', 'chapters': 5},
        25: {'name': 'EZK', 'chapters': 48},
        26: {'name': 'DAN', 'chapters': 12},
        27: {'name': 'HOS', 'chapters': 14},
        28: {'name': 'JOL', 'chapters': 3},
        29: {'name': 'AMO', 'chapters': 9},
        30: {'name': 'OBA', 'chapters': 1},
        31: {'name': 'JON', 'chapters': 4},
        32: {'name': 'MIC', 'chapters': 7},
        33: {'name': 'NAM', 'chapters': 3},
        34: {'name': 'HAB', 'chapters': 3},
        35: {'name': 'ZEP', 'chapters': 3},
        36: {'name': 'HAG', 'chapters': 2},
        37: {'name': 'ZEC', 'chapters': 14},
        38: {'name': 'MAL', 'chapters': 4},
        39: {'name': 'MAT', 'chapters': 28},
        40: {'name': 'MRK', 'chapters': 16},
        41: {'name': 'LUK', 'chapters': 24},
        42: {'name': 'JHN', 'chapters': 21},
        43: {'name': 'ACT', 'chapters': 28},
        44: {'name': 'ROM', 'chapters': 16},
        45: {'name': '1CO', 'chapters': 16},
        46: {'name': '2CO', 'chapters': 13},
        47: {'name': 'GAL', 'chapters': 6},
        48: {'name': 'EPH', 'chapters': 6},
        49: {'name': 'PHP', 'chapters': 4},
        50: {'name': 'COL', 'chapters': 4},
        51: {'name': '1TH', 'chapters': 5},
        52: {'name': '2TH', 'chapters': 3},
        53: {'name': '1TI', 'chapters': 6},
        54: {'name': '2TI', 'chapters': 4},
        55: {'name': 'TIT', 'chapters': 3},
        56: {'name': 'PHM', 'chapters': 1},
        57: {'name': 'HEB', 'chapters': 13},
        58: {'name': 'JAS', 'chapters': 5},
        59: {'name': '1PE', 'chapters': 5},
        60: {'name': '2PE', 'chapters': 3},
        61: {'name': '1JN', 'chapters': 5},
        62: {'name': '2JN', 'chapters': 1},
        63: {'name': '3JN', 'chapters': 1},
        64: {'name': 'JUD', 'chapters': 1},
        65: {'name': 'REV', 'chapters': 22},
    }

def get_next_book_index(current_book_index):
        total_books = 66
        return (current_book_index + 1) % total_books

def backup():
    text = "Hi, It is time to wake up.\n Hello Sir and Ma, Good Morning to you. I believe you slept well. \n Here is the word of God for today. \nHe that dwelleth in the secret place of the most High shall abide under the shadow of the Almighty. \n2 I will say of the Lord, He is my refuge and my fortress: my God; in him will I trust. \n3 Surely he shall deliver thee from the snare of the fowler, and from the noisome pestilence. \n4 He shall cover thee with his feathers, and under his wings shalt thou trust: his truth shall be thy shield and buckler. \n5 Thou shalt not be afraid for the terror by night; nor for the arrow that flieth by day; \n6 Nor for the pestilence that walketh in darkness; nor for the destruction that wasteth at noonday. \n7 A thousand shall fall at thy side, and ten thousand at thy right hand; but it shall not come nigh thee. \n8 Only with thine eyes shalt thou behold and see the reward of the wicked. \n9 Because thou hast made the Lord, which is my refuge, even the most High, thy habitation;\n 10 There shall no evil befall thee, neither shall any plague come nigh thy dwelling. \n11 For he shall give his angels charge over thee, to keep thee in all thy ways. \n12 They shall bear thee up in their hands, lest thou dash thy foot against a stone. \n13 Thou shalt tread upon the lion and adder: the young lion and the dragon shalt thou trample under feet. \n14 Because he hath set his love upon me, therefore will I deliver him: I will set him on high, because he hath known my name. \n15 He shall call upon me, and I will answer him: I will be with him in trouble; I will deliver him, and honour him. \n16 With long life will I satisfy him, and shew him my salvation.\n"
    language = 'en'
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("output.mp3")
    print("Conversion Complete")
    sound2 = pygame.mixer.Sound("output.mp3")
    sound1.set_volume(0.3)
    sound2.play()
    os.remove("output.mp3")

pygame.mixer.init()

while True: 
    config_file_path = "fam_dev.config"
    chapter = 1
    index = 0
    random_number = random.randint(1, 24)
    filename = str(random_number) + ".mp3"
    sound1 = pygame.mixer.Sound(filename)

    while True:
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"Current time: {current_time}", end='\r') 
        if current_time == "07:00:00":
            print("\nAlarm! Time to wake up!")
            break
        time.sleep(1)

    print("Current Working Directory:", os.getcwd())
    sound1.set_volume(1)
    sound1.play()
    if os.path.exists(config_file_path):
        with open(config_file_path, "r") as config_file:
            config_data = config_file.read()
            config_data = json.loads(config_data)
            chapter = config_data['chapter']
            index = int(config_data['index'])
            url = "https://api.scripture.api.bible/v1/bibles/de4e12af7f28f599-01/chapters/" + config_data['book'] + "." + chapter + "?content-type=text&include-notes=false&include-titles=true&include-chapter-numbers=false&include-verse-numbers=true&include-verse-spans=false"
    else:
        print(f"The file {config_file_path} does not exist. Will start from the beginning")

        url = "https://api.scripture.api.bible/v1/bibles/de4e12af7f28f599-01/chapters/GEN.1?content-type=text&include-notes=false&include-titles=true&include-chapter-numbers=false&include-verse-numbers=true&include-verse-spans=false"
        

    print(url)
    headers = {
        "api-key": "",
        "accept": "application/json"
    }

                
    try:      
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            print("Chapter retrieved successfully\n")
            if 'data' in data and 'content' in data['data']:
                text = data['data']['content']
                text = text.replace('¶', '')
                text = "Hi, It is time to wake up.\n Hello Sir and Ma, Good Morning to you. I believe you slept well. \n Here is the word of God for today.\n" + text

                language = 'en'
                tts = gTTS(text=text, lang=language, slow=False)
                tts.save("output.mp3")
                print("Conversion Complete")
                sound2 = pygame.mixer.Sound("output.mp3")
                sound1.set_volume(0.3)
                sound2.play()
                os.remove("output.mp3")
                if int(chapter) < Bible[index]['chapters']:
                    empty_data = {
                        "index": str(index),
                        "chapter": str(int(chapter) + 1),
                        "book": Bible[index]['name']
                    }

                else:
                    index = get_next_book_index(index)
                    empty_data = {
                        "index": str(index),
                        "chapter": str(1),
                        "book": Bible[index]['name']
                    }

                json_string = json.dumps(empty_data)
                print(json_string)
                config_file = open(config_file_path, "w")
                config_file.write(json_string)
                config_file.close()
                
            else:
                print("Content not found in the response.")
        else:
            text = "Hi, It is time to wake up.\n Hello Sir and Ma, Good Morning to you. I believe you slept well. \n Here is the word of God for today. \nHe that dwelleth in the secret place of the most High shall abide under the shadow of the Almighty. \n2 I will say of the Lord, He is my refuge and my fortress: my God; in him will I trust. \n3 Surely he shall deliver thee from the snare of the fowler, and from the noisome pestilence. \n4 He shall cover thee with his feathers, and under his wings shalt thou trust: his truth shall be thy shield and buckler. \n5 Thou shalt not be afraid for the terror by night; nor for the arrow that flieth by day; \n6 Nor for the pestilence that walketh in darkness; nor for the destruction that wasteth at noonday. \n7 A thousand shall fall at thy side, and ten thousand at thy right hand; but it shall not come nigh thee. \n8 Only with thine eyes shalt thou behold and see the reward of the wicked. \n9 Because thou hast made the Lord, which is my refuge, even the most High, thy habitation;\n 10 There shall no evil befall thee, neither shall any plague come nigh thy dwelling. \n11 For he shall give his angels charge over thee, to keep thee in all thy ways. \n12 They shall bear thee up in their hands, lest thou dash thy foot against a stone. \n13 Thou shalt tread upon the lion and adder: the young lion and the dragon shalt thou trample under feet. \n14 Because he hath set his love upon me, therefore will I deliver him: I will set him on high, because he hath known my name. \n15 He shall call upon me, and I will answer him: I will be with him in trouble; I will deliver him, and honour him. \n16 With long life will I satisfy him, and shew him my salvation.\n"
            # print(text)
            language = 'en'
            tts = gTTS(text=text, lang=language, slow=False)
            tts.save("output.mp3")
            print("Conversion Complete")
            sound2 = pygame.mixer.Sound("output.mp3")
            sound1.set_volume(0.3)
            sound2.play()
            # os.system("mpg321 output.mp3")
            os.remove("output.mp3")

            

    except RequestException as e:
        text = "Hi, It is time to wake up.\n Hello Sir and Ma, Good Morning to you. I believe you slept well. \n Here is the word of God for today. \nHe that dwelleth in the secret place of the most High shall abide under the shadow of the Almighty. \n2 I will say of the Lord, He is my refuge and my fortress: my God; in him will I trust. \n3 Surely he shall deliver thee from the snare of the fowler, and from the noisome pestilence. \n4 He shall cover thee with his feathers, and under his wings shalt thou trust: his truth shall be thy shield and buckler. \n5 Thou shalt not be afraid for the terror by night; nor for the arrow that flieth by day; \n6 Nor for the pestilence that walketh in darkness; nor for the destruction that wasteth at noonday. \n7 A thousand shall fall at thy side, and ten thousand at thy right hand; but it shall not come nigh thee. \n8 Only with thine eyes shalt thou behold and see the reward of the wicked. \n9 Because thou hast made the Lord, which is my refuge, even the most High, thy habitation;\n 10 There shall no evil befall thee, neither shall any plague come nigh thy dwelling. \n11 For he shall give his angels charge over thee, to keep thee in all thy ways. \n12 They shall bear thee up in their hands, lest thou dash thy foot against a stone. \n13 Thou shalt tread upon the lion and adder: the young lion and the dragon shalt thou trample under feet. \n14 Because he hath set his love upon me, therefore will I deliver him: I will set him on high, because he hath known my name. \n15 He shall call upon me, and I will answer him: I will be with him in trouble; I will deliver him, and honour him. \n16 With long life will I satisfy him, and shew him my salvation.\n"
        # print(text)
        language = 'en'
        tts = gTTS(text=text, lang=language, slow=False)
        tts.save("output.mp3")
        print("Conversion Complete")
        sound2 = pygame.mixer.Sound("output.mp3")
        sound1.set_volume(0.3)
        sound2.play()
        # os.system("mpg321 output.mp3")
        os.remove("output.mp3")





