## Use Swagger code generator

```bash
docker run -d -e GENERATOR_HOST=http://localhost -p 80:8080 swaggerapi/swagger-generator
```

```bash
## without options and faulty swagger spec..
# curl -sX POST --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{
#     "swaggerUrl": "https://portal.victorops.com/public/api-docs/victorops-api-v1.yaml"
# }' 'http://localhost/api/gen/clients/python' | jq .

## with options and fixed swagger spec
curl -sX POST --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{
    "options": {
      "packageName":"victorops_client",
      "packageVersion":"1.0.0"
    },
    "swaggerUrl": "https://gist.github.com/so0k/70fe2239e639476d4f990b92e7f29191/raw/66f9fc360fa02c8db53c280b3b84ea4598b0f956/victorops.yaml"
}' 'http://localhost/api/gen/clients/python' | jq .
```

Download the python-client:
```bash
curl -sLo python-victorops.zip http://localhost/api/gen/download/<uid>
unzip python-victorops.zip
rm python-victorops.zip
```

Build base image:
```bash
cp Dockerfile python-client/
docker build -t victorops python-client/
```

Build sample image
```bash
docker build -t vo_client sample/
```

Get a container with a python shell and the project dependencies:
```bash
docker run -it --rm -v $PWD/sample:/usr/src/app vo_client /bin/sh
```

Test sample script
```bash
. .env
python script.py
```