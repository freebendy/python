# -*- coding: cp936 -*-
import sys,os
#��ȡ�ű��ļ��ĵ�ǰ·��
def cur_file_dir():
    #��ȡ�ű�·��
    path = sys.path[0]
    #�ж�Ϊ�ű��ļ�����py2exe�������ļ�������ǽű��ļ����򷵻ص��ǽű���Ŀ¼�������py2exe�������ļ����򷵻ص��Ǳ������ļ�·��
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)
#��ӡ���
#print cur_file_dir()