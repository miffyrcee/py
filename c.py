import base64


def safe_base64_decode(s):  # 解码
    try:
        if len(s) % 4 != 0:
            s = s + '=' * (4 - len(s) % 4)
        base64_str = base64.urlsafe_b64decode(s)
        return bytes.decode(base64_str)
    except Exception as e:
        print('解码错误')


print(
    safe_base64_decode(
        'aHVnLm1lbmdkaS5pbms6MTgwMzpvcmlnaW46cmM0LW1kNTpodHRwX3NpbXBsZTpSMU5JWjNSNWVYSTRhSE0vP29iZnNwYXJhbT1OV1V5T0RRNU5qRTJPUzU2YUdGdmFpNXBiZyZwcm90b3BhcmFtPU9UWXhOams2UjIxQldXUnYmcmVtYXJrcz02YWFaNXJpdkxURWdXMU5JWFEmZ3JvdXA9U0U5TlJTMU5SVTVIUkVrdFEyeHZkV1FzYkc1akxn'
    ))
