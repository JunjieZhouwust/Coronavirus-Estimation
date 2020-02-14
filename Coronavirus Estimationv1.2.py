import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用于正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

L = 60  # 1月1日开始计算，总共预测50天
Today = 44  # 今天第44天
dti = pd.date_range('20200101', periods=L, freq='1D', name='dt')
pydate_array = dti.to_pydatetime()
date_only_array = np.vectorize(lambda s: s.strftime('%m/%d'))(pydate_array)
date_only_series = pd.Series(date_only_array)


def dShift(lst, k):
    return lst[k:] + lst[:k]


def dPPNum(n, k, rate, ShutDay=24, StartDay=16, StartNum=100):
    dFun = lambda v, n, k: v[n - 1] + k * (v[n - 3] - v[n - 9]) - v[0]

    Y = [0 for i in range(L)]
    lst = [0 for i in range(n)]
    lst[-1] = StartNum
    for i, y in enumerate(Y):
        y = dFun(lst, n, k)
        y = np.maximum(y, 0)
        if i > ShutDay:  # 封城在1月24日左右，传播率降低，假定每天以rate系数衰减
            k = k * rate
            k = np.fmax(k, 0.15)

        if i > StartDay:  # 默认从1月1号开始
            lst = dShift(lst, 1)
            lst[-1] = y
            Y[i] = y
    return Y


def dPPNum0():
    Y00 = [0 for i in range(Today)]  # 国家
    Y00[20] = 291  # 国家卫健委
    Y00[21] = 440  # 国家卫健委
    Y00[22] = 571  # 国家卫健委
    Y00[23] = 830  # 国家卫健委
    Y00[24] = 1287  # 国家卫健委
    Y00[25] = 1975  # 国家卫健委
    Y00[26] = 2744  # 国家卫健委
    Y00[27] = 4515  # 国家卫健委
    Y00[28] = 5974  # 国家卫健委
    Y00[29] = 7711  # 国家卫健委
    Y00[30] = 9692  # 国家卫健委
    Y00[31] = 11791  # 国家卫健委
    Y00[32] = 14380  # 国家卫健委
    Y00[33] = 17205  # 国家卫健委
    Y00[34] = 20438  # 国家卫健委
    Y00[35] = 24324  # 国家卫健委
    Y00[36] = 28018  # 国家卫健委
    Y00[37] = 31161  # 国家卫健委
    Y00[38] = 34546  # 国家卫健委
    Y00[39] = 37198  # 国家卫健委
    Y00[40] = 40171  # 国家卫健委
    Y00[41] = 42638  # 国家卫健委
    Y00[42] = 59804  # 国家卫健委
    Y00[43] = 63851  # 国家卫健委

    Y01 = [0 for i in range(Today)]  # 湖北
    Y01[20] = 270  # 湖北卫健委
    Y01[21] = 375  # 湖北卫健委
    Y01[22] = 444  # 湖北卫健委
    Y01[23] = 549  # 湖北卫健委
    Y01[24] = 729  # 湖北卫健委
    Y01[25] = 1052  # 湖北卫健委
    Y01[26] = 1423  # 湖北卫健委
    Y01[27] = 2714  # 湖北卫健委
    Y01[28] = 3554  # 湖北卫健委
    Y01[29] = 4586  # 湖北卫健委
    Y01[30] = 5806  # 湖北卫健委
    Y01[31] = 7153  # 湖北卫健委
    Y01[32] = 9074  # 湖北卫健委
    Y01[33] = 11177  # 湖北卫健委
    Y01[34] = 13522  # 湖北卫健委
    Y01[35] = 16678  # 湖北卫健委
    Y01[36] = 19665  # 湖北卫健委
    Y01[37] = 22112  # 湖北卫健委
    Y01[38] = 24953  # 湖北卫健委
    Y01[39] = 27100  # 湖北卫健委
    Y01[40] = 29631  # 湖北卫健委
    Y01[41] = 31728  # 湖北卫健委
    Y01[42] = 48206  # 湖北卫健委
    Y01[43] = 51986  # 湖北卫健委

    Y02 = [0 for i in range(Today)]  # 武汉
    Y02[20] = 258  # 武汉卫健委
    Y02[21] = 363  # 武汉卫健委
    Y02[22] = 425  # 武汉卫健委
    Y02[23] = 495  # 武汉卫健委
    Y02[24] = 572  # 武汉卫健委
    Y02[25] = 618  # 武汉卫健委
    Y02[26] = 698  # 武汉卫健委
    Y02[27] = 1590  # 武汉卫健委
    Y02[28] = 1905  # 武汉卫健委
    Y02[29] = 2261  # 武汉卫健委
    Y02[30] = 2639  # 武汉卫健委
    Y02[31] = 3215  # 武汉卫健委
    Y02[32] = 4109  # 武汉卫健委
    Y02[33] = 5142  # 武汉卫健委
    Y02[34] = 6384  # 武汉卫健委
    Y02[35] = 8351  # 武汉卫健委
    Y02[36] = 10117  # 武汉卫健委
    Y02[37] = 11618  # 武汉卫健委
    Y02[38] = 13603  # 武汉卫健委
    Y02[39] = 14982  # 武汉卫健委
    Y02[40] = 16902  # 武汉卫健委
    Y02[41] = 18454  # 武汉卫健委
    Y02[42] = 32994  # 武汉卫健委
    Y02[43] = 35991  # 武汉卫健委

    Y03 = [Y00[i] - Y01[i] for i in range(Today)]  # 外省=国家-湖北
    Y04 = [Y01[i] - Y02[i] for i in range(Today)]  # 外地=湖北-武汉
    Y05 = [Y03[i] / (500 * 0.35) * (1400) for i in range(Today)]  # 外省-反推
    Y06 = [Y04[i] / (500 * 0.65) * (1400) for i in range(Today)]  # 外地-反推
    return Y00, Y01, Y02, Y03, Y04, Y05, Y06


