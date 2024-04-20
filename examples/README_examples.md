## using HTTPie:

- http localhost:9000/echo/Sergio 
  #### responce: 
  HTTP/1.1 200 OK                         # Response HTTP version and status code indicating success
content-length: 16                      # Response header indicating the length of the content
content-type: application/json          # Response header indicating the type of content (JSON)
date: Sat, 20 Apr 2024 18:47:39 GMT     # Response header indicating the date and time of the response
server: uvicorn                         # Response header indicating the server software

"echoing Sergio"                        # Response body, containing the echoed string "Sergio"

- http -p HBh https://www.edu.goit.global/uk/calendar 
  #### responce: 
  GET /uk/calendar HTTP/1.1                    # Request method, path, and HTTP version
Accept: */*                                  # Request header indicating acceptable content types
Accept-Encoding: gzip, deflate               # Request header indicating acceptable content encodings
Connection: keep-alive                        # Request header indicating persistent connection
Host: www.edu.goit.global                    # Request header indicating the host
User-Agent: HTTPie/3.2.2                     # Request header indicating the user agent

HTTP/1.1 200 OK                               # Response HTTP version and status code
Access-Control-Allow-Origin: *                # Response header allowing cross-origin resource sharing
Age: 209625                                   # Response header indicating the age of the response
Cache-Control: public, max-age=0, must-revalidate  # Response header controlling caching behavior
Connection: keep-alive                        # Response header indicating persistent connection
Content-Disposition: inline; filename="calendar"  # Response header indicating how to handle the content
Content-Encoding: gzip                        # Response header indicating content encoding
Content-Type: text/html; charset=utf-8        # Response header indicating content type and charset
Date: Sat, 20 Apr 2024 18:44:19 GMT           # Response header indicating the date
Etag: W/"f17f1b8a7ef77fd7a8b41a3aeab0515d"    # Response header indicating entity tag for cache validation
Server: Vercel                                # Response header indicating the server
Strict-Transport-Security: max-age=63072000   # Response header indicating strict transport security

- http http://127.0.0.1:9000/explorer/
  #### responce:
  HTTP/1.1 200 OK                     # HTTP status code indicating success
  content-length: 23                  # Length of the response body in bytes
  content-type: application/json      # Type of content in the response (JSON)
  date: Sat, 20 Apr 2024 19:12:50 GMT # Date and time when the response was generated
  server: uvicorn                     # Server software used to handle the request

  "top explorer endpoint"             # Response body, indicating the top explorer endpoint


