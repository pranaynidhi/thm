XXE-FTP
----

Basic FTP server to receive payloads from instances of XXE. This will record all data received and respond in a manner which ensures the client keeps sending data. This will keep listening until you shut it down, allowing for multiple XXE file retreivals via FTP. Java connections shouldn't hang connecting to this either.

Has a unique "uno port" option, where everything is served from one port. This means you can serve HTTP/HTTPS/FTP over a single port. When a connection is received, the server will work out which protocol was requested, and handle it accordingly. This is not flawless, but works in most cases.

For more info, see the blog-post: [https://staaldraad.github.io/2016/12/11/xxeftp/](https://staaldraad.github.io/2016/12/11/xxeftp/)

## Usage

Built for Linux, so use

```
./xxeserv -p 2121
```

There are multiple modes. The server can host both FTP and HTTP, thus making it capable of serving the DTD and receiving the FTP payload.

To start the web-server (off by default) use `-w`

```
./xxeserv -w
```

To change the web-port, use `-wp`.

To Change the FTP port, use `-p`.

The DTD is served out of the CWD by default. To change, use `-wd`.

To save the data received via FTP to file, use `-o filename`. The file will be created if it doesn't exist.

```
./xxeserv --help 
Usage of ./xxeserv:
  -o string
        File location to log to
  -p int
        Port to listen on (default 2121)
  -uno int
        Global port to listen on (default 5000)
  -w    Setup web-server for DTDs
  -wd string
        Folder to server DTD(s) from (default "./")
  -wp int
        Port to serve DTD on (default 2122)
  -wps int
        SSL Port to serve DTD on (default 2123)
```

## To build:

```
go build
```
