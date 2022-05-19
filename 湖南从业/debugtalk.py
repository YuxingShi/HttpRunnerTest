import random
import time
import json
import re
import hashlib
import xmltodict

from httprunner import __version__

_first_name = ["赵", "钱", "孙", "李", "周", "吴", "郑", "王", "冯", "陈", "褚", "卫", "蒋", "沈", "韩", "杨", "朱", "秦", "尤", "许", "何",
               "吕", "施", "张", "孔", "曹", "严", "华", "金", "魏", "陶", "姜", "戚", "谢", "邹", "喻", "柏", "水", "窦", "章", "云", "苏",
               "潘", "葛", "奚", "范", "彭", "郎", "鲁", "韦", "昌", "马", "苗", "凤", "花", "方", "俞", "任", "袁", "柳", "酆", "鲍", "史",
               "唐", "费", "廉", "岑", "薛", "雷", "贺", "倪", "汤", "滕", "殷", "罗", "毕", "郝", "邬", "安", "常", "乐", "于", "时", "傅",
               "皮", "卞", "齐", "康", "伍", "余", "元", "卜", "顾", "孟", "平", "黄", "和", "穆", "萧", "尹", "姚", "邵", "湛", "汪", "祁",
               "毛", "禹", "狄", "米", "贝", "明", "臧", "计", "伏", "成", "戴", "谈", "宋", "茅", "庞", "熊", "纪", "舒", "屈", "项", "祝",
               "董", "梁", "杜", "阮", "蓝", "闵", "席", "季", "麻", "强", "贾", "路", "娄", "危", "江", "童", "颜", "郭", "梅", "盛", "林",
               "刁", "钟", "丘", "徐", "邱", "骆", "高", "夏", "蔡", "田", "樊", "胡", "凌", "霍", "虞", "万", "支", "柯", "昝", "管", "卢",
               "莫", "经", "房", "裘", "缪", "干", "解", "应", "宗", "丁", "宣", "贲", "邓", "单", "杭", "洪", "包", "诸", "左", "石", "崔",
               "吉", "钮", "龚", "程", "嵇", "邢", "滑", "裴", "陆", "荣", "翁", "荀", "羊", "於", "惠", "甄", "曲", "家", "封", "芮", "羿",
               "储", "靳", "汲", "邴", "糜", "松", "井", "段", "富", "巫", "乌", "焦", "巴", "弓", "牧", "隗", "山", "谷", "车", "侯", "宓",
               "蓬", "全", "郗", "班", "仰", "秋", "仲", "伊", "宫", "宁", "仇", "栾", "暴", "甘", "钭", "厉", "戎", "祖", "武", "符", "刘",
               "景", "詹", "束", "龙", "叶", "幸", "司", "韶", "郜", "黎", "蓟", "薄", "印", "宿", "白", "怀", "蒲", "台", "从", "鄂", "索",
               "咸", "籍", "赖", "卓", "蔺", "屠", "蒙", "池", "乔", "阴", "郁", "胥", "能", "苍", "双", "闻", "莘", "党", "翟", "谭", "贡",
               "劳", "逢", "逄", "姬", "申", "扶", "堵", "冉", "宰", "郦", "雍", "?S", "璩", "桑", "桂", "濮", "牛", "寿", "通", "边", "扈",
               "燕", "冀", "郏", "浦", "尚", "农", "温", "别", "庄", "晏", "柴", "瞿", "阎", "充", "慕", "连", "茹", "习", "宦", "艾", "鱼",
               "容", "向", "古", "易", "慎", "戈", "廖", "庚", "终", "暨", "居", "衡", "步", "都", "耿", "满", "弘", "匡", "国", "文", "寇",
               "广", "禄", "阙", "东", "欧", "殳", "沃", "利", "蔚", "越", "夔", "隆", "师", "巩", "厍", "聂", "晁", "勾", "敖", "融", "冷",
               "訾", "辛", "阚", "那", "简", "饶", "空", "曾", "毋", "沙", "乜", "养", "鞠", "须", "丰", "巢", "关", "蒯", "相", "查", "荆",
               "红", "游", "竺", "权", "逯", "盖", "益", "桓", "公", "万俟", "司马", "上官", "欧阳", "夏侯", "诸葛", "闻人", "东方", "赫连", "皇甫",
               "尉迟", "公羊", "澹台", "公冶", "宗政", "濮阳", "淳于", "单于", "太叔", "申屠", "公孙", "仲孙", "轩辕", "令狐", "钟离", "宇文", "长孙",
               "慕容", "鲜于", "闾丘", "司徒", "司空", "亓官", "司寇", "仉督", "子车", "颛孙", "端木", "巫马", "公西", "漆雕", "乐正", "壤驷", "公良",
               "拓拔", "夹谷", "宰父", "谷粱", "晋", "楚", "阎", "法", "汝", "鄢", "涂", "钦", "段干", "百里", "东郭", "南门", "呼延", "归", "海",
               "羊舌", "微生", "岳", "帅", "缑", "亢", "况", "后", "有", "琴", "梁丘", "左丘", "东门", "西门", "商", "牟", "佘", "佴", "伯", "赏",
               "南宫", "墨", "哈", "谯", "笪", "年", "爱", "阳", "佟", "第五", "言", "福"]
