aws_policy={
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "FirstStatement",
      "Effect": "Allow",
      "Action": ["iam:ChangePassword"],
      "Resource": "*"
    },
    {
      "Sid": "SecondStatement",
      "Effect": "Allow",
      "Action": "s3:ListAllMyBuckets",
      "Resource": "*"
    },
    {
      "Sid": "ThirdStatement",
      "Effect": "Allow",
      "Action": [
        "s3:List*",
        "s3:Get*"
      ],
      "Resource": [
        "arn:aws:s3:::amzn-s3-demo-bucket-confidential-data",
        "arn:aws:s3:::amzn-s3-demo-bucket-confidential-data/*"
      ],
      "Condition": {"Bool": {"aws:MultiFactorAuthPresent": "true"}}
    }
  ]
}

print(aws_policy)
print("\n")
print(aws_policy["Version"])
print("\n")
print(aws_policy["Statement"][0]["Sid"])
print("\n")
print(aws_policy["Statement"][1]["Effect"])
print("\n")
print(aws_policy["Statement"][2]["Sid"])
print("\n")
print(aws_policy["Statement"][2]["Action"][0])
print("\n")
print(aws_policy["Statement"][2]["Resource"])
print("\n")
print(aws_policy["Statement"][2]["Condition"])
print("\n")
print(aws_policy["Statement"][2]["Condition"]["Bool"])
print("\n")
print(aws_policy["Statement"][2]["Condition"]["Bool"]["aws:MultiFactorAuthPresent"])
