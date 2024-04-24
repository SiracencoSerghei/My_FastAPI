export PYTHONPATH=/home/Desktop/My_FastAPI/examples:$PYTHONPATH



## using HTTPie:

- http localhost:9000/echo/Sergio 
  <em>............-- Response for http localhost:9000/echo/Sergio -</em><br>
  <strong>*responce:*</strong>

  HTTP/1.1 200 OK                         
  <em>............-- Response HTTP version and status code indicating success -</em><br>
  *content-length: 16*                      
  <em>............-- Response header indicating the length of the content -</em><br>
  *content-type: application/json*          
  <em>............-- Response header indicating the type of content (JSON) -</em><br>
  *date: Sat, 20 Apr 2024 18:47:39 GMT*     
  <em>............-- Response header indicating the date and time of the response -</em><br>
  *server: uvicorn*                         
  <em>............-- Response header indicating the server software -</em><br>

  "echoing Sergio"                        
  <em>............-- Response body, containing the echoed string "Sergio" -</em><br>

- http -p HBh https://www.edu.goit.global/uk/calendar 
  <em>............-- Response for http -p HBh https://www.edu.goit.global/uk/calendar -</em><br>
  <strong>*responce:*</strong>

  GET /uk/calendar HTTP/1.1                    
  <em>............-- Request method, path, and HTTP version -</em><br>
  *Accept: */*                                  
  <em>............-- Request header indicating acceptable content types -</em><br>
  *Accept-Encoding: gzip, deflate*               
  <em>............-- Request header indicating acceptable content encodings -</em><br>
  *Connection: keep-alive*                        
  <em>............-- Request header indicating persistent connection -</em><br>
  *Host: www.edu.goit.global*                    
  <em>............-- Request header indicating the host -</em><br>
  *User-Agent: HTTPie/3.2.2*                     
  <em>............-- Request header indicating the user agent -</em><br>

  HTTP/1.1 200 OK                               
  <em>............-- Response HTTP version and status code -</em><br>
  *Access-Control-Allow-Origin: *                
  <em>............-- Response header allowing cross-origin resource sharing -</em><br>
  *Age: 209625*                                   
  <em>............-- Response header indicating the age of the response -</em><br>
  *Cache-Control: public, max-age=0, must-revalidate*  
  <em>............-- Response header controlling caching behavior -</em><br>
  *Connection: keep-alive*                        
  <em>............-- Response header indicating persistent connection -</em><br>
  *Content-Disposition: inline; filename="calendar"*  
  <em>............-- Response header indicating how to handle the content -</em><br>
  *Content-Encoding: gzip*                        
  <em>............-- Response header indicating content encoding -</em><br>
  *Content-Type: text/html; charset=utf-8*        
  <em>............-- Response header indicating content type and charset -</em><br>
  *Date: Sat, 20 Apr 2024 18:44:19 GMT*           
  <em>............-- Response header indicating the date -</em><br>
  *Etag: W/"f17f1b8a7ef77fd7a8b41a3aeab0515d"*    
  <em>............-- Response header indicating entity tag for cache validation -</em><br>
  *Server: Vercel*                                
  <em>............-- Response header indicating the server -</em><br>
  *Strict-Transport-Security: max-age=63072000*   
  <em>............-- Response header indicating strict transport security -</em><br>

- http http://127.0.0.1:9000/explorer/
  <em>............-- Response for http http://127.0.0.1:9000/explorer/ -</em><br>
  <strong>*responce:*</strong>

  HTTP/1.1 200 OK                     
  <em>............-- HTTP status code indicating success -</em><br>
  *content-length: 23*                  
  <em>............-- Length of the response body in bytes -</em><br>
  *content-type: application/json*      
  <em>............-- Type of content in the response (JSON) -</em><br>
  *date: Sat, 20 Apr 2024 19:12:50 GMT* 
  <em>............-- Date and time when the response was generated -</em><br>
  *server: uvicorn*        ==================================
(my-fastapi-py3.11) (base) ➜  My_FastAPI git:(master) ✗              
  <em>............-- Server software used to handle the request -</em><br>

  "top explorer endpoint"             
  <em>............-- Response body, indicating the top explorer endpoint -</em><br>

- http -b http://127.0.0.1:9000/explorer/
<!-- When you use -b, only the response body will be displayed, and the headers will be omitted. -->

- http -b http://127.0.0.1:9000/explorer/"Noah Weiser"

- http PUT localhost:9000/explorer/ name="Noah Weiser" country="DE" description="Myopic machete man"
- http PATCH localhost:9000/explorer/ name="Noah Weiser" country="DE" description="Myopic machete man"
- http -b DELETE localhost:9000/explorer/Edmund%20Hillary 
- http -b DELETE localhost:9000/explorer/"Edmund Hillary"
  

- http -b http://127.0.0.1:9000/creature/
- http -b http://127.0.0.1:9000/creature/"Yeti"
- http PUT localhost:9000/creature/ name="Yeti" aka="Abominable Snowman" country="CN" area="Himalayas" description="Hirsute Himalayan"
- http PATCH localhost:9000/creature/  name="Yeti" aka="Abominable Snowman" country="CN" area="Himalayas" description="Hirsute Himalayan"
- http -b DELETE localhost:9000/creature/"Yeti"


 http localhost:9000/explorer/
 http localhost:9000/explorer

 http localhost:9000/explorer/"Beau Buffette" 


 http post localhost:9000/explorer name="Beau Buffette",contry="US", description=""

## pytest:

- pytest -v test/unit/service/test_creature.py
- pytest -v test/unit/service/test_explorer.py

