from stock.models import StockModel
class StockService:
    @staticmethod
    def sock_managment_down(stock: StockModel, qt):
        #resta del stock
        stock.qt -= qt
        stock.save()