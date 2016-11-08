### Plot Assignment(dlk253) LINK: https://github.com/xingezhong/PUI2016_dlk253/blob/master/HW7_dlk253/HW7_dlk253_viz.ipynb

## Clarity
### Good part: The plot contains labels both for x-axis and y-axis(with unit behind), straightforward legend explanation for the comparison between male and female, corresponding color distinction between male and female.
### Possible improving part: The currrent title is "CItibike Trip Durations < 20 minutes based on on Age and Gender for May 2016". Maybe we could rephrase this so as to make the information of label and title don't overlap and be more concise. How about change it as " Citybike Trip Duration's Comparison on Age and Gender"?

## Esthetic
### The whole page of the axis has been used wisely. And I noticed that you had used plt.xlim, plt.ylim, and plt.subplots to adjust your plot. I have to say this is very inspiring for me.

## Honesty
### In this part, I will draw some of my confusion and my true feelings towards your plot, just sharing with you. 
### First, when I saw your title, you limited the citibike trip duration to 20 mins, I may wonder why you did so, and I don't know the whole histogram of trip duration, so can this plot be representable enough to deliver the population to us?
### Second, please look at the lower part of your scatter plot, I can't differ the male dot and female dot, so this part of information may be not that clear and complementary. We visualise data in order to communicate and explore, right? You have used two indicator as comparison, one is age, the other is gender, what I expected is a story that you want to tell, so please explore deeper as you can !
### Third, the plot code "plt.plot(df.males.age,df.males.tripduration/60,'o', label='My Data', color='b', alpha = 0.5, linewidth=0.5)", I didn't see any influence of " label='My Data'" on your plot, maybe you could just delete it!


### If you have anything concerning the above, please be free to discuss with me at anytime.
