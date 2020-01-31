# Coronavirus-Estimation
Estimate the development tendency of 2019-nCoV
A Simple Model for Novel Coronavirus 2020

大学算法课和小学奥数中有这样一道经典题
有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？ 
这道题表现的本质就是斐波那契数列：
f(n)=f(n-1)+f(n-2) (当前项等于前两项之和)。 
这样1到12月小兔子分别有1,1,2,3,5,8,13,21,34,55,89,144。 哇！到了12月，你拥有了144对小兔子，可以天天吃野味兔头。可是野味不能吃，因为1月有了新型非典型肺炎。
让我们改造上面这个小学题“
有个新型传染病，1号开始有41个人，染病的人从第3天可以开始传播，每天传播k个人，但是第14天这个染病的人被治愈，那么斐波那契数列变为：
f(n)=f(n-1)+k*f(n-3)-f(n-14) 。
其中k就是传播系数，我们命名为14天治愈模型，让我们大致令k=0.33到0.36，可以理解为每天大致传染0.33个人，即3天传染1个人。算算看
![Image text](https://github.com/JunjieZhouwust/Coronavirus-Estimation/tree/master/images/image1.png)

好吓人，如果k=0.36，就能传播17500人。
  不要担心，我们祖国采取了封城模式，1月24号左右，各地限制了人流。我们可以继续改造这个模型，当n>24，传播系数k=0.7*k，每天衰减为原先的0.7倍。这样有了14天封城模型：
  
![Image text](https://github.com/JunjieZhouwust/Coronavirus-Estimation/tree/master/images/image2.png)

我们对比一下，人数降低了许多不是，所以不要抱怨封城，数据分析告诉我们，此举措能大大降低传播的人数。
可是，还不对啊，卫健委数据曲线超过了模型曲线包围线。嗯！这一定是传播系数不对，调大一些，改为0.34-0.4，见下图

![Image text](https://github.com/JunjieZhouwust/Coronavirus-Estimation/tree/master/images/image3.png)
 
看来封城模型能在传播系数为0.4时，大致有7000人（看趋势这个传播系数还有点危险），但是如果不封城呢，数据就飞了（见14天治愈模型）。

1.0版更新：
数据已经明显分化，目前分为武汉，外地（湖北除武汉），外省（全国除湖北）（用红绿蓝3个虚线） （1）武汉（采用26日治愈+24号封城模型）（2）外地和外省（采用22日治愈+27号封城模型）。细看，外地与外省两个曲线高度相似，但是外地滞后一个节拍。

![Image text](https://github.com/JunjieZhouwust/Coronavirus-Estimation/tree/master/images/image4.png)
