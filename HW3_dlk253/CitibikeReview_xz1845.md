a.

The idea is that the ratio of male to female riders varies over the time of day. The null hypothesis is formulated as the ratio of female to male riders during the evening (say, 4 to 7 pm) is larger than the ratio of female to male riders in the morning (say, 7 to 10 am). The alternative hypothesis is complementary the null hypothesis, which is saying the ratio (female to male riders) during the evening is less than or equal to that of the morning's. The null and hypotheses are formulated correctly since they are mathematically measurable and comparable, and they are multually exclusive. However, it will be a good idea to represent the hypotheses in the form of mathematical equations (H0 = ... ; H1 = ...). And significane level should be given.

b.

The data supports the project. The author used the start time data of a bike trip as the time of using bike. The data was well-processed with changing data formats (from string to datetime and to numeric for the starting time of rides). And the data was subsetted for the hour intervals of interest. In addition, the author may want to normalize the data for better comparison.

c. Chose an appropriate test to test H0 given the type of data, and the question asked. You can refer to the flowchart of statistical tests for this in the slides, or to the CSU cheat-sheet here, of Statistics in a Nutshell.

Two methods may be approperiate. First, a Pearson's chi-square test for independence can be conducted to investigate if the number of female and male riders is independent of time. Since the null hypothesis can be further elaborated as whether there will be a signficant change in terms of the female to male ratio subject to the different time periods, it is possible to construct a contigency table with rows of time intervals (say, 7-10AM, 11-2PM, ...) and columns of number of female and male riders. Second, one-way ANOVA may be feasible for this study to compute the F ratio between morning and evening groups to see whether there is significant differences.


