
# CSMinds Web Server

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