_last_name = ["坚锋", "破天", "无忌", "念慈", "达开", "靖", "康", "蓉", "国藩", "清照", "渠梁", "操", "天佑", "亮", "长平"]


def get_httprunner_version():
    return __version__


def sum_two(m, n):
    return m + n


def sleep(n_secs):
    time.sleep(n_secs)


def page_element_exist(tag_name, text, response):
    pattern = r'<{0} .*?>[.\s]*{1}'.format(tag_name, text)
    print('pattern', pattern)
    pattern_list = re.findall(pattern, response.text)
    if len(pattern_list):
        print('pattern_list', pattern_list)
        return True
    else:
        return False


def _get_id_no(str17):
    str_sum = 0
    str_count = 0
    # 18位身份证17位系数
    ratio_tuple = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
    # 余数取值对应
    remainder = '10X98765432'
    if str17.__len__() != 17:
        print('不是17位数字字符串无法计算！')
        return
    for i in ratio_tuple:
        str_sum += int(str17[str_count]) * i
        str_count += 1
    check_code = remainder[str_sum % 11]
    return '{}{}'.format(str17, check_code)


def get_id_no():
    """获取身份证号码"""
    region_code = '350101'
    year = random.randint(1949, 2000)
    month = str(random.randint(1, 12)).zfill(2)
    day = str(random.randint(1, 28)).zfill(2)
    index = str(random.randint(1, 99)).zfill(2)
    sex_code = random.randint(1, 9)
    id_no = '%s%s%s%s%s%s' % (region_code, year, month, day, index, sex_code)
    return _get_id_no(id_no)


def get_id():
    """获取32位ID"""
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    md5 = hashlib.md5()
    md5.update(bytes(timestamp, encoding='utf-8'))
    return md5.hexdigest().upper()


def get_name():
    """获取姓名"""
    first_name = _first_name[random.randint(0, _first_name.__len__() - 1)]
    last_name = _last_name[random.randint(0, _last_name.__len__() - 1)]
    return first_name + last_name


def xml_to_json(xml_str):
    # parse是的xml解析器
    xml_parse = xmltodict.parse(xml_str)
    # json库dumps()是将dict转化成json格式,loads()是将json转化成dict格式。
    # dumps()方法的ident=1,格式化json
    json_str = json.dumps(xml_parse, indent=1)
    return json_str


def teardown_hook_xml_json(response):
    """
    将xml报文内容转化为json格式内容,并将返回内容替换成json格式
    :param response: 返回报文对象
    """
    jsoninfo = xml_to_json(response.body)
    response.body = json.loads(jsoninfo)


_keyword_dict = {'${NAME}': get_name(),
                 '${IDCARD}': get_id_no(),
                 '${ID}': get_id()}


def get_xml_body(file_path):
    with open(file_path, 'r', encoding='utf-8') as fp:
        text = fp.read()
        keyword_list = re.findall('(\$\{.*?\})', text)
        for keyword in set(keyword_list):
            value = _keyword_dict.get(keyword)
            text = text.replace(keyword, value)
        # return quote(result_text, safe='<=? /\r\n">', encoding='gbk')
        return text.encode()
