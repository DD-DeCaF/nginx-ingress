# nginx-ingress

Modifications ot the NGINX ingress controller deployment. The full deplyoment follows the [official installation guide](https://kubernetes.github.io/ingress-nginx/deploy/).

* `mandatory.patch` contains the modifications to the current version
* `mandatory.yaml` contains the resulting configuration file

To compare with the newest version on github:

```bash
curl https://raw.githubusercontent.com/kubernetes/ingress-nginx/master/deploy/mandatory.yaml | diff -u - mandatory.yaml
```

To update, download the newest deployment configuration, apply the patch and commit the changes.

## Current changes

* Increase livenessProbe.initialDelaySeconds from 10 to 60 as controller startup currently exceeds 10 seconds
* Set guaranteed QoS class
