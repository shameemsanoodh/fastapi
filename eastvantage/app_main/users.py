from common_includes import *


def get_all_users(api_handle: api_handler, record_id: int = None, fields: list = None, num_records: int = None):
    return get_record_by_field(api_handle=api_handle, table_name='users', field_name="id", field_value=record_id, fields=fields, num_records=num_records)


def add_users(api_handle: api_handler, record_dict: dict):
    return insert_record(api_handle=api_handle, table_name='users', record_dict=record_dict)


def update_users(api_handle: api_handler, record_id: int, record_dict: dict):
    return update_record_by_id(api_handle=api_handle, table_name='users', record_id=record_id, record_dict=record_dict)


def delete_users(api_handle: api_handler, record_id: int):
    return delete_record_by_id(api_handle=api_handle, table_name='users', record_id=record_id)