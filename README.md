```shell
docker build . -t fetch-gpt2-models
docker run -v $PWD/checkpoint:/checkpoint fetch-gpt2-models
```
