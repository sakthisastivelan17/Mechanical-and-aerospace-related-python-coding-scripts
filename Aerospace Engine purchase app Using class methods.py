class JetEngine_purchase:

    company1='Rolls Royce'
    company2='Boeing'
    company3='Airbus'
    orders1=0
    orders2=0
    orders3=0


    @classmethod
    def order_in_RR(cls):
        cls.orders1 += 1
        print('Company Name:',cls.company1)
        print('Number. of Orders:',cls.orders1)

    @classmethod
    def order_in_Boeing(cls):
        cls.orders2 +=1
        print('Company Name:',cls.company2)
        print('Number. of Orders:',cls.orders2)

    @classmethod
    def order_in_Airbus(cls):
        cls.orders3 +=1
        print('Company Name:',cls.company3)
        print('Number. of Orders:',cls.orders3)

JetEngine_purchase.order_in_RR()
JetEngine_purchase.order_in_RR()
JetEngine_purchase.order_in_RR()
JetEngine_purchase.order_in_RR()
JetEngine_purchase.order_in_RR()
JetEngine_purchase.order_in_RR()
JetEngine_purchase.order_in_Boeing()
JetEngine_purchase.order_in_Airbus()
JetEngine_purchase.order_in_RR()
JetEngine_purchase.order_in_RR()





        








