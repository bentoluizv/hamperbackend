from project.ext.database import db
from project.models.restaurant_model import Restaurant
from project.service.restaurant_service import get_all_restaurants


restaurants = [
    {
        "products": [],
        "id": 1,
        "name": "Bode do Nô",
        "description": "Saboreie a Vida Com o Gosto do Nordeste!",
        "classification": 4.9,
        "location": "Recife-PE",
        "url_image_logo": "https://img.freepik.com/vetores-premium/mascote-de-logotipo-de-cabra-bonito-dos-desenhos-animados_634248-1061.jpg?w=740",
        "url_image_banner": "https://ibb.co/r4dKhnd",
        "associated_products": []
    },
    {
        "products": [],
        "id": 2,
        "name": "Imperador dos camarões",
        "description": "Delícias do Mar",
        "classification": 5.0,
        "location": "Maceió-AL",
        "url_image_logo": "https://st2.depositphotos.com/4265001/12342/v/950/depositphotos_123429178-stock-illustration-brine-shrimp-logo.jpg",
        "url_image_banner": "https://super.abril.com.br/wp-content/uploads/2016/12/fundo-do-mar-site-copy.jpg?quality=90&strip=info&w=720&h=440&crop=1",
        "associated_products": []
    },
    {
        "products": [],
        "id": 4,
        "name": "Boi na Brasa",
        "description": "O Churrasco Gaúcho de Ser",
        "classification": 4.7,
        "location": "Porto Alegre-RS",
        "url_image_logo": "https://img.freepik.com/vetores-premium/logotipo-da-vaca_701103-18.jpg",
        "url_image_banner": "https://s.tmimgcdn.com/scr/800x500/317900/estilo-de-logotipo-de-desenho-animado-de-vaca-fofa_317900-original.jpg",
        "associated_products": []
    },
    {
        "products": [],
        "id": 3,
        "name": "Bar da Sogra",
        "description": "Cerveja boa e bons amigos! 🍺",
        "classification": 4.4,
        "location": "Salvador-BA",
        "url_image_logo": "https://www.shutterstock.com/image-vector/bar-lettering-illustration-label-badge-600nw-1034296870.jpg",
        "url_image_banner": "https://www.creativefabrica.com/wp-content/uploads/2020/10/09/Bar-Cafe-logo-design-Vector-illustration-Graphics-5947541-1-1-580x387.jpg",
        "associated_products": []
    },
    {
        "products": [],
        "id": 6,
        "name": "Sushi 'n Roll",
        "description": "Provou, gostou, viciou",
        "classification": 5.0,
        "location": "São Paulo-SP",
        "url_image_logo": "https://i.pinimg.com/originals/70/3c/20/703c204900d897e07ed5735f1c98e5fa.jpg",
        "url_image_banner": "https://www.creativefabrica.com/wp-content/uploads/2022/10/14/Japanese-sushi-food-delivery-logo-design-Graphics-41575180-1.jpg",
        "associated_products": []
    },
    {
        "products": [],
        "id": 7,
        "name": "Massucar Doceria",
        "description": "O doce da felicidade",
        "classification": 4.5,
        "location": "Curitiba-PR",
        "url_image_logo": "https://i.pinimg.com/originals/d0/e8/00/d0e8005c0035230d88468739f74fb4a4.jpg",
        "url_image_banner": "https://img.lovepik.com/background/20211021/medium/lovepik-pink-banner-background-image_500374994.jpg",
        "associated_products": []
    },
    {
        "products": [],
        "id": 5,
        "name": "Casa De Lanches e Grill Madrid",
        "description": "Lanches e chapeados",
        "classification": 4.9,
        "location": "Florianópolis-SC",
        "url_image_logo": "https://i.pinimg.com/736x/71/82/0b/71820bb5162d62a6848c6ac74e1a6ab2.jpg",
        "url_image_banner": "https://logo.criativoon.com/wp-content/uploads/2016/07/logotipo-lanchonete.png",
        "associated_products": []
    },
    {
        "products": [],
        "id": 8,
        "name": "Pizzaria Q-Massa",
        "description": "A felicidade está a algumas fatias de distância!",
        "classification": 4.9,
        "location": "Belo Horizonte-MG",
        "url_image_logo": "https://static.vecteezy.com/ti/vetor-gratis/p1/7944092-pizza-logo-design-modelo-ilustracaoial-gratis-vetor.jpg",
        "url_image_banner": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRNu7UZ1fJEOEyoWiCHhuKw1Oeze-lE1VfbxnIvPwIbBxFY_gd1h261MgGIASJiDmdzvA&usqp=CAU",
        "associated_products": []
    }
]

