from calculator import Calculator, MoreCalculator
import game
from Bird import *

if __name__ == '__main__':
    '''
    05-1 클래스, 05-2 모듈
    
    a1 = Calculator(4, 0)
    b1 = MoreCalculator(4, 0)
    # c.setdata(4, 2)
    print(a1.add())
    print(a1.mul())
    print(a1.sub())
    print(a1.c)
    a1.c = 33
    print(a1.c)
    # print(a1.div())
    print(a1.a)
    print(b1.pow())
    print(b1.div())
    '''

    '''
    05-3 패키지
    
    game.sound.echo.echo_test()
    print(game.VERSION)
    game.print_version()
    game.render_test()
    game.echo.echo_test()
    '''

    '''
    05-4 예외처리
    
    # 1
    try:
        a = [1, 2]
        print(a[3])
        4 / 0
    except (ZeroDivisionError, IndexError) as e:
        print(f'zero err. {e}')
    except IndexError as e:
        print(f'index err. {e}')

    # 2
    try:
        f = open('test.txt', 'w')
    finally:
        f.close()

    # 3
    try:
        # age = int(input('나이를 입력하세요: '))
        age = 20
    except:
        print('입력이 정확하지 않습니다.')
    else:
        if age <= 18:
            print('미성년자는 출입금지입니다.')
        else:
            print('환영합니다.')

    # 4
    try:
        eagle = Eagle()
        eagle.fly()
        eagle.say_name('참새')
        eagle.say_name('독수리')
    except ErrorException as e:
        print(e)
    '''
