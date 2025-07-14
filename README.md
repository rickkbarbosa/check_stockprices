# check_stockprices
Tracks Stock Market Prices (Ações) 

Uses https://fundamentus.com.br API to collects Stock prices. 
Build and launch an sidecar container with Fundamentus API  results in (http://your-zabbix-server:5000), and use this gathered data to perform fundamentalist analysis for Stock Market.

Additionally, contains a Zabbix 7.0 template to stores collected data.

HOW TO USE THIS REPOSITORY
==========================

Clone the repo
```
git pull git@github.com:rickkbarbosa/check_stockprices.git
git submodule update --init --recursive
./start_fundamentus.sh

```


IN ZABBIX
=========

- Import Zabbix template to your zabbix server
- Attach the template to a host
- Set the variable `{$STOCK_BVMF_NAMES}` with te stocks you'd like to track


Reference Guide
===============

* [FUNDAMENTUS by @Phoemur](https://github.com/phoemur/fundamentus)