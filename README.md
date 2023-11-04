# Introduction

This project is designed for IOT laboratory personnel check-in and attendance, and the system implements the following functions:
**1. Personnel face recognition and complete check-in/check-out
2. Calculation of attendance time
3. Save the attendance data in CSV format (Excel) **

PS: This system 2D face recognition, saving the tedious face recognition training part, simple and fast

This project is a beta version, the official version will add more features, continue to update.....
I'll put the beta project address at the end

## Project renderings

**System initialization login interface**
![在这里插入图片描述](https://img-blog.csdnimg.cn/f48f7936b3ff4a5496e188c13c64dc36.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQklHQk9TU3lpZmk=,size_20,color_FFFFFF,t_70,g_se,x_16)
**Main interface display picture:**
![在这里插入图片描述](https://img-blog.csdnimg.cn/c2d5b4d272ad4a7eac5ae8107dfb56e9.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQklHQk9TU3lpZmk=,size_20,color_FFFFFF,t_70,g_se,x_16)
**Sign in function display **
![在这里插入图片描述](https://img-blog.csdnimg.cn/61685dd4b9184bdb8c33379f0e52833d.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQklHQk9TU3lpZmk=,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://img-blog.csdnimg.cn/0a2258078cc84c16b941cc4220a7aca0.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQklHQk9TU3lpZmk=,size_20,color_FFFFFF,t_70,g_se,x_16)
**Sign out function display**
![在这里插入图片描述](https://img-blog.csdnimg.cn/4cc3fd36c2584623b277994dbe1c9b1e.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQklHQk9TU3lpZmk=,size_20,color_FFFFFF,t_70,g_se,x_16)
**Background check-in data recording**
![在这里插入图片描述](https://img-blog.csdnimg.cn/f752bbde1e7b4a4bba2090f38d46ae2b.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQklHQk9TU3lpZmk=,size_20,color_FFFFFF,t_70,g_se,x_16)
**Check in/check out**
![在这里插入图片描述](https://img-blog.csdnimg.cn/eadfab52443c4c29b1829a653a41887f.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQklHQk9TU3lpZmk=,size_20,color_FFFFFF,t_70,g_se,x_16)

# The environment required for the project

**OpenCV-Python     			 4.5.5.64**
**face_recognition					1.30
face_recognition_model   				0.3.0
dlib 								19.23.1**


**PyQt5                        5.15.4
pyqt5-plugins                5.15.4.2.2
PyQt5-Qt5                    5.15.2
PyQt5-sip                    12.10.1
pyqt5-tools                  5.15.4.3.2**

**Pycham 2021.1.3**
![在这里插入图片描述](https://img-blog.csdnimg.cn/ba2d84f8b9704abfbfa359b5bf616fea.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQklHQk9TU3lpZmk=,size_18,color_FFFFFF,t_70,g_se,x_16)

```
**PythonVersion 3.9.12**
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/3050ef31da794f1f98d32fb05a5ae651.png)
**Anaconda**
![在这里插入图片描述](https://img-blog.csdnimg.cn/47462d375b0a4e08a22cf33bc50b0d71.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQklHQk9TU3lpZmk=,size_20,color_FFFFFF,t_70,g_se,x_16)

### QT-designer

![在这里插入图片描述](https://img-blog.csdnimg.cn/d7e826c9112f4f27b462f3a1b3e3b891.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQklHQk9TU3lpZmk=,size_20,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://img-blog.csdnimg.cn/e9bef28e2e0241828bcd633769542490.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQklHQk9TU3lpZmk=,size_20,color_FFFFFF,t_70,g_se,x_16)

#### Setting

![在这里插入图片描述](https://img-blog.csdnimg.cn/b8c6fa4783d243f2b2ba4702c1ae52e3.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQklHQk9TU3lpZmk=,size_19,color_FFFFFF,t_70,g_se,x_16)

# Code

## CoreCode

**MainWindow.py**
*UI File：*

```python
class Ui_Dialog(QDialog):
    def __init__(self):
        super(Ui_Dialog, self).__init__()
        loadUi("mainwindow.ui", self)       #加载QTUI文件

        self.runButton.clicked.connect(self.runSlot)

        self._new_window = None
        self.Videocapture_ = None
```

*Camera：*

```python
    def refreshAll(self):
        print("当前调用人俩检测摄像头编号（0为笔记本内置摄像头，1为USB外置摄像头）：")
        self.Videocapture_ = "0"
```

**OutWindow.py**
*request Time*

```python
class Ui_OutputDialog(QDialog):
    def __init__(self):
        super(Ui_OutputDialog, self).__init__()
        loadUi("./outputwindow.ui", self)   #加载输出窗体UI

        #datetime 时间模块
        now = QDate.currentDate()
        current_date = now.toString('ddd dd MMMM yyyy')  #时间格式
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        self.Date_Label.setText(current_date)
        self.Time_Label.setText(current_time)

        self.image = None
```

*Check in time*

```python
    def ElapseList(self,name):
        with open('Attendance.csv', "r") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 2

            Time1 = datetime.datetime.now()
            Time2 = datetime.datetime.now()
            for row in csv_reader:
                for field in row:
                    if field in row:
                        if field == 'Clock In':
                            if row[0] == name:
                                Time1 = (datetime.datetime.strptime(row[1], '%y/%m/%d %H:%M:%S'))
                                self.TimeList1.append(Time1)
                        if field == 'Clock Out':
                            if row[0] == name:
                                Time2 = (datetime.datetime.strptime(row[1], '%y/%m/%d %H:%M:%S'))
                                self.TimeList2.append(Time2)
```

*FaceRecognition*

```python
# 人脸识别部分
        faces_cur_frame = face_recognition.face_locations(frame)
        encodes_cur_frame = face_recognition.face_encodings(frame, faces_cur_frame)

        for encodeFace, faceLoc in zip(encodes_cur_frame, faces_cur_frame):
            match = face_recognition.compare_faces(encode_list_known, encodeFace, tolerance=0.50)
            face_dis = face_recognition.face_distance(encode_list_known, encodeFace)
            name = "unknown"    #未知人脸识别为unknown
            best_match_index = np.argmin(face_dis)
            if match[best_match_index]:
                name = class_names[best_match_index].upper()
                y1, x2, y2, x1 = faceLoc
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(frame, (x1, y2 - 20), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
            mark_attendance(name)

        return frame
```

*CheckData*

```python
# csv表格保存数据
        def mark_attendance(name):
            """
            :param name: 人脸识别部分
            :return:
            """
            if self.ClockInButton.isChecked():
                self.ClockInButton.setEnabled(False)
                with open('Attendance.csv', 'a') as f:
                        if (name != 'unknown'):         #签到判断：是否为已经识别人脸
                            buttonReply = QMessageBox.question(self, '欢迎 ' + name, '开始签到' ,
                                                               QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                            if buttonReply == QMessageBox.Yes:

                                date_time_string = datetime.datetime.now().strftime("%y/%m/%d %H:%M:%S")
                                f.writelines(f'\n{name},{date_time_string},Clock In')
                                self.ClockInButton.setChecked(False)

                                self.NameLabel.setText(name)
                                self.StatusLabel.setText('签到')
                                self.HoursLabel.setText('开始签到计时中')
                                self.MinLabel.setText('')

                                self.Time1 = datetime.datetime.now()
                                self.ClockInButton.setEnabled(True)
                            else:
                                print('签到操作失败')
                                self.ClockInButton.setEnabled(True)
            elif self.ClockOutButton.isChecked():
                self.ClockOutButton.setEnabled(False)
                with open('Attendance.csv', 'a') as f:
                        if (name != 'unknown'):
                            buttonReply = QMessageBox.question(self, '嗨呀 ' + name, '确认签退?',
                                                              QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                            if buttonReply == QMessageBox.Yes:
                                date_time_string = datetime.datetime.now().strftime("%y/%m/%d %H:%M:%S")
                                f.writelines(f'\n{name},{date_time_string},Clock Out')
                                self.ClockOutButton.setChecked(False)

                                self.NameLabel.setText(name)
                                self.StatusLabel.setText('签退')
                                self.Time2 = datetime.datetime.now()

                                self.ElapseList(name)
                                self.TimeList2.append(datetime.datetime.now())
                                CheckInTime = self.TimeList1[-1]
                                CheckOutTime = self.TimeList2[-1]
                                self.ElapseHours = (CheckOutTime - CheckInTime)
                                self.MinLabel.setText("{:.0f}".format(abs(self.ElapseHours.total_seconds() / 60)%60) + 'm')
                                self.HoursLabel.setText("{:.0f}".format(abs(self.ElapseHours.total_seconds() / 60**2)) + 'h')
                                self.ClockOutButton.setEnabled(True)
                            else:
                                print('签退操作失败')
                                self.ClockOutButton.setEnabled(True)
```

### Project directory structure

![在这里插入图片描述](https://img-blog.csdnimg.cn/985c4a761fce457cb773e87fde0903ee.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQklHQk9TU3lpZmk=,size_8,color_FFFFFF,t_70,g_se,x_16)

# At Last

***Because there is no face training model in this system, the system misrecognition rate is high and the security is low
The system optimization is poor, the camera captures a low number of frames (8-9), the background occupies a high, and the CPU utilization is high
Data is saved in CSV format, which has low security***

