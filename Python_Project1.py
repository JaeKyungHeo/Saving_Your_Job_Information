{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "--------Job생각--------\n",
      "\n",
      "성명을 입력해주세요 : 허정용\n",
      "1.기본정보/스펙 입력\n",
      "2.활동및자소서입력\n",
      "3.정보확인하기\n",
      "4.프로그램 종료\n",
      "4\n",
      "여러분의 취업을 응원합니다.\n",
      "Program_End...\n"
     ]
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "import openpyxl\n",
    "from openpyxl import load_workbook\n",
    "import pandas as pd\n",
    "\n",
    "print('--------Job생각--------\\n')\n",
    "name = input('성명을 입력해주세요 : ')\n",
    "\n",
    "file = open('{}_인적및스펙.txt'.format(name),'a')\n",
    "file.close()\n",
    "file = open('{}_활동.txt'.format(name),'a')\n",
    "file.close()\n",
    "file = open('{}_자소서.txt'.format(name),'a')\n",
    "file.close()\n",
    "\n",
    "def command():\n",
    "    com = int(input('1.기본정보/스펙 입력\\n2.활동및자소서입력\\n3.정보확인하기\\n4.프로그램 종료\\n'))\n",
    "    return com\n",
    "    \n",
    "class JobAnalysis:\n",
    "\n",
    "    def __init__(self,name = [],english_name = [], date_of_birth = [],email = [],address = [],school = [],linguistics = [],mylicense = [],internship = [],awards = [],society = [],voluntary_service = []):\n",
    "        self.name = name[:]\n",
    "        self.english_name = english_name[:]\n",
    "        self.date_of_birth = date_of_birth[:]\n",
    "        self.email = email[:]\n",
    "        self.address = address[:]\n",
    "        self.school = school[:]\n",
    "        self.linguistics = linguistics[:]\n",
    "        self.mylicense = mylicense[:]\n",
    "        self.internship = internship[:]\n",
    "        self.awards = awards[:]\n",
    "        self.society = society[:]\n",
    "        self.voluntary_service = voluntary_service[:]\n",
    "\n",
    "    def analysis_school(self):\n",
    "        score = \"\"\n",
    "        for count in range(len(self.school)):\n",
    "            score += '■'\n",
    "        return score\n",
    "\n",
    "    def analysis_linguistics(self):\n",
    "        score = \"\"\n",
    "        for count in range(len(self.linguistics)):\n",
    "            score += '■'\n",
    "        return score\n",
    "\n",
    "    def analysis_mylicense(self):\n",
    "        score = \"\"\n",
    "        for count in range(len(self.mylicense)):\n",
    "            score += '■'\n",
    "        return score\n",
    "\n",
    "    def analysis_internship(self):\n",
    "        score = \"\"\n",
    "        for count in range(len(self.internship)):\n",
    "            score += '■'\n",
    "        return score\n",
    "\n",
    "    def analysis_awards(self):\n",
    "        score = \"\"\n",
    "        for count in range(len(self.awards)):\n",
    "            score += '■'\n",
    "        return score\n",
    "            \n",
    "    def analysis_society(self):\n",
    "        score = \"\"\n",
    "        for count in range(len(self.society)):\n",
    "            score += '■'\n",
    "        return score\n",
    "\n",
    "    def analysis_voluntary_service(self):\n",
    "        score = \"\"\n",
    "        for count in range(len(self.voluntary_service)):\n",
    "            score += '■'\n",
    "        return score\n",
    "\n",
    "\n",
    "    def __str__(self):              \n",
    "        result = \"--기본정보--\\n성명 {0}\\n영문이름 {1}\\n생년월일 {2}\\n이메일 {3}\\n주소 {4}\\n출신학교 \\n{5}\\n\\n어학 \\n{6}\\n자격증\\n{7}\\n인턴십/아르바이트\\n{8}\\n수상내역\\n{9}\\n동아리/대외활동\\n{10}\\n봉사활동\\n{11}\".format(self.name, self.english_name, self.date_of_birth, self.email, self.address, self.school, self.linguistics, self.mylicense, self.internship, self.awards, self.society, self.voluntary_service)\n",
    "        #result = \"--my_information--\\n myname: {0}\\n english_name: {1}\\n date_of_birth: {2}\\n email: {3}\\n address: {4}\\n school: {5}\\n linguistics: {6}\\n mylicense: {7}\\n internship: {8}\\n awards: {9}\\n society: {10}\\n voluntary service: {11}\".format(self.name, self.english_name, self.date_of_birth, self.email, self.address, self.school, self.linguistics, self.mylicense, self.internship, self.awards, self.society, self.voluntary_service) \n",
    "        outfile = open('{}_인적및스펙.txt'.format(name),'w')\n",
    "        outfile.write(result)\n",
    "        outfile.close()\n",
    "        return result\n",
    "\n",
    "while True:\n",
    "    com = command()\n",
    "    if com == 1:\n",
    "        wb = openpyxl.Workbook()\n",
    "    \n",
    "        sheet1 = wb.active\n",
    "        sheet1.title = \"기본정보\"\n",
    "        sheet1.append(['기본정보'])\n",
    "        sheet1.append([''])\n",
    "        info = []\n",
    "\n",
    "        a = True\n",
    "        while a:\n",
    "            answer = int(input(\"취업준비를 시작하시겠습니까?\\n 1.예\\t2.아니오\\n\"))\n",
    "            if(answer == 2):\n",
    "                print(\"한번더 고민해주세요.\")\n",
    "            else:\n",
    "                print(\"준비를 시작하겠습니다.\")\n",
    "                a = False\n",
    "\n",
    "        list_text = [\"이름\", \"영문이름\", \"생년월일\", \"이메일\", \"주소\"]\n",
    "        list_list = [\"학교\",\"어학\", \"자격증\", \"인턴십/아르바이트\",\"수상경력\", \"동아리/대외활동\", \"봉사활동\"]\n",
    "        list_list_analysis = [\"어학\", \"자격증\", \"인턴십/아르바이트\",\"수상경력\", \"동아리/대외활동\", \"봉사활동\"]\n",
    "\n",
    "        info_text = []\n",
    "        for item in list_text:\n",
    "            info += [input(\"{}(을/를) 입력해주세요 : \".format(item))]\n",
    "\n",
    "        for i in range(len(list_text)):\n",
    "            sheet1.append([list_text[i],info[i]])\n",
    "\n",
    "        for item in list_list:\n",
    "            if item == \"학교\":\n",
    "                sheet1.append([''])\n",
    "                sheet1.append(['학교'])\n",
    "                sheet1.append(['학교명','재학기간','전공','성적/학점'])\n",
    "                info_high = [input(\"고등학교명을 입력해주세요(ex.OO고등학교) : \")] + [input(\"고등학교 재학기간을 입력해주세요(ex.2012.02-2015.01) : \")]\n",
    "                info_college = [input(\"대학교명을 입력해주세요(ex.OO대학교) : \")] + [input(\"대학교 재학기간을 입력해주세요(ex.2015.02-2020.01) : \")]+[input(\"전공을 입력해주세요 : \")]+[input(\"학점입력해주세요(4.5만점기준) : \")]\n",
    "                info_school = [info_high]+[info_college]\n",
    "                info += [info_school]\n",
    "                sheet1.append(info_high)\n",
    "                sheet1.append(info_college)\n",
    "    \n",
    "            information = []\n",
    "            if item == \"어학\":\n",
    "                sheet1.append([''])\n",
    "                sheet1.append(['스펙목록'])\n",
    "                sheet1.append([''])\n",
    "                sheet1.append(['어학'])\n",
    "                sheet1.append(['어학명','점수/레벨','취득일'])\n",
    "                juge = int(input(\"{}(을/를) 입력하시겠습니까?\\n 1.예\\t2.아니오\\n\".format(item)))\n",
    "                while juge == 1:\n",
    "                    info_item = [input(\"어학명을 입력해주세요(ex.TOEIC, TOEIC-Speaking...) : \")]+[input(\"점수 및 레벨을 입력해주세요 : \")]+[input(\"취득날짜를 입력해주세요(ex.2020.02) : \")]\n",
    "                    information += [info_item]\n",
    "                    sheet1.append(info_item)\n",
    "                    juge = int(input(\"어학을 추가입력하시겠습니까? \\n 1.예\\t2.아니오\\n\")) \n",
    "                \n",
    "            if item == \"자격증\":\n",
    "                sheet1.append([''])\n",
    "                sheet1.append(['자격증'])\n",
    "                sheet1.append(['자격증명','급수','취득일'])\n",
    "                juge = int(input(\"{}(을/를) 입력하시겠습니까?\\n 1.예\\t2.아니오\\n\".format(item)))\n",
    "                while juge == 1:\n",
    "                    info_item = [input(\"자격증명을 입력해주세요(ex.운전면허,컴퓨터활용능력...) : \")]+[input(\"급수를 입력해주세요(ex.1종보통,1급...) : \")]+[input(\"취득날짜를 입력해주세요(ex.2020.02) : \")]\n",
    "                    information += [info_item]\n",
    "                    sheet1.append(info_item)\n",
    "                    juge = int(input(\"자격증을 추가입력하시겠습니까? \\n 1.예\\t2.아니오\\n\"))\n",
    "\n",
    "            if item == \"인턴십/아르바이트\":\n",
    "                sheet1.append([''])\n",
    "                sheet1.append(['인턴십/아르바이트'])\n",
    "                sheet1.append(['활동명','활동기간','활동내용'])\n",
    "                juge = int(input(\"{}(을/를) 입력하시겠습니까?\\n 1.예\\t2.아니오\\n\".format(item)))\n",
    "                while juge == 1:\n",
    "                    info_item = [input(\"활동명을 입력해주세요(ex.삼성채용형 인턴, 네이버 인턴...) : \")]+[input(\"활동기간을 입력해주세요(ex.2020.02-2020.06) : \")]+[input(\"주요업무를 입력해주세요 : \")]\n",
    "                    information += [info_item]\n",
    "                    sheet1.append(info_item)\n",
    "                    juge = int(input(\"인턴십/아르바이트를 추가입력 하시겠습니까? \\n 1.예\\t2.아니오\\n\"))\n",
    "                \n",
    "            if item == \"수상경력\":\n",
    "                sheet1.append([''])\n",
    "                sheet1.append(['수상내역'])\n",
    "                sheet1.append(['수상명','수상내용','수상일'])\n",
    "                juge = int(input(\"{}(을/를) 입력하시겠습니까?\\n 1.예\\t2.아니오\\n\".format(item)))\n",
    "                while juge == 1:\n",
    "                    info_item = [input(\"수상명을 입력해주세요(ex.Kms주관 대학생수학경시대회) : \")]+[input(\"내용을 입력해주세요 : \")]+[input(\"수상날짜를 입력해주세요(ex.2020.12) : \")]\n",
    "                    information += [info_item]\n",
    "                    sheet1.append(info_item)\n",
    "                    juge = int(input(\"수상경력을 추가하시겠습니까? \\n 1.예\\t2.아니오\\n\"))\n",
    "                \n",
    "            if item == \"동아리/대외활동\":\n",
    "                sheet1.append([''])\n",
    "                sheet1.append(['동아리/대외활동'])\n",
    "                sheet1.append(['활동명','활동내용','활동기간'])\n",
    "                juge = int(input(\"{}(을/를) 입력하시겠습니까?\\n 1.예\\t2.아니오\\n\".format(item)))\n",
    "                while juge == 1:\n",
    "                    info_item = [input(\"활동명을 입력해주세요(ex.수학과 코딩동아리('콤마'),경희랑달리기) : \")]+[input(\"활동내용을 입력해주세요 : \")]+[input(\"활동기간을 입력해주세요(ex.2020.02) : \")]\n",
    "                    information += [info_item]\n",
    "                    sheet1.append(info_item)\n",
    "                    juge = int(input(\"동아리/대외활동을 추가하시겠습니까? \\n 1.예\\t2.아니오\\n\"))\n",
    "                \n",
    "            if item == \"봉사활동\":\n",
    "                sheet1.append([''])\n",
    "                sheet1.append(['봉사활동'])\n",
    "                sheet1.append(['활동명','활동내용','활동시간'])\n",
    "                juge = int(input(\"{}(을/를) 입력하시겠습니까?\\n 1.예\\t2.아니오\\n\".format(item)))\n",
    "                while juge == 1:\n",
    "                    info_item = [input(\"활동명을 입력해주세요(ex.농민의 날기념 가래떡 나눔) : \")]+[input(\"기관명을 입력해주세요 : \")]+[input(\"활동시간을 입력해주세요(ex.0시간) : \")]\n",
    "                    information += [info_item]\n",
    "                    sheet1.append(info_item)\n",
    "                    juge = int(input(\"봉사활동을 추가하시겠습니까? \\n 1.예\\t2.아니오\\n\"))\n",
    "\n",
    "            info += [information] \n",
    "        wb.save('{}_인적및스펙.xlsx'.format(name))\n",
    "        \n",
    "        myinfo = JobAnalysis(info[0],info[1],info[2],info[3],info[4],info[5],info[7],info[8],info[9],info[10],info[11],info[12])\n",
    "        print(myinfo)\n",
    "        print(\"---------------------분석------------------------\")\n",
    "        print(\"어학부분          => {}\".format(myinfo.analysis_linguistics()))\n",
    "        print(\"자격증부분        => {}\".format(myinfo.analysis_mylicense()))\n",
    "        print(\"인턴십/아르바이트 => {}\".format(myinfo.analysis_internship()))\n",
    "        print(\"수상경력          => {}\".format(myinfo.analysis_awards()))\n",
    "        print(\"동아리/대외활동   => {}\".format(myinfo.analysis_society()))\n",
    "        print(\"봉사활동          => {}\".format(myinfo.analysis_voluntary_service()))\n",
    "\n",
    "        xs = ['linguistics','mylicense','internship','awards','society','voluntary']\n",
    "        ys = [len(info[7]),len(info[8]),len(info[9]),len(info[10]),len(info[11]),len(info[12])]\n",
    "        plt.plot(xs,ys,'o')\n",
    "        plt.show()\n",
    "\n",
    "        for i in range(len(list_list_analysis)):\n",
    "            if(len(info[i+6])==0):\n",
    "                print(\"{}에대한 우선적 보강이 필요합니다.\".format(list_list_analysis[i]))\n",
    "            elif(len(info[i+6])==1):\n",
    "                print(\"{}에대한 추가적인 보충이 필요합니다.\".format(list_list_analysis[i]))\n",
    "    elif(com == 2):\n",
    "        ans = input('무엇을 입력하시겠습니까?\\n1.활동\\t2.자소서\\n')\n",
    "        if(ans == '1'):\n",
    "            ans1 = '1'\n",
    "            while ans1 == '1':\n",
    "                a = ['------------------------------',\"\\n-활동명 : \"+input('활동명을 입력하세요 : ')+'\\n','-활동기간 : '+input('활동기간를 입력하세요 : ')+'\\n','-활동내용\\n'+input('활동내용을 입력하세요.\\n')+'\\n','-느낀점\\n'+input('활동을 통해 느낀점을 적어주세요.\\n')+'\\n']\n",
    "                for i in a:\n",
    "                    outfile = open('{}_활동.txt'.format(name),'a')\n",
    "                    outfile.write(i)\n",
    "                    outfile.close()\n",
    "                ans1 = input('활동내용을 추가하시겠습니까?\\n1.예\\t2.아니오\\n')\n",
    "        elif(ans == '2'):\n",
    "            ans2 = '1'\n",
    "            while ans2 == '1':\n",
    "                a = ['\\n-질문 : \\n',input('질문을 입력하세요 : ')+'\\n','\\n-자소서내용\\n',input('자소서내용을 입력하세요: ')+'\\n\\n']\n",
    "                for i in a:\n",
    "                    outfile = open('{}_자소서.txt'.format(name),'a')\n",
    "                    outfile.write(i)\n",
    "                    outfile.close()\n",
    "                ans2 = input('자소서를 추가하시겠습니까?\\n1.예\\t2.아니오\\n')\n",
    "                    \n",
    "    elif(com == 3):\n",
    "        ans = input('기본/스펙정보, 활동, 자소서 입력을 완료하셨나요?\\n1.예\\t2.아니오\\n')\n",
    "        if ans == '1':\n",
    "            com1 = int(input('1.기본정보및스펙\\n2.활동보기\\n3.자소서보기\\n'))\n",
    "            if(com1 == 1):\n",
    "                file = open('{}_인적및스펙.txt'.format(name),'r')\n",
    "                infos = file.readlines()\n",
    "                file.close()\n",
    "                for p in infos:\n",
    "                    print(p)\n",
    "            if(com1 == 2):\n",
    "                file = open('{}_활동.txt'.format(name),'r')\n",
    "                infos = file.readlines()\n",
    "                file.close()\n",
    "                for p in infos:\n",
    "                    print(p)\n",
    "            if(com1 == 3):\n",
    "                file = open('{}_자소서.txt'.format(name),'r')\n",
    "                infos = file.readlines()\n",
    "                file.close()\n",
    "                for p in infos:\n",
    "                    print(p)\n",
    "        else:\n",
    "            print('정보입력을 완료해주시기 바랍니다.')\n",
    "    else :   \n",
    "        print(\"여러분의 취업을 응원합니다!\\nProgram_End...\")\n",
    "        break"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}