#参加晚会
guest=['dong yan','li guang kun','kangshuo']
print('参加晚会的名单:')
print(guest[0].title())
print(guest[1].title())
print(guest[2].title())
print(guest[2].title() + '无法赴约')
guest.insert(0,'wang jun lei')
guest.insert(2,'li jia tong')
guest.append('xin ran')
print(guest[0])
print(guest[1])
print(guest[2])
print(guest[3])
print(guest[4])
print(guest[5])
print(len(guest))
print('Sorry,因为新买的餐桌无法送达，只能邀请两名嘉宾')

print(guest[5].title() + '我很抱歉，无法邀请你来参加晚餐')
guest.pop()
print(guest[4].title() + '我很抱歉，无法邀请你来参加晚餐')
guest.pop()
print(guest[3].title() + '我很抱歉，无法邀请你来参加晚餐')
guest.pop()
print(guest[2].title() + '我很抱歉，无法邀请你来参加晚餐')
guest.pop()
print(guest[0].title() + '您仍在邀请之列')
print(guest[1].title() + '您仍在邀请之列')
print(len(guest))
del guest[1]
del guest[0]
print(guest)
