---
title: "My Personal Finance App"
date: 2016-03-13T15:06:53+02:00
slug: ""
description: ""
keywords: []
tags: ["finance", "personal-finance"]
math: false
toc: false
---

The past few months I’ve been building an app to help manage my personal finances. “Why?” You might ask. First, let me say that I consider myself a Mint.com power user.&nbsp;
![image](https://64.media.tumblr.com/f64f5e5603f240bf6f181bf011d7647c/tumblr_inline_nrlyaz2EuD1r18ptj_540.png)

I carefully manage my budget, tweaking every month or so and manage my goals like a hawk. I auto tag and manually tag my transactions and generally check Mint at least once a day. However, ever since 2009 I've also kept a running log of bills to pay and kept careful track of how much cash I would have on hand after getting paid.&nbsp;

Back in the dark ages of 2009 I kept my finances in a small book and wrote out my expenses out by hand (!) and checked off when I paid it.&nbsp;
![image](https://64.media.tumblr.com/37bd06489d39d73b1b2abd71c277ceff/tumblr_inline_nrlyv9LQj51r18ptj_540.png)

I wish I could get back to the days of $775 rent!

I have quite a few credit cards and so my main reason for keeping track of things this way was to see what my statement balance is record it, and make sure I have enough to pay that off and to pay it off on time. When I did pay it, I would mark it off and move on. At the end of the month, I would take a quick glance at all my bills and would know without a doubt that everything was paid off. I would also be sure that I wouldn’t overdraw my account because I knew when certain bills were getting paid etc.

About a year ago I wised up and stopping writing things by hand and started recording all that info plus some notes and income calculations in a text document. I stored those notes on dropbox so I could access and reference remotely. Even though this system worked out quite nicely I soon grew tired of using this as well. It was cumbersome to copy over the same data all the time and do the calculations by hand. I decided to set out to build a simple app to manage all of these things I had been tracking by hand for all these years.

I knew what my fixed costs would be each month like rent, student loan, and how much I wanted to save. I also knew what my income would be each month. WIth these things in mind I set out to map out some json documents basically recreating my dropbox documents into json.&nbsp;

You might be wondering why I would need an app or dropbox or anything to manage my bill paying in the first place. I pretty much pay for everything using my credit cards, and I also have ~10 credit cards which I juggle what I use based on what gives the highest cash back award. Since there is some float on how much I pay vs. how much I actually owe I wanted the statement balance each month and keep track of what was paid and what was not at the end of the month. &nbsp;I also found it useful to have some general notes and things to remember about my various accounts, and about my financial situation in general.

So with this app I built out what I wanted it to do:

*   Keep track of multiple credit cards and know when it is paid

*   Know how much I owed total at the end of each month

*   Keep track of how much debt I have on my accounts
*   Map my fixed costs vs. my paycheck
*   Have some notes that I can keep for each month
*   Forecast spending and available money months ahead

You might be wondering at this point why I built this app when there are things like [mint](https://www.mint.com/) and also [mint bills](https://bills.mint.com/jsp/userLogin.jsp)&nbsp;([article on mint bills](http://lifehacker.com/how-i-used-mint-bills-to-finally-simplify-my-bill-payme-1717972364)). The main thing I wanted in addition to these things were custom notes and also the ability to forecast my spending and know how much I would probably be spending, and more importantly how much I could save moving forward.

I really enjoyed building something that I get so much use out of and hope others can get some use out of it as well which is why I’m open sourcing the app for others to potentially use. The Github repository can be found here:&nbsp;[https://github.com/khaliqgant/finance-app](https://github.com/khaliqgant/finance-app). Any feedback / pull requests are more than welcome!
