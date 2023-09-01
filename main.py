from project import create_app

"""Arquivo para execução da aplicação"""
app = create_app()

if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
