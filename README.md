Khaliqgant.com Static Site
=========

# Technology
* Built using [Hugo](https://gohugo.io/documentation/) and using the [Codex theme](https://themes.gohugo.io/hugo-theme-codex/)

# Deployment
* Deployments are triggered to my Kubernetes cluster using Github actions
* Hugo builds are done by using this Docker build: https://github.com/klakegg/docker-hugo
* [Configuration](https://github.com/klakegg/docker-hugo#configuration) environment variables:
```
HUGO_BIND - Bind address for server. Default: 0.0.0.0
HUGO_CACHEDIR - Cache directory for modules. Default: /tmp
HUGO_DESTINATION - Location of output folder. Default: public
HUGO_PANDOC - Pandoc command to be triggered. Default: pandoc-default
HUGO_ENV - Selecting environment ("DEV"/"production"). Default: DEV
HUGO_VERSION - Version of Hugo to use. Requires images for Hugo 0.71.1 or newer. Default: blank
```
* Using [docker-nginx-certbot](https://github.com/staticfloat/docker-nginx-certbot) for
SSL cert renewal

# Writing A New Blog Post
```
./blog.sh my-new-post
```
