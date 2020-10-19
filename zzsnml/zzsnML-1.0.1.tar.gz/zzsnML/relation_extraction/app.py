# -*- coding: utf-8 -*-
from flask import Flask, g, render_template, flash, redirect, url_for, request, abort, session
from werkzeug.utils import secure_filename
import time
import os
#import sys
#sys.path.append("./src")


#os.chdir(os.path.join(os.getcwd(),'src'))

#import rel_prediction
import traceback
from relation_extraction.preprocessing_xls import paragraph_sectioning,preprocessing_xls_4train,preprocessing_xls_4pred
from relation_extraction.rel_train import train_
from relation_extraction.rel_prediction import prediction_,left_bag_of_words_featurizer,simple_bag_of_words_featurizer,right_bag_of_words_featurizer,get_high_prob_excel

DEBUG = False
PORT = 8017
HOST = '0.0.0.0'

app = Flask(__name__)

   
@app.route('/', methods=('GET', 'POST'))
def index():
    return ''

# def index():
#     query_form = QueryForm()
#     if request.method == 'POST':
#         if query_form.validate_on_submit():
#             query_file = request.files.get('query', None)
#             query_file_name = secure_filename(str(int(time.time()*100)) + '_' + query_file.filename)
#             path = os.path.join(app.config['UPLOAD_FOLDER'], query_file_name)
#             query_file.save(path)
#             session['query_file'] = query_file_name

#         return redirect(url_for('show_result'))
#     return render_template('index.html', query_form=query_form)


@app.route('/proces_train_xls/', methods=('GET', 'POST'))
def preprocessing_4train():
    xls_name = str(request.form.get('xls_name'))
    print(xls_name)
    if not os.path.isfile(xls_name):
        return 'xls文件不存在！'
    try:
        preprocessing_xls_4train(xls_name)
    except Exception as e:
        print(e)
        return '0'
    return '1'

@app.route('/train/', methods=('GET', 'POST'))
def get_train():
    try:
        train_()
    except Exception as e:
        print(e)
        return '0'
    return '1'


from flask import jsonify
import json
def get_return_info(_message, _prob_sorted=None, _text=None):
    return json.dumps({'message': _message, 'prob': _prob_sorted, 'min_text':  _text},ensure_ascii=False)

@app.route('/predict/', methods=('GET', 'POST'))
def get_prediction():
    e1 = request.form.get('e1')
    e2 = request.form.get('e2')
    test_text = str(request.form.get('test_text'))
#    list = {'a1':0.9,'a2':0.8}
#    content = {'e1': list, 'e2': e2, 'text': test_text}
#    return jsonify(content)

    if (e1 is None) and (e2 is not None): 
        return get_return_info('输入格式应是：e1=XX&e2=YY&test_text=ZZ, 且句中应有左右实体名') 
    if (e2 is None) and (e1 is not None):
        return get_return_info('输入格式应是：e1=XX&e2=YY&test_text=ZZ, 且句中应有左右实体名') 
     
    if (e1 is None):
        print('左实体名 is None\n')
    if (e2 is None):
        print('右实体名 is None\n')
    
    #test_text = str(request.args.get('test_text'))

    #print(rel_prediction.OLD_URL)
    
