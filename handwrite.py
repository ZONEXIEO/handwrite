from PIL import Image

img = Image.new('RGB', (3508, 2480), color=(255, 255, 255))
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
    count = 0

    for line in f.readlines():
        if "Static" not in line and "{" not in line and "}" not in line:
            for char in line:
                if count != 2:
                    if char.replace(" ","") != '':
                        new_text += char
                    else:
                        count +=1
                else:
                    new_text += char
        else:
            new_text += line

        count=0

    #print(new_text)
    f.truncate(0)
    f.seek(0)
    f.write(new_text)
    
    #function to remove useless spaces in order to make more space in the page
    #personal use for the dev

def check_special_char(char):
    global char_x_pos, back_im, quotation_mark_count
    ####################################################################################
    # this function is made to check special chars to separate this from the abc..     #
    ####################################################################################

    if char == ".":
        char_img = Image.open(f"abc/point.png")
        char_img = char_img.resize((char_width,char_height))
        char_img = char_img.convert("RGBA")

        back_im.paste(char_img, (char_x_pos, char_y_pos+50), char_img)
        char_x_pos += 70
    elif char == '"':
        print(quotation_mark_count)
        if quotation_mark_count == 0:
            char_img = Image.open(f"abc/quotation_mark_1.png")
            char_img = char_img.resize((char_width,char_height))
            char_img = char_img.convert("RGBA")

            back_im.paste(char_img, (char_x_pos-10, char_y_pos-20), char_img)
            char_x_pos += 70
            quotation_mark_count += 1

        else: 
            char_img = Image.open(f"abc/quotation_mark_2.png")
            char_img = char_img.resize((char_width,char_height))
            char_img = char_img.convert("RGBA")

            back_im.paste(char_img, (char_x_pos-10, char_y_pos-20), char_img)
            char_x_pos += 70
            quotation_mark_count = 0
    elif char == ",":
        char_img = Image.open(f"abc/{char}.png")
        char_img = char_img.resize((100,150)) ## special width and height 
        char_img = char_img.convert("RGBA")

        back_im.paste(char_img, (char_x_pos, char_y_pos+30), char_img)
        char_x_pos += 70
    elif char == ">":
        char_img = Image.open(f"abc/greaterthan.png")
        char_img = char_img.resize((char_width,char_height)) 
        char_img = char_img.convert("RGBA")

        back_im.paste(char_img, (char_x_pos, char_y_pos+30), char_img)
        char_x_pos += 70
        quotation_mark_count = 0
    elif char == "<":
        char_img = Image.open(f"abc/less-than.png")
        char_img = char_img.resize((char_width,char_height)) ## special width and height 
        char_img = char_img.convert("RGBA")

        back_im.paste(char_img, (char_x_pos, char_y_pos+30), char_img)
        char_x_pos += 70
        quotation_mark_count = 0
    elif char == "*":
        char_img = Image.open(f"abc/star.png")
        char_img = char_img.resize((char_width,char_height)) 
        char_img = char_img.convert("RGBA")

        back_im.paste(char_img, (char_x_pos, char_y_pos+30), char_img)
        char_x_pos += 70
        quotation_mark_count = 0
    elif char == "/":
        char_img = Image.open(f"abc/slash.png")
        char_img = char_img.resize((char_width, char_height))
        char_img = char_img.convert("RGBA")

        back_im.paste(char_img, (char_x_pos, char_y_pos+30), char_img)
        char_x_pos += 70
        quotation_mark_count = 0
    elif char == "(":
        char_img = Image.open(f"abc/{char}.png")
        char_img = char_img.resize((char_width, char_height))
        char_img = char_img.convert("RGBA")

        back_im.paste(char_img, (char_x_pos, char_y_pos), char_img)
        char_x_pos += 70
        quotation_mark_count = 0
    elif char == ")":
        char_img = Image.open(f"abc/{char}.png")
        char_img = char_img.resize((char_width, char_height))
        char_img = char_img.convert("RGBA")

        back_im.paste(char_img, (char_x_pos, char_y_pos), char_img)
        char_x_pos += 70
        quotation_mark_count = 0
    elif char == "{":
        char_img = Image.open(f"abc/{char}.png")
        char_img = char_img.resize((150, 150))
        char_img = char_img.convert("RGBA")

        back_im.paste(char_img, (char_x_pos, char_y_pos), char_img)
        char_x_pos += 70
        quotation_mark_count = 0
    elif char == "}":
        char_img = Image.open(f"abc/{char}.png")
        char_img = char_img.resize((150, 150))   
        char_img = char_img.convert("RGBA")

        back_im.paste(char_img, (char_x_pos, char_y_pos), char_img)
        char_x_pos += 70
        quotation_mark_count = 0
    elif char == "=":
        char_img = Image.open(f"abc/{char}.png")
        char_img = char_img.resize((char_width, char_height))   
        char_img = char_img.convert("RGBA")

        back_im.paste(char_img, (char_x_pos, char_y_pos), char_img)
        char_x_pos += 70
    elif char == "-":
        char_img = Image.open(f"abc/{char}.png")
        char_img = char_img.resize((char_width, char_height))
        char_img = char_img.convert("RGBA")

        back_im.paste(char_img, (char_x_pos, char_y_pos), char_img)
        char_x_pos += 70
    elif char == ";":
        char_img = Image.open(f"abc/{char}.png")
        char_img = char_img.resize((char_width,char_height))   
        char_img = char_img.convert("RGBA")

        back_im.paste(char_img, (char_x_pos, char_y_pos), char_img)
        char_x_pos += 70
    elif char == "!":
        char_img = Image.open(f"abc/{char}.png")
        char_img = char_img.resize((char_width,char_height))   
        char_img = char_img.convert("RGBA")

        back_im.paste(char_img, (char_x_pos, char_y_pos), char_img)
        char_x_pos += 70
    elif char == "%":
        char_img = Image.open(f"abc/{char}.png")
        char_img = char_img.resize((char_width,char_height))   
        char_img = char_img.convert("RGBA")

        back_im.paste(char_img, (char_x_pos, char_y_pos), char_img)
        char_x_pos += 70
    elif char == "+":
        char_img = Image.open(f"abc/{char}.png")
        char_img = char_img.resize((char_width,char_height))   
        char_img = char_img.convert("RGBA")

        back_im.paste(char_img, (char_x_pos, char_y_pos), char_img)
        char_x_pos += 70


