import sys
sys.stdin = open('input.txt', 'r')

# t = int(input())
# for tc in range(1, t+1):
#     bnum = list(input())
#     tnum = list(input())
#
#     blist = []
#     tlist = []
#     b = []
#     t = []
#     for i in range(len(bnum)):
#
#         if bnum[i] == '1':
#            new = bnum[:]
#            new[i] = '0'
#            blist.append(new)
#         else:
#             new = bnum[:]
#             new[i] = '1'
#             blist.append(new)
#     for j in range(len(tnum)):
#         if tnum[j] == '0':
#             new = tnum[:]
#             new[j] = '1'
#             tlist.append(new)
#             new = tnum[:]
#             new[j] = '2'
#             tlist.append(new)
#         elif tnum[j] == '1':
#             new = tnum[:]
#             new[j] = '0'
#             tlist.append(new)
#             new = tnum[:]
#             new[j] = '2'
#             tlist.append(new)
#         else:
#             new = tnum[:]
#             new[j] = '0'
#             tlist.append(new)
#             new = tnum[:]
#             new[j] = '1'
#             tlist.append(new)
#
#     for i in blist:
#         b.append(int(''.join(i), 2))
#     for i in tlist:
#         t.append(int(''.join(i), 3))
#
#     for i in b:
#         for j in t:
#             if i==j:
#                 print('#{} {}'.format(tc, i))
#                 break
for t in range(int(input())):
    b=[*input()];d=[*input()];c=0
    for i in range(2*len(b)):
        p=b[:];p[i//2]=str(i%2);a=''.join(p)
        for j in range(3*len(d)):
            e=d[:];e[j//3]=str(j%3);f=''.join(e)
            if int(a,2)==int(f,3):print(f'#{t+1}',int(a,2));c=1;break
        if c:break