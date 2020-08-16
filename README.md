# Iris website
## Launch App

`python3 app.py`

Click on link `http://127.0.0.1:5000/` to direct you to the website.

## curl post json

Only use in macos, linux or ubuntu. With window we must use postman sorfware.

* Predict:
`
curl --header "Content-Type: application/json"   --request POST   --data '{"sp_len":5,"sp_wid":5, "pen_len":4, "pen_wid":5}'   http://127.0.0.1:5000/predict
`
* Hello world:
`
curl --header "Content-Type: application/json"   --request GET  http://127.0.0.1:5000/
`

## Predict

Insert value into those blank cells and click submit. In case you don't input any values, those values going to be 0 at default.

![](https://imgur.com/lvlatS3.png)

