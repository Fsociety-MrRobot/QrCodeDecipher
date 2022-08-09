import cv2
from pyzbar import pyzbar


from colorama import Fore
from pyfiglet import Figlet
from prettytable import PrettyTable

class Dcphr:
	def __init__(self, direct):
		self.dir = direct
		self.table = None
		self.image = None
		self.content = None		
		self.barcodes = None     
	
	def decipher(self):
		self.image = cv2.imread(self.dir)
		self.table = PrettyTable(['QR-Code', 'Content'])
		self.barcodes = pyzbar.decode(self.image)
		
		for barcode in self.barcodes:
			barcode_data = barcode.data.decode('utf-8')
			self.conent = barcode_data
		
		tmp = (self.dir.split("/"))[len(self.dir.split("/")) - 1].split('.')[0]
		
		self.table.add_row([tmp, barcode_data])	
		self.output()
			
	def output(self):
		print(Fore.LIGHTRED_EX + f'\n{self.table}')
		

def main():
	banner = Figlet()
	print('\n\033[H\033[J' + Fore.LIGHTCYAN_EX + banner.renderText('QR  Decipher'))
	directory = input(Fore.LIGHTCYAN_EX + "\nEnter QR-CODE Image Path : ")

	_ex = Dcphr(direct = directory)
	_ex.decipher()

		
if __name__ == '__main__':
	main()
