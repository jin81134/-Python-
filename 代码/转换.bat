@echo off
rem ��Ҫʹ�����jq��ȷ���价��������ȷ
rem set /a ����Ϊ0

cd  %tmp%
set "path1=D:\����\ԤԼ����\"
set "path2=D:\����\����ץȡ\"
set "file1=%path1%ԤԼ����.csv"
set "file2=%path2%ε����������ץȡ_Bվ.csv"
set "file3=%path2%ε����������ץȡ_Tap.csv"

if not exist "%path1%" (
    mkdir "%path1%"
    echo �Ѵ����ļ���: %path1%
    ) else (
    echo �ļ����Ѵ���: %path1%
)

if not exist "%path2%" (
    mkdir "%path2%"
    echo �Ѵ����ļ���: %path2%
) else (
    echo �ļ����Ѵ���: %path2%
)

IF EXIST %file1% (
    REM �ļ�����ʱҪִ�е�����
) ELSE (
    echo ʱ��,��������,Bվ����,Tap����,�ϼ�����>>"%file1%"
)

IF EXIST %file2%  (
    REM �ļ�����ʱҪִ�е�����
) ELSE (
    echo ʱ��,Bilibili����,��������,1��,2��,3��,4��,5��,��������-��������>>"%file2%"
)

IF EXIST  %file3%  (
    REM �ļ�����ʱҪִ�е�����
) ELSE (
    echo ʱ��,Tap����,��������,1��,2��,3��,4��,5��,��������-��������>>"%file3%"
)

set "expected_header=ʱ��,��������,Bվ����,Tap����,�ϼ�����"
set /p header=<%file1%
if "%header%"=="%expected_header%" (
  echo ��ͷ��ȷ.
) else (
  echo ��ͷ������ޣ����飡[%expected_header%]
  echo �ļ����� %file1%
  exit /b 1
)

set "expected_header=ʱ��,Bilibili����,��������,1��,2��,3��,4��,5��,��������-��������"
set /p header=<%file2%
if "%header%"=="%expected_header%" (
  echo ��ͷ��ȷ.
) else (
  echo ��ͷ������ޣ����飡[%expected_header%]
  echo �ļ����� %file2%
  exit /b 1
)

set "expected_header=ʱ��,Tap����,��������,1��,2��,3��,4��,5��,��������-��������"
set /p header=<%file3%
if "%header%"=="%expected_header%" (
  echo ��ͷ��ȷ.
) else (
  echo ��ͷ������ޣ����飡[%expected_header%]
  echo �ļ����� %file3%
  exit /b 1
)

:loop

rem "ε��������������-ԤԼ����"
set "url=https://bluearchive-cn.com/api/pre-reg/stats"
set "user_agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
curl -s -H "User-Agent: %user_agent%" "%url%" > %tmp%\response.txt
for /f "delims=" %%i in ('type response.txt ^| jq -r ".data.count"') do set "Ba_ba_api=%%i"
echo %Ba_ba_api%>> "%file1%"

rem "Bilibili����-ԤԼ����"
set "url=https://line1-h5-pc-api.biligame.com/game/detail/gameinfo?game_base_id=109864&ts=1680239994877&request_id=cbniUTkIyXpfwxAB83WGglr8getUcGIP&appkey=h9Ejat5tFh81cq8V&sign=b7c535ab5c6b5c9ca718dd430e8928bc"
set "user_agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
curl -s -H "User-Agent: %user_agent%" "%url%" > %tmp%response.txt
for /f "delims=" %%i in ('type response.txt ^| jq -r ".data.book_num"') do set "Bili_ba_api=%%i"
echo %Bili_ba_api%>> "%file1%"

rem "Bilibili��������"
set "url=https://line1-h5-pc-api.biligame.com/game/comment/summary?game_base_id=109864&ts=1680585215754&request_id=ZgNwydOaxhj62MXUz3L1FgYrnIsudEgC&appkey=h9Ejat5tFh81cq8V&sign=39b48ab6cd61acf044cda2493af9d15e"
set "user_agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
curl -s -H "User-Agent: %user_agent%" "%url%" > %tmp%\response.txt
for /f "delims=" %%i in ('type response.txt ^| jq -r ".data.grade"') do set "Bili_ba_api0=%%i"
for /f "delims=" %%i in ('type response.txt ^| jq -r ".data.comment_number"') do set "Bili_ba_api1=%%i"
for /f "delims=" %%i in ('type response.txt ^| jq -r ".data.valid_comment_number"') do set "Bili_ba_api2=%%i"
for /f "delims=" %%i in ('type response.txt ^| jq -r ".data.star_number_list[0]"') do set "stra_1=%%i"
for /f "delims=" %%i in ('type response.txt ^| jq -r ".data.star_number_list[1]"') do set "stra_2=%%i"
for /f "delims=" %%i in ('type response.txt ^| jq -r ".data.star_number_list[2]"') do set "stra_3=%%i"
for /f "delims=" %%i in ('type response.txt ^| jq -r ".data.star_number_list[3]"') do set "stra_4=%%i"
for /f "delims=" %%i in ('type response.txt ^| jq -r ".data.star_number_list[4]"') do set "stra_5=%%i"

