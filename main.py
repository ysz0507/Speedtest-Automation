import speedtest
import time
from matplotlib import pyplot as plt 
import matplotlib
from time import localtime, strftime


def test_internet_speed(fake=False):
    if fake:
        download_speed = time.time() % 15
        time.sleep(.2)
    else:
        try:
            st = speedtest.Speedtest()
            download_speed = st.download() / 1e6
        except Exception as e:
            download_speed = 0
            print(f"Error encountered: {e}")
            time.sleep(15)
        
    print("Download Speed: {:.2f} Mbps".format(download_speed))
    return download_speed

def output_data(time_stamps, download_data):
    print(download_data)
    
    font = {
        'weight' : 'bold',
        'size'   : 22
    }

    matplotlib.rc('font', **font)
    plt.rcParams["figure.figsize"] = (14,10)

    current_time = strftime('%Y-%m-%d_%H:%M:%S', localtime())

    plt.title("Download Speeds using Speedtest.net") 
    plt.xlabel(f"Minimum: {min(download_data):.2f}   Maximum: {max(download_data):.2f}   {current_time}") 
    plt.ylabel("Speed in Mbps") 
    plt.grid()

    plt.plot(time_stamps, download_data) 
    plt.savefig(f"data/{current_time}.png")
    plt.show()

def collect_data(duration: int, fake=False):
    start = time.time()
    download_data = []
    time_stamps = []
    time_left = duration * 60
    while time_left > 0:
        print(f"only {int(time_left // 60)}min {int(time_left % 60)}s left")
        time_stamps.append((time.time() - start)/60)
        download_data.append(test_internet_speed(fake=fake))

        time_left = duration * 60 - (time.time() - start)
    output_data(time_stamps, download_data)


collect_data(5, fake=False)