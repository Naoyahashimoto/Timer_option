import numpy as np
import matplotlib.pyplot as plt

#株価の確率微分方程式に従うサンプルパスを生成
#dS/S = r * dt + vol * dW_t
def generate_path(S0, T, r, vol, N, M):
    dt = T/M
    w = np.cumsum(np.reshape(np.random.standard_normal(N*M), (N,M)), 1) * (dt**0.5)
    t = np.cumsum(np.ones((N,M)), 1)*dt   
    return S0 * np.exp((r-0.5*vol**2)*t + vol*w)

if __name__ == "__main__":
    #株価・満期・瞬間金利・ボラティリティ
    S0  = 100.0
    T   = 3.0
    R   = 0.01
    VOL = 0.2
    #パス数・時間刻み数
    N = 50
    M = 200
    #パスの生成＆描画
    x = generate_path(S0, T, R, VOL, N, M)
    plt.plot(x.T)
    plt.show()