#    print(type(test_text),test_text)
    #test_text = str('郑新聪	国资国企改革发展	要坚持用习近平新时代中国特色社会主义思想指导福建国资国企改革发展，牢牢把握国有企业改革的正确方向。李南轩摄学习宣传贯彻党的十九大精神是全党全国当前和今后一个时期的首要政治任务。如何学习贯彻好党的十九大精神，习近平总书记在十九届中央政治局第一次集体学习时，提出要在学懂弄通做实上下功夫，号召“全党来一个大学习”。日前，福建全省各个领域、各条战线、各行各业兴起习近平新时代中国特色社会主义思想“大学习”热潮。福建省副省长郑新聪前些时候深入三钢集团福建罗源闽光钢铁有限责任公司一线，开展习近平新时代中国特色社会主义思想宣讲。宣讲会前，郑新聪一行深入到罗源闽光公司炼钢厂，沿着参观通道边走边看边听汇报，详细了解罗源闽光公司在绿色发展、技术指标、科技创新、经济效益等方面情况。在随后的宣讲会上，郑新聪以“深入学习习近平新时代中国特色社会主义思想深化和推动国有企业改革发展”为党课主题，分别从习近平新时代中国特色社会主义思想关于“推动我国经济高质量发展”的论述、新时代国资国企改革发展肩负新的历史使命、坚持用习近平新时代中国特色社会主义思想指导福建国资国企改革发展三个方面作了深刻阐释。就下一步如何推进新时代国资国企改革发展，郑新聪要求，要坚持用习近平新时代中国特色社会主义思想指导福建国资国企改革发展，深刻认识深化国有企业改革的重大意义，牢牢把握国有企业改革的正确方向。以新发展理念推动国企发展宣讲中，郑新聪与参会人员共同学习回顾了习近平新时代中国特色社会主义思想关于“推动我国经济高质量发展”的论述：目前，我国经济已由高速增长阶段转向高质量发展阶段。推动高质量发展是保持经济持续健康发展的必然要求；推动高质量发展是适应我国社会主要矛盾变化的必然要求；推动高质量发展是遵循经济规律发展的必然要求。此外，实现高质量发展必须坚持和践行新发展理念。发展是解决我国一切问题的基础和关键，发展必须是科学发展，必须坚定不移贯彻创新、协调、绿色、开放、共享的发展理念。新发展理念是习近平新时代中国特色社会主义经济思想的主要内容，在推进我国经济高质量发展过程中，必须坚定不移贯彻。为推动我国经济高质量发展，我们要坚持适应把握引领经济发展新常态，要把推进供给侧结构性改革作为经济工作的主线，要建设现代化经济体系。针对以上论述，郑新聪强调，全体成员要把握领会习近平新时代中国特色社会主义思想精神，特别是关于深化和推动国有企业改革发展方面，以此推动国企高质量发展。新时代国资国企肩负新使命郑新聪指出，党的十九大提出“要完善各类国有资产管理体制，改革国有资本授权经营体制，加快国有经济布局优化、结构调整、战略性重组，促进国有资产保值增值，推动国有资本做强做优做大，有效防止国有资产流失；深化国有企业改革，发展混合所有制经济，培育具有全球竞争力的世界一流企业。”这“九句话、109字”为国资国企改革发展指明了前进的方向，是我们推进下一步工作的重要行动指南。郑新聪表示，首先要深刻认识深化国有企业改革的重大意义。国有企业是推进国家现代化、保障人民共同利益的重要力量，是党和国家事业发展的重要物质基础和政治基础。深化国有企业改革是坚持和发展中国特色社会主义的必然要求，深化国有企业改革是实现“两个一百年”奋斗目标的重大任务，深化国有企业改革是推动我国经济持续健康发展的客观要求。在明确国企深化改革的重要性后，郑新聪强调，下一步要牢牢把握国有企业改革的正确方向。首先，要坚持和完善基本经济制度。必须毫不动摇巩固和发展公有制经济，毫不动摇鼓励、支持、引导非公有制经济发展。坚持公有制主体地位，发挥国有经济主导作用，做强做优做大国有企业。其次，要坚持社会主义市场经济改革方向。遵循市场经济规律和企业发展规律，坚持政企分开、政资分开、所有权与经营权分离，坚持权利、义务、责任相统一，促使国有企业真正成为独立市场主体。再者，坚持以解放和发展生产力为标准。始终把握有利于国有资产保值增值、有利于提高国有经济竞争力、有利于放大国有资本功能的要求，着力破除束缚国有企业发展的体制机制障碍，发挥国有企业各类人才积极性、主动性、创造性。同时，坚持增强活力与强化监管相结合。增强活力是搞好国有企业的本质要求，强化监管是搞好国有企业的重要保障，必须处理好两者关系，切实做到有机统一。此外，要更加坚持党对国有企业的领导。坚持党对国有企业的领导是重大政治原则，必须一以贯之。2016年10月，习近平在全国国有企业党的建设工作会议上指出：中国特色现代国有企业制度，“特”就特在把党的领导融入公司治理各环节。党建写入章程真正融入国企中心工作，章程明确了党组织在公司法人治理结构中的法定地位，特别是党组织在决策、执行、监督各环节的权责和工作方式。值得一提的是，郑新聪充分肯定三钢集团公司党委探索出的党支部密切联系群众的“五小工作法”，通过为群众讲清小道理、解决小问题、办好小事情、选树小典型、开展小活动，实现党建工作与生产经营、职工生活有机融合。随后，郑新聪指出，省属企业要扎实做好新时期深化国有企业改革的重点任务。“省属企业要完善各类国有资产管理体制。建立健全各类国有资产监督法律法规体系。以管资本为主深化国有资产监管要加快国有经济布局优化、结构调整、战略性重组。”郑新聪指出，省属企业要围绕服务国家战略，推动国有经济向关系国家安全、国民经济命脉和国计民生的重要行业和关键领域、重点基础设施集中。加快处置低效无效资产，淘汰落后产能，剥离办社会职能，解决历史遗留问题，提高国有资本配置效率。日前，国务院国资委下发了《关于加强国有企业资产负债约束的指导意见》是落实党的十九大精神，推动国有企业降杠杆、防范化解国有企业债务风险的重要举措，促使高负债国有企业资产负债率尽快回归合理水平。郑新聪指出，近年来，福建省省属企业也呈现一批改革发展典型。三钢集团通过兼并重组整合区域资源，集团钢产量成功突破1100万吨，真正步入大型钢铁企业行列。特别是2014年重组三金钢铁有限公司，形成了现在的罗源闽光钢铁公司，通过优化机制，改善工艺，2016年扭亏为盈，2018年18月份盈利10.74亿元，资产负债率从90降至目前的40，让一个濒临倒闭的企业成为一个福州区域明星企业，成为钢铁行业兼并重组成功典范。星网锐捷旗下凯米网络科技有限公司积极探索商业模式创新，向KTV提供“管理、流量、内容、广告”四大核心价值，构建互联网聚会娱乐新生态，用户超7500万，成为行业独角兽。发展混合所有制经济亦是新时期深化国有企业改革的重点任务。积极推进主业处于充分竞争行业和领域的商业类国有企业混合所有制改革，有效探索重点领域混合所有制改革，在引导子公司层面改革的同时探索在集团公司层面推进混合所有制改革。大力推动国有企业改制上市。稳妥有序开展国有控股混合所有制企业员工持股。此外，形成有效制衡的公司法人治理结构和灵活高效的市场化经营机制，加强监管有效防止国有资产流失。以国有资产保值增值、防止流失为目标，加强对企业关键业务、改革重点领域、国有资本运营重要环节的监督。建立健全国有企业重大决策失误和失职、渎职责任追究倒查机制。加强审计监督、纪检监督、巡查监督，形成监督合力。郑新聪表示，培育具有全球竞争力的世界一流企业也是目前省属企业的重点任务之一。支持国有企业深入开展国际化经营，在“一带一路”建设中推动优势产业走出去。')
    
    #test_text = str('郝鹏	太钢精带公司	国务院国资委党委书记、主任郝鹏到太钢精带公司调研')    
     
    try:
        test_text7,min_text,original_text = paragraph_sectioning(test_text,e1,e2)

        if len(test_text7) < 20:
            return get_return_info(test_text7)
        message_,prob_text,prob_dict_sorted = prediction_(test_line = test_text7)
        
    except:
        return get_return_info(traceback.print_exc())
    #content_ = {'message': message_, 'prob': prob_dict_sorted, 'min_text': min_text}
    return get_return_info(message_, prob_dict_sorted, min_text)    
#    if (len(min_text) + 10) > len(original_text):
#        return result 

#    return result + '<br> ' + min_text


@app.route('/predict_mass/', methods=('GET', 'POST'))
def get_predict_mass():
    xls_name = str(request.form.get('xls_name'))
    try:        
        tsv_fullname = preprocessing_xls_4pred(xls_name) 
        if not os.path.isfile(tsv_fullname):
            return '处理预测文件tsv不存在！'
        result = prediction_(filename_ = tsv_fullname)        
    except:
        return traceback.print_exc()
    return result

@app.route('/predict_high_prob/', methods=('GET', 'POST'))
def get_high_predict_mass():
    xls_name = str(request.form.get('xls_name'))
    prob_threshold_ = float(str(request.form.get('prob_threshold')))
    if not os.path.isfile(xls_name):
        return '被检索的xls文件不存在！'     
    try:        
        xls_fullname = get_high_prob_excel(predicted_result_file = xls_name,prob_threshold = prob_threshold_)
    except:
        return traceback.print_exc()
    return xls_fullname 

app.run(debug=DEBUG, host=HOST, port=PORT)
