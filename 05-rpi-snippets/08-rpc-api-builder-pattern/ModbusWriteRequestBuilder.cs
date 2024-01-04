using MPC2.ModbusLib.Protocols;
using PMTester.Domain.Commands.Concretes;
using static PMTester.Domain.UpdatePatterns;

namespace PMTester.Domain.Commands.Builders;

public class ModbusWriteRequestBuilder : IModbusRequestBuilder
{
    public void Reset()
    {
        _request = null;
        _command = null;
        _updateDelegate = null;
    }

    public void SetCommandType(ModbusCommand type)
    {
        _command = type;
    }

    public void SetUpdateDelegate(UpdateDelegate? updateDelegate)
    {
        _updateDelegate = updateDelegate;
    }

    public void SetOffset(int offset)
    {
        if (_command is null) throw new Exception("ModbusCommand type not set!");
        _command.Offset = offset;
    }

    public void SetCount(int count)
    {
        if (_command is null) throw new Exception("ModbusCommand type not set!");
        _command.Count = count;
    }

    public void SetData(ushort[] data)
    {
        if (_command is null) throw new Exception("ModbusCommand type not set!");
        _command.Data = data;
    }

    public void FinalizeRequest(ModbusTcpMaster owner)
    {
        if (_command is null) throw new Exception("ModbusCommand type not set!");
        _request = new ModbusWriteRequest(owner, _command);
    }

    public IModbusRequest GetRequest()
    {
        if (_request is null) throw new Exception("No request has been built!");
        return _request;
    }


    private IModbusRequest? _request;
    private ModbusCommand? _command;
    private UpdateDelegate? _updateDelegate;


    public ModbusWriteRequestBuilder() {}
}