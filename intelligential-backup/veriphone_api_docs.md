[Skip to main content](https://developer.veriph.one/api#__docusaurus_skipToContent_fallback)

- Introduction
- OpenAPI Specification
- Authentication
- Versioning
- 1\. SDK Integration
  - postStart a verification session
  - getGet verification result (v1.0.0)
  - getGet verification result (v1.1.0)
- 2\. Helper Services
  - getGet phone country codes
  - postSend a non-SDK OTP
- 3\. Identity Validation
  - postProof of address validation (OCR + Attestation)
  - postProof of address OCR (v1.0.0)
  - postProof of address attestation
  - postTax ID validation
  - postEducation history search
- 4\. Insights
  - postPhone number insights
  - postEmail analysis and insights
  - postIP address analysis and insights
  - postGeolocation insights and area analysis
  - postDigital footprint search
- 5\. Misc
  - getHealth Check

[![redocly logo](https://cdn.redoc.ly/redoc/logo-mini.svg)API docs by Redocly](https://redocly.com/redoc/)

# Veriph.One's API (1.X.X)

Download OpenAPI specification: [Download](https://service.veriph.one/swagger-yaml)

This is the documentation for Veriph.One's integration and service APIs. You can find more information about our company at [www.veriph.one](https://veriph.one/).

## [section/Introduction](https://developer.veriph.one/api\#section/Introduction) Introduction

This API is grouped into specific categories based on common platform use-cases; for example:

- The **SDK Integration** group is used to make a complete integration with our platform and use all of our verification methods insided your mobile and web apps. This is the most common use case.
- The **Helper Services** section aggregates endpoints used for more complex interactions with our platforms where you want to go beyond our SDK's functionality.
- The **Identity Validation** category aggregates endpoints relevant to complement identity verifications during a KYC flow.
- The **Insights** bracket helps your company perform deep analysis of a user profile to protect against fraud and identity theft without adding friction to your user experience.
- Lastly, the **Misc** category is used to interact and monitor our infrastructure.

## [section/OpenAPI-Specification](https://developer.veriph.one/api\#section/OpenAPI-Specification) OpenAPI Specification

This API is documented in **OpenAPI format** and can also be explored using Swagger via its [standalone website](https://service.veriph.one/swagger), or its [JSON](https://service.veriph.one/swagger-json) and [YAML](https://service.veriph.one/swagger-yaml) definitions.

## [section/Authentication](https://developer.veriph.one/api\#section/Authentication) Authentication

The endpoints shown here are offered under API-Key-based authentication. Please consider that some endpoints require only your API Key, while others need your Secret as well. Keep your credentials safe and never include them in your code repositories as plain text. Also, don't expose your API Secret to client-side code, as it can be reverse-engineered.

## [section/Versioning](https://developer.veriph.one/api\#section/Versioning) Versioning

Our versioning strategy goes beyond a global API version, and we follow a pattern where endpoints have individual versions instead of the API as a whole. This allows for more versatility and better backwards compatibility. Please consider that only major versions (e.g., v1.X.X or v2.X.X) will be incompatible to endpoints with previous versions.

## [tag/1.-SDK-Integration](https://developer.veriph.one/api\#tag/1.-SDK-Integration) 1\. SDK Integration

## [tag/1.-SDK-Integration/operation/createSession](https://developer.veriph.one/api\#tag/1.-SDK-Integration/operation/createSession) Start a verification session

Create a verification session for the SDK using the configuration of the API Key provide as credentials. It can be further customized by passing the optional `configuration` parameter. Please ensure that the `metadata` object is correctly filled as it is used to configure the user experience and detect fraud. Additionally, if you pass an object to the optional `prefilledPhoneNumber`, you can set up a 2FA/MFA flow or one where the user will need to verify a specific number; this interacts `prefilledPhoneNumber.userCanEdit` to allow them to change the number to be verified.

##### header Parameters

|     |     |
| --- | --- |
| x-api-key<br>required | string<br>Your Veriph.One API Key |

##### Request Body schema: application/json  required

|     |     |
| --- | --- |
| prefilledPhoneNumber | object<br>This object determines whether the verification process will capture an unknown number or do a 2FA/MFA flow with a known one. In case of the latter, the verification will be rejected if the user verifies a different number. |
| metadata<br>required | object<br>Necessary data to detect bots, unique transactions, fraudsters, and user's approximate location. |
| configuration | object<br>Used to setup the verification process based on context provided by your application. |

### Responses

**200**

Phone verification was created successfully and ready to start.

**400**

No API Key provided, credentials invalid, or invalid values in request contents (e.g. body).

**403**

API Key or Client status have made the credentials unusable; or there's an issue with the credentials provided.

post/sdk-api/phone-verification/create-session/v1.0.0

https://service.veriph.one/sdk-api/phone-verification/create-session/v1.0.0

### Request samples

- Payload

Content type

application/json

Copy
Expand all  Collapse all

`{"prefilledPhoneNumber": {"countryCode": "string",

"cellphoneNumber": "string",

"userCanEdit": false

},

"metadata": {"userId": "string",

"userAgent": "string",

"ipAddress": "string"

},

"configuration": {"locale": "en",

"enforceInput": false

}

}`

### Response samples

- 200
- 400
- 403

Content type

application/json

Copy

`{"uuid": "string",

"createdAt": "2019-08-24T14:15:22Z",

"redirectionUrl": "string"

}`

## [tag/1.-SDK-Integration/operation/getVerificationResult](https://developer.veriph.one/api\#tag/1.-SDK-Integration/operation/getVerificationResult) Get verification result (v1.0.0)

Obtain the results of a verification using a session UUID and your API Key credentials. This endpoint should never be called from client-side software to avoid leaking your API Key.

##### query Parameters

|     |     |
| --- | --- |
| sessionUuid<br>required | string |

##### header Parameters

|     |     |
| --- | --- |
| authorization<br>required | string<br>Your Veriph.One API Key Secret; using the Basic auth structure: `Basic XXXX...XXXX` |
| x-api-key<br>required | string<br>Your Veriph.One API Key |

### Responses

**200**

Successful request.

**400**

No API Key provided, credentials invalid, or invalid values in request contents (e.g. body).

**403**

API Key or Client status have made the credentials unusable; or there's an issue with the credentials provided.

get/sdk-api/phone-verification/verification-result/v1.0.0

https://service.veriph.one/sdk-api/phone-verification/verification-result/v1.0.0

### Response samples

- 200
- 400
- 403

Content type

application/json

Copy
Expand all  Collapse all

`{"prefilledCountryCode": "string",

"prefilledPhoneNumber": "string",

"createdAt": "2019-08-24T14:15:22Z",

"closedAt": "2019-08-24T14:15:22Z",

"userId": "string",

"firstSuccessfulAttempt": {"uuid": "string",

"countryCodeInput": "string",

"phoneNumberInput": "string",

"method": 0,

"status": 0,

"createdAt": "2019-08-24T14:15:22Z"

},

"attempts": [{"uuid": "string",\
\
"countryCodeInput": "string",\
\
"phoneNumberInput": "string",\
\
"method": 0,\
\
"status": 0,\
\
"createdAt": "2019-08-24T14:15:22Z"\
\
}\
\
]

}`

## [tag/1.-SDK-Integration/operation/getEnrichedVerificationResult](https://developer.veriph.one/api\#tag/1.-SDK-Integration/operation/getEnrichedVerificationResult) Get verification result (v1.1.0)

Obtain the results of a verification using a session UUID and your API Key credentials. This endpoint should never be called from client-side software to avoid leaking your API Key. Version 1.1.0 also includes data enrichment objects that contain information on the phone number that was verified and the context of the verification process. These data points are optional and can be ommitted to reduce latency.

##### query Parameters

|     |     |
| --- | --- |
| sessionUuid<br>required | string |
| enrichmentType<br>required | number<br>Default: 0<br>Determines the type of enrichment you want to obtain. Take into consideration that if you request all of the data points, the payload will increase in size substantially and latency might be introduced. We recommend only getting the data points you need based on the context around the verification. By default, no enrichment is done. See [catalog of possible values here](https://developer.veriph.one/docs/catalogs#verification-data-enrichment-flags). |

##### header Parameters

|     |     |
| --- | --- |
| authorization<br>required | string<br>Your Veriph.One API Key Secret; using the Basic auth structure: `Basic XXXX...XXXX` |
| x-api-key<br>required | string<br>Your Veriph.One API Key |

### Responses

**200**

Successful request.

**400**

No API Key provided, credentials invalid, or invalid values in request contents (e.g. body).

**403**

API Key or Client status have made the credentials unusable; or there's an issue with the credentials provided.

get/sdk-api/phone-verification/verification-result/v1.1.0

https://service.veriph.one/sdk-api/phone-verification/verification-result/v1.1.0

### Response samples

- 200
- 400
- 403

Content type

application/json

Copy
Expand all  Collapse all

`{"uuid": "string",

"createdAt": "2019-08-24T14:15:22Z",

"closedAt": "2019-08-24T14:15:22Z",

"initialConfiguration": {"prefilledCountryCode": {"countryIsoCode3166_2": "string",

"phoneCode": "string"

},

"prefilledPhoneNumber": "string",

"userId": "string",

"locale": "string",

"enforceInput": true

},

"type": "string",

"result": {"status": 0,

"parsedStatus": {"isOpen": true,

"wasSuccessful": true,

"hasErrors": true,

"errorDestinationMismatch": true,

"errorOriginMismatch": true,

"errorInvalidated": true,

"errorExpired": true,

"errorClientDisabled": true,

"errorMethodTampering": true,

"errorTooManySubmissions": true,

"errorExceededAttemptQuota": true,

"errorUserCancelledAttempt": true

},

"methodUsedSuccessfully": 0,

"verifiedNumber": {"countryCode": {"countryIsoCode3166_2": "string",

"phoneCode": "string"

},

"phoneNumber": "string",

"metadata": {"serviceProvider": {"legalName": "string",

"brandName": "string",

"isRetail": true,

"isB2B": true,

"sellsVirtualNumbers": true,

"sellsSatellitePhones": true,

"isWhiteLabel": true,

"sellsIPTelephony": true,

"sellsVoIP": true,

"sellsVoLTE": true

},

"numberMetadata": {"isGeographic": true,

"geographicData": {"locality": "string",

"municipality": "string",

"state": "string",

"type": 0

},

"nonGeographicData": {"type": 0

}

},

"blacklistMatches": {"publicVirtualNumbers": [{"firstAppearance": "2019-08-24T14:15:22Z",\
\
"lastReport": "2019-08-24T14:15:22Z",\
\
"listName": "string"\
\
}\
\
],

"scammerBlacklists": [{"firstAppearance": "2019-08-24T14:15:22Z",\
\
"lastReport": "2019-08-24T14:15:22Z",\
\
"listName": "string"\
\
}\
\
],

"communityFraudBlacklists": [{"firstAppearance": "2019-08-24T14:15:22Z",\
\
"lastReport": "2019-08-24T14:15:22Z",\
\
"listName": "string"\
\
}\
\
]

},

"knownCapabilities": {"lastSMSReceived": "2019-08-24T14:15:22Z",

"lastSMSSent": "2019-08-24T14:15:22Z",

"lastWhatsAppReceived": "2019-08-24T14:15:22Z",

"lastWhatsAppSent": "2019-08-24T14:15:22Z",

"lastPhoneCallReceived": "2019-08-24T14:15:22Z",

"lastPhoneCallMade": "2019-08-24T14:15:22Z"

}

}

}

},

"verificationMetadata": {"userAgent": "string",

"userIpAddress": "string",

"proxyIpAddress": "string",

"userIpMetadata": {"geolocation": {"city": {"geoNameId": 0,

"localizedName": "string",

"confidence": 0

},

"continent": {"geoNameId": 0,

"localizedName": "string",

"code": "string"

},

"country": {"geoNameId": 0,

"localizedName": "string",

"confidence": 0,

"isoCode": "string"

},

"accuracyRadiusInKm": 0,

"avgIncomeInUSD": 0,

"latitude": 0,

"longitude": 0,

"populationDensity": 0,

"timezone": "string",

"zipCode": "string",

"zipCodeConfidence": 0

},

"ipCountryRegistration": {"geoNameId": 0,

"localizedName": "string",

"confidence": 0,

"isoCode": "string"

},

"ipCountryAssociation": {"geoNameId": 0,

"localizedName": "string",

"confidence": 0,

"isoCode": "string",

"type": "string"

},

"ipCountrySubdivisions": [{"geoNameId": 0,\
\
"localizedName": "string",\
\
"confidence": 0,\
\
"isoCode": "string"\
\
}\
\
],

"autonomousSystemNumber": 0,

"autonomousSystemOrganization": "string",

"connectionType": "string",

"domain": "string",

"externalIpAddress": "string",

"isAnonymous": true,

"isAnonymousVpn": true,

"isHostingProvider": true,

"isPublicProxy": true,

"isResidentialProxy": true,

"isTorExitNode": true,

"ispName": "string",

"mobileCountryCode": "string",

"mobileNetworkCode": "string",

"network": "string",

"organization": "string",

"staticIpScore": 0,

"userCountInLast24Hrs": 0,

"userType": "string"

},

"sessionDuration": 0,

"attempts": [{"uuid": "string",\
\
"method": 0,\
\
"status": 0,\
\
"createdAt": "2019-08-24T14:15:22Z",\
\
"attemptCancellationReason": "string",\
\
"numberUsed": {"countryCode": {"countryIsoCode3166_2": "string",\
\
"phoneCode": "string"\
\
},\
\
"phoneNumber": "string",\
\
"metadata": {"serviceProvider": {"legalName": "string",\
\
"brandName": "string",\
\
"isRetail": true,\
\
"isB2B": true,\
\
"sellsVirtualNumbers": true,\
\
"sellsSatellitePhones": true,\
\
"isWhiteLabel": true,\
\
"sellsIPTelephony": true,\
\
"sellsVoIP": true,\
\
"sellsVoLTE": true\
\
},\
\
"numberMetadata": {"isGeographic": true,\
\
"geographicData": {"locality": "string",\
\
"municipality": "string",\
\
"state": "string",\
\
"type": 0\
\
},\
\
"nonGeographicData": {"type": 0\
\
}\
\
},\
\
"blacklistMatches": {"publicVirtualNumbers": [{"firstAppearance": "2019-08-24T14:15:22Z",\
\
"lastReport": "2019-08-24T14:15:22Z",\
\
"listName": "string"\
\
}\
\
],\
\
"scammerBlacklists": [{"firstAppearance": "2019-08-24T14:15:22Z",\
\
"lastReport": "2019-08-24T14:15:22Z",\
\
"listName": "string"\
\
}\
\
],\
\
"communityFraudBlacklists": [{"firstAppearance": "2019-08-24T14:15:22Z",\
\
"lastReport": "2019-08-24T14:15:22Z",\
\
"listName": "string"\
\
}\
\
]\
\
},\
\
"knownCapabilities": {"lastSMSReceived": "2019-08-24T14:15:22Z",\
\
"lastSMSSent": "2019-08-24T14:15:22Z",\
\
"lastWhatsAppReceived": "2019-08-24T14:15:22Z",\
\
"lastWhatsAppSent": "2019-08-24T14:15:22Z",\
\
"lastPhoneCallReceived": "2019-08-24T14:15:22Z",\
\
"lastPhoneCallMade": "2019-08-24T14:15:22Z"\
\
}\
\
}\
\
},\
\
"messagesReceivedFromUser": [{"sentAt": "2019-08-24T14:15:22Z",\
\
"receivedAt": "2019-08-24T14:15:22Z",\
\
"channel": 0,\
\
"wasOTP": true,\
\
"userWhatsAppProfileName": "string",\
\
"usedThirdPartyIntegration": true\
\
}\
\
],\
\
"messagesSentToUser": [{"sentAt": "2019-08-24T14:15:22Z",\
\
"receivedAt": "2019-08-24T14:15:22Z",\
\
"channel": 0,\
\
"wasOTP": true,\
\
"userWhatsAppProfileName": "string",\
\
"usedThirdPartyIntegration": true\
\
}\
\
]\
\
}\
\
],

"languagesUsed": ["string"\
\
]

}

}`

## [tag/2.-Helper-Services](https://developer.veriph.one/api\#tag/2.-Helper-Services) 2\. Helper Services

## [tag/2.-Helper-Services/operation/getAllCountryCodes](https://developer.veriph.one/api\#tag/2.-Helper-Services/operation/getAllCountryCodes) Get phone country codes

Obtain the full list of country codes including ISO 3166-2 codes.

##### header Parameters

|     |     |
| --- | --- |
| x-api-key<br>required | string<br>Your Veriph.One API Key |

### Responses

**200**

Successful request that returns the list of country codes.

**400**

No API Key provided, credentials invalid, or invalid values in request contents (e.g. body).

**403**

API Key or Client status have made the credentials unusable; or there's an issue with the credentials provided.

get/sdk-api/phone-verification/country-codes/v1.0.0

https://service.veriph.one/sdk-api/phone-verification/country-codes/v1.0.0

### Response samples

- 200
- 400
- 403

Content type

application/json

Copy
Expand all  Collapse all

`[{"uuid": "string",\
\
"phoneCode": "string",\
\
"iso3166Code": "string"\
\
}\
\
]`

## [tag/2.-Helper-Services/operation/sendOTP](https://developer.veriph.one/api\#tag/2.-Helper-Services/operation/sendOTP) Send a non-SDK OTP

This endpoint is a standalone service that allows your application to send OTP messages via SMS, WhatsApp (requires initial setup; contact us for more information), and phone call without using the Veriph.One SDK. Please note that this service has an independent billing scheme (per message sent not successful verification), and by using it you are losing SMS pumping protection and other important security features.

##### header Parameters

|     |     |
| --- | --- |
| authorization<br>required | string<br>Your Veriph.One API Key Secret; using the Basic auth structure: `Basic XXXX...XXXX` |
| x-api-key<br>required | string<br>Your Veriph.One API Key |

##### Request Body schema: application/json  required

|     |     |
| --- | --- |
| countryCode<br>required | string<br>Expected number's country code, without '+' sign or non-numeric characters |
| cellphoneNumber<br>required | string<br>Expected phone number without country code or non-numeric characters |
| channel<br>required | number<br>The channel to use for the message. Values: SMS \[0\], WhatsApp \[1\], Phone Call \[2\]. |
| otpCode<br>required | string<br>The OTP to include in the message template. Enforced string length range: 4-16. Only alphanumeric characters accepted (no diacritics, whitespace or symbols): 0-9, a-z, and A-Z. |
| brandLabel<br>required | string<br>A string ignored for WhatsApp but used for other channels with the purpose of letting the user know who is sending the OTP. Use a short brand/product name, at least 2 characters long. The string might be shortened if space is needed to fit the message inside a single SMS message. The string is shown inside parentheses for SMS; for example, in english: `({brandLabel}) Your verification code is ${otpCode}. Do not share it with others`. For phone calls, the structure is as follows: `Your verification code for ${brandLabel} is ${otpCode}. Do not share it with others.`. |
| locale<br>required | string<br>Default: "en"<br>String determining the language of the message to be sent in ISO 639-1 format. Currently, only `en` and `es` are supported. |
| userAgent<br>required | string or null<br>Used to detect fraudsters, bots, and identity theft; please ensure that you are sending proper values as obtained by your server. |
| ipAddress<br>required | string or null<br>The user's IP address captured by your server. This is a critical data point to detect fraud, offer the best verification methods available, among other operations. |

### Responses

**200**

OTP message was successfully triggered; the SMS/WhatsApp messages was sent or the automated phone call was made.

**400**

No API Key provided, credentials invalid, or invalid values in request contents (e.g. body).

**401**

Your application needs to be setup before using the features you requested; please contact us to assist you.

**402**

Your application is on a free plan or doesn't have sufficient balance to perform the operation. Visit [https://dashboard.veriph.one](https://dashboard.veriph.one/) to fix the issue.

**403**

API Key or Client status have made the credentials unusable; or there's an issue with the credentials provided.

post/standalone/send-otp/v1.0.0

https://service.veriph.one/standalone/send-otp/v1.0.0

### Request samples

- Payload

Content type

application/json

Copy

`{"countryCode": "string",

"cellphoneNumber": "string",

"channel": 0,

"otpCode": "string",

"brandLabel": "string",

"locale": "en",

"userAgent": "string",

"ipAddress": "string"

}`

### Response samples

- 200
- 400
- 401
- 402
- 403

Content type

application/json

Copy

`{"createdAt": "2019-08-24T14:15:22Z",

"countryCode": "string",

"phoneNumber": "string",

"channel": 0,

"locale": "string",

"referenceId": "string"

}`

## [tag/3.-Identity-Validation](https://developer.veriph.one/api\#tag/3.-Identity-Validation) 3\. Identity Validation

## [tag/3.-Identity-Validation/operation/proofOfAddressValidation](https://developer.veriph.one/api\#tag/3.-Identity-Validation/operation/proofOfAddressValidation) Proof of address validation (OCR + Attestation)

Send a PDF or JPG file of a proof-of-address document to extract its contents using Optical Character Recognition (OCR), and, if the type of document is supported, validate its authenticity (attestation) against the company or institution that creates that type of document. Supported types:

- Mexico: OCR (Comisión Federal de Electricidad / CFE, Telmex, Telcel, Megacable, Sky, Izzi) & Attestation (Comisión Federal de Electricidad / CFE).

Please note, the resulting payload and billing will change depending on the the type of document provided and if attestation is supported.

##### header Parameters

|     |     |
| --- | --- |
| authorization<br>required | string<br>Your Veriph.One API Key Secret; using the Basic auth structure: `Basic XXXX...XXXX` |
| x-api-key<br>required | string<br>Your Veriph.One API Key |

##### Request Body schema: application/json  required

|     |     |
| --- | --- |
| transactionUuid | string<br>An optional UUID used to identify a group of identity validation requests as a unique transaction. Used for billing and data-coherence analysis of a single end-user identity. If one isn't provided, a new one will be provided as part of the response if the request was successful and `useTransaction` is set to `true`. |
| useTransaction | boolean<br>A boolean value that governs whether the request will create a request-bundling transaction if `transactionUuid` wasn't provided (ignored otherwise). The default is false. It is recommended to use transactions if you will query multiple web services to validate or obtain insights for a single user's identity; by doing so, you can leverage lower pricing (if your plan allows it) and obtain additional data points and better scoring (as we integrate more sources in our data-coherence analysis). |
| requestUuid | string<br>An optional string containing a UUID provided by your application to leverage idempotency and retrieve the results of the request in case of an interrupted connection. |
| documentB64<br>required | string<br>A PDF document or JPG image of the Proof of Address to validate encoded as a Base64 string. For better performance and reduced response time, use JPG images and keep the file size as small as possible without compromising readability (please keep in mind that that if the image is too small or pixelated, the OCR will fail and the service can have unintended results). Usually a reasonable file size is within 1 to 3 MBs. |
| timeoutInSeconds | number \[ 1 .. 3600 \] <br>An optional value that governs how long the service will wait for an attestation response from the PoA's issuer. If the third-party is under heavy load or facing availability issues, requests can hang or be delayed. If not provided, the service will default to 60 seconds. The value must be an integer between 1 and 3600. |

### Responses

**200**

A successful response after processing the provided Proof of Address document; the result will include:

1. The details obtained from the OCR (if the document type is supported and valid).

2. The results of the attestation against the entity or authority that generates this type of document.

3. A score measuring the similarity of the received document and the emitting authority's records.


**400**

No API Key provided, credentials invalid, or invalid values in request contents (e.g. body).

**402**

Your application is on a free plan or doesn't have sufficient balance to perform the operation. Visit [https://dashboard.veriph.one](https://dashboard.veriph.one/) to fix the issue.

**403**

API Key or Client status have made the credentials unusable; or there's an issue with the credentials provided.

**422**

An error related to the provide file or its contents. For example:

1. The file is empty or not a valid base64 string. Error code 70012.
2. The file is corrupted or unreadable. Error code 70015.
3. The document type is unsupported or invalid. Error code 70011.

post/identity/validation/proof-of-address/v1.0.0

https://service.veriph.one/identity/validation/proof-of-address/v1.0.0

### Request samples

- Payload

Content type

application/json

Copy

`{"transactionUuid": "string",

"useTransaction": true,

"requestUuid": "string",

"documentB64": "string",

"timeoutInSeconds": 1

}`

### Response samples

- 200
- 400
- 402
- 403
- 422

Content type

application/json

Copy
Expand all  Collapse all

`{"transactionUuid": "string",

"validityChecks": {"issuanceDate": {"olderThan60Days": true,

"olderThan90Days": true,

"olderThan120Days": true

},

"paymentExpectedBy": {"olderThan60Days": true,

"olderThan90Days": true,

"olderThan120Days": true

},

"paymentOverdueDate": {"olderThan60Days": true,

"olderThan90Days": true,

"olderThan120Days": true

},

"billingPeriodStartDate": {"olderThan60Days": true,

"olderThan90Days": true,

"olderThan120Days": true

},

"billingPeriodEndDate": {"olderThan60Days": true,

"olderThan90Days": true,

"olderThan120Days": true

}

},

"ocrExtractedData": {"issuer": "CFE",

"clientName": "string",

"address": {"addressLine1": "string",

"references": "string",

"city": "string",

"zipCode": "string",

"neighborhood": "string",

"state": "string"

},

"issuanceDate": "string",

"paymentExpectedBy": "string",

"paymentOverdueDate": "string",

"billingPeriod": "string",

"amountDue": "string",

"serviceDetails": {"cfeServiceDetails": {"serviceNumber": "string",

"rmu": "string",

"barCode": "string",

"meterId": "string",

"priceType": "string",

"multiplier": "string"

},

"telmexServiceDetails": {"barCode": "string",

"invoiceNumber": "string",

"numericalCode": "string",

"phoneNumber": "string"

},

"telcelServiceDetails": {"barCode": "string",

"accountId": "string",

"phoneNumber": "string",

"numericalCode": "string",

"mobilePlanName": "string",

"mobilePlanMonthlyCost": "string"

},

"megacableServiceDetails": {"barCode": "string",

"phoneNumber": "string",

"previousBalance": "string",

"accountId": "string",

"numericalCode": "string"

},

"skyServiceDetails": {"accountId": "string",

"previousBalance": "string",

"phoneNumber": "string",

"invoiceNumber": "string"

},

"izziServiceDetails": {"phoneNumber": "string",

"previousBalance": "string",

"accountId": "string",

"numericalCode": "string"

}

}

},

"basicCoherenceChecks": [{"title": "ServiceNumber",\
\
"successful": true\
\
}\
\
],

"issuerProvidedData": {"invoiceData": {"date": "string",

"invoiceNumber": "string",

"paymentMethodCode": "string",

"items": [{"quantity": "string",\
\
"serviceCode": "string",\
\
"unitCode": "string",\
\
"description": "string",\
\
"amount": "string",\
\
"taxConceptId": "string",\
\
"unitPrice": "string",\
\
"taxes": [{"taxableBase": "string",\
\
"taxAmount": "string",\
\
"taxCode": "string",\
\
"factorType": "string"\
\
}\
\
]\
\
}\
\
],

"issuer": {"name": "string",

"taxRegimeCode": "string",

"rfc": "string"

},

"taxes": {"totalTransferTaxes": "string"

},

"placeOfIssuance": "string",

"paymentMethod": "string",

"currency": "string",

"recipient": {"recipientTaxAddress": "string",

"name": "string",

"recipientTaxRegime": "string",

"rfc": "string",

"cfdiUsage": "string"

},

"series": "string",

"subTotal": "string",

"invoiceType": "string",

"total": "string",

"version": "string"

},

"customerData": {"customer": {"name": "string",

"address": {"addressLine1": "string",

"references": "string",

"city": "string",

"zipCode": "string",

"neighborhood": "string",

"state": "string"

}

},

"cfeServiceData": {"name": "string",

"address": {"addressLine1": "string",

"references": "string",

"city": "string",

"zipCode": "string",

"neighborhood": "string",

"state": "string"

}

}

}

},

"attestationResultCode": "ATTESTATION_UNSUPPORTED",

"validationAnalysis": {"score": 100,

"resultCode": "LIKELY_AUTHENTIC",

"anomaliesFound": [{"type": "FullNameComparison",\
\
"description": "string",\
\
"score": 1,\
\
"fieldDetails": {"label": "name",\
\
"valueFromOcr": "string",\
\
"valueFromIssuingSource": "string",\
\
"distinctness": 1,\
\
"weight": 0\
\
}\
\
}\
\
]

}

}`

## [tag/3.-Identity-Validation/operation/proofOfAddressOcr](https://developer.veriph.one/api\#tag/3.-Identity-Validation/operation/proofOfAddressOcr) Proof of address OCR (v1.0.0)

Note: This service, along with the attestation service, is a split form of the overall Proof of Address validation service; we recommend using that one, unless your use case requires the separation of OCR and attestation processes.

Send a PDF or JPG file of a proof-of-address document to extract its contents using Optical Character Recognition (OCR). Supported types:

- Mexico: OCR (Comisión Federal de Electricidad / CFE, Telmex, Telcel, Megacable, Sky, Izzi).

Please note, the resulting payload and billing will change depending on the the type of document provided.

##### header Parameters

|     |     |
| --- | --- |
| authorization<br>required | string<br>Your Veriph.One API Key Secret; using the Basic auth structure: `Basic XXXX...XXXX` |
| x-api-key<br>required | string<br>Your Veriph.One API Key |

##### Request Body schema: application/json  required

|     |     |
| --- | --- |
| transactionUuid | string<br>An optional UUID used to identify a group of identity validation requests as a unique transaction. Used for billing and data-coherence analysis of a single end-user identity. If one isn't provided, a new one will be provided as part of the response if the request was successful and `useTransaction` is set to `true`. |
| useTransaction | boolean<br>A boolean value that governs whether the request will create a request-bundling transaction if `transactionUuid` wasn't provided (ignored otherwise). The default is false. It is recommended to use transactions if you will query multiple web services to validate or obtain insights for a single user's identity; by doing so, you can leverage lower pricing (if your plan allows it) and obtain additional data points and better scoring (as we integrate more sources in our data-coherence analysis). |
| requestUuid<br>required | string<br>A string containing a UUID provided by your application to leverage idempotency and retrieve the results of the request in case of an interrupted connection. |
| documentB64<br>required | string<br>A PDF document or JPG image of the Proof of Address to validate encoded as a Base64 string. For better performance and reduced response time, use JPG images and keep the file size as small as possible without compromising readability (please keep in mind that that if the image is too small or pixelated, the OCR will fail and the service can have unintended results). Usually a reasonable file size is within 1 to 3 MBs. |

### Responses

**200**

A successful response after processing the provided Proof of Address document; the result will include the details obtained from the OCR (if the document type is supported and valid).

**400**

No API Key provided, credentials invalid, or invalid values in request contents (e.g. body).

**402**

Your application is on a free plan or doesn't have sufficient balance to perform the operation. Visit [https://dashboard.veriph.one](https://dashboard.veriph.one/) to fix the issue.

**403**

API Key or Client status have made the credentials unusable; or there's an issue with the credentials provided.

**422**

An error related to the provide file or its contents. For example:

1. The file is empty or not a valid base64 string. Error code 70012.
2. The file is corrupted or unreadable. Error code 70015.
3. The document type is unsupported or invalid. Error code 70011.

post/identity/validation/proof-of-address/ocr/v1.0.0

https://service.veriph.one/identity/validation/proof-of-address/ocr/v1.0.0

### Request samples

- Payload

Content type

application/json

Copy

`{"transactionUuid": "string",

"useTransaction": true,

"requestUuid": "string",

"documentB64": "string"

}`

### Response samples

- 200
- 400
- 402
- 403
- 422

Content type

application/json

Copy
Expand all  Collapse all

`{"transactionUuid": "string",

"validityChecks": {"issuanceDate": {"olderThan60Days": true,

"olderThan90Days": true,

"olderThan120Days": true

},

"paymentExpectedBy": {"olderThan60Days": true,

"olderThan90Days": true,

"olderThan120Days": true

},

"paymentOverdueDate": {"olderThan60Days": true,

"olderThan90Days": true,

"olderThan120Days": true

},

"billingPeriodStartDate": {"olderThan60Days": true,

"olderThan90Days": true,

"olderThan120Days": true

},

"billingPeriodEndDate": {"olderThan60Days": true,

"olderThan90Days": true,

"olderThan120Days": true

}

},

"ocrExtractedData": {"issuer": "CFE",

"clientName": "string",

"address": {"addressLine1": "string",

"references": "string",

"city": "string",

"zipCode": "string",

"neighborhood": "string",

"state": "string"

},

"issuanceDate": "string",

"paymentExpectedBy": "string",

"paymentOverdueDate": "string",

"billingPeriod": "string",

"amountDue": "string",

"serviceDetails": {"cfeServiceDetails": {"serviceNumber": "string",

"rmu": "string",

"barCode": "string",

"meterId": "string",

"priceType": "string",

"multiplier": "string"

},

"telmexServiceDetails": {"barCode": "string",

"invoiceNumber": "string",

"numericalCode": "string",

"phoneNumber": "string"

},

"telcelServiceDetails": {"barCode": "string",

"accountId": "string",

"phoneNumber": "string",

"numericalCode": "string",

"mobilePlanName": "string",

"mobilePlanMonthlyCost": "string"

},

"megacableServiceDetails": {"barCode": "string",

"phoneNumber": "string",

"previousBalance": "string",

"accountId": "string",

"numericalCode": "string"

},

"skyServiceDetails": {"accountId": "string",

"previousBalance": "string",

"phoneNumber": "string",

"invoiceNumber": "string"

},

"izziServiceDetails": {"phoneNumber": "string",

"previousBalance": "string",

"accountId": "string",

"numericalCode": "string"

}

}

},

"basicCoherenceChecks": [{"title": "ServiceNumber",\
\
"successful": true\
\
}\
\
]

}`

## [tag/3.-Identity-Validation/operation/proofOfAddressAttestation](https://developer.veriph.one/api\#tag/3.-Identity-Validation/operation/proofOfAddressAttestation) Proof of address attestation

Note: This service, along with the OCR service, is a split form of the overall Proof of Address validation service; we recommend using that one, unless your use case requires the separation of OCR and attestation processes.

Trigger the attestation process of a proof-of-address document previously sent to our OCR processing service to validate its authenticity (attestation) against the company or institution that creates that type of document. Supported types:

- Mexico: Attestation (Comisión Federal de Electricidad / CFE).

Please note, the resulting payload and billing will change depending on the the type of document provided and if attestation is supported.

##### header Parameters

|     |     |
| --- | --- |
| authorization<br>required | string<br>Your Veriph.One API Key Secret; using the Basic auth structure: `Basic XXXX...XXXX` |
| x-api-key<br>required | string<br>Your Veriph.One API Key |

##### Request Body schema: application/json  required

|     |     |
| --- | --- |
| transactionUuid | string<br>An optional UUID used to identify a group of identity validation requests as a unique transaction. Used for billing and data-coherence analysis of a single end-user identity. If one isn't provided, a new one will be provided as part of the response if the request was successful and `useTransaction` is set to `true`. |
| useTransaction | boolean<br>A boolean value that governs whether the request will create a request-bundling transaction if `transactionUuid` wasn't provided (ignored otherwise). The default is false. It is recommended to use transactions if you will query multiple web services to validate or obtain insights for a single user's identity; by doing so, you can leverage lower pricing (if your plan allows it) and obtain additional data points and better scoring (as we integrate more sources in our data-coherence analysis). |
| timeoutInSeconds | number \[ 1 .. 3600 \] <br>An optional value that governs how long the service will wait for an attestation response from the PoA's issuer. If the third-party is under heavy load or facing availability issues, requests can hang or be delayed. If not provided, the service will default to 60 seconds. The value must be an integer between 1 and 3600. |
| ocrRequestUuid<br>required | string<br>A string containing the UUID provided by your application to the OCR endpoint. The attestation process will be executed against the information extracted by that service. This service is idempotent, and repeated calls with the same `ocrRequestUuid` will return the same result (unless the result is not ready). |

### Responses

**200**

A successful response after processing the provided Proof of Address document; the response will include the results of the attestation against the entity or authority that generates this type of document and a score measuring the similarity of the received document and the emitting authority's records.

**400**

No API Key provided, credentials invalid, or invalid values in request contents (e.g. body).

**402**

Your application is on a free plan or doesn't have sufficient balance to perform the operation. Visit [https://dashboard.veriph.one](https://dashboard.veriph.one/) to fix the issue.

**403**

API Key or Client status have made the credentials unusable; or there's an issue with the credentials provided.

**412**

An error related to a failed precondition such as a non-existent OCR extraction process for the provided request UUID, an invalid request UUID or an unsupported document type.

post/identity/validation/proof-of-address/attestation/v1.0.0

https://service.veriph.one/identity/validation/proof-of-address/attestation/v1.0.0

### Request samples

- Payload

Content type

application/json

Copy

`{"transactionUuid": "string",

"useTransaction": true,

"timeoutInSeconds": 1,

"ocrRequestUuid": "string"

}`

### Response samples

- 200
- 400
- 402
- 403
- 412

Content type

application/json

Copy
Expand all  Collapse all

`{"transactionUuid": "string",

"issuerProvidedData": {"invoiceData": {"date": "string",

"invoiceNumber": "string",

"paymentMethodCode": "string",

"items": [{"quantity": "string",\
\
"serviceCode": "string",\
\
"unitCode": "string",\
\
"description": "string",\
\
"amount": "string",\
\
"taxConceptId": "string",\
\
"unitPrice": "string",\
\
"taxes": [{"taxableBase": "string",\
\
"taxAmount": "string",\
\
"taxCode": "string",\
\
"factorType": "string"\
\
}\
\
]\
\
}\
\
],

"issuer": {"name": "string",

"taxRegimeCode": "string",

"rfc": "string"

},

"taxes": {"totalTransferTaxes": "string"

},

"placeOfIssuance": "string",

"paymentMethod": "string",

"currency": "string",

"recipient": {"recipientTaxAddress": "string",

"name": "string",

"recipientTaxRegime": "string",

"rfc": "string",

"cfdiUsage": "string"

},

"series": "string",

"subTotal": "string",

"invoiceType": "string",

"total": "string",

"version": "string"

},

"customerData": {"customer": {"name": "string",

"address": {"addressLine1": "string",

"references": "string",

"city": "string",

"zipCode": "string",

"neighborhood": "string",

"state": "string"

}

},

"cfeServiceData": {"name": "string",

"address": {"addressLine1": "string",

"references": "string",

"city": "string",

"zipCode": "string",

"neighborhood": "string",

"state": "string"

}

}

}

},

"attestationResultCode": "ATTESTATION_UNSUPPORTED",

"validationAnalysis": {"score": 100,

"resultCode": "LIKELY_AUTHENTIC",

"anomaliesFound": [{"type": "FullNameComparison",\
\
"description": "string",\
\
"score": 1,\
\
"fieldDetails": {"label": "name",\
\
"valueFromOcr": "string",\
\
"valueFromIssuingSource": "string",\
\
"distinctness": 1,\
\
"weight": 0\
\
}\
\
}\
\
]

}

}`

## [tag/3.-Identity-Validation/operation/taxIdValidation](https://developer.veriph.one/api\#tag/3.-Identity-Validation/operation/taxIdValidation) Tax ID validation

An endpoint that validates a person's tax ID or national ID in the country's governmental official database. Supported types:

- Mexico: RFC or CURP (When using CURP, the tax ID number will be built from scratch and might lead to a lower accuracy).

Please note, the resulting payload and billing will change depending on the the type of ID provided.

##### header Parameters

|     |     |
| --- | --- |
| authorization<br>required | string<br>Your Veriph.One API Key Secret; using the Basic auth structure: `Basic XXXX...XXXX` |
| x-api-key<br>required | string<br>Your Veriph.One API Key |

##### Request Body schema: application/json  required

|     |     |
| --- | --- |
| transactionUuid | string<br>An optional UUID used to identify a group of identity validation requests as a unique transaction. Used for billing and data-coherence analysis of a single end-user identity. If one isn't provided, a new one will be provided as part of the response if the request was successful and `useTransaction` is set to `true`. |
| useTransaction | boolean<br>A boolean value that governs whether the request will create a request-bundling transaction if `transactionUuid` wasn't provided (ignored otherwise). The default is false. It is recommended to use transactions if you will query multiple web services to validate or obtain insights for a single user's identity; by doing so, you can leverage lower pricing (if your plan allows it) and obtain additional data points and better scoring (as we integrate more sources in our data-coherence analysis). |
| requestUuid | string<br>An optional string containing a UUID provided by your application to leverage idempotency and retrieve the results of the request in case of an interrupted connection. |
| searchParams<br>required | object<br>The search parameters for the tax ID validation request. |

### Responses

**200**

A successful response after processing the provided tax ID; the response will include the results of the validation against the country's tax authority.

**400**

No API Key provided, credentials invalid, or invalid values in request contents (e.g. body).

**402**

Your application is on a free plan or doesn't have sufficient balance to perform the operation. Visit [https://dashboard.veriph.one](https://dashboard.veriph.one/) to fix the issue.

**403**

API Key or Client status have made the credentials unusable; or there's an issue with the credentials provided.

post/identity/validation/tax-id/v1.0.0

https://service.veriph.one/identity/validation/tax-id/v1.0.0

### Request samples

- Payload

Content type

application/json

Copy
Expand all  Collapse all

`{"transactionUuid": "string",

"useTransaction": true,

"requestUuid": "string",

"searchParams": {"country": "MX",

"nationalId": "string",

"taxId": "string",

"listsToSearch": ["SAT_Article69"\
\
]

}

}`

### Response samples

- 200
- 400
- 402
- 403

Content type

application/json

Copy
Expand all  Collapse all

`{"transactionUuid": "string",

"normalizedTaxId": "string",

"isValid": true,

"personType": "Individual",

"name": "string",

"mexico": {"canReceiveInvoices": true,

"listSearchResult": {"isBlacklisted": true,

"isRisky": true,

"humanReviewRecommended": true,

"listMatchesForArticle69": [{"listName": "CancelledCredit",\
\
"state": "string",\
\
"dateFirstPublished": "2019-08-24T14:15:22Z",\
\
"yearOfAppearance": "string",\
\
"reasonOrCause": "string",\
\
"riskLevel": "Unknown",\
\
"formattedAssociatedAmount": "string"\
\
}\
\
],

"blacklistMatchForArticle69B": {"status": "Active",

"makesItBlacklisted": true,

"makesItRisky": true,

"dateMarkedAsActivelyBlacklisted": "2019-08-24T14:15:22Z",

"datePublishedAsActivelyBlacklisted": "2019-08-24T14:15:22Z",

"dateMarkedAsUnderInvestigation": "2019-08-24T14:15:22Z",

"datePublishedAsUnderInvestigation": "2019-08-24T14:15:22Z",

"dateMarkedAsRebutted": "2019-08-24T14:15:22Z",

"datePublishedAsRebutted": "2019-08-24T14:15:22Z",

"dateMarkedAsCourtOverturned": "2019-08-24T14:15:22Z",

"datePublishedAsCourtOverturned": "2019-08-24T14:15:22Z"

}

}

}

}`

## [tag/3.-Identity-Validation/operation/educationHistorySearch](https://developer.veriph.one/api\#tag/3.-Identity-Validation/operation/educationHistorySearch) Education history search

A service that searches for a person's educational history (undergrad and postgrad degrees) in the country's governmental official database. Supported countries:

- Mexico (your application can provide a full name (and optional date of birth) or a national ID (CURP) to perform the search).

Please note, the resulting payload and billing will change depending on the the type of data used provided for the search.

##### header Parameters

|     |     |
| --- | --- |
| authorization<br>required | string<br>Your Veriph.One API Key Secret; using the Basic auth structure: `Basic XXXX...XXXX` |
| x-api-key<br>required | string<br>Your Veriph.One API Key |

##### Request Body schema: application/json  required

|     |     |
| --- | --- |
| transactionUuid | string<br>An optional UUID used to identify a group of identity validation requests as a unique transaction. Used for billing and data-coherence analysis of a single end-user identity. If one isn't provided, a new one will be provided as part of the response if the request was successful and `useTransaction` is set to `true`. |
| useTransaction | boolean<br>A boolean value that governs whether the request will create a request-bundling transaction if `transactionUuid` wasn't provided (ignored otherwise). The default is false. It is recommended to use transactions if you will query multiple web services to validate or obtain insights for a single user's identity; by doing so, you can leverage lower pricing (if your plan allows it) and obtain additional data points and better scoring (as we integrate more sources in our data-coherence analysis). |
| requestUuid | string<br>An optional string containing a UUID provided by your application to leverage idempotency and retrieve the results of the request in case of an interrupted connection. |
| searchParams<br>required | object<br>The search parameters for the education history search request. Please note that using national ID for the search will incur in additional costs. |
| options | object<br>An optional object that contains configuration options for the search operation, such as the timeout or whether to use the cache or not. |

### Responses

**200**

A successful response after performing the search; the response will include the available results from the country's governmental official database.

**400**

No API Key provided, credentials invalid, or invalid values in request contents (e.g. body).

**402**

Your application is on a free plan or doesn't have sufficient balance to perform the operation. Visit [https://dashboard.veriph.one](https://dashboard.veriph.one/) to fix the issue.

**403**

API Key or Client status have made the credentials unusable; or there's an issue with the credentials provided.

**408**

The search request exceeded the configured timeout. Consider retrying with a higher `options.timeoutInSeconds` value or enable `options.useCache` to fall back to a previously cached result when available.

**424**

The educational records service is currently unreachable or undergoing maintenance. Retry later; if caching is enabled, a previously cached result may still be returned as part of a 200 response.

**500**

An unexpected error occurred while communicating with the external records service. Retry later.

post/identity/validation/education-history/search/v1.0.0

https://service.veriph.one/identity/validation/education-history/search/v1.0.0

### Request samples

- Payload

Content type

application/json

Copy
Expand all  Collapse all

`{"transactionUuid": "string",

"useTransaction": true,

"requestUuid": "string",

"searchParams": {"country": "MX",

"nationalId": "string",

"identity": {"firstName": "string",

"middleName": "string",

"firstSurname": "string",

"secondSurname": "string",

"dateOfBirth": "string",

"gender": "Male"

},

"enrichNationalId": true

},

"options": {"useCache": true,

"staleThresholdInDays": null,

"timeoutInSeconds": 3

}

}`

### Response samples

- 200
- 400
- 402
- 403
- 408
- 424
- 500

Content type

application/json

Copy
Expand all  Collapse all

`{"transactionUuid": "string",

"searchResults": [{"nameOrNames": "string",\
\
"firstSurname": "string",\
\
"secondSurname": "string",\
\
"dateOfBirth": "string",\
\
"gender": "Male",\
\
"nationalId": "string",\
\
"placeOfBirth": "string",\
\
"matchConfidenceLevel": "Low",\
\
"academicDegrees": [{"professionalLicenseNumber": "string",\
\
"professionalLicenseType": "string",\
\
"issueDate": "2019-08-24T14:15:22Z",\
\
"registrationYear": "string",\
\
"isHigherEducation": true,\
\
"isUndergraduate": true,\
\
"isPostgraduate": true,\
\
"title": "string",\
\
"issuer": "string",\
\
"issuerLocation": "string",\
\
"knowledgeArea": "string",\
\
"graduationDate": "2019-08-24T14:15:22Z"\
\
}\
\
]\
\
}\
\
],

"metadata": {"searchPerformed": true,

"error": {"code": 0,

"message": "string"

},

"identityUsedForSearch": {"nameOrNames": "string",

"firstSurname": "string",

"secondSurname": "string",

"dateOfBirth": "string",

"nationalId": "string",

"gender": "Male",

"placeOfBirth": "Aguascalientes"

},

"usedCacheTimestamp": "2019-08-24T14:15:22Z"

}

}`

## [tag/4.-Insights](https://developer.veriph.one/api\#tag/4.-Insights) 4\. Insights

## [tag/4.-Insights/operation/phoneInsights](https://developer.veriph.one/api\#tag/4.-Insights/operation/phoneInsights) Phone number insights

This endpoint is our most complete phone insights service that allows your application to get critical data on a phone number. It can be used to better understand user profiles, feed risk and credit models, stop fraud, detect hackers, and more. Please note that this service has an independent billing scheme. Finally, this service is only available to paid plans and accounts with a minimum balance of 1 USD.

##### header Parameters

|     |     |
| --- | --- |
| authorization<br>required | string<br>Your Veriph.One API Key Secret; using the Basic auth structure: `Basic XXXX...XXXX` |
| x-api-key<br>required | string<br>Your Veriph.One API Key |

##### Request Body schema: application/json  required

|     |     |
| --- | --- |
| transactionUuid | string<br>An optional UUID used to identify a group of identity validation requests as a unique transaction. Used for billing and data-coherence analysis of a single end-user identity. If one isn't provided, a new one will be provided as part of the response if the request was successful and `useTransaction` is set to `true`. |
| useTransaction | boolean<br>A boolean value that governs whether the request will create a request-bundling transaction if `transactionUuid` wasn't provided (ignored otherwise). The default is false. It is recommended to use transactions if you will query multiple web services to validate or obtain insights for a single user's identity; by doing so, you can leverage lower pricing (if your plan allows it) and obtain additional data points and better scoring (as we integrate more sources in our data-coherence analysis). |
| requestUuid | string<br>An optional string containing a UUID provided by your application to leverage idempotency and retrieve the results of the request in case of an interrupted connection. |
| dataPackages<br>required | Array of strings<br>Items Enum:"standard""pro""premium""live-data-3""id-verification"<br>The desired data bundles to return in the form of a string array, please consider that this is directly linked to pricing and omitting a package will return some fields as null. Morever, including a package might increase the cost of your request and make it slower (as more data is queried and generated). Contact your sales representative for more details. |
| phoneNumber<br>required | object or null<br>The phone number to obtain insights from. It can be provided as a string in E.164 format (e.g., +14155552671) or an object containing the country code and number separately. |
| configuration | object or null<br>An object used to configure the data to return. Mandatory for the premium package, ignored for others. |

### Responses

**200**

Insights data was successfully retrieved; the body of the response includes the payload with known information.

**400**

No API Key provided, credentials invalid, or invalid values in request contents (e.g. body).

**402**

Your application is on a free plan or doesn't have sufficient balance to perform the operation. Visit [https://dashboard.veriph.one](https://dashboard.veriph.one/) to fix the issue.

**403**

API Key or Client status have made the credentials unusable; or there's an issue with the credentials provided.

**423**

Your application is requesting access to a data package that requires additional configuration or approval. Contact [support@veriph.one](mailto:support@veriph.one) for assistance.

post/insights/phone/v1.2.1

https://service.veriph.one/insights/phone/v1.2.1

### Request samples

- Payload

Content type

application/json

Copy
Expand all  Collapse all

`{"transactionUuid": "string",

"useTransaction": true,

"requestUuid": "string",

"dataPackages": ["standard"\
\
],

"phoneNumber": {"ituFormatedPhoneNumber": "string",

"splitPhoneNumber": {"countryCode": "string",

"phoneNumber": "string"

}

},

"configuration": {"carrierScores": {"returnAllScores": true,

"requestedScores": ["activityLevel"\
\
]

}

}

}`

### Response samples

- 200
- 400
- 402
- 403
- 423

Content type

application/json

Copy
Expand all  Collapse all

`{"transactionUuid": "string",

"countryIsoCode3166_2": "string",

"phoneCode": "string",

"phoneNumber": "string",

"serviceProvider": {"legalName": "string",

"brandName": "string",

"isRetail": true,

"isB2B": true,

"sellsVirtualNumbers": true,

"sellsSatellitePhones": true,

"isWhiteLabel": true,

"sellsIPTelephony": true,

"sellsVoIP": true,

"sellsVoLTE": true,

"mobileCountryCode": "string",

"mobileNetworkCode": "string"

},

"carrierIdentityVerificationStatus": "NOT_VERIFIED",

"placeOfRegistration": {"locality": "string",

"municipality": "string",

"state": "string"

},

"lineType": "string",

"liveDataTier1": {"isValid": "string",

"isActive": "string"

},

"liveDataTier2": {"isVoIp": true,

"isPrepaid": true,

"lineSubtype": 0,

"listedOnDNC": true

},

"liveDataTier3": {"accountBalance": 152.75,

"totalCostOfServices": 599,

"totalCostOfServicesConfidence": "high",

"hasServiceLoan": false,

"hasPrepaidSelfRenewal": true,

"inferredUnassigned": false,

"inferredTargetUser": "individual",

"inferredUnlimitedData": false,

"hasActiveService": true,

"dataPackageSize": "above_average",

"percentageOfDataUsed": 42,

"sumOfDataUsed": 420,

"sumOfDataRemaining": 420,

"sumOfDataIncluded": 420,

"hasMobileDataAvailable": true,

"currentUsageLevel": "expected",

"currentUsageLevelConfidence": "high",

"isDataAllowanceDepleted": false,

"includesPlanAllowance": true,

"includesAddon": true,

"includesTopUp": false,

"daysLeftInCycle": 14.25,

"activeServicePackages": [{"paymentType": "generic_postpaid",\
\
"type": "mobile",\
\
"targetUser": "individual",\
\
"billingModel": "monthly",\
\
"cost": {"amount": 299,\
\
"characterization": "average",\
\
"currency": "MXN"\
\
},\
\
"dataPackageSize": "large",\
\
"hasUnlimitedData": false,\
\
"hasSpendingCap": true,\
\
"activationType": "renewal",\
\
"paymentMethod": "credit_card",\
\
"isDeprecatedOrLegacy": false\
\
}\
\
]

},

"portability": {"portsInLastThreeYears": 0,

"wasPorted": true,

"originalCarrier": {"legalName": "string",

"brandName": "string",

"isRetail": true,

"isB2B": true,

"sellsVirtualNumbers": true,

"sellsSatellitePhones": true,

"isWhiteLabel": true,

"sellsIPTelephony": true,

"sellsVoIP": true,

"sellsVoLTE": true,

"mobileCountryCode": "string",

"mobileNetworkCode": "string"

}

},

"riskAndFraudScoring": {"fraudScore": 0,

"recentAbuse": true,

"isRisky": true,

"wasLeaked": true,

"reportedAsSpam": true

},

"associatedIdentities": {"knownNames": ["string"\
\
],

"associatedEmails": ["string"\
\
]

},

"linkedIpAddresses": {"dateOfFirstAppearance": "2019-08-24T14:15:22Z",

"associatedIpAddresses": [{"ipAddress": "string",\
\
"metadata": { },\
\
"dateOfLastUsage": "2019-08-24T14:15:22Z",\
\
"usageCount": 0\
\
}\
\
]

},

"blacklistMatches": {"publicVirtualNumbers": [{"firstAppearance": "2019-08-24T14:15:22Z",\
\
"lastReport": "2019-08-24T14:15:22Z",\
\
"listName": "string"\
\
}\
\
],

"scammerBlacklists": [{"firstAppearance": "2019-08-24T14:15:22Z",\
\
"lastReport": "2019-08-24T14:15:22Z",\
\
"listName": "string"\
\
}\
\
],

"communityFraudBlacklists": [{"firstAppearance": "2019-08-24T14:15:22Z",\
\
"lastReport": "2019-08-24T14:15:22Z",\
\
"listName": "string"\
\
}\
\
]

},

"knownCapabilities": {"lastSMSReceived": "2019-08-24T14:15:22Z",

"lastSMSSent": "2019-08-24T14:15:22Z",

"lastWhatsAppReceived": "2019-08-24T14:15:22Z",

"lastWhatsAppSent": "2019-08-24T14:15:22Z",

"lastPhoneCallReceived": "2019-08-24T14:15:22Z",

"lastPhoneCallMade": "2019-08-24T14:15:22Z"

},

"telcoScoring": {"postpaidInsights": {"usageLevel": 1,

"creditLimit": 1,

"hasDirectDebit": true

},

"prepaidInsights": {"topUpVolume": 1,

"topUpFrequency": 1

},

"activityLevel": 1,

"simCardChangeRate": 1,

"usageTrend": 1,

"contactNetwork": 1,

"userRating": 1,

"reachabilityScore": 1,

"techAdoption": 1,

"fraudScore": 1,

"riskScore": 1,

"insightsSummary": {"riskAssessment": {"fraudLikelihood": {"level": "low",

"confidence": "high"

},

"creditRiskLevel": {"level": "low",

"confidence": "high"

},

"realIdentityConfidence": {"level": "high",

"confidence": "high"

}

},

"profileClassification": {"subscriberProfile": {"profile": "standard_active",

"confidence": "high"

},

"financialCapacityIndicator": {"level": "moderate",

"confidence": "high"

},

"reachabilityAnalysis": {"level": "moderately_reachable",

"confidence": "high"

}

},

"behavioralFlags": {"constantSimChange": false,

"decliningUsage": false,

"isHighValue": false,

"isLowValue": false,

"lowReachability": false,

"rapidUsageGrowth": false,

"highTechProfile": false,

"lowTechProfile": false,

"seemsRisky": false

}

}

}

}`

## [tag/4.-Insights/operation/emailInsights](https://developer.veriph.one/api\#tag/4.-Insights/operation/emailInsights) Email analysis and insights

This service analyzes an email address to generate relevant data points on the risk of interacting with it; ranging from detecting disposable accounts, flagging fraudlent and malicious addresses, and obtaining behavioral information.
Please note that this service has an independent billing scheme and each search type has a different pricing. Finally, this service is only available to paid plans and accounts with a minimum balance of 1 USD.

##### header Parameters

|     |     |
| --- | --- |
| authorization<br>required | string<br>Your Veriph.One API Key Secret; using the Basic auth structure: `Basic XXXX...XXXX` |
| x-api-key<br>required | string<br>Your Veriph.One API Key |

##### Request Body schema: application/json  required

|     |     |
| --- | --- |
| transactionUuid | string<br>An optional UUID used to identify a group of identity validation requests as a unique transaction. Used for billing and data-coherence analysis of a single end-user identity. If one isn't provided, a new one will be provided as part of the response if the request was successful and `useTransaction` is set to `true`. |
| useTransaction | boolean<br>A boolean value that governs whether the request will create a request-bundling transaction if `transactionUuid` wasn't provided (ignored otherwise). The default is false. It is recommended to use transactions if you will query multiple web services to validate or obtain insights for a single user's identity; by doing so, you can leverage lower pricing (if your plan allows it) and obtain additional data points and better scoring (as we integrate more sources in our data-coherence analysis). |
| requestUuid | string<br>An optional string containing a UUID provided by your application to leverage idempotency and retrieve the results of the request in case of an interrupted connection. |
| configuration<br>required | object or null<br>Options and potential configurations for your request that determine sensitivity levels and the type of analysis you want to perform. Sending this value as null will set all of the underlying properties to their defaults. |
| email<br>required | string<br>The email address that you want to analyze and obtain insights from. |

### Responses

**200**

Successful request, the results of the analysis and its insights are available in the response's body.

**400**

No API Key provided, credentials invalid, or invalid values in request contents (e.g. body).

**402**

Your application is on a free plan or doesn't have sufficient balance to perform the operation. Visit [https://dashboard.veriph.one](https://dashboard.veriph.one/) to fix the issue.

**403**

API Key or Client status have made the credentials unusable; or there's an issue with the credentials provided.

post/insights/email/v1.0.0

https://service.veriph.one/insights/email/v1.0.0

### Request samples

- Payload

Content type

application/json

Copy
Expand all  Collapse all

`{"transactionUuid": "string",

"useTransaction": true,

"requestUuid": "string",

"configuration": {"smtpCheck": {"timeoutInSeconds": 1

},

"strictness": {"abuse": "STRICTEST",

"spamAndHoneypot": "STRICTEST"

}

},

"email": "string"

}`

### Response samples

- 200
- 400
- 402
- 403

Content type

application/json

Copy
Expand all  Collapse all

`{"transactionUuid": "string",

"normalizedEmail": "string",

"potentiallyCorrectDomain": "string",

"basicChecks": {"isFormatValid": true,

"isCommon": true,

"isGeneric": true,

"isDisposable": true,

"wasRecentlyLeaked": true,

"isCatchAll": true,

"isValidAndReachable": true,

"canReceiveEmail": true,

"isValidAndVerified": true

},

"traits": {"deliverabilityLevel": "high",

"emailUsageLevel": "high",

"dateFirstSeen": "2019-08-24T14:15:22Z",

"isFrequentComplainer": true

},

"linkedIdentities": {"name": "string",

"isLikelyCorporateEmail": true,

"knownNamesAndAliases": ["string"\
\
],

"knownPhoneNumbers": ["string"\
\
]

},

"riskAnalysis": {"isValiditySuspicious": true,

"spamTrapLikelihood": "high",

"usesRiskyTld": true,

"hasCommittedRecentAbuse": true,

"isHoneypot": true,

"domainTrustLevel": "trusted",

"fraudScore": 0

},

"technicalTraits": {"smtpServerTimedOut": true,

"isDnsValid": true,

"wasDeliverabilityTestRejected": true,

"hasProperSpfRecord": true,

"hasProperDmarcRecord": true,

"mxRecords": ["string"\
\
],

"aRecords": ["string"\
\
],

"domainLegitimacyLevel": "high",

"domainRegistrationDate": "2019-08-24T14:15:22Z"

}

}`

## [tag/4.-Insights/operation/ipAddressInsights](https://developer.veriph.one/api\#tag/4.-Insights/operation/ipAddressInsights) IP address analysis and insights

This service analyzes an IP address and web interaction metadata (user agent, language headers) to generate relevant data points on the risk of interacting with it; ranging from anonymous connections, flagging fraudlent and malicious addresses, and obtaining behavioral information. The process also returns information about the IP address's geolocation and performs reverse geocoding.
Please note that this service has an independent billing scheme and each search type has a different pricing. Finally, this service is only available to paid plans and accounts with a minimum balance of 1 USD.

##### header Parameters

|     |     |
| --- | --- |
| authorization<br>required | string<br>Your Veriph.One API Key Secret; using the Basic auth structure: `Basic XXXX...XXXX` |
| x-api-key<br>required | string<br>Your Veriph.One API Key |

##### Request Body schema: application/json  required

|     |     |
| --- | --- |
| transactionUuid | string<br>An optional UUID used to identify a group of identity validation requests as a unique transaction. Used for billing and data-coherence analysis of a single end-user identity. If one isn't provided, a new one will be provided as part of the response if the request was successful and `useTransaction` is set to `true`. |
| useTransaction | boolean<br>A boolean value that governs whether the request will create a request-bundling transaction if `transactionUuid` wasn't provided (ignored otherwise). The default is false. It is recommended to use transactions if you will query multiple web services to validate or obtain insights for a single user's identity; by doing so, you can leverage lower pricing (if your plan allows it) and obtain additional data points and better scoring (as we integrate more sources in our data-coherence analysis). |
| requestUuid | string<br>An optional string containing a UUID provided by your application to leverage idempotency and retrieve the results of the request in case of an interrupted connection. |
| ipAddress<br>required | string<br>The IP address to obtain insights from; must be in IPv4 or IPv6 format. Please note that invalid, reserved, private, or local IP addresses (e.g., 127.0.0.1) will return no information. |
| userAgent | string or null<br>The user agent string associated with the IP address, which we strongly recommend you provide if possible. If sent, we will run additional checks to detect bots and suspicious/invalid browsers. The value is also used to generate the fraud score and can improve scoring accuracy by over 20%. |
| userLanguage | string or null<br>The user's language header associated with the IP address; if provided, the value will improve the resulting fraud score. Example of expected value: en-US. |
| connectionIsMobileApp | boolean<br>Default: false<br>If set to true, the process will ignore the user agent string and treat the IP address as a connection from a mobile app, rather than a browser. Use this field carefully, as it can cause unexpected results if the IP address is not coming from a mobile device. Default value is false. |
| configuration | object<br>A configuration object to override default settings. It is recommended to use this field to fine-tune the insight-generation process. We strongly suggest that if your application is not time-sensitive, you enable forensic checks to obtain the most accurate results. |

### Responses

**200**

Successful request, the results of the analysis and its insights are available in the response's body.

**400**

No API Key provided, credentials invalid, or invalid values in request contents (e.g. body).

**402**

Your application is on a free plan or doesn't have sufficient balance to perform the operation. Visit [https://dashboard.veriph.one](https://dashboard.veriph.one/) to fix the issue.

**403**

API Key or Client status have made the credentials unusable; or there's an issue with the credentials provided.

post/insights/ip/v1.0.0

https://service.veriph.one/insights/ip/v1.0.0

### Request samples

- Payload

Content type

application/json

Copy
Expand all  Collapse all

`{"transactionUuid": "string",

"useTransaction": true,

"requestUuid": "string",

"ipAddress": "string",

"userAgent": "string",

"userLanguage": "string",

"connectionIsMobileApp": false,

"configuration": {"reverseGeocodingLanguage": "en",

"fraudStrictness": "STRICTEST",

"enableForensicChecks": false,

"allowPublicIpAddresses": true,

"relaxedScoring": false

}

}`

### Response samples

- 200
- 400
- 402
- 403

Content type

application/json

Copy
Expand all  Collapse all

`{"transactionUuid": "string",

"mostLikelyGeolocation": {"city": {"geoNameId": 0,

"localizedName": "string",

"confidence": 100

},

"continent": {"geoNameId": 0,

"localizedName": "string",

"code": "string"

},

"country": {"geoNameId": 0,

"localizedName": "string",

"confidence": 100,

"isoCode": "string"

},

"accuracyRadiusInKm": 0,

"avgIncomeInUSD": 0,

"latitude": 0,

"longitude": 0,

"populationDensity": 0,

"timezone": "string",

"zipCode": "string",

"zipCodeConfidence": 100,

"countrySubdivisions": [{"geoNameId": 0,\
\
"localizedName": "string",\
\
"confidence": 100,\
\
"isoCode": "string"\
\
}\
\
],

"ipCountryAssociation": {"geoNameId": 0,

"localizedName": "string",

"confidence": 100,

"isoCode": "string",

"type": "military"

},

"ipCountryRegistration": {"geoNameId": 0,

"localizedName": "string",

"confidence": 100,

"isoCode": "string"

}

},

"alternativeGeolocation": {"countryIsoCode": "string",

"city": "string",

"regionOrState": "string",

"latitude": 0,

"longitude": 0,

"timezone": "string",

"zipCode": "string"

},

"technicalTraits": {"ispName": "string",

"organization": "string",

"autonomousSystemNumber": 0,

"autonomousSystemOrganization": "string",

"mobileCountryCode": "string",

"mobileNetworkCode": "string",

"network": "string"

},

"usageTraits": {"connectionType": "Cable/DSL",

"domain": "string",

"staticIpScore": 99.99,

"userCountInLast24Hrs": 0,

"userType": "business"

},

"securityChecks": {"externalIpAddress": "string",

"isAnonymous": true,

"isAnonymousVpn": true,

"isVpn": true,

"isHostingProvider": true,

"isProxy": true,

"isPublicProxy": true,

"isResidentialProxy": true,

"isTorNodeOrExit": true,

"isCrawler": true,

"isActiveVpn": true,

"isSharedConnection": true,

"isDynamicConnection": true,

"isSecurityScanner": true

},

"fraudAnalysis": {"isTrustedNetwork": true,

"hasReportsOfRecentAbuse": true,

"abuseVelocity": "high",

"isFraudulentBot": true,

"fraudScore": 0,

"isFrequentAbuser": true,

"isEngagedInHighRiskAttacks": true

},

"userAgentStringAnalysis": {"isMobile": true,

"operatingSystem": "string",

"browser": "string",

"deviceBrand": "string",

"deviceModel": "string"

}

}`

## [tag/4.-Insights/operation/analyzeGeolocation](https://developer.veriph.one/api\#tag/4.-Insights/operation/analyzeGeolocation) Geolocation insights and area analysis

This endpoint provides comprehensive geolocation information including reverse geocoding, area statistics and nearby infrastructure analysis. It returns address details (with accuracy-based masking), security statistics, quality of life indicators, and financial infrastructure information for a given latitude and longitude. The accuracy radius parameter controls the precision of the returned address information. Even though the reverse geocoding service is available globally, statistics and risk location analysis are only available for locations within Mexico. The service also requires a paid plan.

##### header Parameters

|     |     |
| --- | --- |
| authorization<br>required | string<br>Your Veriph.One API Key Secret; using the Basic auth structure: `Basic XXXX...XXXX` |
| x-api-key<br>required | string<br>Your Veriph.One API Key |

##### Request Body schema: application/json  required

|     |     |
| --- | --- |
| transactionUuid | string<br>An optional UUID used to identify a group of identity validation requests as a unique transaction. Used for billing and data-coherence analysis of a single end-user identity. If one isn't provided, a new one will be provided as part of the response if the request was successful and `useTransaction` is set to `true`. |
| useTransaction | boolean<br>A boolean value that governs whether the request will create a request-bundling transaction if `transactionUuid` wasn't provided (ignored otherwise). The default is false. It is recommended to use transactions if you will query multiple web services to validate or obtain insights for a single user's identity; by doing so, you can leverage lower pricing (if your plan allows it) and obtain additional data points and better scoring (as we integrate more sources in our data-coherence analysis). |
| requestUuid | string<br>An optional string containing a UUID provided by your application to leverage idempotency and retrieve the results of the request in case of an interrupted connection. |
| latitude<br>required | number \[ -90 .. 90 \] <br>Latitude coordinate between -90 and 90 |
| longitude<br>required | number \[ -180 .. 180 \] <br>Longitude coordinate between -180 and 180 |
| accuracyRadiusInMeters | number \[ 0 .. 50000 \] <br>Default: 0<br>Accuracy radius in meters (max 50000). If not provided, defaults to 0. Note: High-precision security signals (e.g., isInsidePrison) are only computed when accuracy <= 500 meters; otherwise those fields will be null to avoid false positives. |
| financialSearchRadiusInMeters | number \[ 100 .. 10000 \] <br>Default: 3000<br>Custom radius in meters for the financial infrastructure search (defaults to 3000 when omitted). |
| language | string<br>Default: "en"<br>Enum:"af""sq""am""ar""hy""az""eu""be""bn""bs""bg""my""ca""zh""zh-CN""zh-HK""zh-TW""hr""cs""da""nl""en""en-AU""en-GB""et""fa""fi""fil""fr""fr-CA""gl""ka""de""el""gu""iw""hi""hu""is""id""it""ja""kn""kk""km""ko""ky""lo""lv""lt""mk""ms""ml""mr""mn""ne""no""pl""pt""pt-BR""pt-PT""pa""ro""ru""sr""sr-Latn""si""sk""sl""es""es-419""sw""sv""ta""te""th""tr""uk""ur""uz""vi""zu"<br>IETF language code used to localize the reverse geocoded address (e.g., zh-CN, fr, es-419). |

### Responses

**200**

Geolocation data was successfully retrieved with address and statistical information.

**400**

No API Key provided, credentials invalid, or invalid values in request contents (e.g. body).

**402**

Your application is on a free plan or doesn't have sufficient balance to perform the operation. Visit [https://dashboard.veriph.one](https://dashboard.veriph.one/) to fix the issue.

**403**

API Key or Client status have made the credentials unusable; or there's an issue with the credentials provided.

post/insights/geolocation/v1.0.0

https://service.veriph.one/insights/geolocation/v1.0.0

### Request samples

- Payload

Content type

application/json

Copy

`{"transactionUuid": "string",

"useTransaction": true,

"requestUuid": "string",

"latitude": 19.4326,

"longitude": -99.1332,

"accuracyRadiusInMeters": 1000,

"financialSearchRadiusInMeters": 1500,

"language": "es"

}`

### Response samples

- 200
- 400
- 402
- 403

Content type

application/json

Copy
Expand all  Collapse all

`{"transactionUuid": "string",

"address": {"country": "México",

"countryIsoCode": "MX",

"firstLevelDivision": "Ciudad de México",

"secondLevelDivision": "Cuauhtémoc",

"locality": "Centro Histórico",

"streetLine": "Calzada de Tlalpan",

"streetNumber": "123"

},

"stats": {"security": {"highRiskLocations": {"isInsidePrison": true,

"nearnessToPrison": 0

},

"criminalIncidence": {"relativeToCountry": 100,

"relativeToState": 100

}

},

"qualityOfLife": {"costOfLiving": 0,

"socialLag": 0,

"humanDevelopmentIndex": 1,

"marginalizationIndex": 100,

"medianIncome": 0,

"isRuralArea": true

},

"relevantLocations": {"financialInfrastructure": {"numOfAtms": 0,

"numOfBankBranches": 0

}

}

}

}`

## [tag/4.-Insights/operation/searchDigitalFootprint](https://developer.veriph.one/api\#tag/4.-Insights/operation/searchDigitalFootprint) Digital footprint search

Search for a phone number's and/or email address's presence in social media, popular mobile apps, and over 100 platforms. This process can help detect fraudsters and identity theft events. The service operates under two modes:

- Quick search: returns a record-based payload from a limited number of sites (+30); data uses inference in some cases, so it can be outdated or imprecise.
- Deep search: a robust process that leverage several real-time inquiry methods to obtain up-to-date and precise data on accounts; this type can take minutes to complete.
Please note that this service operates under an independent billing scheme, and each search type has a distinct price. Although your app can send either a phone number or an email address, we recommend sending both for better results. Finally, this service is only available to paid plans and accounts with a minimum balance of 1 USD.

##### header Parameters

|     |     |
| --- | --- |
| authorization<br>required | string<br>Your Veriph.One API Key Secret; using the Basic auth structure: `Basic XXXX...XXXX` |
| x-api-key<br>required | string<br>Your Veriph.One API Key |

##### Request Body schema: application/json  required

|     |     |
| --- | --- |
| transactionUuid | string<br>An optional UUID used to identify a group of identity validation requests as a unique transaction. Used for billing and data-coherence analysis of a single end-user identity. If one isn't provided, a new one will be provided as part of the response if the request was successful and `useTransaction` is set to `true`. |
| useTransaction | boolean<br>A boolean value that governs whether the request will create a request-bundling transaction if `transactionUuid` wasn't provided (ignored otherwise). The default is false. It is recommended to use transactions if you will query multiple web services to validate or obtain insights for a single user's identity; by doing so, you can leverage lower pricing (if your plan allows it) and obtain additional data points and better scoring (as we integrate more sources in our data-coherence analysis). |
| requestUuid | string<br>An optional string containing a UUID provided by your application to leverage idempotency and retrieve the results of the request in case of an interrupted connection. |
| phoneNumber<br>required | object or null<br>The phone number to use for the search. It can be provided as a string in E.164 format (e.g., +14155552671) or an object containing the country code and number separately. Can only be null if an email is provided. |
| email<br>required | string or null<br>The email address to use for the search. Must be a valid email address; if the email is invalid, the service will treat it as null. Can only be null if phoneNumber is provided. |
| searchTypes<br>required | Array of strings<br>Items Enum:"quick""deep"<br>The desired search method to be used in the form of a string array, please consider that this is directly linked to pricing and using quick search will return some fields as null. Morever, including a search method might increase the cost of your request and make it slower (as more data is queried and generated). Contact your sales representative for more details. |

### Responses

**200**

Search data was successfully retrieved; the body of the response includes the payload with the information found.

**400**

No API Key provided, credentials invalid, or invalid values in request contents (e.g. body).

**402**

Your application is on a free plan or doesn't have sufficient balance to perform the operation. Visit [https://dashboard.veriph.one](https://dashboard.veriph.one/) to fix the issue.

**403**

API Key or Client status have made the credentials unusable; or there's an issue with the credentials provided.

**423**

Your application is not configured to access this service and requires approval. Contact [support@veriph.one](mailto:support@veriph.one) for assistance.

post/standalone/digital-footprint-search/v1.0.0

https://service.veriph.one/standalone/digital-footprint-search/v1.0.0

### Request samples

- Payload

Content type

application/json

Copy
Expand all  Collapse all

`{"transactionUuid": "string",

"useTransaction": true,

"requestUuid": "string",

"phoneNumber": {"ituFormatedPhoneNumber": "string",

"splitPhoneNumber": {"countryCode": "string",

"phoneNumber": "string"

}

},

"email": "string",

"searchTypes": ["quick"\
\
]

}`

### Response samples

- 200
- 400
- 402
- 403
- 423

Content type

application/json

Copy
Expand all  Collapse all

`{"transactionUuid": "string",

"stats": {"email": {"totalAssociatedServices": 0,

"associatedServicesByCategory": {"adult": 0,

"blogging": 0,

"business": 0,

"creative": 0,

"crypto": 0,

"dating": 0,

"delivery": 0,

"design": 0,

"ecommerce": 0,

"education": 0,

"emailService": 0,

"employment": 0,

"entertainment": 0,

"events": 0,

"finance": 0,

"freelancing": 0,

"gambling": 0,

"gigEconomy": 0,

"messaging": 0,

"news": 0,

"socialMedia": 0,

"softwareEngineering": 0,

"sports": 0,

"streaming": 0,

"technology": 0,

"travel": 0,

"utilities": 0,

"workTools": 0

},

"servicesWithoutAssociation": 0,

"riskLevel": "low",

"wasRecentlyLeaked": true,

"footprintTenureInYears": 0,

"probabilityOfPersonalUsage": "low",

"probabilityOfWorkUsage": "low"

},

"phone": {"totalAssociatedServices": 0,

"associatedServicesByCategory": {"adult": 0,

"blogging": 0,

"business": 0,

"creative": 0,

"crypto": 0,

"dating": 0,

"delivery": 0,

"design": 0,

"ecommerce": 0,

"education": 0,

"emailService": 0,

"employment": 0,

"entertainment": 0,

"events": 0,

"finance": 0,

"freelancing": 0,

"gambling": 0,

"gigEconomy": 0,

"messaging": 0,

"news": 0,

"socialMedia": 0,

"softwareEngineering": 0,

"sports": 0,

"streaming": 0,

"technology": 0,

"travel": 0,

"utilities": 0,

"workTools": 0

},

"servicesWithoutAssociation": 0,

"riskLevel": "low",

"wasRecentlyLeaked": true,

"footprintTenureInYears": 0,

"probabilityOfPersonalUsage": "low",

"probabilityOfWorkUsage": "low"

},

"allPlusInference": {"totalAssociatedServices": 0,

"associatedServicesByCategory": {"adult": 0,

"blogging": 0,

"business": 0,

"creative": 0,

"crypto": 0,

"dating": 0,

"delivery": 0,

"design": 0,

"ecommerce": 0,

"education": 0,

"emailService": 0,

"employment": 0,

"entertainment": 0,

"events": 0,

"finance": 0,

"freelancing": 0,

"gambling": 0,

"gigEconomy": 0,

"messaging": 0,

"news": 0,

"socialMedia": 0,

"softwareEngineering": 0,

"sports": 0,

"streaming": 0,

"technology": 0,

"travel": 0,

"utilities": 0,

"workTools": 0

},

"servicesWithoutAssociation": 0,

"riskLevel": "low",

"wasRecentlyLeaked": true,

"footprintTenureInYears": 0,

"probabilityOfPersonalUsage": "low",

"probabilityOfWorkUsage": "low"

}

},

"accountMatches": [{"siteOrService": "string",\
\
"accountExists": true,\
\
"categories": ["string"\
\
],\
\
"inputsUsed": ["email"\
\
],\
\
"details": {"id": "string",\
\
"createdAt": "2019-08-24T14:15:22Z",\
\
"updatedAt": "2019-08-24T14:15:22Z",\
\
"username": "string",\
\
"fullName": "string",\
\
"alias": "string",\
\
"url": "string",\
\
"photoUrl": "string",\
\
"bio": "string",\
\
"headline": "string",\
\
"confidence": 0,\
\
"gender": "string",\
\
"social": {"numOfConnections": "string",\
\
"numOfFollowers": 0,\
\
"following": 0,\
\
"isBusinessAccount": true,\
\
"isVerified": true,\
\
"numOfPosts": 0,\
\
"numOfInteractions": 0,\
\
"isPremium": true,\
\
"isAdult": true\
\
},\
\
"messaging": {"canBeCalled": true,\
\
"canReceiveVideoCalls": true,\
\
"isBanned": true,\
\
"markedAsFake": true,\
\
"markedAsSpam": true,\
\
"lastActivity": "2019-08-24T14:15:22Z",\
\
"status": "string",\
\
"isPrivateProfile": true\
\
},\
\
"locations": {"setByUser": "string",\
\
"placeOfOrigin": "string"\
\
},\
\
"professionalInfo": {"employed": true,\
\
"currentCompany": "string",\
\
"currentPosition": "string",\
\
"industry": "string",\
\
"workLocation": "string",\
\
"lastPositionDurationInMonths": 0,\
\
"totalExperienceInYears": 0,\
\
"employmentHistory": [{"company": {"name": "string",\
\
"profileUrl": "string",\
\
"id": "string",\
\
"logoUrl": "string",\
\
"size": "string"\
\
},\
\
"location": "string",\
\
"position": "string",\
\
"startDate": "string",\
\
"endDate": "string",\
\
"industries": ["string"\
\
],\
\
"description": "string"\
\
}\
\
]\
\
},\
\
"educationHistory": [{"institution": {"name": "string",\
\
"logoUrl": "string",\
\
"profileUrl": "string"\
\
},\
\
"degree": "string",\
\
"fieldOfStudy": "string",\
\
"startDate": "string",\
\
"endDate": "string",\
\
"activities": "string",\
\
"description": "string"\
\
}\
\
]\
\
}\
\
}\
\
],

"dataLeaks": {"firstMatch": "2019-08-24T14:15:22Z",

"lastMatch": "2019-08-24T14:15:22Z",

"numOfLeaks": 0,

"linkedToPhoneNumber": {"firstMatch": "2019-08-24T14:15:22Z",

"lastMatch": "2019-08-24T14:15:22Z",

"total": 0,

"listOfLeaks": ["string"\
\
]

},

"linkedToEmail": {"firstMatch": "2019-08-24T14:15:22Z",

"lastMatch": "2019-08-24T14:15:22Z",

"total": 0,

"listOfLeaks": ["string"\
\
]

}

}

}`

## [tag/5.-Misc](https://developer.veriph.one/api\#tag/5.-Misc) 5\. Misc

## [tag/5.-Misc/operation/checkServiceHealth](https://developer.veriph.one/api\#tag/5.-Misc/operation/checkServiceHealth) Health Check

Simple endpoint to check on our servers' availability.

### Responses

**200**

Successful request.

get/health-api/check

https://service.veriph.one/health-api/check

### Response samples

- 200

Content type

application/json

Copy

`{"module": "string",

"now": "string"

}`