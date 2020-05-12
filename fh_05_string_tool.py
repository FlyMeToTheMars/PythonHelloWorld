

def main():
    print('"{" + ')
    # 创建列表
    field = ['imei',
             'alarm_type',
             'lat',
             'lng',
             'createtime',
             'device_status',
             'mc_type',
             'push_time',
             'read_status',
             'speed',
             'status',
             'addr',
             'id',
             'index_name',
             'user_id',
             'user_parent_id',
             'car_ovner_id',
             'geo_id',
             'extendedField_3',
             'extendedField_4',
             'extendedField_5']
    # 通过while循环遍历列表

    i = 0
    while i < len(field):
        if i == len(field) - 1:
            print('  "\\""+"%s"+"\\":\\""+s"$%s"+"\\""+' % (field[i], field[i]))
            break

        print('  "\\""+"%s"+"\\":\\""+s"$%s"+"\\""+","+' % (field[i], field[i]))
        i += 1

    print('"}"')


if __name__ == '__main__':
    main()
