import time
import pygame
import os

pygame.init()
base_dir_1 = './sounds/vie/north/'
# duong dan tieng bac
base_dir_2 = './sounds/vie2/south/'
# duong dan tieng nam

my_dict = {'0': 'không', '1': 'một', '2': 'hai', '3': 'ba', '4': 'bốn', '5': 'năm', '6': 'sáu', '7': 'bảy', '8': 'tám',
           '9': 'chín', '10': 'mười'}
# my_dict la dictionary doc cac so tu 1 den 10

# dict_to_read la dictionary dung de chuyen cac chu co dau thanh cac chu khong dau giong voi ten file doc tu thu muc tieng noi
dict_to_read = {'lăm': 'lam', 'không': 'khong', 'một': 'mot1', 'hai': 'hai', 'ba': 'ba', 'bốn': 'bon', 'năm': 'nam',
                'sáu': 'sau',
                'bảy': 'bay', 'tám': 'tam', 'triệu': 'trieu', 'tỷ': 'ty', 'mốt': 'mot2',
                'chín': 'chin', 'mười': 'muoi1', 'mươi': 'muoi2', 'linh': 'linh', 'nghìn': 'nghin', 'trăm': 'tram',
                'lẻ': 'le', 'ngàn': 'ngan'}

number1 = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
           9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
           16: 'sixteen', 17: 'seventeen',18: 'eighteen', 19: 'nineteen', 20: 'twenty'}
number2 = {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}


def read_a_part(s):
    # ham dung de doc 3 so 1 lan
    s = str(s)
    # ep chuoi de lay tung so trong chuoi

    if len(s) == 3:
        # truong hop so la so 3 chu so
        if s[2] == '0' and s[1] == '0':  # neu vi tri hang chuc va hang don vi la so khong thi doc so dau + tram
            return my_dict[s[0]] + ' trăm '

        elif s[1] == '1':  # neu vi tri hang chuc la 1 doc so dau + tram + muoi + doc so sau
            return my_dict[s[0]] + ' trăm ' ' mười ' + my_dict[s[2]]

        elif s[2] == '0':  # neu vi tri hang don vi la 0 thi doc so dau + tram + so hang chuc + muoi
            return my_dict[s[0]] + ' trăm ' + my_dict[s[1]] + ' mươi '

        elif s[1] == '0':  # neu vi tri hang chuc la 0 doc vij tri hang chuc la linh
            return my_dict[s[0]] + ' trăm ' + 'linh ' + my_dict[s[2]]

        elif s[2] == '5':  # neu vi tri hang tram vi tri hang chuc la cac so khac 0 hang don vi la 5 doc la lam
            return my_dict[s[0]] + ' trăm ' + my_dict[s[1]] + ' mươi lăm'

        elif s[2] == 1:  # neu vi tri hang don vi bang 1 doc la muoi mot
            return my_dict[s[0]] + ' trăm ' + my_dict[s[1]] + ' mươi mốt'

        else:  # truong hop con lai doc day du
            return my_dict[s[0]] + ' trăm ' + my_dict[s[1]] + ' mươi ' + my_dict[s[2]]

    if len(s) == 2:  # truong hop neu la so co hai chu so

        if s[0] == '1' and s[1] == '0':  # neu vi tri hang chuc va don vi la 0 doc la 10
            return '  mười  '

        elif s[1] == '0':  # neu vi tri hang don vi la 0 doc so dau + muoi
            return my_dict[s[0]] + ' mươi '

        elif s[0] == '1':  # neu vi tri hang chuc la 1 doc hang chuc la 10 + so sau
            return ' mười ' + my_dict[s[1]]

        elif s[1] == '1':  # neu vi tri don vi la 1 doc mốt
            return my_dict[s[0]] + ' mốt '

        elif s[1] == '5':  # neu hang don vi la 5 doc la lam
            return my_dict[s[0]] + ' mươi lăm '

        elif s[0] == '1' and s[1] == '5':  # neu hang chuc la 1 hang don vi la 5 doc la muoi lam
            return ' mười ' + ' lăm '

        else:  # truong hop binh thuong
            return my_dict[s[0]] + ' mươi ' + my_dict[s[1]]

    if len(s) == 1:  # truong hop so la 1 chu so doc chinh no
        return my_dict[s[0]]


