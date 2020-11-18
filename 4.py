PrevX,PrevY = 1,1

n=int(input('введіть номер шуканого X: '))

if n>=2:

    for i in range(2,n+1):
        CurY = PrevY + PrevX/i
        CurX = PrevX + PrevY/(i*i)
        PrevX, PrevY = CurX, CurY
        print('CurX=%-8f, CurX=%-8f' % (CurX, CurY))
    print('шукане: %-8f'% CurX)