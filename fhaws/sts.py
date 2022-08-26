# quick function to role chain into a child account
# can use as standalone or within loop to perform operations each child assoc w/ acct profile"
# uses parent account of pre-configured profile
def role_chain(profile, role, child_account):
    from fhaws.org import getaccounts
    import boto3
    acctlist = getaccounts('default')
    for acct in acctlist:
        if (acct['Name']) == child_account:
            child_account_id = (acct['Id'])
        elif (acct['Id']) == child_account:
            child_account_id = child_account
    sts_client = boto3.client('sts')
    assumed_role_object = sts_client.assume_role(
            RoleArn=str("arn:aws:iam::" + child_account_id + ":role/" + role),
            RoleSessionName="AssumeRoleSession")
    return assumed_role_object