# prometheus-hands-on-json-exporter

Repository for the hands on Youtube video using Prometheus & the json_exporter.


```
pip install -r requirements.txt
```

Download and extract json_exporter from [here](https://github.com/prometheus-community/json_exporter/releases)

Start JSON server on `:9123`:

```
fastapi dev main.py --port 9213
```

Visit `http://127.0.0.1:9123` in a browser and validate that things are working

Start json_exporter:

```
./json_exporter --config.file=json-exporter-config.yaml
```

Visit `http://127.0.0.1:7979/probe?target=http://127.0.0.1:9123` to validate that the json_exporter is transforming the JSON endpoint into valid Prometheus metrics

Start Prometheus:

```
./prometheus --config.file=prometheus.yml
```

Go to `http://127.0.0.1:9090/targets` and validate that everything is working.

Go to `http://127.0.0.1:9090/graph` and chart `my_first_metric`
