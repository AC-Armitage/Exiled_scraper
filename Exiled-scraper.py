import requests
import sys
from bs4 import BeautifulSoup

class exiled_script:
    def __init__():
        self.chap_num = chap_num
    def main_page(self):
        global exi_ch_link
        main_page = requests.get(exiled_link)
        if main_page.status_code == 200:
            print("connected")
            main_soup = BeautifulSoup(main_page.content, "html.parser")
            chapter_rows = main_soup.find_all(class_="chapter-row")
            num_chapter = len(chapter_rows)
            progress = 0
            while num_chapter > progress:
                for row in chapter_rows:
                    chapter = row.get_text().strip()
                    #print(chapter.splitlines())
                    progress += 1
            if num_chapter == progress:
                try_link = row.find("a")
                sub_link = try_link["href"]
                exi_ch_link = "https://www.royalroad.com"+sub_link
                num_chapter -= 1
                final_chapter = chapter.splitlines()
                print(f"Number of chapter : {num_chapter}")
                print(f"Latest chapter : {final_chapter[0]}\nuploaded {final_chapter[5]}\nLink : {exi_ch_link}")    
        else:   
            print(f"connection failed status : {main_page.status_code}")
            sys.exit()

    def chapter_page(exi_ch_link):

        
        chapter_page = requests.get(exi_ch_link)
        if chapter_page.status_code == 200:
            chapter_soup = BeautifulSoup(chapter_page.content, "html.parser")
            auth_note = chapter_soup.find("p")
            print(f"AUTOR NOTE:\n{auth_note.text}\n")
            acua_chapter = chapter_soup.find(class_="chapter-inner chapter-content")
            print(f"Chapter:\n\n{acua_chapter.text}")

        else:
            print(f"failed status : {main_page.status_code}")
            sys.exit()
    def chap_choice(chap_num):
        main_page = requests.get(exiled_link)
        if main_page.status_code == 200:
            print("connected")
            main_soup = BeautifulSoup(main_page.content, "html.parser")
            chapter_rows = main_soup.find_all(class_="chapter-row")
            num_chapter = len(chapter_rows)
            progress = -1
            while num_chapter > progress:
                for row in chapter_rows:
                    chapter = row.get_text().strip()
                    progress += 1
                    if chap_num == progress:
                        try_link = row.find("a")
                        sub_link = try_link["href"]
                        exi_ch_link = "https://www.royalroad.com"+sub_link
                        num_chapter -= 1
                        final_chapter = chapter.splitlines()
                        chapter_page = requests.get(exi_ch_link)
                        if chapter_page.status_code == 200:
                            chapter_soup = BeautifulSoup(chapter_page.content, "html.parser")
                            auth_note = chapter_soup.find("p")
                            print(f"AUTOR NOTE:\n{auth_note.text}\n")
                            acua_chapter = chapter_soup.find(class_="chapter-inner chapter-content")
                            print(f"Chapter:\n\n{acua_chapter.text}")
                        else:
                            print(f"failed status : {main_page.status_code}")
                            sys.exit()


if __name__ == "__main__":
    exiled_link = "https://www.royalroad.com/fiction/48769/exiled-prince-reboot"
    exiled_script.main_page(exiled_link)
    while True:
        choice = input("Do you want to read this schapter (y/n/q)?")
        if choice == "y":   
            exiled_script.chapter_page(exi_ch_link)
            break
        elif choice == "n":
            while True:
                choice_2 = input("Do you want to read another chapter (y/n)")
                if choice_2 == "y":
                    try:
                        ch_num = int(input("Insert the chapter number: "))
                        
                        exiled_script.chap_choice(ch_num)

                    except ValueError:
                        print("please insert a valid chapter number!!")
                        pass
                elif choice == "n":
                    print("Okay, closing programe, goodbye")
                    sys.exit()
                else:
                    print("Invalid input plesae retry!!\n")
                    continue
        elif choice == "q":
            print("Okay, closing programe, goodbye")
            sys.exit()
        else:
            print("Invalid input plesae retry!!\n")
            continue
