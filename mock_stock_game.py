import random
import time
import math

# 주식이 올랐다!
def stock_up(chs_):
    global increase

    if chs_ <= 20000: 
        increase = random.randrange(1000, 5000)
    elif chs_ <=100000:
        increase = random.randrange(5000, 20000)
    chs_ += increase
    up_value = increase

    return chs_, up_value

# 주식이 떨어졌다!
def stock_down(chs_):
    global decrease

    if chs_ <= 20000:
        decrease = random.randrange(1000, 3000)
    elif chs_ <=100000:
        decrease = random.randrange(10000, 20000)
    chs_ -= decrease
    down_value = decrease
    if chs_ <= 0:
        chs_ = 1

    return chs_, down_value

# 주식 변화율 설정
def stock_variance():
    global stock_1
    global stock_2
    global stock_3
    global stock_1_up
    global stock_2_up
    global stock_3_up
    global stock_1_down
    global stock_2_down
    global stock_3_down
    
    up = 0
    down = 0

# chs = choice_stock
    chs_N = random.randrange(1,4)
    if chs_N == 1:
        chs = stock_1
        if True == random.choice([True, False]):
            chs, up = stock_up(chs)
        else:
            chs, down = stock_down(chs)
        stock_1 = chs
        stock_1_up += up
        stock_1_down += down

    elif chs_N ==2:
        chs = stock_2
        if True == random.choice([True, False]):
            chs, up = stock_up(chs)
        else:
            chs, down = stock_down(chs)
        stock_2 = chs
        stock_2_up += up
        stock_2_down += down

    elif chs_N ==3:
        chs = stock_3
        if True == random.choice([True, False]):
            chs, up = stock_up(chs)
        else:
            chs, down = stock_down(chs)
        stock_3 = chs
        stock_3_up += up
        stock_3_down += down


# 주식 계속 변동 시키기!
def stock_play():
    global stock_1_up
    global stock_2_up
    global stock_3_up
    global stock_1_down
    global stock_2_down
    global stock_3_down
    global stock_1_up_
    global stock_2_up_
    global stock_3_up_
    global stock_1_down_
    global stock_2_down_
    global stock_3_down_

    for i in range(1,6):
        stock_variance()

    stock_1_up_ = stock_1_up
    stock_2_up_ = stock_2_up
    stock_3_up_ = stock_3_up
    stock_1_down_ = stock_1_down
    stock_2_down_ = stock_2_down
    stock_3_down_ = stock_3_down


    # 주식 증, 감 초기화
    stock_1_up = 0
    stock_2_up = 0
    stock_3_up = 0
    stock_1_down = 0
    stock_2_down = 0
    stock_3_down = 0

def xp_give_buy(transaction_num, stock_price):
    if stock_price <= 5000:
        xp_num = int(transaction_num*int((stock_price)/1000)/(transaction_num/3))
        return xp_num
    elif stock_price <= 20000:
        xp_num = int(transaction_num*int((stock_price)/1000))
        return xp_num
    else:
        xp_num = int(transaction_num*int((stock_price)/1000)*2)
        return xp_num

def xp_give_sell(transaction_num, stock_price):
    if stock_price <= 5000:
        xp_num = int(transaction_num*int((stock_price)/1000)*2)
        return xp_num
    elif stock_price <= 20000:
        xp_num = int(transaction_num*int((stock_price)/1000))
        return xp_num
    else:
        xp_num = int(transaction_num*int((stock_price)/1000)/(transaction_num/3))
        return xp_num

def level_up(old_level):
    global level
    global xp
    need_xp = 0

    if level <= 16:
        while xp >= need_xp:
            need_xp = int(level**2 + 6*level)
            if xp >= need_xp:
                xp += -need_xp
                level += 1
    elif level <= 31:
        while xp >= need_xp:
            need_xp = int(2.5*(level**2) - 40.5*level + 360)
            if xp >= need_xp:
                xp += -need_xp
                level += 1
    else:
        while xp >= need_xp:
            need_xp = int(4.5*(level**2) - 162.5*level + 2220)
            if xp >= need_xp:
                xp += -need_xp
                level += 1
    if level > old_level:
        print('''
-------------------
축하합니다! {} lv이 되었습니다.
-------------------
                '''.format(level))

