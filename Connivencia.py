follower_discount = 10
discount_500 = 100
discount_300 = 50
discount_100 = 20
shipment_cost = 10
orders = [(280,True), (120,True), (634,False), (385,True), (490,False)]
#创建空列表
final_payment_list = []


#循环
for i in range(0,5):

    #判断是否关注
    if orders[i][1] == False:
        follower_discount = 0
    else:
        follower_discount = 10

    #判断哪种优惠
    if orders[i][0] >= 500:
        shipment_cost = 0
        #应付款=订单+邮费-关注优惠-满减优惠
        payment = orders[i][0] + shipment_cost - follower_discount - discount_500
        #加入到输出列表
        final_payment_list.append(payment)

    elif orders[i][0] >= 300:
        shipment_cost = 0
        payment = orders[i][0] + shipment_cost - follower_discount - discount_300
        final_payment_list.append(payment)

    elif orders[i][0] >= 100:
        shipment_cost = 0
        payment = orders[i][0] + shipment_cost - follower_discount - discount_100
        final_payment_list.append(payment)  
          
    else:
        shipment_cost += 10
        payment = orders[i][0] + shipment_cost - follower_discount
        final_payment_list.append(payment)

print(final_payment_list)