from typing import Optional,List
from fastapi import APIRouter,Header
from fastapi.responses import Response
from starlette.responses import HTMLResponse
router=APIRouter(
    prefix='/product',
    tags=['product']
)
products=['watch','camera','phone']
@router.get('/all')
def get_all_products():
    data="".join(products)
    response=Response(content=data,media_type="text/plain")
    response.set_cookie(key='test_coockie',value='test_cookie value')
    return response
@router.get('/withheader')
def get_products(
        response:Response,
        custom_header:Optional[List[str]] = Header(None)
):
    response.headers['custom_response_header']="and".join(custom_header)
    return products

@router.get('/{id}',responses={
    200:{
        "content":{
            "text/html":{
                "<div>product</div>"
            }
        },
        "description":"Returns the html for an object"
    },
404:{
        "content":{
            "text/html":{
                "<div>product</div>"
            }
        },
        "description":"Returns the html for an object"
    },

})
def get_product(id:int):
    product=products[id]
    out=f"""
    <head>
        <style>
    .product{{
        width:500px;
        height:30px;
        border:2px inset green
        background-color:lightblue;
        text-align:center;
    }}"""
    return HTMLResponse(content=out,media_type="text/html")

