In this page, you will configure your Google Cloud profile.

You need to 
   
* Create a cloud storage bucket to store the resultant images
    * Login to Google Cloud Console.
    * Search for __Cloud Storage__ product.
    * Here your should see the list of buckets.
    * Now either, you create a new bucket or use the existing bucket.
    * Lets say, we will create a new bucket.
    * Now click on the `CREATE BUCKET` to create a new bucket.
    * Enter the bucket name, say __radongcs__ for this webinar.
    * Leave rest of the configuration to default and hit `CREATE` button.

* Get the essential credentials
    * Go to [Google Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)
    * Select the project
    * Under `Actions` (three dots) -> `Manage keys` -> `Create new key` -> `JSON` -> `CREATE`
    * Now the credential json will be downloaded. Save it somewhere.