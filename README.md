# boschshcpy(_1st-shot)
**Warning: This package is deprecated and will be deleted soon. Please follow the new package [boschshcpy](https://github.com/tschamm/boschshcpy)**

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
