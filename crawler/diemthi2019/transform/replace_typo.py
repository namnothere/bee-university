#   Copyright (c) 2019 BeeCost Team <beecost.com@gmail.com>. All Rights Reserved
#   BeeCost Project can not be copied and/or distributed without the express permission of @tuantmtb
import json

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from helper.logger_helper import LoggerSimple
from helper.reader_helper import load_jsonl_from_gz, store_jsons_perline_in_file
from helper.reader_helper import get_files_absolute_in_folder

logger = LoggerSimple(name=__name__).logger


def fix_typo(diemthi_2019_folder_path='/bee_university/crawler/common/diemthi_2019'):
    for idx, diemthi_2019_file_path in enumerate(get_files_absolute_in_folder(diemthi_2019_folder_path)):
        logger.info(f'loading {diemthi_2019_file_path}')
        data = load_jsonl_from_gz(diemthi_2019_file_path)
        data_new = []
        for obj_info in data:
            if 'Đia' in obj_info:
                obj_info.update({'Dia': obj_info.get('Đia')})
                obj_info.pop('Đia', None)
                logger.info(obj_info)
            data_new.append(obj_info)
            # fix_typo
        store_jsons_perline_in_file(jsons_obj=data_new, file_output_path=diemthi_2019_file_path)
    logger.info('done')


if __name__ == '__main__':
    diemthi_2019_folder_path = '/bee_university/crawler/common/diemthi_2019'
    fix_typo(diemthi_2019_folder_path)
