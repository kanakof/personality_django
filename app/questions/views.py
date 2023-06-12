from django.shortcuts import render, redirect
from django.views.generic import View


class ProcessView(View):
    def get(self, request):
        return render(request, "questions/question_list.html")

    def post(self, request):
        """POSTの結果次第で、レンダリングする"""
        print("post request is received")
        result_type = self.get_personality_type(request)
        if result_type == "type A":
            return redirect("result")
        elif result_type == "type B":
            return redirect("result")
        elif result_type == "type C":
            return redirect("result")
        return redirect("result")

    def get_personality_type(self, request):
        """group1(=タイプA),group2(=タイプB),group3(=タイプC)"""
        """[]内の数値はhtmlのitem名"""
        group1 = ["1", "4", "8", "10", "13", "17"]
        group2 = ["2", "6", "9", "12", "15", "18"]
        group3 = ["3", "5", "7", "11", "14", "16"]

        """group1(=タイプA)の合計を算出"""
        total = 0
        for i in group1:
            point_str = request.POST.get("item{}".format(i))
            print(point_str)
            if point_str:
                total += int(point_str)
        print(total)

        """group2(=タイプB)の合計を算出"""
        total2 = 0
        for i in group2:
            point_str = request.POST.get("item{}".format(i))
            print(point_str)
            if point_str:
                total2 += int(point_str)
        print(total2)

        """group3(=タイプC)の合計を算出"""
        total3 = 0
        for i in group3:
            point_str = request.POST.get("item{}".format(i))
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
        elif total2 == total3 > total:
            personality_type = "C"
        personality_type = "type " + personality_type
        return personality_type


class ResultView(View):
    def get(self, request):
        redirect_template = "questions/result_a.html"
        redirect_template = "questions/result_b.html"
        redirect_template = "questions/result_c.html"
        return render(request, redirect_template)