def integer_to_vietnamese_numeral(n, region='north',
                                  activate_tts=False):  # ham chinh dung de doc so tu nhien dung lai ham read_a_part
    result = ''

    if n < 0:  # neu n nho hon khong chuong trinnh se bao loi
        raise ValueError('Not a positive integer')

    elif not isinstance(n, int):  # neu n khong phai la int chuong trinh se bao loi
        raise TypeError('Not an integer')

    elif n > 999999999999:  # neu n lon hon 999999999999 thi chuong trinh se bao loi
        raise ('Integer greater than 999999999999')

    else:  # neu cac so nahp vao khong bi bao loi thi chuong trinh chay
        n = str(n)  # ep chuoi n de lay cac phan tong so do

        if len(n) <= 3:  # neu so be hon hoac bang 3 chu so doc ham tren
            result = read_a_part(n)

        elif 6 >= len(n) > 3:  # neu so la so thuoc hang nghin

            if int(n[-3:]) == 0:  # neu so cuoi bang 0 doc 3 so dau + nghin
                result = read_a_part(n[:-3]) + ' nghìn '

            elif not int(n[-3:]) == 0:  # neu 3 so cuoi khac 0 thi
                result = read_a_part(n[:-3]) + ' nghìn ' + read_a_part(n[-3:])

        elif 9 >= len(n) > 6:  # neu so thuoc hang trieu

            if int(n[-6:]) == 0:  # neu 6 so cuoi la 0 doc la nghin
                result = read_a_part(n[:-6]) + ' triệu '

            elif int(n[-3:]) == 0:  # neu 3 so sau bang 0 thi khong doc 3 so do
                result = read_a_part(n[:-6]) + ' triệu ' + read_a_part(n[-6:-3]) + ' nghìn '

            else:  # truong hop cac so khong thuoc truong hop dac biet
                result = read_a_part(n[:-6]) + ' triệu ' + read_a_part(n[-6:-3]) + ' nghìn ' + read_a_part(n[-3:])

        elif len(n) > 9 and len(n) <= 12:  # truong hop so thuoc hang ty

            if int(n[-9:]) == 0:  # truong hop cac so tu hang trieu la 0 thi
                result = read_a_part(n[:-9]) + ' tỷ '

            elif int(n[-6:]) == 0:  # 6 so cuoi la 0 thi k doc 6 so do
                result = read_a_part(n[:-9]) + ' tỷ ' + read_a_part(n[-9:-6]) + ' triệu '

            elif int(n[-9:-3]) == 0:  # neu 6 so o giua la 0 thi khong doc
                result = read_a_part(n[:-9]) + ' tỷ ' + read_a_part(n[-3:])

                if int(n[-9:-6]) == 0 and not int(n[
                                                  -6:-3]) == 0:  # neu 3 so hang trieu la 0 va ca so hang nghin khac 0 thif k doc so o hang trieu
                    result = read_a_part(n[:-9]) + ' tỷ ' + read_a_part(n[-6:-3]) + ' nghìn ' + read_a_part(n[-3:])

            elif int(n[-3:]) == 0:  # neu 3 so sau =0 thi khong doc 3 so do
                result = read_a_part(n[:-9]) + ' tỷ ' + read_a_part(n[-9:-6]) + ' triệu ' + read_a_part(
                    n[-6:-3]) + ' nghìn '

            else:  # truong hop con lai
                result = read_a_part(n[:-9]) + ' tỷ ' + read_a_part(n[-9:-6]) + ' triệu ' + read_a_part(
                    n[-6:-3]) + ' nghìn ' + read_a_part(n[-3:])

        my_string = result.split()  # bien ket qua o phan tren thanh list de chay vong lap
        this_result = []
        if region == "south":  # neu argument region la south thi chay vong lap i trong list my_string
            #
            for i in range(len(my_string)):
                if my_string[i] == "nghìn":  # trong my-string neu phan tu i nao ten nghin doi thanh ngan
                    my_string[i] = "ngàn"

                elif my_string[i] == 'linh':  # trong i phan tu nao la linh doi thanh le
                    my_string[i] = 'lẻ'

            this_result = " ".join(my_string)  # chuyen ket qua tu dang list ve dang chuoi

        elif region == "north":  # neu argument region la north thi ket qua la giu nguyen
            this_result = ' '.join(my_string)

        elif region == None:  # nhu tren
            this_result = ' '.join(my_string)

        elif not region == 'south' or not region == 'north':  # neu region khong phai la south hay north thi bao loi
            raise ValueError('Argument "region" has not a correct value')

        elif not isinstance(region, str):  # neu region k phai dang chuoi khi nhap vao thi bao loi
            raise TypeError('Argument "region" is not a string')

        the_list = this_result.split(' ')  # tach chuoi thanh list

        if not isinstance(activate_tts, bool):  # neu argument activate khong thuoc dang bool thi bao loi
            raise TypeError('Argument "activate_tts" is not a boolean')

        if activate_tts == True:  # neu argument ac - tts la True chay chuong trinh va in chu neu khong thi chi chay va in ra chu nhung k doc

            for word in the_list:  # neu la true chay word trong the-list
                if region == 'north':  # neu la bac thi bien cac chu co dau thanh chu k dau nho dict o dau chuong trinh
                    lst = base_dir_1 + dict_to_read[word] + '.ogg'  # roi cong them duong dan va duoi .ogg
                    speak_1 = pygame.mixer.Sound(lst)
                    speak_1.play()  # doc no
                    pygame.time.delay(700)

                elif region == 'south':  # tuong tu voi giong nam
                    lst = base_dir_2 + dict_to_read[word] + '.ogg'
                    speak_2 = pygame.mixer.Sound(lst)
                    speak_2.play()
                    pygame.time.delay(700)
    return this_result


