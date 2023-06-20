from django.db import models

class Order(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField() #남은 수량
    created_dt = models.DateTimeField(auto_now_add=True)

    def __str__(self): # 관리자 페이지에서 객체를 확인할때 해당 값의 명이 출력
        return self.user

    class Meta: # 관리자 페이지 설정
        db_table = 'my_order' # DB에 저장될 테이블 이름 지정
        verbose_name = '주문'
        verbose_name_plural = '주문'