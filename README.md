# RobotProject  
# 모바일 로봇 프로그래밍 중간과제 레포지토리  
컴퓨터학부 신성한  
2017110157

# About System  
기존의 Drawing 로봇은 이미지 파일 (JPG, JPEG, PNG 등)을 SVG 파일로 변환하여 G Code를 생성해야하는 불편함이 있습니다.
하지만 이 시스템은 Python Imaging Library(PIL)을 활용하여 Raw 이미지 데이터를 바로 G Code화 할 수 있습니다.
## Initial Screen  

## System 명세
해당 레포지토리는 Back-End, Front-End 디렉토리로 구분되어있습니다. 각각 Flask, React 애플리케이션 코드를 가지고 있습니다.
gcode_handler 디렉토리의 경우 gcode 변환 및 전송 테스트 디렉토리입니다.
## How to use  
0. backend/main.py 상단의 app.config['TEST_MODE'] 는 시스템 테스트모드 콜백입니다.
// app.config['TEST_MODE'] = True:
// 테스트모드입니다. 시스템 백엔드에 사용되는 gcode generator, sender 메소드의 테스트 로그가 출력됩니다.
// app.config['TEST_MODE'] = False:
// 일반모드입니다. 불필요한 테스트 로그가 출력되지 않고, 로봇에게 gcode를 전송합니다.
1. 아래에 명시된 방식으로 Back-End, Front-End 애플리케이션을 구동합니다.  
2. React App을 구동하면 웹 브라우저에 자동으로 창이 뜹니다.  
// 창이 뜨지 않는 경우 http://localhost:3000/ 으로 접속합니다.
3. 생성하고싶은 이미지를 선택하고 Upload 버튼을 누릅니다.
// Bug: 고화질의 이미지를 첨부하는 경우 gcode 생성단계에서 오류가 발생합니다.
//      1900x1200 이하의 이미지를 첨부하거나 레포지토리내에 저장되어있는
//      이미지를 활용하십시오.
4. Back-End 콘솔에 gcode가 생성되었다는 메세지가 뜨면 RobotProject/backend/gcode/gcode.txt에 gcode가 저장됩니다.
5. 생성된 gcode를 지정된 포맷으로 로봇에게 전송합니다.

## Robot
### Converts image to g-code  
https://github.com/KoAhauCaleb/drawing_robot_gcode_generator.git  
### G-Code receive format  
http://192.168.120.36/command?commandText={G-Code}  

## Back-End  
### How to install Flask on Ububtu:  
pip install Flask  
pip install flask_cors  
### How to install PIL:  
sudo apt install python3-pil python3-pil.imagetk 
### How to run Backend Server:  
(Project Directory)/RobotProject/backend/main.py  

## Front-End  
### How to install React on Ububtu:  
sudo apt-get update  
sudo apt-get install build-essential  
sudo apt-get install curl  
curl -sL https://deb.nodesource.com/setup_20.x | sudo -E bash --   
sudo apt-get install nodejs  
cd frontend  
npm install  
export NODE_OPTIONS=--openssl-legacy-provider  
### How to run React app:  
npm start  
### 'error:03000086:digital envelope routines::initialization error' 가 발생하는 경우  
export NODE_OPTIONS=--openssl-legacy-provider