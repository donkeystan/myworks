from django.db import models

# Create your models here.
class Uniform(models.Model):
    CustName = models.CharField(max_length=20, null=False)
    CustNo = models.CharField(max_length=20, blank=True, default='')
    OrgnizationName = models.CharField(max_length=50, blank=True, default='')
    Gender = models.CharField(max_length=2, default='M', null=False)
    CustPhone = models.CharField(max_length=50, blank=True, default='')
    CustEmail = models.EmailField(max_length=100, blank=True, default='')
    CustAddr = models.CharField(max_length=255,blank=True, default='')
    DateOfCreated = models.DateField(null=False)
    Hat = models.CharField(max_length=10, blank=True, default='')
    ShoulderWidth = models.CharField(max_length=10, blank=True, default='')
    SleeveLength = models.CharField(max_length=10, blank=True, default='')
    BackLength = models.CharField(max_length=10, blank=True, default='')
    CenterBack = models.CharField(max_length=10, blank=True, default='')
    ShirtLength = models.CharField(max_length=10, blank=True, default='')
    Collar = models.CharField(max_length=10, blank=True, default='')
    Chest = models.CharField(max_length=10, blank=True, default='')
    Waist = models.CharField(max_length=10, blank=True, default='')
    Seat = models.CharField(max_length=10, blank=True, default='')
    WaistBelt = models.CharField(max_length=10, blank=True, default='')
    Hip = models.CharField(max_length=10, blank=True, default='')
    Crotch = models.CharField(max_length=10, blank=True, default='')
    FrontCrotch = models.CharField(max_length=10, blank=True, default='')
    Thigh = models.CharField(max_length=10, blank=True, default='')
    PantsLength = models.CharField(max_length=10, blank=True, default='')
    SkirtLength = models.CharField(max_length=10, blank=True, default='')
    Remark = models.CharField(max_length=30, blank=True, default='')

    def __str__(self):
        return self.CustName

'''
資料庫Model

Mandatory Field
    姓名 (requuired)
    
Optional
    學號/員編
    團體/客戶名稱
    性別 (requuired)
    聯絡電話
    E-Mail
    地址

上衣
    頭圍 hat
    肩寬 shoulder_width
    袖長 sleeve_length
    背長 back_width
    背心長 center_back
    衣長 shirt_length
    領圍 collar
    上圍 chest
    腰圍 waist
    下圍 seat

褲/裙
    褲腰圍 waist_belt
    褲下圍 hip
    褲襠 crotch
    前襠 front_crotch
    大腿 thigh
    褲長 pants_length
    裙長 skirt_length
    備註 remark
'''


class perm():
    def permutaion(self, nums:list) -> list:
        def isSkip(path:list, curr_level:int) -> int:
            for i in range(curr_level+1):
                for j in range(i+1, curr_level+1):
                    if (path[i] == path[j]):
                        return 1
            return 0

        def permutaions(nums:list, path:list, level:int, result:list) -> list:
            if (level == len(nums)):
                result.append([ nums[idx] for idx in path ])
                return nums, path, result
            path[level] = 0
            while (path[level] < len(nums)):
                if (isSkip(path, level)):
                    path[level] += 1
                    continue
                permutaions(nums, path, level+1, result)
                path[level] += 1
            return nums, path, result

        result = []
        path = [ 0 for i in nums ]
        level = 0
        permutaions(nums, path, level, result)
        return result