#초기 설정 시작
commhelp = '''
-----도움말-----
!도움말 : 게임에 필요한 도움말을 보여줍니다.
!게임 정보 : 게임에 대한 정보를 보여줍니다.
!게임 설명 : 게임을 할 때 필요한 설명을 보여줍니다.
!게임 시작 : 게임을 시작합니다.
----------------
'''
info = '''
-----게임 정보-----
모의로 만들어진 주식 3개를 사고 팔며
돈을 버는 모의주식 게임입니다.
---------------
'''
gameinfo = '''
-----게임 설명-----
게임에 입장하면 기초 자금 10만원을 받을 수 있습니다.
10만원을 가지고 주식에 투자를 하여 돈을 불리는 게임입니다.

xp : 주식을 거래하면서 xp를 모을 수 있습니다.
level : 일정 조건 만큼 xp를 모으면 레벨업합니다.
주식 수수료 : 수수료는 판매 할 때만 붙으며 20%입니다.
-----------------
'''
play_message = '''
-------------------
게임이 곧 시작됩니다.
-------------------
'''
play = False
#초기 설정 끝

print('''
<모의 주식 게임>

모의 주식에 투자하여 수익을 내는 가상 게임입니다.
'!도움말'을 입력하여 게임이용에 관한 도움말을 볼 수 있습니다.

Made by busi
문의 및 버그제보 : https://litt.ly/busi
''')

