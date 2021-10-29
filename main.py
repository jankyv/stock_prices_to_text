from binanceApi import *
from degiroApi import *
import time


class UpdateOBSText:
    def __init__(self, interval):
        self.interval = interval
        self.file = "C:/Users/Jancorne/Pictures/OBS/stock-info.txt"
        self.file_content = ''

    def addbtcprice(self):
        price, change = getBTCPrice()
        bitcoin_text = 'BTC/USDT ' + str(price) + ' (' + str(change) + '%) | '

        # Write to file
        self.file_content += bitcoin_text

    def addethprice(self):
        price, change = getETHPrice()
        etherium_text = 'ETH/USDT ' + str(price) + ' (' + str(change) + '%) | '

        # Write to file
        self.file_content += etherium_text

    def addGMEprice(self):
        price, change = getGMEprice()
        pfizer_text = 'GME/USDT ' + str(price) + ' (' + str(change) + '%) | '

        # Write to file
        self.file_content += pfizer_text

    def addPfizerprice(self):
        price, change = getpfizerprice()
        pfizer_text = 'PFIZER/USDT ' + str(price) + ' (' + str(change) + '%) | '

        # Write to file
        self.file_content += pfizer_text

    def addAMDprice(self):
        price, change = getamdprice()
        amd_text = 'AMD/USDT ' + str(price) + ' (' + str(change) + '%) | '

        # Write to file
        self.file_content += amd_text

    def addShellprice(self):
        price, change = getshellprice()
        shell_text = 'SHELL/EUR ' + str(price) + ' (' + str(change) + '%) | '

        # Write to file
        self.file_content += shell_text

    def main(self):
        while True:
            self.file_content = ''
            self.addbtcprice()
            self.addethprice()
            # self.addPfizerprice()
            self.addAMDprice()
            # self.addGMEprice()
            # self.addShellprice()
            f = open(self.file, "w")
            f.write(self.file_content)
            f.close()
            time.sleep(self.interval)


updateText = UpdateOBSText(2)

updateText.main()
