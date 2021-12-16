# PYnema 

🎥 PYnema is a simple UDP server written in python, allows you to watch downloaded videos.
The default video you can watch is the first video on youtube called (Me at the zoo), you can choose between the SD and HD versions of this video

SD - Me_at_the_zoo.mp4

HD - Me_at_the_zooHD.mp4

Feel free to download any video and put it in the movies folder!

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install PYnema.

## Usage
```bash
BUFFOR_SIZE_DATA = 65507 - UDP max packet size to avoid this use TCP instead of UDP
```

```bash
host_ip_adress = ' ' - localhost by default(127.0.0.1)
```

```bash
host_port = 1337 - free PORT
```

```bash
avg_tmt = socket.getdefaulttimeout() - avarage default timeout
```

```bash
cv2.VideoCapture('movies\Me_at_the_zoo.mp4') - video u want to watch
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[GNU](https://choosealicense.com/licenses/gnu/)
