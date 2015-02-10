Title: Hosting on Amazon S3
Date: 2015-02-06 21:00
Tags: amazon, S3, route 53
Category: Web Dev
Slug: hosting-on-amazon-s3
Authors: Matthew Power
Summary: How I hosted this blog on Amazon S3.

Amazon has an [excellent guide](http://docs.aws.amazon.com/gettingstarted/latest/swh/awsgsg-swh.pdf) for hosting a static website on S3. It covers the whole process from setting up the buckets and uploading files, setting up DNS rules to redirect visitors to the buckets and setting up a CDN using Cloudfront. I didn't go as far as setting up a CDN, but it's reassuring to know the option is there, and isn't much added effort beyond what I've already done.

For registering my domain, I recieved recommendations for Gandi and Namecheap, and ended up going with Gandi, if only for their motto ("No Bullshit"), and the option of a cheap SSL certificate if I decide I want to use it.

In my mind, one key benefit with using S3 for hosting this static website, is that there was no server configuration at all. I only had to flick a switch to turn the S3 bucket into "webserver mode", and point it to my index.html. Amazon recommend their Route 53 DNS, which has no immediate benefit to me right now, but if I put any future projects on AWS, it has features for health-checking and failover.

Like most of Amazon Web Services, you are charged on the basis of what you use, I've had no upfront cost associated with my project, except registering my domain. Amazon clearly go to a great effort to make the barrier of entry as low as possible.

I didn't actually upload my files to S3 through the web interface. [s3cmd](http://s3tools.org/s3cmd) is a command line tool that allows you to upload files very easily. The advantage of this is I that I can make simple fabric or Make scripts to automate the the process of generating the blog with production settings and uploading to S3. Pelican and s3cmd only require a few commands, but it's nice to be able to reduce that further, and if I needed to add more steps before I could publish, then a script handles this better than an increasing list of commands to run in order.
