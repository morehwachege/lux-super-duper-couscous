from instascrape import *
acc = Profile('https://www.instagram.com/muriithigakuru_official/')
acc_post = Post('https://www.instagram.com/p/CQyM5ZWFALg/')
acc.scrape()
acc_post.scrape()
print(acc.followers)