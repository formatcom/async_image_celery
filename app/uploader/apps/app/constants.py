UPLOADING_STATUS = 'UPLOADING'
UPLOAD_STATUS = 'UPLOAD'
INITIAL_STATUS = 'CREATED'
FAIL_STATUS = 'FAIL'
FAIL_RESPONSE = {'error': 'No se permite esta operacion'}

CHOICES_STATUS = (
    (UPLOAD_STATUS, UPLOAD_STATUS),
    (UPLOAD_STATUS, UPLOAD_STATUS),
    (FAIL_STATUS, FAIL_STATUS),
    (INITIAL_STATUS, INITIAL_STATUS)
)