def check_line_length(line):
    #### Function to check if line is longer than 50 chars, if true creating a new line that writing the continue of the previous one ####
    content_start_index = 0 # this int is used to show when the content that in the " " are start

    if len(line) > 50 and "C.WL" in line or "Console.WriteLine" in line:
        content_start_index = line.index('("')
        return content_start_index
    return False

def text_to_img(file):
    global char_x_pos, char_y_pos, quotation_mark_count, files_count, back_im

    f = open(file, "r")
    for line in f.readlines():
        line_check = check_line_length(line)
        if char_y_pos + 100 > 2480:
            back_im.save(f'handwrite_{files_count}.png', quality=95)
            files_count += 1
            back_im = img.copy()
            char_y_pos = 0
            char_x_pos = 0


        for char in line:
            if char == " ":
                char_x_pos += 100

            if line_check != False and char_x_pos + 70 > 3508:
                char_y_pos += 100
                char_x_pos = line_check * 70 + 100

            if char != "\n":
                if char.isupper():
                    char_img = Image.open(f"abc/{char}_.png")
                    char_img = char_img.resize((char_width,char_height))
                    char_img = char_img.convert("RGBA")

                    back_im.paste(char_img, (char_x_pos, char_y_pos-10), char_img)
                    char_x_pos += 70
                elif char.islower(): 
                    char_img = Image.open(f"abc/{char}.png")
                    char_img = char_img.resize((char_width,char_height))
                    char_img = char_img.convert("RGBA")

                    back_im.paste(char_img, (char_x_pos, char_y_pos), char_img)
                    char_x_pos += 70
                elif char.isnumeric():
                    char_img = Image.open(f"abc/{char}.png")
                    char_img = char_img.resize((char_width,char_height))
                    char_img = char_img.convert("RGBA")

                    back_im.paste(char_img, (char_x_pos, char_y_pos), char_img)
                    char_x_pos += 70

                else:
                    check_special_char(char)

        char_y_pos += 100
        char_x_pos =0

    back_im.save(f'handwrite_{files_count}.png', quality=95)





if __name__ == "__main__":
    file_name = "data.txt" #input("enter file name (example.txt): ")
    remove_spaces(file_name)
    computer_science_convert(file_name)
    text_to_img(file_name)