products = [
    {
        "id": 28,
        "name": "Pizza de brócolis",
        "value": 40.0,
        "description": "Tamanho pequena, 6 fatias",
        "url_image": "https://www.comidaereceitas.com.br/wp-content/uploads/2015/07/Pizza-de-brocolis-com-azeitonas-780x521.jpg"
    },
    {
        "id": 29,
        "name": "Pizza de bacon",
        "value": 85.0,
        "description": "Tamanho família, 20 fatias",
        "url_image": "https://img.freepik.com/fotos-premium/uma-fatia-de-pizza-coberta-com-bacon-cogumelos-e-tomate_942932-337.jpg"
    },
    {
        "id": 1,
        "name": "X-Bacon",
        "value": 20.0,
        "description": "Pão com gergelim, hambúrguer, bacon, queijo cheddar e molho especial",
        "url_image": "https://www.sabornamesa.com.br/media/k2/items/cache/5098e75e57e36807c173cb7490b1b0d2_XL.jpg"
    },
    {
        "id": 2,
        "name": "Chapeado de Carne",
        "value": 55.5,
        "description": "Chapeado de carne acompanhado de batatas fritas",
        "url_image": "https://i.pinimg.com/736x/69/96/80/6996806ae90f27521a851963d94d4053.jpg"
    },
    {
        "id": 3,
        "name": "Costela assada",
        "value": 75.0,
        "description": "Costela assada e bem temperada",
        "url_image": "https://www.sabornamesa.com.br/media/k2/items/cache/8a7eacb7a228abdc187ecece4128652b_XL.jpg"
    },
    {
        "id": 4,
        "name": "X-Frango",
        "value": 18.5,
        "description": "Pão com gergelim, frango, alface, tomate e molho",
        "url_image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQHJdHOtml7WXO9U7JS9yZcta1AAf17nJyJkyHpxL2zCShYJQ1b0u60N6uWDuW7RPcjIO4&usqp=CAU"
    },
    {
        "id": 30,
        "name": "Pizza sensação",
        "value": 35.0,
        "description": "Tamanho broto, 4 fatias",
        "url_image": "https://www.sabornamesa.com.br/media/k2/items/cache/14985840dca330e3b808aa792fa422f9_XL.jpg"
    },
    {
        "id": 5,
        "name": "Coca Cola 2L",
        "value": 12.0,
        "description": "",
        "url_image": "https://static.paodeacucar.com/img/uploads/1/120/24982120.png"
    },
    {
        "id": 6,
        "name": "Suco de Uva Natural",
        "value": 7.5,
        "description": "400ml de suco de uva natural",
        "url_image": "https://img.cybercook.com.br/receitas/612/suco-de-uva-natural.jpeg"
    },
    {
        "id": 8,
        "name": "Acarajé com vatapá",
        "value": 8.0,
        "description": "Clássico acarajé baiano",
        "url_image": "https://receitinhas.com.br/wp-content/uploads/2017/01/divulgacao.jpg"
    },
    {
        "id": 9,
        "name": "Bobó de camarão",
        "value": 49.9,
        "description": "Purê de mandioca, camarão, ervas e especiarias, leite de coco, azeite de dendê...",
        "url_image": "https://s2-receitas.glbimg.com/GyuIST9HlLttYS1X9ZO0T--q8wI=/0x0:1280x800/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_1f540e0b94d8437dbbc39d567a1dee68/internal_photos/bs/2022/U/K/zp2llURnexxCaOgLe8iA/bobo-de-camarao-receita-2.jpg"
    },
    {
        "id": 10,
        "name": "Moqueca Maranhense",
        "value": 35.8,
        "description": "Peixe cozido com outros frutos do mar e temperos como leite de coco e o azeite de dendê",
        "url_image": "https://www.cnnbrasil.com.br/wp-content/uploads/sites/12/2023/01/comidas-da-regiao-do-nordeste-moqueca-maranhense.jpg?w=750"
    },
    {
        "id": 11,
        "name": "Arroz de Cuxá",
        "value": 29.0,
        "description": "Arroz branco cozido em água e sal, acompanhado de um molho conhecido como cuxá na culinária maranhense",
        "url_image": "https://www.cnnbrasil.com.br/wp-content/uploads/sites/12/2023/01/pratos-tipicos-da-regiao-nordeste-arroz-de-cuxa.jpg?w=874"
    },
    {
        "id": 12,
        "name": "Tapioca de Frango",
        "value": 8.0,
        "description": "Tapioca de frango com queijo e tomate",
        "url_image": "https://blog.supernovaera.com.br/wp-content/webp-express/webp-images/uploads/2022/11/receita-de-tapioca.jpeg.webp"
    },
    {
        "id": 13,
        "name": "Cajuína",
        "value": 7.5,
        "description": "Bebida de caju típica do nordeste brasileiro",
        "url_image": "https://estarbem.vtexassets.com/arquivos/ids/155594/548221.png?v=637962536158770000"
    },
    {
        "id": 14,
        "name": "Risoto de camarão",
        "value": 28.8,
        "description": "Camarões frescos com o arroz arbóreo, um toque de queijo parmesão e uma seleção precisa de temperos",
        "url_image": "https://s2-receitas.glbimg.com/KWpGf7SHzNbPSab_Z3fmhDOGCmo=/0x0:1080x608/924x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2022/A/5/RQBWn4SlyzO0JWxYflwg/capa-materia-gshow-102-.png"
    },
    {
        "id": 15,
        "name": "Iscas de peixe",
        "value": 32.0,
        "description": "Filé de peixe empanado",
        "url_image": "https://espetinhodesucesso.com.br/wp-content/uploads/2022/04/Como-fritar-peixe-igual-da-praia.jpg"
    },
    {
        "id": 16,
        "name": "Ceviche de camarão",
        "value": 35.5,
        "description": "Camarão marinado em suco de limão e laranja com cebolas, tomate e coentro",
        "url_image": "https://i.pinimg.com/736x/e8/98/4f/e8984ffb8261510b95fef959f6c8ba0b.jpg"
    },
    {
        "id": 17,
        "name": "Bolinho de bacalhau",
        "value": 24.8,
        "description": "Preparado com bacalhau desfiado, batatas, cebola, salsa e azeite de oliva",
        "url_image": "https://static.itdg.com.br/images/360-240/a71f4fd47fc37eeb98a662bc69e304be/shutterstock-2005565906.jpg"
    },
    {
        "id": 18,
        "name": "Bolinho de salmão",
        "value": 26.8,
        "description": "Filé de salmão, cream cheese, cebola, raspas de limão e azeite de oliva",
        "url_image": "https://media-cdn.tripadvisor.com/media/photo-s/12/36/4d/be/bolinho-de-salmao.jpg"
    },
    {
        "id": 19,
        "name": "Maionese de batata com lagosta",
        "value": 24.5,
        "description": "Maionese de batata com lagosta temperado com azeite, cebolinha, coentro e cebola.",
        "url_image": "https://www.receiteria.com.br/wp-content/uploads/maionese-de-batata-com-lagosta.jpg"
    },
    {
        "id": 20,
        "name": "Picanha assada",
        "value": 89.9,
        "description": "Picanha assada acompanhada de arroz, batata frita, maionese e vinagrete.",
        "url_image": "https://img.cybercook.com.br/receitas/667/picanha-assada-no-forno-1.jpeg"
    },
    {
        "id": 21,
        "name": "Asinha de frango com batata",
        "value": 35.9,
        "description": "Asinha de frango com batata temperada",
        "url_image": "https://www.receitasnestle.com.br/sites/default/files/srh_recipes/c44c2da22695fb5021136c1dff9e71f0.jpg"
    },
    {
        "id": 22,
        "name": "Pão de alho",
        "value": 14.5,
        "description": "Quatro pães de alho",
        "url_image": "https://amopaocaseiro.com.br/wp-content/uploads/2022/02/yt-055_pao-de-alho_receita.jpg"
    },
    {
        "id": 23,
        "name": "Espetinho de carne",
        "value": 6.0,
        "description": "Espetinho de carne acompanhado de farofa",
        "url_image": "https://imac.agr.br/wp-content/uploads/2023/02/IMAC-FEV-Espetinho-de-carne-quais-as-melhores-carnes-para-petiscar-Autores-GS2-Marketing-Digital-Freepik.jpg"
    },
    {
        "id": 24,
        "name": "Assado de porco",
        "value": 99.9,
        "description": "Assado de porco acompanhado de arroz, batata fria, maionese caseira, feijão e lasanha de frango",
        "url_image": "https://diariodonordeste.verdesmares.com.br/image/contentid/policy:1.3270565:1661291875/Assado%20de%20carne%20de%20porco.jpg?f=4x3&$p$f=7cde45d"
    },
    {
        "id": 25,
        "name": "Guaraná Antarctica 2L",
        "value": 10.0,
        "description": "Guaraná Antarctica 2 litros",
        "url_image": "https://emporiokaminski.com.br/wp-content/uploads/2020/07/Refrigerante-Guarana%CC%81-Antarctica-2l.jpg"
    },
    {
        "id": 27,
        "name": "Pizza de frango com catupiry",
        "value": 48.0,
        "description": "Tamanho Média, 8 fatias",
        "url_image": "https://receitas123.com/wp-content/uploads/2023/05/pizza-de-frango-com-catupiry.png"
    },
    {
        "id": 26,
        "name": "Pizza de calabresa",
        "value": 63.0,
        "description": "Tamanho Grande, 12 fatias",
        "url_image": "https://cdn0.tudoreceitas.com/pt/posts/9/8/3/pizza_calabresa_e_mussarela_4389_600.jpg"
    },
    {
        "id": 31,
        "name": "Pizza dois amores",
        "value": 73.0,
        "description": "Tamanho gigante, 16 fatias",
        "url_image": "https://static.wixstatic.com/media/3e7d9c_071a30683eb5483b9aea7bacac36024d~mv2.jpg/v1/fill/w_270,h_180,al_c,q_80,usm_0.66_1.00_0.01,enc_auto/IMG_8105.jpg"
    },
    {
        "id": 32,
        "name": "Bolo de pote",
        "value": 12.0,
        "description": "Sabor morango",
        "url_image": "https://bolosparavender.com.br/wp-content/uploads/2018/10/bolo-de-pote-de-morango-receita-1200x900.jpg"
    },
    {
        "id": 33,
        "name": "Brownie de chocolate",
        "value": 8.0,
        "description": "Sabor chocolate ao leite",
        "url_image": "https://img.saborosos.com.br/imagens/brownie-de-chocolate-848x477.jpg"
    },
    {
        "id": 34,
        "name": "Copo da felicidade",
        "value": 17.0,
        "description": "Sabor Kinder Bueno",
        "url_image": "https://i0.wp.com/meucadernodereceitas.xyz/wp-content/uploads/2020/08/Copo-da-Felicidade-Kinder-Bueno1.png?fit=571%2C378&ssl=1"
    },
    {
        "id": 35,
        "name": "Mousse de Maracujá",
        "value": 6.5,
        "description": "Sabor Maracujá",
        "url_image": "https://static.itdg.com.br/images/360-240/8fed8f60d3c8e3990396e2478cbc7f2a/shutterstock-1905617575-1-.jpg"
    },
    {
        "id": 36,
        "name": "Cone recheado",
        "value": 8.5,
        "description": "Sabor Oreo",
        "url_image": "https://cdn0.tudoreceitas.com/pt/posts/4/8/9/cone_trufado_de_oreo_9984_orig.jpg"
    },
    {
        "id": 37,
        "name": "Trufa de morango",
        "value": 4.5,
        "description": "Sabor Morango",
        "url_image": "https://www.sabornamesa.com.br/media/k2/items/cache/8c42edabbb432b8d634ad0a8fb8f91ae_XL.jpg"
    },
    {
        "id": 38,
        "name": "Salmão",
        "value": 36.9,
        "description": "10 unid.",
        "url_image": "https://receitinhas.com.br/wp-content/uploads/2018/12/iStock-623858612-1200x800.jpg"
    },
    {
        "id": 39,
        "name": "Niguiri",
        "value": 39.9,
        "description": "12 unid.",
        "url_image": "https://sumidasushi.com.br/wp-content/uploads/ESSA-nisalmao.png"
    },
    {
        "id": 40,
        "name": "Sasaki de polvo",
        "value": 29.9,
        "description": "Sashimi de polvo regado ao molho de limão, sal, azeite, cebolinha e furikake",
        "url_image": "https://thumb-cdn.soluall.net/prod/shp_products/sp1280fw/62c5a6da-83b0-431c-96cd-4b95ac1e09ff/62c5a6da-ab64-439d-aa01-4b95ac1e09ff.png"
    },
    {
        "id": 41,
        "name": "Temaki misto simples",
        "value": 22.0,
        "description": "Salmão e atum, peixe branco",
        "url_image": "https://img77.uenicdn.com/image/upload/v1611665862/service_images/shutterstock_1021362085.jpg"
    },
    {
        "id": 42,
        "name": "Hot Skin",
        "value": 18.0,
        "description": "10 unid.",
        "url_image": "https://s3-sa-east-1.amazonaws.com/deliveryon-uploads/products/chefrudi/260_6192fdfdc7509.jpg"
    },
    {
        "id": 43,
        "name": "Sashimi atum",
        "value": 10.0,
        "description": "5 unid.",
        "url_image": "https://media-cdn.tripadvisor.com/media/photo-s/04/b2/33/02/sushi-hokkai.jpg"
    },
    {
        "id": 44,
        "name": "Porção de batata frita",
        "value": 17.9,
        "description": "300g de batata frita",
        "url_image": "https://static.wixstatic.com/media/a037bb_95c9809d8f2a466784365ba9acfa698e~mv2.jpg/v1/fill/w_480,h_406,al_c,q_80,usm_0.66_1.00_0.01,enc_auto/a037bb_95c9809d8f2a466784365ba9acfa698e~mv2.jpg"
    },
    {
        "id": 45,
        "name": "Tilápia frita",
        "value": 27.9,
        "description": "300g de tilápia frita",
        "url_image": "https://s2.glbimg.com/dtNRaCF79uFjiXayBn2Lsy1jViQ=/e.glbimg.com/og/ed/f/original/2022/03/02/maxresdefault_2.jpg"
    },
    {
        "id": 46,
        "name": "Anéis de cebola",
        "value": 25.9,
        "description": "Anéis de cebola frita acompanhada de molho especial",
        "url_image": "https://www.culinariadavovo.com.br/wp-content/uploads/2021/03/anel-de-cebola-na-AirFryer.jpg"
    },
    {
        "id": 47,
        "name": "Gin Tônica",
        "value": 17.9,
        "description": "Gin, água tônica, framboesa e manjericão",
        "url_image": "https://gastronomiacarioca.zonasul.com.br/wp-content/uploads/2021/10/gin_tonica_rodrigo_azevedo_zona_sul_destaque.jpg"
    },
    {
        "id": 48,
        "name": "Água mineral sem gás",
        "value": 3.5,
        "description": "Garrafa 500ml",
        "url_image": "https://io.convertiez.com.br/m/trimais/shop/products/images/3174/medium/agua-mineral-natural-sem-gas-crystal-garrafa-500ml_3146.jpg"
    },
    {
        "id": 49,
        "name": "Caneca de Chopp",
        "value": 11.5,
        "description": "500ml",
        "url_image": "https://cdnm.westwing.com.br/glossary/uploads/br/2015/02/02195523/caneca-de-chopp-bem-gelada_pinterest_c-a1849.jpg"
    }
]


def populate_db_mock_restaurant():
    for restaurant in restaurants:
        restaurant_model = Restaurant(name=restaurant["name"],
                                      description=restaurant["description"],
                                      classification=restaurant["classification"],
                                      location=restaurant["location"],
                                      url_image_logo=restaurant["url_image_logo"],
                                      url_image_banner=restaurant["url_image_banner"])
        db.session.add(restaurant_model)
        db.session.commit()

def populate_db_mock_product():
    restaurants = get_all_restaurants()
    