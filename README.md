# who-logged-in-aws
---

* This lambda function records who has logged in in the last five minutesk, and sends it to CloudWatch for viewing.
  * We use Grafana tables to view who has logged into AWS across various accounts.

* Example:
```
aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventName,AttributeValue=ConsoleLogin
```

## Setup
`npm install -g serverless`

## Deploy
```
saml2aws login
export AWS_PROFILE=saml
```

or

```
export AWS_ACCESS_KEY_ID=<>
export AWS_SECRET_ACCESS_KEY=<>
export AWS_DEFAULT_REGION=<some region>
export AWS_PROFILE=default
```

* Edit `serverless.yaml` for project specific values..

```
cd ./rds-expiry-checks

# Deploy everything
serverless deploy -v

# Deploy just the function
serverless deploy function -f whos-logged-in 
```

* Invoke:
```
serverless invoke -f whos-logged-in -l -v
