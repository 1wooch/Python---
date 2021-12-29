import telegram
토큰='5081033456:AAFC9HDCGCdGyvKe2inpuxkHfKSV7Ab1Rww'
봇 = telegram.Bot(token=토큰)

#for i in 봇.getUpdates():
#    print(i.message)


#chat id =1054405622
#https://api.telegram.org/bot5081033456:AAFC9HDCGCdGyvKe2inpuxkHfKSV7Ab1Rww/getUpdates
# 봇.send_message("안녕")
봇.send_message(1054405622,"hi")