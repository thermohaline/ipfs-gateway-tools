from is_ipfs import Validator
from typing import Union


class IpfsGatewayTools:
    def __init_(self):
        return

    def contains_CID(self, url: str) -> Union[bool, str]:
        split_url = url.split("/")

        for split in split_url:
            if Validator(split).is_ipfs():
                return True, split

            elif Validator(split.split(".")[0]).is_ipfs():
                return True, split.split(".")[0]

        return False, None

    def convert_to_desired_gateway(
        self, source_url: str, desired_gateway_prefix: str
    ) -> str:
        result, cid = self.contains_CID(source_url)

        if result != True:
            raise ValueError("Url does not contain CID")

        split_url = source_url.split(cid)

        if f"ipfs://{cid}" in source_url:
            return f"{desired_gateway_prefix}/ipfs/{cid}{split_url[1]}"

        elif f"/ipfs/{cid}" in source_url:
            return f"{desired_gateway_prefix}/ipfs/{cid}{split_url[1]}"

        elif f"/ipns/{cid}" in source_url:
            return f"{desired_gateway_prefix}/ipns/{cid}{split_url[1]}"

        else:
            raise ValueError(
                "Unsupported URL pattern, please submit a github issue with the URL utilized"
            )
