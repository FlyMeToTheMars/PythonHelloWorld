import psutil


def main():
    cpu_times = psutil.cpu_times()
    print(cpu_times)

    count = psutil.cpu_count()
    print("cpu cores: %r " % count)


    print(">>>>>>>>>>>>>>>>>>>>分割")
    print(type(count))


# 根据__name__判断是否执行下方代码
if __name__ == "__main__":
    main()
