"""
批量测试文件编码
"""
import chardet
import os
import time
import multiprocessing

start_time=time.time()
base_dir='../文本分类语料库'
total_number=0
number_info={}
error_info=[]
is_delete=True

for category_dir in os.listdir(base_dir):
    each_category_number=0
    for file_name in os.listdir(os.path.join(base_dir,category_dir)):
        with open(os.path.join(base_dir,category_dir,file_name),'rb') as f:
            file_obj=f.read()
            if(chardet.detect(file_obj).get('encoding')!='GB2312'):
                error_info.append(os.path.join(category_dir,file_name))
                if(is_delete):
                    os.remove(os.path.join(base_dir,category_dir,file_name))
        total_number+=1
        each_category_number+=1
    number_info[category_dir]=each_category_number
print('样本总数为%d'%total_number)
print('各分类信息为%s'%number_info)
print('出错的文件%s'%error_info)
end_time=time.time()
print('程序耗时为%f'%end_time-start_time)