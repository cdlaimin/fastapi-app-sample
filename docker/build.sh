set -e
image="hub.tess.io/altus_gont/topoanalysis"
timestamp=$(date +%Y%m%d%H%M%S)
#tag=$image:$timestamp
tag=$image:demo
docker build -t $tag .
docker push $tag

