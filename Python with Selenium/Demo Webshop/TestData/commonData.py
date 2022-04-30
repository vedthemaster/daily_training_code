import openpyxl

class CommonData:
    book = openpyxl.load_workbook("C:\\Users\\vedpa\\OneDrive\\Desktop\\Training Folder\\Python with Selenium\\Demo Webshop\\commonData.xlsx")
    sheet = book.active
    ccNumber = sheet['A3'].value
    ccName =sheet['A2'].value
    ccMonth = sheet['A5'].value
    ccYear = sheet['A6'].value
    cvv = sheet['A4'].value
    ccType = sheet['A1'].value
    coupon1 = sheet['A8'].value
    coupon2 = sheet['A9'].value
    coupon3 = sheet['A10'].value
    coupon4 = sheet['A11'].value
    coupon5 = sheet['A12'].value
    
    def __init__(self,ccNumber,ccName,ccMonth,ccYear,cvv,ccType,coupon1,coupon2,coupon3,coupon4,coupon5):
        self.ccNumber = ccNumber
        self.ccName = ccName
        self.ccMonth = ccMonth
        self.ccYear = ccYear
        self.cvv = cvv
        self.ccType = ccType
        self.coupon1= coupon1
        self.coupon2= coupon2
        self.coupon3 = coupon3
        self.coupon4 = coupon4
        self.coupon5 = coupon5
        
# print(CommonData.coupon4)
        
        
    
    