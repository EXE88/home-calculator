from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,permissions
from .models import Material
from bs4 import BeautifulSoup
import requests

class UpdatePrices(APIView):
    permission_classes = [permissions.IsAuthenticated]
    url = 'https://kargosha.com/material/'
    
    def get(self,request,category_id):
        print(self.finder(category_id))
        return Response('updated',status=status.HTTP_200_OK)
    
    def finder(self,category_id):
        url = f'{self.url}{category_id}'
        for i in range(100):
            if i == 0:
                continue
            page = f'{url}?page={i}'
            response = requests.get(page)
            page_content = BeautifulSoup(response.text,'html.parser')
            elements = page_content.find_all('div',class_="chakra-stack css-fa-iz2xud")
            if len(elements) == 0:
                return f'done! count of pages : {i-1}'
            self.updater(elements)
            
    def updater(self,elements):
        for element in elements:
            name = element.find_all('p', class_='truncate')[0].text.strip()
            group = element.find_all('p', class_='truncate')[1].text.strip()
            brand = element.find_all('p', class_='truncate')[2].text.strip()
            unit = element.find_all('p', class_='truncate')[3].text.strip()
            price = element.find_all('p', class_='truncate')[4].text.strip()
            description = element.find_all('p', class_='truncate')[5].text.strip()
            last_price = element.find_all('p', class_='truncate')[6].text.strip()
        
            name = name.replace("نام:","").strip()
            group = group.replace("دسته بندی:","").strip()
            brand = brand.replace("برند:","").strip()
            unit = unit.replace("واحد:","").strip()
            price = price.replace("قیمت:","").strip()
            description = description.replace("توضیحات:","").strip()
            last_price = last_price.replace("آخرین قیمت:","").strip()
        
            model , created = Material.objects.update_or_create(
                name=name,
                group=group,
                brand=brand,
                defaults={'unit':unit,'price':price,'description':description,'last_price':last_price}
            )
            
class CurrentPrice(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request):
        data = {
            "تجهیزات پایدارسازی گود":[],
            "لوازم و تجهیزات اجرایی":[],
            "مصالح پایه":[],
            "فلزات":[],
            "لوازم و تجهیزات اجرای سقف":[],
            "شیمی ساختمان":[],
            "عایق":[],
            "لوازم و تجهیزات الکتریکی":[],
            "لوازم و تجهیزات مکانیکی":[],
            "دیوارپوش":[],
            "کفپوش":[],
            "سرویس بهداشتی و شیرآلات":[],
            "درب و پنجره و یراق آلات":[],
            "تجهیزات آشپزخانه":[],
            "مصالح و تجهیزات محوطه و روف گاردن":[],
            "تزئینات داخلی":[],
            "هوشمند سازی":[],
            "استخر و جکوزی و سونا":[],
            "اسانسور و تجهیزات":[],
            "تجهیزات فنی و مهندسی":[],
            "قطعات پیش ساخته":[],
            "سنگ،سرامیک،کاشی":[]
        }
        for key in data.keys():
            for object in Material.objects.filter(group=key):
                data[key].append({
                                'name': object.name,
                                'group': object.group,
                                'brand': object.brand,
                                'unit': object.unit,
                                'price': object.price,
                                'description': object.description,
                                'last price': object.last_price
                                })
        return Response(data, status.HTTP_200_OK)