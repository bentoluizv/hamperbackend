# from cryptography.hazmat.primitives.serialization import pkcs12, Encoding, NoEncryption
# from cryptography.hazmat.primitives.serialization import PrivateFormat, BestAvailableEncryption
# from cryptography.hazmat.primitives import serialization
# import os

# def convert_p12_to_pem(p12_path, pem_path, p12_password=None, pem_password=None):
#     try:
#         # Lendo o arquivo .p12
#         with open(p12_path, "rb") as p12_file:
#             p12_data = p12_file.read()

#         # Carregando o certificado e a chave privada
#         private_key, certificate, additional_certs = pkcs12.load_key_and_certificates(
#             p12_data, 
#             password=p12_password.encode() if p12_password else None
#         )

#         if not private_key or not certificate:
#             raise ValueError("Erro ao carregar o certificado ou a chave privada do arquivo .p12.")

#         # Convertendo a chave privada para .pem
#         pem_private_key = private_key.private_bytes(
#             Encoding.PEM,
#             PrivateFormat.TraditionalOpenSSL,
#             BestAvailableEncryption(pem_password.encode()) if pem_password else NoEncryption()
#         )

#         # Convertendo o certificado para .pem
#         pem_certificate = certificate.public_bytes(Encoding.PEM)

#         # Convertendo certificados adicionais, se existirem
#         pem_additional_certs = b""
#         if additional_certs:
#             for cert in additional_certs:
#                 pem_additional_certs += cert.public_bytes(Encoding.PEM)

#         # Escrevendo no arquivo de saída
#         with open(pem_path, "wb") as pem_file:
#             pem_file.write(pem_private_key)
#             pem_file.write(pem_certificate)
#             pem_file.write(pem_additional_certs)

#         print(f"Conversão concluída! Certificado salvo em: {pem_path}")
    
#     except Exception as e:
#         print(f"Erro ao converter o certificado: {e}")

# p12_file_path = "project/utils/producao-588587-Hamperapp.p12"
# pem_file_path = "project/utils/certificado.pem"  # Arquivo de saída

# # 🔑 Se o .p12 tiver senha, coloque aqui. Se não tiver, deixe None
# p12_password = None  # Exemplo: "sua_senha"

# # 🔒 Se quiser proteger o .pem com senha, defina aqui. Se não quiser, deixe None
# pem_password = None  # Exemplo: "nova_senha"

# # 🚀 Executando a conversão
# convert_p12_to_pem(p12_file_path, pem_file_path, p12_password, pem_password)
