using PMTester.Domain.Enums;
using PMTester.Domain.Commands.Builders;
using PMTester.Models;

namespace PMTester.Domain.Commands;

public class ModbusRequestDirector {
    public void MakeModbusRequest(ModbusRequest request, eModbusTestCase? testCase) {
        _builder = SetBuilder((eFunctionCode)request.FunctionCode);
        if (_builder is null) throw new Exception("Unknown Modbus function code!");

        _builder.Reset();
        
        switch (request.FunctionCode) {
            case (int)eFunctionCode.ReadMultipleRegisters:
                _builder.SetCommandType(_owner.ReadCommand3);
                break;

            case (int)eFunctionCode.ReadInputRegisters:
                _builder.SetCommandType(_owner.ReadCommand4);
                break;

            case (int)eFunctionCode.WriteMultipleRegisters:
                _builder.SetCommandType(_owner.WriteCommand16);
                break;
        }

        if (_builder is ModbusReadRequestBuilder) {
            if (testCase is null) throw new Exception("Cannot create update pattern without knowing the testCase. No testcase provided!");
            if (testCase <= eModbusTestCase.Read3)
                _builder.SetUpdateDelegate(UpdatePatterns.ReadUI8PNU);
            if (testCase == eModbusTestCase.Read1V)
                _builder.SetUpdateDelegate(UpdatePatterns.ReadF32PNU);
        }

        _builder.SetOffset(request.Address);
        _builder.SetCount(request.Count);
        _builder.SetData(request.Data);
        _builder.FinalizeRequest(_owner);
    }

    public IModbusRequest DeliverRequest() {
        if (_builder is null) throw new Exception("No ModbusRequest has been made!");
        return _builder.GetRequest();
    }


    private ModbusTcpMaster _owner;
    private IModbusRequestBuilder? _builder;


    private IModbusRequestBuilder? SetBuilder(eFunctionCode functionCode) {
        switch (functionCode) {
            case eFunctionCode.ReadInputRegisters:
            case eFunctionCode.ReadMultipleRegisters:
                return new ModbusReadRequestBuilder();

            case eFunctionCode.WriteMultipleRegisters:
                return new ModbusWriteRequestBuilder();

            default:
                return null;
        }
    }


    public ModbusRequestDirector(ModbusTcpMaster owner) {
        _owner = owner;
    }
}