# youth-fire-fighters-24h-practise-alerting-system
In this repo a software is provided which is used by the youth fire fighters for the 24 hours practise. 
First, a configuration can be created and then the software "alarms" at the specified times to simulate real operations.

## structure of config.json

```json
[{
    "numberOfOperations": int
  },
  {
  "operationNumber": int,
  "operationDescription": string,
  "address": string,
  "operationDate": date
  "operationTime": time,
  "1-19": boolean,
  "1-42": boolean,
  "2-42": boolean,
  "3-48": boolean,
  "oil": boolean,
  "hoseCart": boolean,
  "drk": boolean,
  "police": boolean
},
...]
```