# waypoint5 + waypoint6


# ham chinh de su dung lai
def main_function(n):
    if n <= 20:
        return number1[n]

    if 20 < n < 100:

        if n % 10 == 0:
            return number2[n // 10]

        else:
            return number2[n // 10] + "-" + number1[n % 10]


# doc so co 2 chu so
def two_digits(m):
    if m <= 20:
        return main_function(m)

    if 20 < m < 100:
        return main_function(m)


# doc so co ba chu so
def three_digits(x):
    if x < 1000:
        # truong hop neu so la 100, 200 den 900

        if x % 100 == 0:
            return str(main_function(x // 100)) + " hundred "
            # cac truong hop khac

        else:
            return str(main_function(x // 100)) + " hundred and " + str(two_digits(x % 100))


# doc so tu bon den sau chu so
def four_to_six_digits(y):
    if 1000 <= y <= 99999:
        # truong hop la 1000, 2000 den 90000

        if y % 1000 == 0:
            return str(main_function(y // 1000)) + " thousand "

        # neu y%1000 du hai chu so, tra ve ham xu ly hai chu so
        elif 0 < y % 1000 <= 99:

            return str(main_function(y // 1000)) + " thousand and " + str(two_digits(y % 1000))
        # neu y%1000 du ba chu so, tra ve ham xu ly ba chu so
        elif 100 < y % 1000 <= 999:
            return str(main_function(y // 1000)) + " thousand and " + str(three_digits(y % 1000))

    elif 100000 <= y <= 999999:
        # truong hop neu la 100000, 200000 den 900000

        if y % 100000 == 0:
            return str(three_digits(y // 1000)) + " thousand "

        elif 0 < y % 1000 <= 99:
            return str(three_digits(y // 1000)) + " thousand and " + str(two_digits(y % 1000))

        elif 100 <= y % 1000 <= 999:
            return str(three_digits(y // 1000)) + " thousand and " + str(three_digits(y % 1000))


# doc so tu bay den chin chu so
def seven_to_nine_digits(z):
    # 7 den 8 chu so
    if 1000000 <= z <= 99999999:

        # truong hop la 1000000, 2000000 den 90000000
        if z % 100000 == 0:
            return str(two_digits(z // 1000000)) + " million "

            # neu z%1000000 phan du la 3 chu so
        if 100 < z % 1000000 < 999:
            return str(main_function(z // 1000000)) + " million and " + str(three_digits(z % 1000000))

        # neu z%1000000 phan du la 2 chu so
        if 0 < z % 1000000 < 99:
            return str(main_function(z // 1000000)) + " million and " + str(two_digits(z % 1000000))

        # neu phan du tu 4 den 6 chu so
        else:
            return str(main_function(z // 1000000)) + " million and " + str(four_to_six_digits(z % 1000000))

        # 9 chu so
    elif 100000000 <= z <= 999999999:

        # neu  z= 100000000, 200000000 den 900000000
        if z % 1000000 == 0:
            return str(three_digits(z // 1000000)) + "billion"

        # z% 1000000 phan du la 3 so
        if 100 < z % 1000000 < 999:
            return str(three_digits(z // 1000000)) + " million and " + str(three_digits(z % 1000000))

        # z%1000000 phan du la 2 so
        elif 0 < z % 1000000 < 99:
            return str(three_digits(z // 1000000)) + " million and " + str(two_digits(z % 1000000))

        # z%1000000 phan du tu 4 den 6 so
        else:
            return str(three_digits(z // 1000000)) + " million and " + str(four_to_six_digits(z % 1000000))


def ten_to_twelve_digits(t):
    # 10 den 11 chu so
    if 1000000000 <= t <= 99999999999:

        # neu t = 1000000000, 2000000000 den 90000000000
        if t % 1000000000 == 0:
            return str(two_digits(t // 1000000000)) + " billion "

        # neu t%1000000000 phan du la 2 chu so
        if 0 < t % 1000000000 < 99:
            return str(main_function(t // 1000000000)) + " billion " + str(two_digits(t % 1000000000))

        # neu t%1000000000 phan du la 3 chu so
        if 100 < t % 1000000000 < 999:
            return str(main_function(t // 1000000000)) + " billion " + str(three_digits(t % 1000000000))

        # neu t%1000000000 phan du tu 4 den 8 chu so
        else:
            return str(main_function(t // 1000000000)) + " billion " + str(seven_to_nine_digits(t % 1000000000))

    # 12 so
    elif 100000000000 <= t <= 999999999999:

        # neu t la 100000000000, 200000000000 den 900000000000
        if t % 100000000000 == 0:
            return str(main_function(t // 100000000000)) + " hundred billion "

        # neu t%100000000000 phan du la 2 chu so
        if 0 < t % 100000000000 <= 99:
            return str(three_digits(t // 1000000000)) + " billion " + str(two_digits(t % 1000000000))

        # neu t%100000000000 phan du la 3 chu so
        elif 100 <= t % 1000000000 <= 999:
            return str(three_digits(t // 1000000000)) + " billion " + str(three_digits(t % 1000000000))

        # neu t%100000000000 phan du tu 4 den 6 chu so
        elif 1000 <= t % 1000000000 <= 999999:
            return str(three_digits(t // 1000000000)) + " billion " + str(four_to_six_digits(t % 1000000000))

        # neu t%1000000000 phan du tu 7 den 9 chu so
        elif 1000000 <= t % 1000000000 <= 999999999:
            return str(three_digits(t // 1000000000)) + " billion " + str(seven_to_nine_digits(t % 1000000000))


# ham de goi so
def integer_to_english_numeral(s, activate_tts=False):
    sum = ''

    if not isinstance(s, int):
        raise TypeError('Not a integer')

    if s < 0:
        raise ValueError('Not a positive integer')

    if 0 <= s <= 99:
        sum = two_digits(s)

    if 100 <= s <= 999:
        sum = three_digits(s)

    elif 1000 <= s <= 999999:
        sum = four_to_six_digits(s)

    elif 1000000 <= s <= 999999999:
        sum = seven_to_nine_digits(s)

    elif 1000000000 <= s <= 999999999999:
        sum = ten_to_twelve_digits(s)

    # doc so bang tieng anh
    if activate_tts is True:
        notes = sum.split()
        for i in range(len(notes)):
            notes1 = notes[i].split('-')
            for j in range(len(notes1)):
                pygame.init()
                sound = pygame.mixer.Sound('./sounds/eng/' + notes1[j] + '.ogg')
                channel = sound.play(0, 1000, 0)
                sound = pygame.time.delay(600)
    return sum
