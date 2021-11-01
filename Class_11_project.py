def handcricket():
    print("Let's play Hand cricket .........")
    cho=input('Enter toss(odd/even): ')
    toss=int(input('Enter a number for toss: '))
    if toss>=0 and toss<=7:
        import random
        ss=random.randint(0,7)
        t_sum=toss+ss
        if t_sum%2==0:
            if cho=='even':
                print('Congrats you won the toss')
                dec=input('You want to bat or ball(bat/ball): ')
                if dec=='bat':
                    b_score=0
                    while True:
                        b=random.randint(0,7)
                        bat=int(input('Enter your score: '))
                        print('I bowled ',b)
                        if bat>=0 and bat<=7:
                            if bat!=b:
                                b_score+=bat
                            elif bat==b:
                                print('Oops, you are out')
                                break
                    print('Your batting score is ',b_score)
                    print("Now it's time to defend your score")
                    print('Now you have to defend a total of ',b_score+1)
                    bas=0
                    while True:
                        ba=random.randint(0,7)
                        ball=int(input('Put the ball from 0 to 7: '))
                        print('I scored ',ba,' runs.')
                        if ball>=0 and ball<=7:
                            if ball!=ba:
                                bas+=ba
                                if bas>b_score:
                                    break
                            elif ball==ba:
                                print('Oops,now I am out')
                                break
                    print('My batting score is',bas)
                    if bas<b_score+1:
                        print('Oh, you won the game')
                    else:
                        print('I won the game , better luck next time')
                elif dec=='ball':
                    bas=0
                    while True:
                        ba=random.randint(0,7)
                        ball=int(input('Put the ball from 0 to 7: '))
                        print('I scored ',ba,' runs.')
                        if ball>=0 and ball<=7:
                            if ball!=ba:
                                bas+=ba
                            elif ball==ba:
                                print('Oops,now I am out')
                                break
                    print('My batting score is',bas)
                    print("Now it's time to chase my score")
                    print("You have to chase a score of ", bas+1)
                    b_score=0
                    while True:
                        b=random.randint(0,7)
                        bat=int(input('Enter your score: '))
                        print('I bowled ',b)
                        if bat>=0 and bat<=7:
                            if bat!=b:
                                b_score+=bat
                                if b_score>bas:
                                    break
                            elif bat==b:
                                print('Oops, you are out')
                                break
                    print('Your batting score is ',b_score)
                    if bas+1>b_score:
                        print('I won the game , better luck next time')
                    else:
                        print('Congrats you won the game')
            elif cho=='odd':
                print('Oops, you lost the toss')
                l=('bat','ball')
                dic=random.choice(l)
                print('I choose to ',dic)
                if dic=='bat':
                    bas=0
                    while True:
                        ba=random.randint(0,7)
                        ball=int(input('Put the ball from 0 to 7: '))
                        print('I scored ',ba,' runs.')
                        if ball>=0 and ball<=7:
                            if ball!=ba:
                                bas=bas+ba
                            elif ball==ba:
                                print('Oops,now I am out')
                                break
                    print('My batting score is',bas)
                    print("Now it's time to chase my score")
                    print("You have to chase a score of ", bas+1)
                    b_score=0
                    while True:
                        b=random.randint(0,7)
                        bat=int(input('Enter your score: '))
                        print('I bowled ',b)
                        if bat>=0 and bat<=7:
                            if bat!=b:
                                b_score+=bat
                                if b_score>bas:
                                    break
                            elif bat==b:
                                print('Oops, you are out')
                                break
                    print('Your batting score is ',b_score)
                    if bas+1>b_score:
                        print('I won the game , better luck next time')
                    else:
                        print('Congrats you won the game')
                elif dic=='ball':
                        b_score=0
                        while True:
                            b=random.randint(0,7)
                            bat=int(input('Enter your score: '))
                            print('I bowled ',b)
                            if bat>=0 and bat<=7:
                                if bat!=b:
                                    b_score+=bat
                                elif bat==b:
                                    print('Oops, you are out')
                                    break
                        print('Your batting score is ',b_score)
                        print("Now it's time to defend your score")
                        print('Now you have to defend a total of ',b_score+1)
                        bas=0
                        while True:
                            ba=random.randint(0,7)
                            ball=int(input('Put the ball from 0 to 7: '))
                            print('I scored ',ba,' runs.')
                            if ball>=0 and ball<=7:
                                if ball!=ba:
                                    bas+=ba
                                    if bas>b_score:
                                        break
                                elif ball==ba:
                                    print('Oops,now I am out')
                                    break
                print('My batting score is',bas)
                if bas<b_score+1:
                    print('Oh, you won the game')
                else:
                    print('I won the game , better luck next time')
        else:
            if cho=='even':
                print('Oops, you lost the toss')
                l=('bat','ball')
                dic=random.choice(l)
                print('I choose to ',dic)
                if dic=='bat':
                    bas=0
                    while True:
                        ba=random.randint(0,7)
                        ball=int(input('Put the ball from 0 to 7: '))
                        print('I scored ',ba,' runs.')
                        if ball>=0 and ball<=7:
                            if ball!=ba:
                                bas=bas+ba
                            elif ball==ba:
                                print('Oops,now I am out')
                                break
                    print('My batting score is',bas)
                    print("Now it's time to chase my score")
                    print("You have to chase a score of ", bas+1)
                    b_score=0
                    while True:
                        b=random.randint(0,7)
                        bat=int(input('Enter your score: '))
                        print('I bowled ',b)
                        if bat>=0 and bat<=7:
                            if bat!=b:
                                b_score+=bat
                                if b_score>bas:
                                    break
                            elif bat==b:
                                print('Oops, you are out')
                                break
                    print('Your batting score is ',b_score)
                    if bas+1>b_score:
                        print('I won the game , better luck next time')
                    else:
                        print('Congrats you won the game')
                elif dic=='ball':
                        b_score=0
                        while True:
                            b=random.randint(0,7)
                            bat=int(input('Enter your score: '))
                            print('I bowled ',b)
                            if bat>=0 and bat<=7:
                                if bat!=b:
                                    b_score+=bat
                                elif b==bat:
                                    print('Oops, you are out')
                                    break
                        print('Your batting score is ',b_score)
                        print("Now it's time to defend your score")
                        print('Now you have to defend a total of ',b_score+1)
                        bas=0
                        while True:
                            ba=random.randint(0,7)
                            ball=int(input('Put the ball from 0 to 7: '))
                            if ball>=0 and ball<=7:
                                if ball!=ba:
                                    bas+=ba
                                    if bas>b_score:
                                        break
                                elif ball==ba:
                                    print('Oops,now I am out')
                                    break
                print('My batting score is',bas)
                if bas<b_score+1:
                    print('Oh, you won the game')
                else:
                    print('I won the game , better luck next time')
            elif cho=='odd':
                print('Congrats you won the toss')
                dec=input('You want to bat or ball(bat/ball): ')
                if dec=='bat':
                    b_score=0
                    while True:
                        b=random.randint(0,7)
                        bat=int(input('Enter your score: '))
                        print('I bowled ',b)
                        if bat>=0 and bat<=7:
                            if bat!=b:
                                b_score+=bat
                            elif bat==b:
                                print('Oops, you are out')
                                break
                    print('Your batting score is ',b_score)
                    print("Now it's time to defend your score")
                    print('Now you have to defend a total of ',b_score+1)
                    bas=0
                    while True:
                        ba=random.randint(0,7)
                        ball=int(input('Put the ball from 0 to 7: '))
                        print('I scored ',ba,' runs.')
                        if ball>=0 and ball<=7:
                            if ball!=ba:
                                bas+=ba
                                if bas>b_score:
                                    break
                            elif ball==ba:
                                print('Oops,now I am out')
                                break
                    print('My batting score is',bas)
                    if bas<b_score+1:
                        print('Oh, you won the game')
                    else:
                        print('I won the game , better luck next time')
                elif dec=='ball':
                    bas=0
                    while True:
                        ba=random.randint(0,7)
                        ball=int(input('Put the ball from 0 to 7: '))
                        print('I scored ',ba,' runs.')
                        if ball>=0 and ball<=7:
                            if ball!=ba:
                                bas+=ba
                            elif ball==ba:
                                print('Oops,now I am out')
                                break
                    print('My batting score is',bas)
                    print("Now it's time to chase my score")
                    print("You have to chase a score of ", bas+1)
                    b_score=0
                    while True:
                        b=random.randint(0,7)
                        bat=int(input('Enter your score: '))
                        print('I bowled ',b)
                        if bat>=0 and bat<=7:
                            if bat!=b:
                                b_score+=bat
                                if b_score>bas:
                                    break
                            elif bat==b:
                                print('Oops, you are out')
                                break
                    print('Your batting score is ',b_score)
                    if bas+1>b_score:
                        print('I won the game , better luck next time')
                    else:
                        print('Congrats you won the game')
handcricket()
while True:
    do=input('''Do you want to play again;

y or Y for yes
n or N or anything else for No

Tell your decision here: ''')
    if do=='y' or do=='Y':
        handcricket()
    else:
        print('Thankyou for playing ... See you soon')
        break
