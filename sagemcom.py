import asyncio
import json
import os
from sagemcom_api.client import SagemcomClient
from sagemcom_api.enums import EncryptionMethod
from sagemcom_api.exceptions import NonWritableParameterException

from dotenv import load_dotenv

load_dotenv()

HOST = "192.168.1.1"
USERNAME = "admin"
ENCRYPTION_METHOD = EncryptionMethod.MD5

async def main() -> None:
    async with SagemcomClient(HOST, USERNAME, os.getenv('sc'), ENCRYPTION_METHOD) as client:
        try:
            await client.login()
        except Exception as exception:  # pylint: disable=broad-except
            print(exception)
            return

        # device_info = await client.get_device_info()
        # print(f"{device_info.id} {device_info.model_name}")

        # devices = await client.get_hosts()
        # for device in devices:
            # if device.active:
                # print(f"{device.name} - {device.ip_address}")

        # Retrieve values via XPath notation, output is a dict
        # custom_command_output = await client.get_value_by_xpath("Device/UserInterface/AdvancedMode")
        custom = await client.get_value_by_xpath("Device/UserInterface")
        print(1,json.dumps(custom, indent=4))
        # Set value via XPath notation and catch specific errors
        try:
            custom_command_output = await client.set_value_by_xpath("Device/UserInterface/AdvancedMode", "true")
        except NonWritableParameterException as exception:  # pylint: disable=broad-except
            print("AdvancedMode not allowed")
            return

        # print(2,custom_command_output)

asyncio.run(main())