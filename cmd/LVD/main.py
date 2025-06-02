from ...internal.adapter.fastapi.app import App


app = App()
app.Setup()
app.Run(host="localhost",port=8000)
