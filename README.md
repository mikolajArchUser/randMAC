# randMAC

repo: https://github.com/mikolajArchUser/randMAC.git

Little python package to quickly change MAC address on linux systems

## Installing

To clone the repo run:

```
git clone https://github.com/mikolajArchUser/randMAC.git
```

Then go to the downloaded repo with:
```
cd randMAC
```

And install the package with:
```
pip install .
```

## Running

You can test if the script is installed correctly by running this script:

```
import randMAC as randmac

print(randmac.generate_mac())
```

This should output a random MAC address :)
