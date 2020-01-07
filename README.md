# boschshcpy
Python3 package to access Bosch Smart Home Components (see https://github.com/BoschSmartHome/bosch-shc-api-docs)

## Usage guide:
Before accessing the Bosch Smart Home Components, a client has to be registered on the controller. For this, a cert/key pair has to be provided to the controller. For starting the registration, press and hold the button on the controller until the led starts flashing.

The usage example will generate a cert/key pair and registers the client on the on the controller:
```bash
cd examples && mkdir keystore
python3 apitest.py -pw "Your base64 encoded controller password" -ac keystore/test-cert.pem -ak keystore/test-key.pem -n "Your Application" -ip "IP of the controller"
```

## Examples
When using the other provided example code, make sure to update the ip address of the Smart Home Controller inside the scripts.

More documentation to follow.
