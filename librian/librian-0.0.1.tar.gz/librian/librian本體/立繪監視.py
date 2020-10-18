import 環境
import os
環境.設定工程路徑('./project/極夜所在的星之海')

import 立繪
from psd生成html import 生成html

格寬=315
格高=350
縮放=0.9

tot=''
tot+=f'''
<style>
#bg{{
    background: url('static/紙背景.jpg');
    background-size: cover;
    position:fixed;
    top:0;
    left:0;
    width: 100%;
    height: 100%;
    margin: 0;
    padding: 0;
    z-index: -1;
}}
.外格{{
    width:{格寬*縮放};
    height:{格高*縮放};
    posision:relative;
    display:inline-block;
    border:1px solid #888;
    overflow:hidden;
}}
.格{{
    transform-origin:top left;
    transform:scale({縮放}) translate(-250px,-100px);
}}
.字{{
    height:0;
    posision:absolute;
    display:inline-block;
}}
.True{{
    opacity: 0; 
    background:rgba(0,0,0,0);
    transition: opacity 0.5s;
    filter:drop-shadow(5px 5px 5px #ccc);
}}
.True:hover{{
    opacity: 1; 
    background:rgba(0,0,0,0.5);
}}
</style>
<div id="bg"></div>
'''
for 名,人 in 立繪.映射.items():
    for 顏 in 人['顏']:
        if type(人['顏'][顏])==dict:
            能語=[False,True]
        else:
            能語=[False]
            
        t=''
        for 語 in 能語: 
            包 = 立繪.人物拆解(名,{'顏':顏,'衣':'_默認','語':語,'位置':[0,0,1],'動作':[]})
            t+=f'<div class="格 {語}">{生成html(包)}</div>'
            
        tot+=f'''
        <div class="外格">
            <div class="字"> 
                {名} {顏}
            </div> 
            {t}
        </div>
        '''
    tot+='<br/>'

with open('./html/_立繪監視.html','w',encoding='utf8') as f:
    f.write(tot)
    
os.system('start "" chrome ./html/_立繪監視.html')