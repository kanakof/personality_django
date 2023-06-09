from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
# from questions.models import 

def index(request):
    return render(request, "questions/index.html")

def page(request):
    return render(request, "questions/page.html")


class ProcessView(View):

    def post(self,request):
        print("post request is received")
        apple = "banana"
        result_type = self.get_personality_type(request,apple)

        """POSTの結果次第で、レンダリングする"""
        # if request.method == 'POST':
        print(result_type)
        # print(type(result_type))
        if result_type == 'type A':
            return render(request, "questions/result_a.html")
        elif result_type == 'type B':
            return render(request, "questions/result_b.html")
        elif result_type == 'type C':
            return render(request, "questions/result_c.html")



    def get_personality_type(self,request,apple):
        """group1(=タイプA),group2(=タイプB),group3(=タイプC)"""
        """[]内の数値はhtmlのitem名"""
        group1 = ["1","4","8","10","13","17"]
        group2 = ["2","6","9","12","15","18"]
        group3 = ["3","5","7","11","14","16"]

        """group1(=タイプA)の合計を算出"""
        total = 0
        for i in group1:
            point_str = request.POST.get('item{}'.format(i))
            print(point_str)
            if point_str:
                total += int(point_str)
        print(total)

        """group2(=タイプB)の合計を算出"""
        total2 = 0
        for i in group2:
            point_str = request.POST.get('item{}'.format(i))
            print(point_str)
            if point_str:
                total2 += int(point_str)
        print(total2)

        """group3(=タイプC)の合計を算出"""
        total3 = 0
        for i in group3:
            point_str = request.POST.get('item{}'.format(i))
            print(point_str)
            if point_str:
                total3 += int(point_str)
        print(total3)

        """
        ↓Type出力ロジック説明↓
        (前提) total=タイプA,total2=タイプB,total3=タイプC
        (前提) タイプの強さ : タイプＡ＞タイプＣ＞タイプＢ）
        -1つが最も高いとき : そのタイプを返す
        -数値が同一のとき  : 強いタイプを優先して返す"""
        personality_type = ""
        if total >= total2 and total3:
            personality_type = "A"
        elif total2 > total and total3:
            personality_type = "B"
        elif total3 > total and total2:
            personality_type = "C"
        elif total == total2 > total3 or total == total3 > total2:
            personality_type = "A"
        elif total2 == total3 >total:
            personality_type = "C"
        personality_type = "type " + personality_type
        return personality_type