while True:
    command = str(input())
    if command == '!도움말':
        print(commhelp)
    elif command == '!게임 정보':
        print(info)
    elif command == '!게임 설명':
        print(gameinfo)
    elif command == '!게임 시작':
        print(play_message)
        play =True
    else:
        print('''
------------------------
유효하지 않은 명령어입니다.
------------------------
        ''')

    if play == True:
        stock_1 = 10000
        stock_2 = 10000
        stock_3 = 10000
        stock_1_up = 0
        stock_2_up = 0
        stock_3_up = 0
        stock_1_down = 0
        stock_2_down = 0
        stock_3_down = 0
        stock_1_own = 0
        stock_2_own = 0
        stock_3_own = 0
        start = 100

        level = 1
        xp = 0
        xp_g = 0
        money = 100000
        print('기초 자금 10만원이 지급 되었습니다.')
        user_name = str(input('당신의 닉네임을 입력해주세요! : '))
        print()
        print(f"반갑습니다! {user_name}님!")
        print()
        print("'!명령어'를 입력하여 게임 중 사용 할 수있는 명령어를 볼 수 있습니다.")
        print()
        print('---------------------------------')
        stock_play()

        command_info = '''
-----명령어 목록-----
!명령어 : 명령어 목록을 보여줍니다.
!내정보 : 나의 대한 정보를 보여줍니다.
!주식 명령어 : 주식에 관련한 명령어를 보여줍니다.
!??? : 업데이트 예정입니다.
-----------------
        '''
        stock_command_info = '''
-----명령어 목록-----
이 명령어는 !주식 뒤에 수식되는 명령어들 입니다.
명령어 : 주식 관련 명령어를 보여줍니다.
목록 : 주식 목록을 보여줍니다.
보유 : 보유하고 있는 주식을 보여줍니다.
갱신 : 주식 가격을 갱신합니다.
구매 : 주식을 구매합니다.
- 풀매수 : 주식을 살 수 있을 만큼 구매합니다.
판매 : 주식을 판매합니다. (수수료 20%)
- 풀매도 : 주식을 팔 수 있을 만큼 구매합니다.
-----------------
        '''
        while True:
            level_up(level)

            command = str(input())
            if command == '!내정보':
                print('''
------------------------
닉네임 : {}
레벨 : {} lv
xp : {:,} xp
지갑 : {:,}원 보유중
------------------------
                '''.format(user_name , level, xp, money))
            elif command == '!명령어':
                print(command_info)
            elif command.startswith('!주식') == True:
                command = command.split(' ')
                if command[0] == '!주식':
                    if len(command) == 1:
                        print('''
------------------------
추가 명령어를 입력해 주세요.
------------------------
            ''')
                    elif command[1] == '목록':
                        print('''
-----주식 목록-----
까까오의 주식 가격 : {:,}원    ㅣ {:,}↑ {:,}↓ {:,}원
삼선전자의 주식 가격 : {:,}원  ㅣ {:,}↑ {:,}↓ {:,}원
데슬라의 주식 가격 : {:,}원    ㅣ {:,}↑ {:,}↓ {:,}원
---------------
    '''.format(stock_1, stock_1_up_, stock_1_down_, stock_1_up_ - stock_1_down_,\
            stock_2, stock_2_up_, stock_2_down_, stock_2_up_ - stock_2_down_,\
                stock_3, stock_3_up_, stock_3_down_, stock_3_up_ - stock_3_down_))
                    elif command[1] == '명령어':
                        print(stock_command_info)
                    elif command[1] == '갱신':
                        if int(time.time() - start) >= 0:
                            stock_play()
                            print('''
------------------------
주식이 갱신 되었습니다.
------------------------
                ''')
                            start = int(time.time())
                        else:
                            print(f'''
------------------------
다음 주식 갱신 까지 {60-int(time.time() - start)}초 남았습니다.
------------------------
                ''')
                    elif command[1] == '보유':
                        print('''
-----보유하고 있는 주식-----
까까오 : {:,}주 / 총 {:,}원
삼선전자 : {:,}주 / 총 {:,}원
데슬라 : {:,}주 / 총 {:,}원
------------------------
                        '''.format(stock_1_own, stock_1*stock_1_own,\
                                stock_2_own, stock_2*stock_2_own,\
                                    stock_3_own, stock_3*stock_3_own))
                    elif command[1] == '구매':
                        purchase_stock = input('구매할 주식 : ')
                        if purchase_stock == '까까오':
                            if stock_1<1000:
                                print('''
------------------------
1,000원 미만의 주식은 구매할 수 없습니다.
------------------------
                        ''')
                            else:
                                try:
                                    purchase_num = str(input('구매할 수량 : '))
                                    if purchase_num != '풀매수':
                                        if stock_1*int(purchase_num) <= money:
                                            purchase_num = int(purchase_num)
                                            xp_g = xp_give_buy(purchase_num, stock_1)
                                            xp += xp_g
                                            print('''
------------------------
까까오 {:,}주를 {:,}원에 구매하셨습니다.
{:,} xp를 획득하셨습니다.
------------------------
                        '''.format(purchase_num, stock_1*purchase_num, xp_g))
                                            stock_1_own += purchase_num
                                            money += -stock_1*purchase_num
                                        else:
                                            print('''
------------------------
돈이 {:,}원 부족합니다.
------------------------
                        '''.format(stock_1*purchase_num-money))
                                    else:
                                            all_purchase_num = math.floor(money/stock_1)
                                            xp_g = xp_give_buy(all_purchase_num, stock_1)
                                            xp += xp_g
                                            print('''
------------------------
까까오 {:,}주를 {:,}원에 풀매수 하셨습니다.
{:,} xp를 획득하셨습니다.
------------------------
                        '''.format(all_purchase_num, stock_1*all_purchase_num, xp_g))
                                            stock_1_own += all_purchase_num
                                            money += -(all_purchase_num * stock_1)
                                except:
                                    print('''
------------------------
잘못된 값입니다.
------------------------    
                        ''')

                        elif purchase_stock == '삼선전자':
                            if stock_2<1000:
                                print('''
------------------------
1,000원 미만의 주식은 구매할 수 없습니다.
------------------------    
                        ''')
                            else:
                                try:
                                    purchase_num = str(input('구매할 수량 : '))
                                    if purchase_num != '풀매수':
                                        if stock_2*int(purchase_num) <= money:
                                            purchase_num = int(purchase_num)
                                            xp_g = xp_give_buy(purchase_num, stock_2)
                                            xp += xp_g
                                            print('''
------------------------
삼선전자 {:,}주를 {:,}원에 구매하셨습니다.
{:,} xp를 획득하셨습니다.
------------------------
                        '''.format(purchase_num, stock_2*purchase_num, xp_g))
                                            stock_2_own += purchase_num
                                            money += -stock_2*purchase_num
                                        else:
                                            print('''
------------------------
돈이 {:,}원 부족합니다.
------------------------
                        '''.format(stock_2*purchase_num-money))
                                    else:
                                            all_purchase_num = math.floor(money/stock_2)
                                            xp_g = xp_give_buy(all_purchase_num, stock_2)
                                            xp += xp_g
                                            print('''
------------------------
삼선전자 {:,}주를 {:,}원에 풀매수 하셨습니다.
{:,} xp를 획득하셨습니다.
------------------------
                        '''.format(all_purchase_num, stock_2*all_purchase_num, xp_g))
                                            stock_2_own += all_purchase_num
                                            money += -(all_purchase_num * stock_2)
                                            xp += xp_give_buy(all_purchase_num, stock_1)
                                except:
                                    print('''
------------------------
잘못된 값입니다.
------------------------    
                        ''')

                        elif purchase_stock == '데슬라':
                            if stock_3<1000:
                                print('''
------------------------
1,000원 미만의 주식은 구매할 수 없습니다.
------------------------    
                        ''')
                            else:
                                try:
                                    purchase_num = str(input('구매할 수량 : '))
                                    if purchase_num != '풀매수':
                                        if stock_3*int(purchase_num) <= money:
                                            purchase_num = int(purchase_num)
                                            xp_g = xp_give_buy(purchase_num, stock_3)
                                            xp += xp_g
                                            print('''
------------------------
데슬라 {:,}주를 {:,}원에 구매하셨습니다.
{:,} xp를 획득하셨습니다.
------------------------ 
                        '''.format(purchase_num, stock_3*purchase_num, xp_g))
                                            stock_3_own += purchase_num
                                            money += -stock_3*purchase_num
                                        else:
                                            print('''
------------------------
돈이 {:,}원 부족합니다.
------------------------
                        '''.format(stock_3*purchase_num-money))
                                    else:
                                            all_purchase_num = math.floor(money/stock_3)
                                            xp_g = xp_give_buy(all_purchase_num, stock_3)
                                            xp += xp_g
                                            print('''
------------------------
데슬라 {:,}주를 {:,}원에 풀매수 하셨습니다.
{:,} xp를 획득하셨습니다.
------------------------
                        '''.format(all_purchase_num, stock_3*all_purchase_num, xp_g))
                                            stock_3_own += all_purchase_num
                                            money += -(all_purchase_num * stock_3)
                                except:
                                    print('''
------------------------
잘못된 값입니다.
------------------------    
                        ''')
                                    
                        else:
                            print('''
------------------------
존재하지 않는 주식입니다.
------------------------
            ''')
                    elif command[1] == '판매':
                        sell_stock = input('판매할 주식 : ')
                        if sell_stock == '까까오':
                            try:
                                if stock_1_own >= 1:
                                    sell_num = str(input('판매할 수량 : '))
                                    if sell_num != '풀매도':
                                        if stock_1_own >= int(sell_num):
                                            sell_num = int(sell_num)
                                            xp_g = xp_give_sell(sell_num, stock_1)
                                            xp += xp_g
                                            print('''
------------------------
까까오 {:,}주를 {:,}원에 판매하셨습니다.
{:,} xp를 획득하셨습니다.
------------------------
                                            '''.format(sell_num, int((stock_1*sell_num)*0.8), xp_g))
                                            stock_1_own += -sell_num
                                            money += int((stock_1*sell_num)*0.8)
                                        else:
                                            print('''
------------------------
보유한 주식보다 많이 판매할 수는 없습니다.
------------------------                                
                                            ''')
                                    else:
                                        all_sell_num = stock_1_own
                                        xp_g = xp_give_sell(all_sell_num, stock_1)
                                        xp += xp_g
                                        print('''
------------------------
까까오 {:,}주를 {:,}원에 풀매도 하셨습니다.
{:,} xp를 획득하셨습니다.
------------------------
                        '''.format(all_sell_num, int((stock_1*all_sell_num)*0.8), xp_g))
                                        stock_1_own = 0
                                        money += int((stock_1*all_sell_num)*0.8)
                                else:
                                    print(f'''
------------------------
까까오를 보유하고 있지 않습니다.
------------------------
                                    ''')
                            except:
                                    print('''
------------------------
잘못된 값입니다.
------------------------    
                        ''')
                        elif sell_stock == '삼선전자':
                            try:
                                if stock_2_own >= 1:
                                    sell_num = str(input('판매할 수량 : '))
                                    if sell_num != '풀매도':
                                        if stock_2_own >= int(sell_num):
                                            sell_num = int(sell_num)
                                            xp_g = xp_give_sell(sell_num, stock_2)
                                            xp += xp_g
                                            print('''
------------------------
삼선전자 {:,}주를 {:,}원에 판매하셨습니다.
{:,} xp를 획득하셨습니다.
------------------------
                                            '''.format(sell_num, int((stock_2*sell_num)*0.8), xp_g))
                                            stock_2_own += -sell_num
                                            money += int((stock_2*sell_num)*0.8)
                                        else:
                                            print('''
------------------------
보유한 주식보다 많이 판매할 수는 없습니다.
------------------------                                
                                            ''')
                                    else:
                                        all_sell_num = stock_2_own
                                        xp_g = xp_give_sell(all_sell_num, stock_2)
                                        xp += xp_g
                                        print('''
------------------------
삼선전자 {:,}주를 {:,}원에 풀매도 하셨습니다.
{:,} xp를 획득하셨습니다.
------------------------
                        '''.format(all_sell_num, int((stock_2*all_sell_num)*0.8), xp_g))
                                        stock_2_own = 0
                                        money += int((stock_2*all_sell_num)*0.8)
                                else:
                                    print(f'''
------------------------
삼선전자를 보유하고 있지 않습니다.
------------------------
                                    ''')
                            except:
                                    print('''
------------------------
잘못된 값입니다.
------------------------    
                        ''')
                        elif sell_stock == '데슬라':
                            try:
                                if stock_3_own >= 1:
                                    sell_num = str(input('판매할 수량 : '))
                                    if sell_num != '풀매도':
                                        if stock_3_own >= int(sell_num):
                                            sell_num = int(sell_num)
                                            xp_g = xp_give_sell(sell_num, stock_3)
                                            xp += xp_g
                                            print('''
------------------------
데슬라 {:,}주를 {:,}원에 판매하셨습니다.
{:,} xp를 획득하셨습니다.
------------------------
                                            '''.format(sell_num, int((stock_3*sell_num)*0.8), xp_g))
                                            stock_3_own += -sell_num
                                            money += int((stock_3*sell_num)*0.8)
                                        else:
                                            print('''
------------------------
보유한 주식보다 많이 판매할 수는 없습니다.
------------------------                                
                                            ''')
                                    else:
                                        all_sell_num = stock_3_own
                                        xp_g = xp_give_sell(all_sell_num, stock_3)
                                        xp += xp_g
                                        print('''
------------------------
데슬라 {:,}주를 {:,}원에 풀매도 하셨습니다.
{:,} xp를 획득하셨습니다.
------------------------
                        '''.format(all_sell_num, int((stock_3*all_sell_num)*0.8), xp_g))
                                        stock_3_own = 0
                                        money += int((stock_3*all_sell_num)*0.8)
                                else:
                                    print(f'''
------------------------
데슬라를 보유하고 있지 않습니다.
------------------------
                                    ''')
                            except:
                                    print('''
------------------------
잘못된 값입니다.
------------------------    
                        ''')

                        else:
                            print('''
------------------------
존재하지 않는 주식입니다.
------------------------
                                ''')
                    else:
                        print('''
------------------------
유효하지 않은 명령어입니다.
------------------------
                            ''')
            elif command.startswith('!???') == True:
                print('''
------------------------
구현 중 입니다.
------------------------
        ''')
            else:
                print('''
------------------------
유효하지 않은 명령어입니다.
------------------------
        ''')
