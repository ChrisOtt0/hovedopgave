using Microsoft.AspNetCore.Mvc;
using System.Diagnostics;

using PMTester.Domain;
using PMTester.Models;
using PMTester.Domain.Enums;

namespace PMTester.Controllers;

[ApiController]
[Route("Integration")]
public class IntegrationController : ControllerBase {
#region Private

    private readonly Services.ILogger _logger;
    private Stopwatch _stopwatch;

    private ModbusTcpMaster? _modbusTcpMaster;


    private void ModbusCreate() {
        if (_modbusTcpMaster == null) {
            _modbusTcpMaster = new ModbusTcpMaster(Env.MODULE_IP, Env.MODULE_PORT);
        }

        _modbusTcpMaster.Connect();
        Thread.Sleep(1000);
    }

#endregion


#region Constructor

    public IntegrationController(Services.ILogger logger) {
        _logger = logger;
        _stopwatch = new Stopwatch();
    }

#endregion


#region Endpoints

    // Read Register with PNU 1, should succeed, however we do not care about data
    [Route("Read1")]
    [HttpPost]
    public TestResult GetReadRegisterTest1(ModbusRequest request) {
        // Arrange
        TimeSpan ts;
        _stopwatch.Reset();
        ModbusCreate();

        var command = _modbusTcpMaster?.GenerateRequest(request, eModbusTestCase.Read1);


        // Act
        _stopwatch.Start();

        command?.Execute();

        _stopwatch.Stop();
        ts = _stopwatch.Elapsed;


        // Collect, Clean & Return
        return new TestResult(
            new Dictionary<string, object?> {
                { "CommandStateDn", command?.Dn },
                { "CommandStateErr", command?.Err },
                { "TimeElapsed", ts.TotalMilliseconds },
                { "Result", command?.Payload },
            }
        );
    }

#endregion
}