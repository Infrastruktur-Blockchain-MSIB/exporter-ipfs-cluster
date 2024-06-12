FROM debian:latest

LABEL maintainer="ghilmanaji2512@gmail.com"

RUN apt-get update && apt-get upgrade -y && apt-get install -y python3 curl python3-prometheus-client python3-regex&& apt-get install wget


RUN wget https://dist.ipfs.tech/ipfs-cluster-service/v1.1.0/ipfs-cluster-service_v1.1.0_linux-amd64.tar.gz
RUN wget https://dist.ipfs.tech/ipfs-cluster-ctl/v1.1.0/ipfs-cluster-ctl_v1.1.0_linux-amd64.tar.gz
RUN tar -xvf ipfs-cluster-service_v1.1.0_linux-amd64.tar.gz
RUN tar -xvf ipfs-cluster-ctl_v1.1.0_linux-amd64.tar.gz
RUN cp ipfs-cluster-ctl/ipfs-cluster-ctl /usr/local/bin/ipfs-cluster-ctl
RUN cp ipfs-cluster-service/ipfs-cluster-service /usr/local/bin/ipfs-cluster-service
RUN rm -r ipfs-cluster-ctl
RUN rm -r ipfs-cluster-service
RUN rm -r ipfs-cluster-service_v1.1.0_linux-amd64.tar.gz
RUN rm -r ipfs-cluster-ctl_v1.1.0_linux-amd64.tar.gz
COPY entry.sh /usr/local/bin/entry.sh
RUN chmod +x /usr/local/bin/entry.sh
ENTRYPOINT ["entry.sh"]
