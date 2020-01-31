import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用于正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

L = 60  # 1月1日开始计算，总共预测50天
Today = 31  # 今天第31天
SN = 100  # 初始以100个病人算


def dShift(lst, k):
    return lst[k:] + lst[:k]


def dPPNum(n, k, rate, ShutDay=24, StartDay=0):
    dFun = lambda v, n, k: v[n - 1] + k * v[n - 3] - v[0]

    Y = [0 for i in range(L)]
    lst = [0 for i in range(n)]
    lst[-1] = SN
    for i, y in enumerate(Y):
        y = dFun(lst, n, k)
        y = np.maximum(y, 0)
        if i > ShutDay:  # 封城在1月24日左右，传播率降低，假定每天以rate系数衰减
            k = k * rate

        if i > StartDay: #默认从1月1号开始
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

    Y02 = [0 for i in range(Today)]  # 武汉
    Y02[20] = 198  # 武汉卫健委
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

    Y03 = [Y00[i] - Y01[i] for i in range(Today)]  # 外省=国家-湖北
    Y04 = [Y01[i] - Y02[i] for i in range(Today)]  # 外地=湖北-武汉
    Y05 = [Y03[i] / (500 * 0.35) * (1400) for i in range(Today)]  # 外省-反推
    Y06 = [Y04[i] / (500 * 0.65) * (1400) for i in range(Today)]  # 外地-反推
    return Y00, Y01, Y02, Y03, Y04, Y05, Y06


def dDrawPlot(N, rate, ShutDay):
    K = np.linspace(0.24, 0.28, 5, endpoint=True)
    P00, P01, P02, P03, P04, P05, P06 = dPPNum0()
    P1 = dPPNum(N, K[1], rate, ShutDay)
    P2 = dPPNum(N, K[2], rate, ShutDay)
    P3 = dPPNum(N, K[3], rate, ShutDay)
    P4 = dPPNum(N, K[4], rate, ShutDay)
    plt.plot(P00, "r--o", lw=1, label="@国家卫健委数据(20-%d日)" % (Today))
    plt.plot(P02, "r--", lw=2, label="@武汉")
    plt.plot(P03, "g--", lw=2, label="@外省=国家-湖北")
    plt.plot(P04, "b--", lw=2, label="@外地=湖北-武汉")
    #  plt.plot(P05, "g--^", lw=1, label="@外省-反推：武汉外流500万，外省占35%")
    #  plt.plot(P06, "g--*", lw=1, label="@外地-反推：武汉外流500万，省内占65%")
    plt.plot(P1, c='#004EFF', lw=1, label="@传播系数k:%.4f 治愈天数:%d" % (K[1], N))
    plt.plot(P2, c='#00FF3F', lw=1, label="@传播系数k:%.4f 治愈天数:%d" % (K[2], N))
    plt.plot(P3, c='#003F00', lw=1, label="@传播系数k:%.4f 治愈天数:%d" % (K[3], N))
    plt.plot(P4, c='#009FEF', lw=1, label="@传播系数k:%.4f 治愈天数:%d" % (K[4], N))

    plt.legend()
    plt.xlabel(r"天数-$day$")
    plt.ylabel(r"数目-$Num$")
    des = r"人数估计曲线图(科研用途)--%d天治愈模型: $y_{%d}=y_{%d}+ky_{%d}-y_{0}$" % (N, N, N - 1, N - 3)
    if rate < 1.0:
        des = r"人数估计曲线图(科研用途)--%d天治愈+%d号封城模型: $y_{%d}=y_{%d}+ky_{%d}-y_{0}$" % (N, ShutDay, N, N - 1, N - 3)
        des = des + r"$(\ if\ i\geq%d\ k_{i}=%.2f*k_{i-1}$)" % (ShutDay, rate)

    plt.title(des, fontsize=12, fontweight='heavy', color='blue')
    plt.grid(axis="x", ls='-.', c='#111111')
    plt.grid(axis="y", ls='-.', c='#111111')
    plt.xlim((0, L))  # 显示用
    plt.ylim((0, np.max(P1 + P2 + P3 + P4) * 1.1))  # 显示用


if __name__ == "__main__":
    plt.subplot(211)
    dDrawPlot(26, 0.7, 24)
    plt.subplot(212)
    dDrawPlot(22, 0.7, 27)

    des = r"人数估计曲线图(科研用途)1"
    plt.get_current_fig_manager().window.showMaximized()
    fig = plt.gcf()
    plt.show()
    fig.savefig("{}.png".format(des), dpi=200, bbox_inches='tight')
