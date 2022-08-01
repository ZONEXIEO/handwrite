from PIL import Image
from PIL import ImageFont, ImageDraw

img = Image.new('RGB', (3508, 2480), color = (255,255,255))
back_im = img.copy()

char_x_pos = 0
char_y_pos = 50

quotation_mark_count = 0

char_width = 100
char_height = 100

files_count = 1

def computer_science_convert(file):
    f = open(file, "r+")

    new_text = str(f.read())
    new_text = new_text.replace("Console.WriteLine","C.WL")
    new_text = new_text.replace("Console.ReadLine","C.WL")            
    f.truncate(0)
    f.seek(0)
    f.write(new_text)


def remove_spaces(file):
    f = open(file, "r+")
    new_text = ""
    for line in f.readlines():
        if "Static" not in line:
            line = line.replace("   ","")
        else:
            pass
        new_text += line

    f.truncate(0)
    f.seek(0)
    f.write(new_text)
    
    #function to remove useless spaces in order to make more space in the page
    #personal use for the dev

def text_to_img(file):
    global char_x_pos, char_y_pos, quotation_mark_count, files_count, back_im

    f = open(file, "r")
    for line in f.readlines():
        if char_y_pos + 100 > 2480:
            back_im.save(f'handwrite_{files_count}.png', quality=95)
            files_count += 1
            back_im = img.copy()
            char_y_pos = 0
            char_x_pos = 0


        for char in line:
            if char == " ":
                char_x_pos += 100

            else:
                if char != "\n":
                    if char.isupper():
                        char_img = Image.open(f"abc/{char}_.png")
                        char_img = char_img.resize((char_width,char_height))
                        char_img = char_img.convert("RGBA")

                        back_im.paste(char_img, (char_x_pos, char_y_pos-10), char_img)
                        char_x_pos+=70
                    elif char == ".":
                        char_img = Image.open(f"abc/point.png")
                        char_img = char_img.resize((char_width,char_height))
                        char_img = char_img.convert("RGBA")

                        back_im.paste(char_img, (char_x_pos, char_y_pos+50), char_img)
                        char_x_pos+=70
                    elif char == '"':
                        if quotation_mark_count == 0:
                            char_img = Image.open(f"abc/quotation_mark_1.png")
                            char_img = char_img.resize((char_width,char_height))
                            char_img = char_img.convert("RGBA")

                            back_im.paste(char_img, (char_x_pos-10, char_y_pos-20), char_img)
                            char_x_pos+=70
                            quotation_mark_count += 1
                        else: 
                            char_img = Image.open(f"abc/quotation_mark_2.png")
                            char_img = char_img.resize((char_width,char_height))
                            char_img = char_img.convert("RGBA")

                            back_im.paste(char_img, (char_x_pos-10, char_y_pos-20), char_img)
                            char_x_pos+=70
                            quotation_mark_count = 0
                    elif char== ",":
                        char_img = Image.open(f"abc/{char}.png")
                        char_img = char_img.resize((100,150)) ## special width and height 
                        char_img = char_img.convert("RGBA")

                        back_im.paste(char_img, (char_x_pos, char_y_pos+30), char_img)
                        char_x_pos+=70
                        quotation_mark_count = 0
                    elif char== "*":
                        char_img = Image.open(f"abc/star.png")
                        char_img = char_img.resize((char_width,char_height)) ## special width and height 
                        char_img = char_img.convert("RGBA")

                        back_im.paste(char_img, (char_x_pos, char_y_pos+30), char_img)
                        char_x_pos+=70
                        quotation_mark_count = 0
                    elif char== "/":
                        char_img = Image.open(f"abc/slash.png")
                        char_img = char_img.resize((char_width,char_height)) ## special width and height 
                        char_img = char_img.convert("RGBA")

                        back_im.paste(char_img, (char_x_pos, char_y_pos+30), char_img)
                        char_x_pos+=70
                        quotation_mark_count = 0
                    else: 
                        char_img = Image.open(f"abc/{char}.png")
                        char_img = char_img.resize((char_width,char_height))
                        char_img = char_img.convert("RGBA")

                        back_im.paste(char_img, (char_x_pos, char_y_pos), char_img)
                        char_x_pos+=70

        char_y_pos += 100
        char_x_pos=0


    back_im.save(f'handwrite_{files_count}.png', quality=95)





if __name__ == "__main__":
    file_name = input("enter file name (example.txt): ")
    remove_spaces(file_name)
    computer_science_convert(file_name)
    text_to_img(file_name)