rem TapTap����-ԤԼ����������
rem ��bat���������ַ����%����Ҫ�ټӸ��ٷֺ�ת��
set "user_agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
set "url=https://www.taptap.cn/webapiv2/app/v2/detail-by-id/316964?X-UA=V%%3D1%%26PN%%3DWebApp%%26LANG%%3Dzh_CN%%26VN_CODE%%3D100%%26VN%%3D0.1.0%%26LOC%%3DCN%%26PLT%%3DPC%%26DS%%3DAndroid%%26UID%%3D403e642a-90ca-42a4-9bef-faa806d58dc1%%26VID%%3D3126483%%26DT%%3DPC%%26OS%%3DWindows%%26OSV%%3D10" > response.txt
curl -s -H "User-Agent: %user_agent%" "%url%" > %tmp%\response.txt
for /f "delims=" %%i in ('type response.txt ^| jq -r ".data.stat.reserve_count"') do set "Tap_ba_api=%%i"
for /f "delims=" %%i in ('type response.txt ^| jq -r ".data.stat.rating.score"') do set "Tap_ba_api0=%%i"
for /f "delims=" %%i in ('type response.txt ^| jq -r ".data.stat.review_count"') do set "Tap_ba_api1=%%i"
jq -r ".data.stat.vote_info" %tmp%\response.txt > %tmp%\response1.txt
for /f "delims=" %%i in ('type response1.txt ^| jq -r ".[\"1\"]"') do set "Tap_ba_api2=%%i"
for /f "delims=" %%i in ('type response1.txt ^| jq -r ".[\"2\"]"') do set "Tap_ba_api3=%%i"
for /f "delims=" %%i in ('type response1.txt ^| jq -r ".[\"3\"]"') do set "Tap_ba_api4=%%i"
for /f "delims=" %%i in ('type response1.txt ^| jq -r ".[\"4\"]"') do set "Tap_ba_api5=%%i"
for /f "delims=" %%i in ('type response1.txt ^| jq -r ".[\"5\"]"') do set "Tap_ba_api6=%%i"

rem del response.txt response1.txt
set /a sum=%Ba_ba_api% + %Bili_ba_api% + %Tap_ba_api%
set /a Difference_value1=%Bili_ba_api1% - (%stra_1% + %stra_2% + %stra_3% + %stra_4% + %stra_5%)
set /a Difference_value2=%Tap_ba_api1% - (%Tap_ba_api2% + %Tap_ba_api3% + %Tap_ba_api4% + %Tap_ba_api5% + %Tap_ba_api6%)
set "minute=%date:~0,4%-%date:~5,2%-%date:~8,2% %time:~0,2%:%time:~3,2%"
echo "%minute%","%minute%","%Bili_ba_api%","%Tap_ba_api%","%sum%">>"%file1%"
echo "%minute%","%Bili_ba_api0%","%Bili_ba_api1%","%stra_1%","%stra_2%","%stra_3%","%stra_4%","%stra_5%","%Difference_value1%">>"%file2%"
echo "%minute%","%Tap_ba_api0%","%Tap_ba_api1%","%Tap_ba_api2%","%Tap_ba_api3%","%Tap_ba_api4%","%Tap_ba_api5%","%Tap_ba_api6%","%Difference_value2%">>"%file3%"
echo ��ǰʱ��---%minute%---
for /f "tokens=1 delims==" %%a in ('set Bili_ba_api') do set %%a=-1
for /f "tokens=1 delims==" %%a in ('set Tap_ba_api') do set %%a=-1
for /f "tokens=1 delims==" %%a in ('set stra_') do set %%a=-1
for /f "tokens=1 delims==" %%a in ('set Difference_value') do set %%a=-1

TIMEOUT /T 60 /NOBREAK

goto loop
