
# CSMinds Web Server

[![pipeline status](https://gitlab.cs.nuim.ie/ehegarty/cs-minds/badges/master/pipeline.svg)](https://gitlab.cs.nuim.ie/ehegarty/cs-minds/commits/master)

## Using Docker on dev machine
### Building Docker image
To generate a Docker image containing installation of pelican issue following
command:
```
docker build -t pelican .
```

### (Re)building the site
Running following command will (re)build the site
```
docker run --rm -ti -v $(pwd):/workdir pelican
```

### Previewing the site
Start the docker command in preview mode:
```
docker run --rm -ti -v $(pwd):/workdir -P pelican serve-global PORT=8000
```

Open new terminal, and run following command to find out on on which port of
the host interface the site has been published:
```
docker ps
```

In the example below the web site will be accessible on localhost:32773.

```
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                     NAMES
61c76cee5cf6        pelican             "/usr/bin/make serve…"   5 seconds ago       Up 5 seconds        0.0.0.0:32773->8000/tcp   happy_montalcini
```
