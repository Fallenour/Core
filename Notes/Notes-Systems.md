# Hard Drive Performance Testing:

https://danielmalmer.medium.com/hard-drive-metrics-that-matter-439d07cd6306

# Types of Drives and their impact on performance

https://techlog360.com/best-ssd-what-is-slc-mlc-tlc-qlc-and-plc/


# Commands to test performance
dd if=/dev/zero of=dd.out bs=512 count=1000000

dd if=dd.out of=/dev/null bs=512