import json

from flask import request
from flask_restx import Resource
from project.ext.serializer import OrderSchema
from project.service.order_service import (delete_one_order, get_all_orders,
                                           get_one_order, post_order,
                                           update_order)
from project.utils.redis_utils import delete_redis_value, get_redis_value, set_redis_value
from project.doc_model.doc_models import order_model, api



order_schema_list = OrderSchema(many=True)
order_schema = OrderSchema(many=False)


class OrderResource(Resource):
    def get(self) -> Tuple[List[Dict[str, Any]], int]:
        key_redis = "orders"
        orders = get_redis_value(key_redis)
        if orders:
            return orders
        orders = get_all_orders()
        orders = order_schema_list.dump(orders)
        set_redis_value(key_redis, json.dumps(orders))
        return orders, 200


    @api.expect(order_model)
    def post(self):
        try:
            order_data = request.json
            if order_data['payment'] == "Pix" or order_data['payment'] == "Dinheiro":
                response = post_order(order_data)
                if response and order_data['payment'] == 'Pix':
                    return {"message": "Pedido cadastrado com sucesso!", "pix_copia_e_cola": response['pixCopiaECola'], "base64": response['pixBase64']}, 201
                elif order_data['payment'] == 'Dinheiro':
                    return {"message": "Pedido cadastrado com sucesso!"}
            else:
                return {"message": "Meio de pagamento inválido. (Opções: Pix e Dinheiro)"}
            delete_redis_value("orders")
        except Exception as e:
            return {"error": str(e)}, 400


class OrderResourceID(Resource):
    def get(self, id: int):
        if order := get_one_order(id):
            return order_schema.dump(order), 200  # type: ignore
        else:
            return {"error": f"Ordem com ID {id} não encontrado."}, 404


    @api.expect(order_model)
    def patch(self, id: int):
        try:
            order_data = request.json
            result = update_order(id, order_data)
            if "error" in result:
                return {"error": result["error"]}, 404
            delete_redis_value("clients")
            return {"message": result["message"]}, 200

        except Exception as e:
            return {"error": str(e)}, 500

    def delete(self, id: int):
        try:
            result = delete_one_order(id)

            if "error" in result:
                return {"error": result["error"]}, 404
            delete_redis_value("orders")
            return {"message": result["message"]}, 200

        except Exception as e:
            return {"error": str(e)}, 500

