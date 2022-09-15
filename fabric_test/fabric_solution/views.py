import datetime
import json

from rest_framework.response import Response
from rest_framework.views import APIView
from fabric_solution.serilizers import *
from fabric_solution.servicelib import *


class ClientView(APIView):
    def post(self, request):
        data = request.data
        client_serialize_list = []
        for item in data:
            client_ser = ClientSerializer(data=item)
            if client_ser.is_valid() and check_num(item.get("phone_number", "0")):
                client_serialize_list.append(client_ser)
            else:
                return Response("Validation Failed", status=400)

        for item in client_serialize_list:
            item.save()

        return Response(status=200)

    def delete(self, request, _id):
        if not Client.objects.filter(client_id=_id).exists():
            return Response("Item not found", status=404)
        client_item = Client.objects.get(client_id=_id)
        client_item.delete()

        return Response(status=200)

    def put(self, request, _id):
        if not Client.objects.filter(client_id=_id).exists():
            return Response("Item not found", status=404)

        data = request.data
        client_item = Client.objects.get(client_id=_id)

        rc = update_client_data(client_item, data, Client)

        return Response(status=200) if rc else Response("Validation Failed", status=400)


class MailView(APIView):
    def post(self, request):
        data = request.data
        mail_serialize_list = []
        for item in data:

            try:
                item["date_start"] = datetime.datetime.strptime(item["date_start"], "%Y-%m-%dT%H:%M:%SZ")
                item["date_end"] = datetime.datetime.strptime(item["date_end"], "%Y-%m-%dT%H:%M:%SZ")
            except:
                return Response("Validation Failed", status=400)

            mail_ser = MailSerializer(data=item)
            if mail_ser.is_valid():
                mail_serialize_list.append(mail_ser)
            else:
                return Response("Validation Failed", status=400)

        for item in mail_serialize_list:
            item.save()

        return Response(status=200)

    def delete(self, request, _id):
        if not Mail.objects.filter(mail_id=_id).exists():
            return Response("Item not found", status=404)
        client_item = Mail.objects.get(mail_id=_id)
        client_item.delete()

        return Response(status=200)

    def put(self, request, _id):
        if not Mail.objects.filter(mail_id=_id).exists():
            return Response("Item not found", status=404)

        data = request.data
        client_item = Mail.objects.get(mail_id=_id)

        rc = update_client_data(client_item, data, Mail)

        return Response(status=200) if rc else Response("Validation Failed", status=400)

    def get(self, request):
        msgs_sent = Message.objects.filter(status="sent")
        msgs_cancelled = Message.objects.filter(status="cancelled")
        response = {
            "sent": [msg.as_json() for msg in msgs_sent],
            "cancelled": [msg.as_json() for msg in msgs_cancelled]
                    }

        return Response(response, status=200)


class MessageView(APIView):
    def get(self, request, mail_id):
        if not Mail.objects.filter(mail_id=mail_id).exists():
            return Response("Item not found", status=404)

        msgs = Message.objects.filter(mail_id=mail_id)
        response = [msg.as_json() for msg in msgs]

        return Response(response, status=200)
