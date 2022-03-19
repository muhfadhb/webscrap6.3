# Import package request dan BeautifulSoup
import requests
from bs4 import BeautifulSoup
import json

# Request to website
page = requests.get("https://republika.co.id/")

# Extract content to BeautifulSoup object
obj = BeautifulSoup(page.text,'html.parser');

print ("\nMenampilkan semua teks headline")
print ("===================================")
for publish in obj.find_all('div',class_='conten1'):
    print(publish.find('h2').text)


print('\nMenampilkan waktu publish')
print("===================================")
for publish in obj.find_all('div',class_='date'):
        print(publish.text)


print('\nMenampilkan kategori')
print("===================================")
for publish in obj.find_all('div',class_='teaser_conten1_center'):
        print(publish.find('a').text)

# Date
import datetime
now = datetime.datetime.now()
print('\nMenampilkan waktu scrapping')
print("===================================")
for publish in obj.find_all('div',class_='teaser_conten1_center'):
        print (now.strftime("%Y-%m-%d %H:%M:%S"))

# Deklarasi list kosong
data=[]
# Lokasi file json
f=open(r'D:\1 Kuliyah\SEM 2\Proyek I Pengembangan Perangkat Lunak Desktop\Code folder\headline1.json','w')
for publish in obj.find_all('div',class_='conten1'):
    # append headline ke variable data
    data.append({"judul":publish.find('h2').text,"kategori":publish.find('a').text,"waktu_publish":publish.find('div',class_='date').text,"waktu_scraping":now.strftime("%Y-%m-%d %H:%M:%S")})
# dump list dictionary menjadi json
jdumps=json.dumps(data, indent = 2)
f.writelines(jdumps)
f.close()

<section class="u-clearfix u-palette-3-dark-3 u-section-7" id="sec-1604">
      <div class="u-clearfix u-sheet u-sheet-1">
        <br><br><br><br>
      <script src="https://code.jquery.com/jquery-3.5.1.js%22%3E</script>
      <style>h1 {text-align: center;}
        table {align: center;}
        table {
            font-family: arial, sans-serif;
            border-collapse: collapse;
            width: 100%;
          }

          td, th {
            border: 3px solid #f1c50e;
            text-align: left;
            padding: 8px;
          }
          tr:nth-child(odd) {
            background-color: #333333;
          }
          tr:nth-child(even) {
            background-color: #333333;
          }

      </style>

      <h1>Artikel republika.co.id Terkini</h1>
      <div id="publish_json"></div>
        <script type="text/javascript">
          $(function(){
              //mengambil data dari file json
              $.get('publish.json',function(obj){
                  var str = "<table border=1>";
                  str +="<tr><td>No</td><td class='tables'>Judul Artikel</td><td class='tables'>Kategori</td><td class='tables'>Waktu Publish</td><td class='tables'>Waktu Scrapping</td></tr>";
                  $.each(obj,function(n,data){
                      str +="<tr><td>" + (n+1) + "</td>";
                      str +="<td>" + data.judul + "</td>";
                      str +="<td class='tables'>" + data.kategori + "</td>";
                      str +="<td class='tables'>" + data.waktu_publish + "</td>";
                      str +="<td class='tables'>" + data.waktu_scraping + "</td></tr>";
                  });
                  str +="</table>";
                  $('#publish_json').html(str);
              });
          });
      </script>

      <br>
      <br>
      </div>
    </section>
