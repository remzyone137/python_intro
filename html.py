from os import walk

_, _, filenames = next(walk(mypath))    #my path

html = '''
<html>
   <head>
      <title></title> 

      <style>
         img  {
             width: 200px;
             height: 150px;
             object-fit: cover;
         }
   </head>
   <body>
     <hl>Meine Bildergalerie</hl>
     <img src='ordner/img.jpg'>              
   </body>
</html>      
'''

for f in filenames:
    html += '<img src="img/0.jpg">'          #'' + f + ''

html += '''






'''



print(html)

#Write HTML String to file.html
with open('index.html', 'w') as file:
    file.write(html)