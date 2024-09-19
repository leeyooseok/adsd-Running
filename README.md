# 자율주행 데이터 학습&주행

------------------------------------------------------------------
## myjoystick.py

- PyQt5를 사용하여 joystick 위젯을 구현한 것으로 사용자가 마우스로 조이스틱을 조작하여 X,Y 축의 좌표를 전송해줍니다.
- 조이스틱의 움직임을 원활하게 하기 위해 GUI를 구성하는 역할을 하였고 마우스의 입력을 받아 드래그 및 클릭 이벤트를 처리할 수 있도록 했습니다.<br>
- 조이스틱의 움직임 좌표는 joystick.py코드에서 실행하여 쉘에서 확인가능합니다.
- 
## joystick.py
![KakaoTalk_20240913_122123160](https://github.com/user-attachments/assets/90215bb3-9bff-4866-94bc-bdbd614ec11c)

- 위젯의 위치와 배경 색을 지정하고 이 위젯에 레이아웃을 설정해 조이스틱, 비디오 라벨, 속도 슬라이더를 배치합니다.
- MyJoystick 클래스를 사용해 Joystick을 생성하고, cbJoyPos 콜백 함수를 통해 Joystick의 위치를 출력합니다.
이 콜백 함수는 Joystick의 좌표를 받아서 print를 통해 콘솔에 출력합니다.
- QSlider를 사용해 수평 슬라이더를 구현하고, 슬라이더 값이 변경될 때마다 valueChanged 시그널을 통해 현재 값을 출력합니다.<br>
슬라이더는 속도를 나타내며 범위는 0에서 100까지로 설정되어 있으며, 10 단위로 표시되도록 하였습니다.

-------------------------------------------------------------------------------------------------

## myjoystickapp.py

- myjoystickapp은 조이스틱,슬라이더,비디오 라벨 등 여러 UI 요소를 포함한 애플리케이션입니다.
- 애플리케이션의 실행과 전체적인 UI 구성을 관리하고 조이스틱과 다른 위젯을 연동하여 하나의 통합된 프로그램을 구성합니다.
-joystick과 myjoystickapp 파일의 형태가 비슷해보이지만 MyJoystick은 Joystick 자체의 기능을 정의한 작은 단위의 클래스이고, MyJoystickApp은 Joystick과 다른 요소들을 포함한 전체 프로그램을 구성하는 클래스입니다.

## joystick_pos.py

![KakaoTalk_20240913_155425257](https://github.com/user-attachments/assets/3cd0a921-20c0-497b-8be3-48c6f41bb526)

- joystick_pos은  위의 myjoystickapp을 동작시키는 역할을 합니다.
- ```cbJoyPos(joystickPosition, app)``` 함수는 조이스틱의 현재 위치 좌표와 속도 정보를 출력하는 콜백입니다.

## joystick_dir.py

![KakaoTalk_20240913_170249743](https://github.com/user-attachments/assets/0f04895f-8bd3-4d39-bbdb-054d6969f0b6)


- joystick_dir은 위에 방식과 유사하지만 좌표를 나누어 방향을 출력하도록 하였습니다.
- 방향으로 바꾸어 출력하여 움직임에 따른 구분이 쉬워졌으며 데이터를 쌓을때 편리성을 높혔습니다.

------------------------------------------------------------------------------------------

## MyJoystickCamApp.py

- MyJoystickCamApp은 MyJoystickApp을 확장하여, 자율주행 RC 카의 실시간 비디오 스트리밍과 프레임 속도를 처리하는 기능을 추가한 애플리케이션입니다.
- 이 클래스는 OpenCV를 사용하여 비디오 스트림을 받아와 PyQt5 인터페이스에 출력하며, 프레임 속도를 실시간으로 계산해 출력합니다.
- 데이터를 쌓기 위해 영상을 스트리밍 받아오는 것이 중요하며 영상을 잘 출력되야 데이터를 쌓을때 변수를 줄일 수 있습니다.

## video_joystick.py

![화면 캡처 2024-09-13 180243](https://github.com/user-attachments/assets/97dfffa6-a14f-49be-88c8-4d0727e8c2d8)

- video_joystick은 MyJoystickCamApp를 기반으로 조이스틱을 이용한 자동차 제어와 실시간 비디오 스트리밍을 결합한 프로그램입니다.
- 조이스틱을 이용하여 RC카의 방향을 제어하며 실시간 비디오 피드를 제공합니다.

## MyJoystickCamApp.py

- MyDataCollectionApp은 MyJoystickCamApp을 상속받아 조이스틱과 카메라 입력을 활용하여 데이터를 수집하는 역할을 합니다.
- 조이스틱의 위치에 따라 프레임을 수집하고 수집한 데이터를 특정 디렉토리에 저장하는 기능을 제공합니다.
- 디렉토리는 forward,right,left,stop으로 나뉘며 앞서 쉘에 나타나는 결과값에 따라 저장이 되도록 합니다.

## _02_video_joystick_data_collection.py

![KakaoTalk_20240919_121931055](https://github.com/user-attachments/assets/84304e10-b085-480b-a5d1-b8591baf107f)

- _02_video_joystick_data_collection은  MyDataCollectionApp을 사용하여 Joystick과 모터 제어를 결합한 애플리케이션입니다.
Joystick의 입력을 받아 RC 카와 같은 장치를 제어하고, 동시에 데이터를 수집하는 기능을 구현하고 있습니다.
- ```mot_serial.write(command.encode())```를 통해 결정된 명령(f, r, l, s)을 아두이노 시리얼 통신으로 모터에 전송합니다. 이를 통해 Joystick 입력에 따라 모터가 RC 카의 움직임을 제어하게 됩니다.
- 위의 사진처럼 움직임에 따른 데이터가 분류되어 디렉토리에 저장됩니다.

  ## _03_data_labelling.py
  
![KakaoTalk_20240919_130133494](https://github.com/user-attachments/assets/7fbd6aa3-2846-431a-b370-e75f4d0efaef)

  - _03_data_labelling은 데이터 디렉터리 내의 파일을 탐색하여, 각 파일의 경로와 레이블 정보를 CSV 파일로 저장하는 작업을 수행합니다. 데이터 수집 후, 이를 레이블링하여 머신러닝 모델에 사용하기 위한 데이터를 준비하는 과정으로 볼 수 있습니다.
  - 머신러닝 모델 학습을 위한 데이터 전처리 과정에서, 수집된 데이터를 체계적으로 정리하고, 이를 모델이 학습할 수 있는 형태로 변환하는 작업을 수행했습니다.<br> 특히, 대규모 데이터를 다루는 자율주행 프로젝트에서 각 데이터의 라벨링과 정리 작업은 모델의 성능에 직접적인 영향을 미치므로 중요한 단계입니다.
