# IPFS Gateway Tools

IPFS Gateway Tools

## Overview

This toolkit contains helper functions for working with IPFS gateway URLs and transforming them as desired.

This package comes with a distributions for the browser and for NodeJS. Take care to ensure you are importing or requiring in the right version.


## Browser Setup

To require this in your project simply include the library at the top of your file like so:

```python
from ipfs_parser import IpfsGatewayTools
gateway_tools = IpfsGatewayTools()
```

## Usage

The IPFS gateway toolkit currently contains the following functions:

- [contains_CID](#containsCID-anchor)
- [convert_to_desired_gateway](#convertToDesiredGateway-anchor)

<a name="contains_cid-anchor"></a>

### contains_cid

##### `IpfsGatewayTools.contains_cid(url)`

##### Params

- `url` - A gateway url that should take one of the following forms:
  - `ipfs://CID`
  - `ipfs://ipfs/CID`
  - `https://example-gateway.com/ipfs/CID`
  - `https://example-gateway.com/ipfs/CID/exampleFile.json`
  - `https://example-gateway.com/ipns/CID`

#### Response

```
{
    contains_cid: (Boolean) - True if the url contains a CID,
    cid: (string) - The CID that the url contains if "containsCid" is true
}
```

<a name="convertToDesiredGateway-anchor"></a>

### convert_to_desired_gateway

##### `ipfsGatewayTools.convert_to_desired_gateway(source_url, desired_gateway_prefix)`

##### Params

- `source_url` - A gateway url that should take one of the following forms:
  - `ipfs://CID`
  - `ipfs://ipfs/CID`
  - `https://example-gateway.com/ipfs/CID`
  - `https://example-gateway.com/ipfs/CID/exampleFile.json`
  - `https://example-gateway.com/ipns/CID`
- `desired_gateway_prefix` - The desired gateway you want to convert your source URL to. A few examples of this would be:
  - `https://mygateway.mypinata.cloud`
  - `https://ipfs.io`

#### Response

Returns a string that uses the desired source gateway prefix.

Example code:

```python
from ipfs_parser import IpfsGatewayTools

gateway_tools = IpfsGatewayTools()

source_url = "https://exampleGateway.com/ipfs/bafybeifx7yeb55armcsxwwitkymga5xf53dxiarykms3ygqic223w5sk3m"
desired_gateway_prefix = "https://mygateway.mypinata.cloud"
converted_gateway_url = gateway_tools.convert_to_desired_gateway(
    source_url, desired_gateway_prefix
)

print(converted_gateway_url)

# In the example above, the resulting value for convertedGatewayUrl would be: https://mygateway.mypinata.cloud/ipfs/bafybeifx7yeb55armcsxwwitkymga5xf53dxiarykms3ygqic223w5sk3m
```

## Questions? Issues? Suggestions?

Feel free to file a github issue or email us at team@pinata.cloud

We'd love to hear from you!
