import csv
from matplotlib import pyplot as plt
from matplotlib import cm
from matplotlib import axes
from matplotlib.font_manager import FontProperties
font = FontProperties(fname='/Library/Fonts/Songti.ttc')

def draw():
	#定義熱圖的橫縱座標
	xLabel = ["viewmainpage", "viewproduct", "viewcategory", "viewactivity", "search", "add", "checkout", "purchase"]
	yLabel = ["viewmainpage", "viewproduct", "viewcategory", "viewactivity", "search", "add", "checkout", "purchase"]
	#矩陣數值
	data = [[137506,25133,79507,4350,4592,967,2175,483],
			[30449,114548,130498,483,725,29725,2417,0],
			[75640,135331,70807,483,0,483,967,242],
			[5800,0,483,5317,0,0,0,0],
			[1450,5075,0,0,2900,0,0,0],
			[4108,17158,23200,0,0,47124,2175,0],
			[1450,967,483,0,0,0,16433,4108],
			[4833,242,1692,0,0,0,0,7492]]
	#作圖階段
	fig = plt.figure()
	#定義畫布為1*1個劃分，並在第1個位置上進行作圖
	ax = fig.add_subplot(111)
	#定義橫縱座標的刻度
	ax.set_yticks(range(len(yLabel)))
	ax.set_yticklabels(yLabel, fontproperties=font, fontsize=5)
	ax.set_xticks(range(len(xLabel)))
	ax.set_xticklabels(xLabel, fontsize=4, rotation=90)
	#作圖並選擇熱圖的顏色填充風格，這裡選擇hot
	im = ax.imshow(data, cmap="YlGnBu", vmax=260000)
	#增加右側的顏色刻度條
	plt.colorbar(im)
	#show
	plt.show()

d = draw()