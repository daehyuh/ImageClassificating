# ImageClassificating
이미지 분류 프로그램

## 이미지 분류를 해줍니다.
## 분류가 된 이미지는 json을 읽어 화면에 그려줍니다

<img width="481" alt="KakaoTalk_20220929_144050674" src="https://user-images.githubusercontent.com/53990946/192948060-4725e2a5-5f45-459f-9798-5163fda92f59.png">

```python
                if result == 49:  # 1 KEY
                    os.rename(full_fname, image_nm + '_drive' + ext)
                if result == 50:  # 2 KEY
                    os.rename(full_fname, image_nm + '_stop' + ext)
                if result == 51:  # 3 KEY
                    os.rename(full_fname, image_nm + '_undecided' + ext)
                if result == 52:  # 4 KEY
                    pass
                if result == 24:  # ctrl+x
                    print(image_nm + ext)
                    os.remove(image_nm + ext)
```
name.png

1키를 누르면 name_drive.png   
2키를 누르면 name_stop.png   
3키를 누르면 name_undecided.png   
ctrl+x키를 누르면 파일삭제   
