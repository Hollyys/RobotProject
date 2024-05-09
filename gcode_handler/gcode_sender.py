# 파일 경로 지정
file_path = '/Users/crossrunway/xsCODE/RobotProject/backend/gcode/gcode.txt'

# 파일 열기
with open(file_path, 'r') as file:
    for line in file:
        if line[0] != '%':
            print()
            print(line)