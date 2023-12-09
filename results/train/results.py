import re

path = 'yolov8x-face/results.txt'

with open(path) as file:
    text = file.read()
    results = re.findall(' +Epoch.+\\s.+(?:\\s +Class.+\\s.+)*', text)

    epoch = []
    memory = []
    box_loss = []
    cls_loss = []
    dfl_loss = []
    instances = []
    train_time = []
    train_iters = []
    eval_time = []
    eval_iters = []
    box_p = []
    box_r = []
    box_map50 = []
    box_map50_95 = []

    for result in results:
        lines = result.splitlines()

        data = re.search(
            '(\\d+)/\\d+ +?([\\d.]+)G +?([\\d.]+) +?([\\d.]+) +?([\\d.]+) +?(\\d+).*\\[(\\d+):(\\d+).*?([\\d.]+)it',
            lines[1].strip()
        )

        epoch.append(data[1])
        memory.append(data[2])
        box_loss.append(data[3])
        cls_loss.append(data[4])
        dfl_loss.append(data[5])
        instances.append(data[6])
        train_time.append(60 * int(data[7]) + int(data[8]))
        train_iters.append(data[9])

        data = re.search(
            '\\[(\\d+):(\\d+).*?([\\d.]+)it',
            lines[2].strip()
        )

        eval_time.append(60 * int(data[1]) + int(data[2]))
        eval_iters.append(data[3])

        data = re.search(
            '\\d+ +?\\d+ +?([\\d.]+) +?([\\d.]+) +?([\\d.]+) +?([\\d.]+)',
            lines[3].strip()
        )

        box_p.append(data[1])
        box_r.append(data[2])
        box_map50.append(data[3])
        box_map50_95.append(data[4])

    total_time = sum(train_time) + sum(eval_time)
    total_hours = total_time / 3600.0

    print('Total training time: %.2f hours' % total_hours)
