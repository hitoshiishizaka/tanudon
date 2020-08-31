#J831 10:53
def get_east_asian_width_count(text):
    import unicodedata 
    #半角と全角の幅を求める(半角:1　全角:2)
    count = 0
    for c in text:
        if unicodedata.east_asian_width(c) in 'FWA':
            count += 2
        else:
            count += 1
    return count

def haba_cal(s,haba=20,embedded='',hoko='<'):
    #半角と全角混在でも幅を揃える文字を返す
    #s:文字列　haba:揃えたい文字数 
    #embeged:埋め込みい文字　
    #hoko:左寄せ< 中央揃え^ 右寄せ>
    n=get_east_asian_width_count(s)
    new_haba=haba+len(s)-n
    ss='{:'+embedded+hoko+str(new_haba)+'}'
    final_s=ss.format(s)
    return final_s

    #F - East Asian Full-width
    #H - East Asian Half-width
    #W - East Asian Wide
    #Na - East Asian Narrow (Na)
    #A - East Asian Ambiguous (A)
    #N - Not East Asian

def test1():
    #     １２３４５６789０１２３４５６７８９０１２３４５６７８９０１　31文字
    #     ２４６８０２345７９１３５７９１３５７９１３５７９１３５７９　59文字
    text="この文字列は123のような半角と、１２３のような全角文字が混在"
    mojisu=get_east_asian_width_count(text)
    len1=len(text)
    
    print("全角も半角もlen関数で計算すると幅は：",len1)
    #全角も半角もlen関数で計算すると幅は： 31

    print("混在を考慮して計算した文字列の幅は：",mojisu)
    #混在を考慮して計算した文字列の幅は： 59
    
def test2():
    name1="3915 テラスカイ"
    date1="2020/7/17"
    open1="3210"
    high1="3720"
    low1="3190"
    close1="3655"
    
    name2="6035 IRジャパン"
    date2="2020/7/17"
    open2="11400"
    high2="12860"
    low2="11240"
    close2="12670"
    
    print("name","date","open","low","close",sep=" ")
    print(name1,date1,open1,high1,low1,close1,sep=" ")
    print(name2,date2,open2,high2,low2,close2,sep=" ")
    
    name0_s=haba_cal('name',haba=20,embedded=' ',hoko='<')
    date0_s=haba_cal('date',haba=10,embedded=' ',hoko='<')
    open0_s=haba_cal('open',haba=8,embedded=' ',hoko='^')
    high0_s=haba_cal('high',haba=8,embedded=' ',hoko='^')
    low0_s=haba_cal('low',haba=8,embedded=' ',hoko='^')
    close0_s=haba_cal('close',haba=8,embedded=' ',hoko='^')
    
    print('-'*62)
    print(name0_s+date0_s+open0_s+high0_s+low0_s+close0_s)
    
    
    name1_s=haba_cal(name1,haba=20,embedded=' ',hoko='<')
    date1_s=haba_cal(date1,haba=10,embedded=' ',hoko='<')
    open1_s=haba_cal(open1,haba=8,embedded=' ',hoko='^')
    high1_s=haba_cal(high1,haba=8,embedded=' ',hoko='^')
    low1_s=haba_cal(low1,haba=8,embedded=' ',hoko='^')
    close1_s=haba_cal(close1,haba=8,embedded=' ',hoko='^')
    
    print(name1_s+date1_s+open1_s+high1_s+low1_s+close1_s)

    name2_s=haba_cal(name2,haba=20,embedded=' ',hoko='<')
    date2_s=haba_cal(date2,haba=10,embedded=' ',hoko='<')
    open2_s=haba_cal(open2,haba=8,embedded=' ',hoko='^')
    high2_s=haba_cal(high2,haba=8,embedded=' ',hoko='^')
    low2_s=haba_cal(low2,haba=8,embedded=' ',hoko='^')
    close2_s=haba_cal(close2,haba=8,embedded=' ',hoko='^')
    
    print(name2_s+date2_s+open2_s+high2_s+low2_s+close2_s)
    print('-'*62)
    
    #name date open low close
    #3915 テラスカイ 2020/7/17 3210 3720 3190 3655
    #6035 IRジャパン 2020/7/17 11400 12860 11240 12670
    #--------------------------------------------------------------
    #name                date        open    high    low    close
    #3915 テラスカイ     2020/7/17   3210    3720    3190    3655
    #6035 IRジャパン     2020/7/17  11400   12860   11240   12670
    #--------------------------------------------------------------

if __name__  == '__main__':
    test1()
    test2()
    a=input()
