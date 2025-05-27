from lxml import etree

def insert_ins_tag(paragraph):
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    ins = etree.Element('{%s}ins' % ns['w'])
    ins.text = '[插入内容]'
    paragraph.append(ins)

def insert_del_tag(paragraph):
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    dele = etree.Element('{%s}del' % ns['w'])
    dele.text = '[删除内容]'
    paragraph.append(dele) 