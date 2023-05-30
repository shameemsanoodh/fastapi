from fastapi import APIRouter
from common_includes import *
from app_main.users import *
import os
router_users = APIRouter()


def check_pass_phase(pass_phase: str = None) -> bool:
    current_valid_pass_phase = "123456"
    if ((pass_phase is None) or (len(pass_phase) <= 0) or (pass_phase != current_valid_pass_phase)):
        return(False)
    return(True)


@router_users.get("/generate_new_token/", tags=["misc"])
async def generate_new_token(request: Request, expiry_secs: int = Query(None), pass_phase: str = Query(None)):
    """
    Generates an access token with long validity by default. You can also generate with custom expiry by passing value in seconds to `expiry_secs` using query param
    """
    response = {'success': False, 'access_token': '', 'message': 'Error: Authentication failed - invalid pass phase suuplied.'}
    if check_pass_phase(pass_phase):
        body = await request.body()
        dummy_payload = {'message': 'token generated for testing purpose'}
        if expiry_secs is None:
            expiry_secs = INT_SECS_90_DAYS
        response = {'access_token': encode_token(payload_dict=dummy_payload, expiry_secs=expiry_secs)}
    return(response)


@router_users.get('/users/', tags=["users"])
async def users(request: Request, fields: Optional[List[str]] = Query(None), num_records: int = Query(None), token: str = Depends(token_auth_scheme), api_handle=Depends(api_handler)):
    """
       Parameters:
       - **fields**: This retrieves only the field name given from all record `example(fields:user_name)`.
       - **num_records**: This retrieves only the number of records mentioned `example(num_records:5)`.
       """
    return get_all_users(api_handle=api_handle, fields=fields, num_records=num_records)


@router_users.get('/users/{record_id}', tags=["users"])
async def users(request: Request, record_id: int, token: str = Depends(token_auth_scheme), api_handle=Depends(api_handler)):
    return get_all_users(api_handle=api_handle, record_id=record_id)


@router_users.post('/users/', tags=["users"])
async def users(request: Request, body: dict = Body(...), token: str = Depends(token_auth_scheme), api_handle=Depends(api_handler)):
    """
    - Data is expected in json like
    - Copy **JSON** and Execute to post records to Database
        ```{
        {
          "status": "active",
          "user_name": "eastvantage",
          "mail_id": "eastvantage@gmail.com",
          "phone_number": "9999999999",
          "user_address": "Bengaluru",
          "latitude": "12345678",
          "longitude": "12345678"
        }
    """
    return add_users(api_handle=api_handle, record_dict=body)


@router_users.patch('/users/{record_id}', tags=["users"])
async def users(record_id, request: Request, record_dict: dict = Body(...), token: str = Depends(token_auth_scheme), api_handle=Depends(api_handler)):
    """
    Edit an item by ID.

    This endpoint get an item with id passed the database `id`.
    ```{
        {
          "user_address": "Salarpuria Triton, 57, 13th Cross Rd, Anepalya, Gajendra Nagar, Bengaluru, Karnataka 560030"
        }
    """
    return update_users(api_handle=api_handle, record_id=record_id, record_dict=record_dict)


@router_users.delete('/users/{record_id}', tags=["users"])
async def users(request: Request, record_id: int, token: str = Depends(token_auth_scheme), api_handle=Depends(api_handler)):
    """
    Delete an item by ID.

    This endpoint get an item with id passed the database `id`.
    """
    return delete_users(api_handle=api_handle, record_id=record_id)


@router_users.get('/address_book/', tags=["users"])
async def users(request: Request, latitude: float, longitude: float, distance: int = 1, token: str = Depends(token_auth_scheme), api_handle=Depends(api_handler)):
    """
    Pass current lat long of user and desired distance

    - Example Latitude `12.993626`.
    - Example Longitude `77.661522`.
    - Distance minimum `1`km.
    """
    sql_str = sql.SQL("SELECT * FROM users WHERE (6371 * 2 * ASIN(SQRT(POWER(SIN((RADIANS(" + str(latitude) + " - latitude)) / 2), 2) + COS(RADIANS(" + str(latitude) + ")) * COS(RADIANS(latitude)) * POWER(SIN((RADIANS(" + str(longitude) + " - longitude)) / 2), 2)))) <= " + str(distance) + ";")
    return db_execute_sql(api_handle=api_handle, sql_str=sql_str)


@router_users.get("/download_code/",  tags=["code"])
async def files(request: Request, api_handle=Depends(api_handler)):
    """
          API for downloading file.
          `Execute` to get source code of fast api.
    """
    home_dir = './files/'
    file_name = 'eastvantage.zip'
    print(home_dir + file_name)
    if not os.path.isfile(home_dir + file_name):
        return {"success": False, "message": 'File does not exist'}
    else:
        return FileResponse(path=home_dir + file_name, filename=file_name)
    return