def dDrawPlot(N, rate, ShutDay, StartDay, StartNum):
    K = 0.70
    StartDay1 = StartDay + 7  # 外省滞后7天
    StartDay2 = StartDay + 7  # 外地滞后7天
    StartDay3 = StartDay  # 开始传播
    ShutDay1 = ShutDay + 3
    ShutDay2 = ShutDay + 4
    ShutDay3 = ShutDay  # 武汉封城日
    P00, P01, P02, P03, P04, P05, P06 = dPPNum0()
    P1 = dPPNum(N, K, rate, ShutDay1, StartDay1, StartNum)
    P2 = dPPNum(N + 4, K, rate, ShutDay2, StartDay2, StartNum)
    P3 = dPPNum(N + 6, K, rate, ShutDay3, StartDay3, StartNum)
    P0 = [P1[i] + P2[i] + P3[i] for i in range(L)]

    plt.plot(P00, "c-o", lw=2, label="@全国数据(%s至%s)" % (date_only_series[20], date_only_series[Today - 1]))
    plt.plot(P03, "r-", lw=2, label="@外省数据(全国减湖北)")
    plt.plot(P04, "g-", lw=2, label="@外地数据(湖北减武汉)")
    plt.plot(P02, "b-", lw=2, label="@武汉数据")

    plt.plot(P0, "c--", lw=1, label="@全国估计: 外省+外地+武汉")
    plt.plot(P1, "r--", lw=1, label="@外省估计：传播系数k:%.4f 传播开始日:%s" % (K, date_only_series[StartDay1 - 1]))
    plt.plot(P2, "g--", lw=1, label="@外地估计：传播系数k:%.4f 传播开始日:%s" % (K, date_only_series[StartDay2 - 1]))
    plt.plot(P3, "b--", lw=1, label="@武汉估计：传播系数k:%.4f 传播开始日:%s" % (K, date_only_series[StartDay3 - 1]))
    plt.legend()
    plt.ylabel(r"$Num$")
    des = r"人数估计曲线图(科研用途)--%d天治愈+%d号封城模型: $y_{[i]}=y_{[i-1]}+k(y_{[i-3]}-y_{[i-9]})-y_{[i-22]}$" % (N, ShutDay)
    des = des + r"$(\ if\ i\geq%d\ k_{i}=%.2f*k_{i-1}$)" % (ShutDay, rate)

    plt.title(des, fontsize=12, fontweight='heavy', color='blue')

    plt.xticks(np.arange(0, L, 1), date_only_series, rotation=45)

    plt.grid(axis="x", ls='-.', c='#111111')
    plt.grid(axis="y", ls='-.', c='#111111')
    plt.xlim((0, L - 1))  # 显示用
    plt.ylim((0, np.max(P0) * 1.02))  # 显示用


if __name__ == "__main__":
    plt.subplot(111)
    dDrawPlot(22, 0.7, 24, 10, 200)

    des = r"人数估计曲线图(科研用途)1"
    plt.get_current_fig_manager().window.showMaximized()
    fig = plt.gcf()
    plt.show()
    fig.savefig("{}.png".format(des), dpi=200, bbox_inches='tight')
