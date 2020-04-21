from datetime import datetime #khai báo module datetime từ thư viện datetime
import pytz #tru cập thư viện pytz

local = datetime.now() #ngày giờ hiện tại
print('local:', local.strftime('%M/%d/%Y, %H:%M:%S')) #in ra ngày giờ hiện tại theo strf

tz_NY = pytz.timezone('America/New_York') #chuyển đổi múi giờ , New York
datetime_NY = datetime.now(tz_NY) #trả về ngày giờ hiện tại ở New_York
print('NY:', datetime_NY.strftime('%m/%D/%Y, %H:%M:%S')) #in ra ngày giờ hiện tại ở New_York theo str

tz_London = pytz.timezone('Europe/London') #chuyển đổi múi giờ ,London
datetime_London = datetime.now(tz_London) #trả về ngày  giờ hiên tại ở London
print('London:', datetime_London.strftime('%m/%D/%Y, %H:%M:%S')) #in ra màn hình ngày giợ hiện tại ở LOn_don theo str  
