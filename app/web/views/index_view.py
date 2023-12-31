
# Create your views here.
from django.http import HttpResponse
from django.views import View
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin
from stock.models import StockModel
from app.settings import IMAGES
class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        template = loader.get_template("web/index.html")
        stock_by_interes = StockModel.objects.filter(business_line=request.user.business_line_interes).exclude(client=request.user)
        context = {
            "stock": stock_by_interes,
            "images": IMAGES
        }
        return HttpResponse(template.render(context, request))