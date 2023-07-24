from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Question, Answer, User

class ProcessView(View):
    def get(self, request):
        questions = Question.objects.all()
        print(questions)
        context = {
            "questions" : questions,
        }
        return render(request, "questions/question_list.html", context)

    def post(self, request):
        """POSTの結果次第で、レンダリングする"""
        print("post request is received")
        result_type = self.get_personality_type(request)

        name = request.POST.get("nickname"), 
        g_choice = request.POST.get("gender"),
        b_choice = request.POST.get("blood")

        """入力されていない場合、エラーを返す"""
        if not name or not g_choice or not b_choice:
            return redirect("questions")
        
        user = User.objects.create(
            name = request.POST.get("nickname"), 
            g_choice = request.POST.get("gender"),
            b_choice = request.POST.get("blood"),)
        
        count = Question.objects.count()
        for i in range(1,count + 1): # indexは1からとする
            Answer.objects.create(
                choice = request.POST.get("item{}".format(i)),
                question = Question.objects.get(id=i),
                user = user
                )
            
        request.session['type'] = result_type
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
        if total >= total2 and total >= total3:
            personality_type = "a"
        elif total2 > total and total2 > total3:
            personality_type = "b"
        elif total3 > total and total3 > total2:
            personality_type = "c"
        elif total == total2 > total3 or total == total3 > total2:
            personality_type = "a"
        elif total2 == total3 > total:
            personality_type = "c"
        print(personality_type)
        return personality_type

class ResultView(View):
    def get(self, request):
        """sessionからtypeを取得"""
        personality_type = request.session.get('type')
        if not personality_type:
            return redirect("questions")
        redirect_template = f"questions/result_{personality_type}.html"
        return render(request, redirect_template)
