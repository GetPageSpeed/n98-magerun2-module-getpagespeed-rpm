# Build RPMS for [GetPageSpeed n98-magerun2 module](https://github.com/GetPageSpeed/n98-magerun2-module-getpagespeed).

[![CircleCI](https://circleci.com/gh/GetPageSpeed/n98-magerun2-module-getpagespeed-rpm/tree/master.svg?style=svg)](https://circleci.com/gh/GetPageSpeed/n98-magerun2-module-getpagespeed-rpm/tree/master)

``` 
sudo yum install https://extras.getpagespeed.com/release-el$(rpm -E %{rhel})-latest.rpm
sudo yum install n98-magerun2-module-getpagespeed
cd /path/to/magento2
# Get tuned Varnish parameters specifc to your Magento 2 instance
n98-magerun2 varnish:tuned 
# Get active themes
n98-magerun2 dev:theme:active
```