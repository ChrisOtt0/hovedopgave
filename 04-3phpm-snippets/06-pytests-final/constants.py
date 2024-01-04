import requests
from enum import IntEnum


BASEURL = "█████████████"


class AbstractTestClass:
    requestSession = requests.Session()
    requestSession.verify = False
    response = None

    def try_act(self, url, data):
        try:
            self.response = self.requestSession.post(url, json=data)
            return True
        except:
            return False
        
    def get_response(self):
        return self.response
    



class AbstractIntegrationTestClass(AbstractTestClass):
    URL = BASEURL + "/Integration"

    
class AbstractFunctionalTestClass(AbstractTestClass):
    URL = BASEURL + "/System"


class CommResponse(IntEnum):
    Unknown = 0
    Ignore = 1
    Critical = 2
    Ack = 3
    Disconn = 4


class ModbusMasterState(IntEnum):
    _None = 0
    Stop = 1
    Connecting = 2
    Initialization = 3
    Ready = 4
    Running = 5
    Error = 6
    Disconnecting = 7


class ModbusFunctionCode(IntEnum):
    ReadCoils = 1
    ReadInputDiscretes = 2
    ReadMultipleRegisters = 3
    ReadInputRegisters = 4
    WriteCoil = 5
    WriteSingleRegister = 6
    ReadExceptionStatus = 7
    ForceMultipleCoils = 15
    WriteMultipleRegisters = 16


class HttpStatusCode(IntEnum):
    # Information
    Continue = 100
    SwitchingProtocols = 101
    Processing = 102
    EarlyHints = 103

    # Success
    Ok = 200
    Created = 201
    Accepted = 202
    NonAuthoritativeInformation = 203
    NoContent = 204
    ResetContent = 205
    PartialContent = 206
    MultiStatus = 207
    AlreadyReported = 208
    ImUsed = 226

    # Redirection
    MultipleChoices = 300
    MovedPermanently = 301
    Found = 302
    SeeOther = 303
    NotModified = 304
    UseProxy = 305
    TemporaryRedirect = 307
    PermanentRedirect = 308

    # Client Error
    BadRequest = 400
    Unauthorized = 401
    PaymentRequired = 402
    Forbidden = 403
    NotFound = 404
    MethodNotAllowed = 405
    NotAcceptable = 406
    ProxyAuthenticationRequired = 407
    RequestTimeout = 408
    Conflict = 409
    Gone = 410
    LengthRequired = 411
    PreconditionFailed = 412
    PayloadTooLarge = 413
    UriTooLong = 414
    UnsupportedMediaType = 415
    RangeNotSatisfiable = 416
    ExpectationFailed = 417
    ImATeapot = 418
    MisdirectionRequest = 421
    UnprocessableContent = 422
    Locked = 423
    FailedDependency = 424
    TooEarly = 425
    UpgradeRequired = 426
    PreconditionRequired = 428
    TooManyRequests = 429
    RequestHeaderFieldsTooLarge = 431
    UnavailableForLegalReasons = 451

    # Server Error
    InternalServerError = 500
    NotImplemented = 501
    BadGateway = 502
    ServiceUnavailable = 503
    GatewayTimeout = 504
    HttpVersionNotSupported = 505
    VariantAlsoNegotiates = 506
    InsufficientStorage = 507
    LoopDetected = 508
    NotExtended = 510
    NetworkAuthenticationRequired = 511