with open('app/src/main/cpp/byedpi/proxy.c', 'r') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'udp addr' in line or 'baddr' in line or 'sa_family' in line:
        start = max(0, i-3)
        end = min(len(lines), i+4)
        print(f"--- найдено на строке {i+1} ---")
        for j in range(start, end):
            print(f"{j+1}: {lines[j]}", end='')
        print()
