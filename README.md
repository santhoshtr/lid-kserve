# Language identification service

## Usage

Build the docker image

```bash
docker build -t lidkserve -f Dockerfile .
```

Run it

````bash
docker run --rm -p 8080:8080 -v `pwd`/models:/mnt/models lidkserve:latest
```

Test locally:

```bash
curl localhost:8181/v1/models/lid-model:predict -d @./sample.json
```
