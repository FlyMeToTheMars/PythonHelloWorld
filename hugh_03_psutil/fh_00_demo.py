import psutil


def main():
    cpu_times = psutil.cpu_times()
    print(cpu_times)

    count = psutil.cpu_count()
    print("cpu cores: %r " % count)

    net_stats = psutil.net_if_stats()
    print(net_stats)

    print(">>>>>>>>>>>>>>>>>>>>分割<<<<<<<<<<<<<<<<<<<<<<")
    print(type(count))


# 根据__name__判断是否执行下方代码
if __name__ == "__main__":
    main()
