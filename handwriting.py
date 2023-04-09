import random
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import config

def get_pos(i, j, bias=4):
    return 70 + random.random() * bias / 2 + 25 * j, 83 + random.random() * bias + i * 48

def draw_word(txt_path='./test.txt', ttf_path="./src/font.TTF", save_path="./result/", offset_size=4, num_cols=1, title=None):
    font = ImageFont.truetype(ttf_path, 25)
    with open(txt_path, 'r', encoding='utf-8') as f:
        string = f.read()
    length = len(string)
    
    rows = 28
    cols = (38-num_cols+1)//num_cols
    page = 1
    
    idx = 0
    while idx < length:
        with Image.open('./src/background.png') as img:
            draw = ImageDraw.Draw(img)
            if page == 1 and title is not None:
                title_len = len(title)
                start_idx = 19-title_len//2
                for j, ch in enumerate(title):
                    draw.text(get_pos(0, j+start_idx, offset_size), ch, (0,0,0), font=font)

            for num_col in range(num_cols):
                if idx >= length:
                    break
                for row in range(rows):
                    if page == 1 and row < 2 and title is not None:
                        continue
                    if idx >= length:
                        break
                    for col in range(cols):
                        if idx >= length:
                            break
                        ch = string[idx]
                        idx += 1
                        if ch == ' ' or ch==' ':
                            continue
                        if ch == '\n':
                            if row==0 and col==0 and idx < length-1:
                                idx += 1
                            else:
                                break
                        i, j = row, num_col * (cols+1) + col
                        pos = get_pos(i, j, offset_size)
                        draw.text(pos, ch, (0,0,0), font=font)
            if title is None:
                img.save(save_path + str(page)+'.png')
            else:
                img.save(save_path + title + "_" + str(page)+'.png')
        page += 1


if __name__ == "__main__":
    offset_size = config.offset_size  # 随机便宜量
    txt_path = config.text_dir + config.text_name
    ttf_path = config.ttf_path
    save_path = config.result_dir
    draw_word(txt_path, ttf_path, save_path,offset_size, num_cols=config.cols, title=config.title_name)
    print("success!")
