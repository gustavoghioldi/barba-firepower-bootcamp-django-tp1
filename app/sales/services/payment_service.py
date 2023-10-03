import requests
from web.forms.checkout_form import CheckoutForm
from app.settings import DECIDIR_APIKEY, DECIDIR_URL, DECIDIR_APIKEY_PRIVATE

class PaymentService:
    
    @staticmethod
    def generate_token(checkout_form: CheckoutForm):
        payload = {
          "card_number":str(checkout_form.cleaned_data["card_number"]),
          "card_expiration_month": str(checkout_form.cleaned_data["card_expiration_month"]).zfill(2) ,
          "card_expiration_year": str(checkout_form.cleaned_data["card_expiration_year"]),
          "security_code": str(checkout_form.cleaned_data["security_code"]).zfill(3),
          "card_holder_name": checkout_form.cleaned_data["card_holder_name"],
          "card_holder_identification": {
            "type": checkout_form.cleaned_data["card_holder_identification_type"],
            "number":str(checkout_form.cleaned_data["card_holder_identification_number"])
          }
        }

        headers = {
            'apikey': DECIDIR_APIKEY,
            'Content-Type': 'application/json',
            }
        
        response = requests.post(f"{DECIDIR_URL}/tokens", json=payload, headers=headers)
        return response 
    
    @staticmethod
    def pay_transaction(amount, site_id, token):
      headers = {
            'apikey': DECIDIR_APIKEY_PRIVATE,
            'Content-Type': 'application/json',
            'cache-control': 'no-cache'
            }
      
      payload = {
         "site_transaction_id":site_id,
         "token":token,
         "payment_method_id":1,
         "bin":"450799",
         "amount":amount,
         "currency":"ARS",
         "installments":1,
         "description":"",
         "payment_type":"single",
         "sub_payments":[]}
      
      response = requests.post(f"{DECIDIR_URL}/payments", json=payload, headers=headers)
      return True if response.status_code == 201 else False