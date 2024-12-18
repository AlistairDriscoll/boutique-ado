from django.http import HttpResponse

class StripeWH_Handler:
    """ Handle stripe webhooks """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected stripe event
        """

        return HttpResponse(
            content=f'Unhandled webhook recieved: {event['type']}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from stripe
        """

        return HttpResponse(
            content=f'Webhook recieved: {event['type']}',
            status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from stripe
        """

        return HttpResponse(
            content=f'Payment failed. Webhook recieved: {event['type']}',
            status=200
        )