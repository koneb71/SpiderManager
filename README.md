# SpiderManager

[![Latest Version](http://img.shields.io/pypi/v/SpiderManager.svg)](https://pypi.python.org/pypi/SpiderManager)
[![Python Versions](http://img.shields.io/pypi/pyversions/SpiderManager.svg)](https://pypi.python.org/pypi/SpiderManager)
[![The MIT License](http://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/koneb71/SpiderManager/blob/master/LICENSE)
   
A scalable admin ui for spider service 

## Features

- Manage your spiders from a dashboard. Schedule them to run automatically
- With a single click deploy the scrapy project
- Show spider running stats
- Provide api


Current Support spider service
- [Scrapy](https://github.com/scrapy/scrapy) ( with [scrapyd](https://github.com/scrapy/scrapyd))

## Screenshot
![job dashboard](https://raw.githubusercontent.com/koneb71/SpiderManager/master/screenshot/screenshot_1.png)
![periodic job](https://raw.githubusercontent.com/koneb71/SpiderManager/master/screenshot/screenshot_2.png)
![running stats](https://raw.githubusercontent.com/koneb71/SpiderManager/master/screenshot/screenshot_3.png)

## Getting Started


### Installing


```
pip install spidermanager
```

### Deployment

``` 

spidermanager [options]

Options:

  -h, --help            show this help message and exit
  --host=HOST           host, default:0.0.0.0
  --port=PORT           port, default:5000
  --username=USERNAME   basic auth username ,default: admin
  --password=PASSWORD   basic auth password ,default: admin
  --type=SERVER_TYPE    access spider server type, default: scrapyd
  --server=SERVERS      servers, default: ['http://localhost:6800']
  --database-url=DATABASE_URL
                        SpiderKeeper metadata database default: sqlite:////home/souche/SpiderKeeper.db
  --no-auth             disable basic auth
  -v, --verbose         log level
  

example:

spiderkeeper --server=http://localhost:6800

```

## Usage

```
Visit: 

- web ui : http://localhost:5000

1. Create Project

2. Use [scrapyd-client](https://github.com/scrapy/scrapyd-client) to generate egg file 

   scrapyd-deploy --build-egg output.egg

2. upload egg file (make sure you started scrapyd server)

3. Done & Enjoy it

- api swagger: http://localhost:5000/api.html

```

## TODO
- [ ] Job dashboard support filter
- [x] User Authentication
- [ ] Collect & Show scrapy crawl stats
- [ ] Optimize load balancing

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/koneb71/SpiderKeeper/tags). 

## Authors

- *Initial work* - [DormyMo](https://github.com/DormyMo)
- *Continued* - [koneb71](https://github.com/koneb71)

See also the list of [contributors](https://github.com/koneb71/SpiderManager/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Contributing

Contributions are welcomed!
