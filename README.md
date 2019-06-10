# who-logged-in-aws
---

* This lambda function records who has logged in in the last five minutesk, and sends it to CloudWatch for viewing.
  * We use Grafana tables to view who has logged into AWS across various accounts.

* Example:
`aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventName,AttributeValue=ConsoleLogin`
