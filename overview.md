![PyPI](https://img.shields.io/pypi/v/cgpt)

# Overview

## Description

- `cgpt` is a REPL that allows you to use AI directly in your favorite Terminal.
- `cgpt` is based on [CLICK](https://github.com/pallets/click) for creating beautiful command line interfaces in a composable way.

##  Prerequisities

- python >=3.7
- openai API KEY :
  You need to register on openai to receive your own api key , here : [api_key](https://platform.openai.com/account/api-keys).

##  Install from pypi

You can install the latest version from pypi.

```
pip install cgpt
```

## Run

We've kept it super simple. Just use the command below, and you're in the conversational loop 🚀.

```
cgpt
```
![cgpt](https://i.imgflip.com/8hdiuv.jpg)


## Use it inside a local network

You can use cgpt inside a LAN thanks to the command : `cgpt --lan` .

- You just need one Host (`connected to internet`) to be the server.
- Other Hosts (`not connected to internet`) can ALWAYS use Chat GPT as `client`.

NOTES :

- For now , a server must be launched inside a `Linux` computer . If the server is inside `Windows` : the address is sometimes wrong (to be fixed in the next version).

- Also , make sure that your `/etc/hosts` is configured correctly like :

```
127.0.0.1	localhost
127.0.1.1	your-hostanme
```

- A `client` can also use his own api_key on future releases.

- This tool is still using `gpt-3.5-turbo` , `gpt-4` and `gpt-4-turbo` are on the way 😉.

###  Run with docker 

Pull the image 
```
# docker pull ainayves/cgpt:latest
```

Run the docker image by using your openai api key :

```
# docker run -e OPENAI_API_KEY="yourapikey" -i -t ainayves/cgpt
```

